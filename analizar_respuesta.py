"""Analiza el piloto de pH/OD sin confundir inicios inferidos con eventos registrados.

Uso: python analizar_respuesta.py
Salidas: CSV en datos_limpios/, JSON/Markdown en resultados/ y PNG en figuras/.
Las ventanas y los inicios inferidos se documentan en ventanas_piloto.json.
"""
from pathlib import Path
import argparse
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parent
AZUL, NARANJA, GRIS = '#2a78d6', '#eb6834', '#66616f'
plt.rcParams.update({'font.size': 10, 'figure.dpi': 160, 'axes.spines.top': False,
                     'axes.spines.right': False, 'axes.grid': True, 'grid.alpha': .2})


def cargar(archivo, hoja):
    """Usa ProcessTime (horas), con resolución subsegundo; conserva huecos de señal."""
    raw = pd.read_excel(archivo, sheet_name=hoja)
    df = raw.loc[raw['PDatTime'].notna()].copy()
    for col in ['ProcessTime', 'pH_1', 'pO2_1']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    if df['ProcessTime'].isna().any():
        raise ValueError(f'{hoja}: tiempos de proceso no numéricos')
    df['t_s'] = (df['ProcessTime'] - df['ProcessTime'].iloc[0]) * 3600
    df = df.rename(columns={'pH_1': 'pH', 'pO2_1': 'OD'})
    if not (df['t_s'].diff().dropna() > 0).all():
        raise ValueError(f'{hoja}: tiempo no estrictamente creciente')
    # Puntos simultáneamente cero en ambas señales: probables artefactos,
    # no equivalen a un cambio físico del sensor. Conservar raw y marcar para el análisis.
    df['posible_artefacto'] = (df['pH'] == 0) & (df['OD'] == 0)
    return df[['PDatTime', 't_s', 'pH', 'OD', 'posible_artefacto']]


def cruce(t, progreso, nivel):
    """Primer cruce ascendente; sin extrapolar ni cruzar huecos de más de 3 s."""
    for i in range(len(t)):
        if not (np.isfinite(t[i]) and np.isfinite(progreso[i])):
            continue
        if progreso[i] >= nivel:
            if i == 0 or not np.isfinite(progreso[i-1]) or t[i]-t[i-1] > 3:
                return None
            a, b = progreso[i-1], progreso[i]
            if b == a:
                return float(t[i])
            return float(t[i-1] + (nivel-a)*(t[i]-t[i-1])/(b-a))
    return None


def metricas(t, y, t0, y0, yf, banda_frac=.05, permanencia_s=30):
    """Métricas operativas de una señal ascendente o descendente.

    Estabilización: primer punto dentro de ±banda_frac*|yf-y0| que
    permanece dentro hasta el fin, con al menos permanencia_s de observación.
    Un hueco >3 s o una muestra inválida impide confirmar el tramo que lo cruza.
    """
    t, y = np.asarray(t, dtype=float), np.asarray(y, dtype=float)
    if len(t) != len(y) or len(t) < 2 or not np.all(np.diff(t) > 0):
        raise ValueError('Se requieren tiempos crecientes y señales de igual longitud')
    if not np.isfinite([t0, y0, yf]).all() or abs(yf-y0) < 1e-9:
        raise ValueError('Se requieren niveles finitos y un cambio no nulo')
    if not 0 < banda_frac < 1 or permanencia_s <= 0:
        raise ValueError('Banda y permanencia deben ser positivas y válidas')
    mask = t >= t0
    tr, yr = t[mask]-t0, y[mask]
    progreso = (yr-y0)/(yf-y0)
    cruces = {f't{int(100*f)}_aparente_s': cruce(tr, progreso, f) for f in [.1, .632, .9]}
    t10, t90 = cruces['t10_aparente_s'], cruces['t90_aparente_s']
    banda = banda_frac * abs(yf-y0)
    estable = None
    for i in range(len(tr)):
        if tr[-1]-tr[i] < permanencia_s:
            break
        if (np.isfinite(yr[i:]).all() and np.all(np.abs(yr[i:]-yf) <= banda)
                and np.all(np.diff(tr[i:]) <= 3)):
            estable = float(tr[i])
            break
    return {**cruces, 't10_90_s': None if t10 is None or t90 is None else t90-t10,
            't_estabilizacion_aparente_s': estable, 'semibanda_unidades_senal': banda,
            'permanencia_minima_s': permanencia_s,
            'duracion_observada_desde_t0_s': float(tr[-1]) if len(tr) else 0}


