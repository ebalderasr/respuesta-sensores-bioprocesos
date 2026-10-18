"""Comprobaciones de las definiciones, no de valores supuestos del piloto."""
import unittest
import numpy as np
from analizar_respuesta import metricas


class MetricasTest(unittest.TestCase):
    def setUp(self):
        self.t = np.arange(0, 100.1, .1)
        self.ascenso = 1-np.exp(-self.t/10)

    def test_ascenso_exponencial(self):
        m=metricas(self.t,self.ascenso,0,0,1)
        self.assertAlmostEqual(m['t90_aparente_s'],10*np.log(10),places=2)
        self.assertAlmostEqual(m['t10_90_s'],10*np.log(9),places=2)
        self.assertAlmostEqual(m['t_estabilizacion_aparente_s'],30,places=1)

    def test_descenso_usa_misma_fraccion(self):
        m=metricas(self.t,8-5*self.ascenso,0,8,3)
        self.assertAlmostEqual(m['t90_aparente_s'],10*np.log(10),places=2)
        self.assertAlmostEqual(m['semibanda_unidades_senal'],.25)

    def test_cruce_no_significa_estabilidad(self):
        y=self.ascenso.copy();y[self.t>=95]=1.2
        m=metricas(self.t,y,0,0,1)
        self.assertIsNotNone(m['t90_aparente_s'])
        self.assertIsNone(m['t_estabilizacion_aparente_s'])

    def test_no_interpolar_hueco_en_el_cruce(self):
        keep=~((self.t>20)&(self.t<27))
        m=metricas(self.t[keep],self.ascenso[keep],0,0,1)
        self.assertIsNone(m['t90_aparente_s'])

    def test_hueco_no_confirma_permanencia(self):
        keep=~((self.t>40)&(self.t<51))
        m=metricas(self.t[keep],self.ascenso[keep],0,0,1)
        self.assertAlmostEqual(m['t_estabilizacion_aparente_s'],51)

    def test_ventana_demasiado_corta(self):
        keep=self.t<10
        m=metricas(self.t[keep],self.ascenso[keep],0,0,1)
        self.assertIsNone(m['t90_aparente_s'])
        self.assertIsNone(m['t_estabilizacion_aparente_s'])

    def test_cambio_nulo_no_es_respuesta_instantanea(self):
        with self.assertRaises(ValueError):metricas(self.t,self.ascenso,0,1,1)


if __name__=='__main__':unittest.main()
