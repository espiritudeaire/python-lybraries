import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat


class EEGSignal:
    def __init__(self, file_path):
        self.data = loadmat (file_path)['data']
        self.original_data = self.data.copy()
        self.canales, self.tiempo, self.epochs = self.data.shape
        self.recorte = None
        self.unificado = None
        
        self._tamaño_señal = self.data.size
        self._dimensiones_señal = self.data.shape
        
        self._tamaño_recorte = None
        self._dimensiones_recorte = None
    
    def recortar(self, epoca_inicio: int, epoca_fin: int):
        self.recorte = self.data[:,:, epoca_inicio:epoca_fin]
        self._dimensiones_recorte = self.recorte.shape
        self._tamaño_recorte = self.recorte.size
        #return self.recorte
    
    def recuperar_señal_original(self):
        return self.original_data
    
    def unificar_epocas_del_recorte(self):
        canales, tiempo, epocas = self.recorte.shape
        self.unificado = self.recorte.reshape(canales, tiempo * epocas)
        return self.unificado
    
    def get_tamaño_dimensiones(self):
        print(f"""
              Original:
              Dimensiones: {self._dimensiones_señal}
              Tamaño: {self._tamaño_señal}
              
              Recorte:
              Dimensiones: {self._dimensiones_recorte}
              Tamaño: {self._tamaño_recorte}""")
    
data = sio.loadmat('S1.mat')['data']


señal1 = EEGSignal('S1.mat')
señal2 = EEGSignal('S2.mat')
señal3 = EEGSignal('S3.mat')
señal1.recortar(4,50)
señal1.unificar_epocas_del_recorte()
señal2.recortar(4,80)
señal3.recortar(70,100)
print(señal1.get_tamaño_dimensiones())
print(señal2.get_tamaño_dimensiones())
print(señal3.get_tamaño_dimensiones())

print(señal3.recuperar_señal_original())
    
