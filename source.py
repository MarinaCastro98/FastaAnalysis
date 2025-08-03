'''Vamos a crear una serie de funciones
básicas para poder realizar un análisis básico
y algunos gráficos de secuencias FASTA'''

from Bio import SeqIO
import pandas as pd

def analizar_fasta(ruta_fasta):
    resultados = []

    for record in SeqIO.parse(ruta_fasta, "fasta"):
        secuencia= str(record.seq).upper()
        longitud = len(secuencia)
        G_count = secuencia.count('G')
        C_count = secuencia.count('C')
        GC_count =  G_count + C_count