def guardar(fig, nombre):
    fig.tight_layout()
    fig.savefig(BASE/'figuras'/nombre, bbox_inches='tight')
    plt.close(fig)


def esquema():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.1))
    for ax, labels, color in [(axes[0], ['Buffer A\npH 8', 'Buffer B\npH 3'], AZUL),
                               (axes[1], ['Agua + aire\nO₂ alto', 'Agua + N₂\nO₂ bajo'], NARANJA)]:
        for x, label in zip([.12,.64], labels):
            ax.plot([x,x,x+.23,x+.23], [.7,.15,.15,.7], color=GRIS, lw=2)
            ax.fill_between([x,x+.23], .15, .48, alpha=.12, color=color)
            ax.text(x+.115,.32,label,ha='center',va='center',fontsize=10)
            ax.plot([x+.07,x+.16],[.19,.19],color=color,lw=4)
            ax.text(x+.115,.06,'Agitación',ha='center',fontsize=9)
        ax.annotate('',xy=(.72,.81),xytext=(.25,.81),arrowprops={'arrowstyle':'<->','color':color,'lw':2})
        ax.text(.49,.9,'Transferir la sonda conectada',ha='center',fontsize=10)
        ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    axes[0].set_title('pH: dos buffers preparados')
    axes[1].set_title('O₂: dos líquidos preequilibrados')
    guardar(fig,'00_montaje.png')

    t=np.linspace(-15,160,700); y=np.where(t<0,0,1-np.exp(-np.maximum(t,0)/20))
    fig,axes=plt.subplots(2,1,figsize=(9,5.8),sharex=True,gridspec_kw={'height_ratios':[1,2]})
    axes[0].step([-15,0,160],[0,100,100],where='post',color=GRIS)
    axes[0].set(ylabel='Cambio real\n[% del recorrido]',title='Ejemplo didáctico: el cambio es rápido; la lectura tarda')
    axes[1].plot(t,100*y,color=AZUL,lw=2)
    axes[1].axhspan(95,105,color=AZUL,alpha=.10,label='Banda ±5 % del cambio')
    for f,label in [(.1,'10 %'),(.632,'63.2 %'),(.9,'90 %')]:
        tx=-20*np.log(1-f);axes[1].plot([tx,tx],[0,100*f],ls=':',color=GRIS)
        axes[1].annotate(label,(tx,100*f),xytext=(6,-15),textcoords='offset points',fontsize=9)
    axes[1].set(xlabel='Tiempo desde la inmersión [s]',ylabel='Lectura [% del recorrido]',ylim=(-5,110))
    axes[1].legend(loc='lower right',fontsize=9)
    guardar(fig,'01_respuesta_didactica.png')


