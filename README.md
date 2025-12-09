# Proyecto Final – Métodos Numéricos

## Descripción

Esta es una **aplicación web interactiva** desarrollada en **Flask** que implementa tres métodos numéricos clásicos para la resolución de ecuaciones no lineales:

- **Método de la Bisección** (método cerrado)
- **Método de Newton-Raphson** (método abierto)
- **Método de la Secante** (método abierto)

La aplicación permite visualizar gráficamente cómo convergen estos métodos hacia la raíz de una ecuación, mostrando el historial detallado de iteraciones.

### 3. Activar el entorno virtual

**En Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**En Windows (CMD):**
```bash
venv\Scripts\activate.bat
```

**En macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución

```bash
python app.py
```

Luego abre tu navegador en:

```
http://127.0.0.1:5000
```

---

## Uso de la Aplicación

### Método de la Bisección
- Ingresa el **intervalo [a, b]** donde sabes que existe una raíz
- Define la **tolerancia** (precisión deseada)
- Haz clic en **Calcular**
- Visualiza la gráfica y el historial de iteraciones

### Método de Newton-Raphson
- Proporciona un **valor inicial x0**
- Define la **tolerancia**
- Haz clic en **Calcular**
- Observa cómo converge cuadráticamente

### Método de la Secante
- Ingresa **dos valores iniciales x0 y x1**
- Define la **tolerancia**
- Haz clic en **Calcular**
- Analiza la convergencia sin necesidad de derivadas

---

## Estructura del Proyecto

```
PROYECTOFINAL/
├── app.py                          # Aplicación principal (rutas y lógica)
├── requirements.txt                # Dependencias
├── Procfile                        # Configuración para deployment
├── README.md                       # Este archivo
├── templates/
│   ├── base.html                   # Plantilla base
│   ├── index.html                  # Página de inicio
│   ├── biseccion.html              # Interfaz bisección
│   ├── newton.html                 # Interfaz Newton
│   └── secante.html                # Interfaz secante
└── static/
    └── (gráficas generadas aquí)
```

---

## Métodos Implementados

### Bisección
```
Intervalo: [a, b]
Condición: f(a) * f(b) < 0
Punto medio: m = (a + b) / 2
Criterio de parada: |f(m)| < tol o (b - a)/2 < tol
```

### Newton-Raphson
```
Valor inicial: x0
Iteración: x_{n+1} = x_n - f(x_n) / f'(x_n)
Criterio de parada: |f(x_n)| < tol
Ventaja: Convergencia cuadrática (muy rápida)
```

### Secante
```
Valores iniciales: x0, x1
Iteración: x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))
Criterio de parada: |f(x_n)| < tol
Ventaja: No requiere derivada analítica
```

---

## Ejemplos de Funciones

La aplicación incluye funciones de prueba:

- **Bisección:** `f(x) = sin(x) - 0.3x`
- **Newton:** `f(x) = x³ - 5x + 1`
- **Secante:** `f(x) = x³ - x - 1`

Puedes modificar estas funciones directamente en `app.py` para probar otras ecuaciones.

Este proyecto está basado en ejercicios de:

- **Chapra & Canale** - *Métodos Numéricos para Ingenieros* (Problemas de balance de masa)
- **Ezquerro** - *Iniciación a los Métodos Numéricos*
- Contenido académico de **análisis numérico** e **ingeniería computacional**

---
