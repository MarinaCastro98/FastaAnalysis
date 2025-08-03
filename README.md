# 🧬 Análisis básico de archivos FASTA

Este módulo realiza un análisis descriptivo de secuencias de ADN contenidas en archivos `.fasta`. Está pensado como parte de una herramienta web bioinformática, pero puede utilizarse de forma independiente para análisis rápidos.

## 📂 ¿Qué hace?

Para cada secuencia del archivo FASTA, el script calcula:

- ID de la secuencia
- Longitud total (número de nucleótidos)
- Porcentaje de GC
- Conteo de bases (A, T, G, C, N)
- Codón más frecuente (si la longitud lo permite)

Los resultados se almacenan en un archivo `.csv` y se pueden visualizar en consola o integrarse en una interfaz web.


## 🧪 Requisitos
- Python 3.8+
- Biopython
- Pandas

Instalar dependencias:
```pip install biopython pandas```

## 📁 Estructura del repositorio
```
│
├── analisis_fasta.py         # Funciones principales de análisis
├── datos/
│   └── ejemplo.fasta         # Archivos FASTA de prueba
├── resultados/
│   └── resultados_fasta.csv  # Resultados generados
├── notebook/
│   └── analisis_fasta.ipynb  # (opcional) Notebook para pruebas
├── requirements.txt          # Lista de dependencias
└── README.md                 # Este archivo
```
---

## ▶️ Ejemplo de uso

```python
from analisis_fasta import analizar_fasta

df = analizar_fasta("ejemplo.fasta")
print(df.head())

# Guardar como CSV
df.to_csv("resultados_fasta.csv", index=False)
```
---

## 🧠 Próximas mejoras (en desarrollo)
- Visualizaciones interactivas (histogramas, GC%)
- Interfaz web
- Cálculo de motivos y regiones conservadas
- Traducción de secuencias a proteínas
- Descarga de informes PDF