def analizar(archivo, configuracion):
    for folder in ['figuras','resultados','datos_limpios']:
        (BASE/folder).mkdir(exist_ok=True)
    esquema()
    hojas={sh:cargar(archivo,sh) for sh in ['pH','OD']}
    calidad={}
    fig,axes=plt.subplots(2,1,figsize=(11,6.2))
    for ax,(sh,df) in zip(axes,hojas.items()):
        df.to_csv(BASE/'datos_limpios'/f'{sh}_completo.csv',index=False,float_format='%.6f')
        dt=df.t_s.diff().dropna()
        calidad[sh]={'filas':len(df),'intervalo_mediano_s':float(dt.median()),
                     'intervalo_maximo_s':float(dt.max()),'marcas_reloj_duplicadas':int(df.PDatTime.duplicated().sum()),
                     'faltantes_pH':int(df.pH.isna().sum()),'faltantes_OD':int(df.OD.isna().sum()),
                     'posibles_artefactos':int(df.posible_artefacto.sum()),'duracion_s':float(df.t_s.iloc[-1])}
        yy=df[sh].mask(df.posible_artefacto)
        ax.plot(df.t_s/60,yy,color=AZUL if sh=='pH' else NARANJA,lw=1)
        ax.set(xlabel=f'Tiempo desde inicio de la hoja {sh} [min]',ylabel='pH' if sh=='pH' else 'O₂ [% sat.]',
               title=f'Piloto del 14 de octubre · hoja {sh}')
    guardar(fig,'02_piloto_completo.png')
    resultados=[]
    fig,axes=plt.subplots(len(configuracion),1,figsize=(10,3.3*len(configuracion)),squeeze=False)
    for ax,c in zip(axes.flat,configuracion):
        df=hojas[c['hoja']];senal=c['senal'];ini,fin=c['ventana_s'];t0=c['t0_inferido_s']
        seg=df[df.t_s.between(ini,fin)].copy()
        seg.loc[seg.posible_artefacto,senal]=np.nan
        previo=df.loc[df.t_s.between(*c['nivel_inicial_s']) & ~df.posible_artefacto,senal].dropna()
        final=df.loc[df.t_s.between(*c['nivel_final_s']) & ~df.posible_artefacto,['t_s',senal]].dropna()
        if len(previo)<10 or len(final)<10:raise ValueError('Ventanas insuficientes para niveles de referencia')
        y0,yf=float(previo.median()),float(final[senal].median())
        m=metricas(seg.t_s,seg[senal],t0,y0,yf)
        r={**c,'nivel_inicial_mediana':y0,'nivel_final_mediana':yf,
           'pendiente_final_unidades_min':float(np.polyfit(final.t_s,final[senal],1)[0]*60),
           'rango_final_unidades':float(final[senal].max()-final[senal].min()),**m,
           'advertencia':'Origen inferido de la señal; valores aparentes, no tiempos certificados del sensor.'}
        resultados.append(r)
        seg['t_desde_inicio_inferido_s']=seg.t_s-t0
        seg.to_csv(BASE/'datos_limpios'/f"{c['id']}.csv",index=False,float_format='%.6f')
        ax.plot(seg.t_s-t0,seg[senal],color=AZUL if senal=='pH' else NARANJA,label='Lectura original')
        b=m['semibanda_unidades_senal'];ax.axhspan(yf-b,yf+b,color=AZUL,alpha=.10,label='Banda ±5 % del cambio')
        ax.axvline(0,color=GRIS,ls='--',label='Inicio inferido')
        t90=m['t90_aparente_s']
        if t90 is not None:
            ax.plot(t90,y0+.9*(yf-y0),'o',color=AZUL)
            ax.annotate(f't₉₀ aparente ≈ {t90:.1f} s',(t90,y0+.9*(yf-y0)),xytext=(12,12),textcoords='offset points',fontsize=9)
        ax.set(xlabel='Tiempo desde el inicio inferido [s]',ylabel='pH' if senal=='pH' else 'O₂ [% sat.]',title=c['titulo'])
        ax.legend(fontsize=8,loc='best')
    guardar(fig,'03_piloto_ventanas.png')
    # Vista de OD completa: conserva los intentos lentos y el cambio final.
    df=hojas['OD'];fig,ax=plt.subplots(figsize=(10,3.7))
    ax.plot(df.t_s,df.OD,color=NARANJA)
    ax.axvspan(0,835,color=GRIS,alpha=.10,label='Intentos previos: entrada no documentada')
    ax.axvline(836.25,color=AZUL,ls=':',label='Inicio inferido del cambio final')
    ax.set(xlabel='Tiempo desde inicio de hoja OD [s]',ylabel='O₂ [% sat.]',title='O₂: distinguir una variación lenta del medio de una transición rápida')
    ax.legend(fontsize=8);guardar(fig,'04_OD_intentos.png')
    resumen={'archivo':Path(archivo).name,'base_tiempo':'ProcessTime relativo, en segundos',
             'calidad':calidad,'criterio':'Banda ±5 % del cambio; permanencia ≥30 s y hasta fin de ventana; sin huecos >3 s.',
             'ventanas':resultados}
    (BASE/'resultados'/'piloto.json').write_text(json.dumps(resumen,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    texto=['# Resultados exploratorios del piloto','',
           'Origen de cada transición inferido; consultar `ventanas_piloto.json`. No son especificaciones del electrodo.','',
           '| Tramo | Inicial → final | t90 aparente [s] | t10–90 [s] | Estabilización aparente [s] |',
           '|---|---|---|---|---|']
    def formato(x):return 'No confirmada' if x is None else f'{x:.1f}'
    for r in resultados:
        texto.append(f"| {r['titulo']} | {r['nivel_inicial_mediana']:.2f} → {r['nivel_final_mediana']:.2f} | {formato(r['t90_aparente_s'])} | {formato(r['t10_90_s'])} | {formato(r['t_estabilizacion_aparente_s'])} |")
    (BASE/'resultados'/'piloto.md').write_text('\n'.join(texto)+'\n')
    print('\n'.join(texto));print(json.dumps(calidad,ensure_ascii=False,indent=2))


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('archivo',nargs='?',default=str(BASE/'B2 Respuesta electrodos.xlsx'))
    ap.add_argument('--config',type=Path,default=BASE/'ventanas_piloto.json')
    args=ap.parse_args()
    analizar(args.archivo,json.loads(args.config.read_text()))
