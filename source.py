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

        # Conteo de bases
        A_count = secuencia.count('A')
        T_count = secuencia.count('T')
        G_count = secuencia.count('G')
        C_count = secuencia.count('C')
        N_count = secuencia.count('N')  # Bases ambiguas
        GC_count =  G_count + C_count
        GC_content = (GC_count / longitud) * 100

        resultado ={
        "ID": record.id,
        "Longitud (bases)": longitud,
        "A": A_count,
            "T": T_count,
            "G": G_count,
            "C": C_count,
            "N": N_count,
        "GC (%)": round(GC_content, 2)}
        
        resultados.append(resultado)

        # Impresión formateada en consola
        print(
            f"ID: {resultado['ID']}\n"
            f"Longitud (bases): {resultado['Longitud (bases)']}\n"
            f"A: {resultado['A']}, T: {resultado['T']}, G: {resultado['G']}, C: {resultado['C']}, N: {resultado['N']}\n"
            f"GC (%): {resultado['GC (%)']}\n"
            "-------------------------"
        )

    return resultado
    


