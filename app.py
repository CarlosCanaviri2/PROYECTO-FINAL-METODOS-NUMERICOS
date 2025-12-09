from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# -----------------------------
# Función para guardar gráficas
# -----------------------------
def guardar_grafica(nombre):
    ruta = os.path.join("static", nombre)
    plt.tight_layout()
    plt.savefig(ruta)
    plt.close()
    return ruta

# -----------------------------
# Métodos Numéricos
# -----------------------------
def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("El intervalo no encierra una raíz.")

    historial = []

    for i in range(max_iter):
        m = (a + b) / 2
        fm = f(m)
        historial.append((i + 1, a, b, m, fm))

        if abs(fm) < tol:
            return m, historial

        if f(a) * fm < 0:
            b = m
        else:
            a = m

    return m, historial


def newton(f, df, x0, tol=1e-6, max_iter=100):
    historial = []
    x = x0

    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        historial.append((i + 1, x, fx))

        if abs(fx) < tol:
            return x, historial

        if dfx == 0:
            raise ValueError("La derivada es cero. Newton falla.")

        x = x - fx / dfx

    return x, historial


def secante(f, x0, x1, tol=1e-6, max_iter=100):
    historial = []

    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)

        historial.append((i + 1, x0, x1, f1))

        if abs(f1) < tol:
            return x1, historial

        denom = f1 - f0
        if denom == 0:
            raise ValueError("División por cero en la secante.")

        x2 = x1 - f1 * (x1 - x0) / denom

        if abs(x2 - x1) < tol:
            return x2, historial

        x0, x1 = x1, x2

    return x1, historial


# -----------------------------
# RUTAS DE LA APLICACIÓN
# -----------------------------
@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/biseccion", methods=["GET", "POST"])
def pagina_biseccion():
    resultado = None
    error = None
    grafica = None

    def f(x):
        return np.sin(x) - 0.3 * x

    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            tol = float(request.form["tol"])

            raiz, historial = biseccion(f, a, b, tol)

            xs = np.linspace(a, b, 400)
            ys = f(xs)

            plt.figure()
            plt.axhline(0, color="black")
            plt.plot(xs, ys, label="f(x)")
            plt.plot(raiz, f(raiz), "ro")
            plt.title("Método de la Bisección")

            grafica = guardar_grafica("biseccion.png")

            resultado = {"raiz": raiz, "historial": historial}

        except Exception as e:
            error = str(e)

    return render_template("biseccion.html", resultado=resultado, error=error, grafica=grafica)


@app.route("/newton", methods=["GET", "POST"])
def pagina_newton():
    resultado = None
    error = None
    grafica = None

    def f(x):
        return x**3 - 5*x + 1

    def df(x):
        return 3*x**2 - 5

    if request.method == "POST":
        try:
            x0 = float(request.form["x0"])
            tol = float(request.form["tol"])

            raiz, historial = newton(f, df, x0, tol)

            xs = np.linspace(raiz - 3, raiz + 3, 400)
            ys = f(xs)

            plt.figure()
            plt.axhline(0, color="black")
            plt.plot(xs, ys)
            plt.plot(raiz, f(raiz), "ro")
            plt.title("Método de Newton-Raphson")

            grafica = guardar_grafica("newton.png")

            resultado = {"raiz": raiz, "historial": historial}

        except Exception as e:
            error = str(e)

    return render_template("newton.html", resultado=resultado, error=error, grafica=grafica)


@app.route("/secante", methods=["GET", "POST"])
def pagina_secante():
    resultado = None
    error = None
    grafica = None

    def f(x):
        return x**3 - x - 1

    if request.method == "POST":
        try:
            x0 = float(request.form["x0"])
            x1 = float(request.form["x1"])
            tol = float(request.form["tol"])

            raiz, historial = secante(f, x0, x1, tol)

            xs = np.linspace(min(x0, x1) - 3, max(x0, x1) + 3, 400)
            ys = f(xs)

            plt.figure()
            plt.axhline(0, color="black")
            plt.plot(xs, ys)
            plt.plot(raiz, f(raiz), "ro")
            plt.title("Método de la Secante")

            grafica = guardar_grafica("secante.png")

            resultado = {"raiz": raiz, "historial": historial}

        except Exception as e:
            error = str(e)

    return render_template("secante.html", resultado=resultado, error=error, grafica=grafica)


if __name__ == "__main__":
    if not os.path.exists("static"):
        os.makedirs("static")
    app.run(debug=True)
