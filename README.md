# analysis_sold_vehicles
This is an EDA analysis for the sale of vehicles with an app for a website in Render

# Análisis del Conjunto de Datos de Vehículos Vendidos

Este proyecto consiste en un análisis exploratorio de datos (EDA) sobre un conjunto de datos de vehículos vendidos, donde exploramos y visualizamos varios aspectos de los datos, como el precio, el kilometraje, las condiciones de los vehículos. Enfocado mas para vizualizacion en app web.

## Descripción del Proyecto

En este proyecto realizamos una exploración de datos y análisis utilizando diversas visualizaciones como histogramas, diagramas de dispersión y gráficos de barras. El conjunto de datos utilizado es `vehicles_us.csv`, que contiene información sobre vehículos vendidos en los EE.UU. a través de publicaciones en internet.

### Características Principales:
- Visualizaciones interactivas de datos con **Streamlit**.
- Análisis Exploratorio de Datos (**EDA**) detallado usando **Plotly**.
- Información sobre la distribución de precios de vehículos, condiciones de los vehículos y lecturas del odómetro.

---

## Conjunto de Datos

El conjunto de datos contiene las siguientes columnas:
- `price`: El precio del vehículo.
- `model_year`: El año del modelo del vehículo.
- `model`: El nombre del modelo del vehículo.
- `condition`: La condición del vehículo (por ejemplo, "nuevo", "usado").
- `cylinders`: El número de cilindros del vehículo.
- `fuel`: El tipo de combustible que usa el vehículo.
- `odometer`: El número de millas que el vehículo ha recorrido.
- `transmission`: El tipo de transmisión que tiene el vehículo.
- `type`: El tipo de vehículo (por ejemplo, SUV, sedán).
- `paint_color`: El color del vehículo.
- `is_4wd`: En caso de tracción en las cuatro ruedas (4WD).
- `date_posted`: La fecha en que se publicó el anuncio.
- `days_listed`: Días que el vehículo estuvo listado para la venta.

---

## Requisitos

- **Python 3.x** (preferiblemente 3.8+)
- **Streamlit** para visualizaciones interactivas
- **Plotly** para crear gráficos interactivos
- **Pandas** para manipulación de datos
- **Jupyter Notebook** para visualizacion de EDA


## Cómo Ejecutar la Aplicación Localmente:

- **Clonar repositorio:**
```bash
git clone https://github.com/El-Only/analysis_sold_vehicles.git
```
- **Instalar dependencias requeridas:**
```bash
pip install -r requirements.txt
```
- **Ejecuta la aplicación de Streamlit:**
```bash
streamlit run app.py
```

## Cómo Ejecutar la Aplicación en Render

- **Clonar repositorio:**
```bash
git clone https://github.com/El-Only/analysis_sold_vehicles.git
```
- **Instalar las dependencias:**
```bash
pip install -r requirements.txt
```
- **Accede a la aplicación:**

- https://analysis-sold-vehicles.onrender.com


## Estructura del Proyecto

```bash
├── README.md                  # Descripción del proyecto e instrucciones
├── app.py                     # Aplicación principal de Streamlit
├── vehicles_us.csv            # Conjunto de datos
├── requirements.txt           # Lista de dependencias
├── notebooks
│   └── EDA.ipynb              # Notebook de Análisis Exploratorio de Datos (EDA)
└── .streamlit
    └── config.toml            # Configuración de Streamlit
