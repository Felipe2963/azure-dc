from flask import Flask, send_from_directory

app = Flask(__name__)

# Servir imágenes desde la carpeta "images"
@app.route("/images/<path:filename>")
def images(filename):
    return send_from_directory("images", filename)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Despliegue Continuo</title>
        </head>

        <body style="
            background-color: #16213e;
            color: white;
            text-align: center;
            font-family: Arial;
            padding-top: 60px;
        ">

            <h1>Despliegue Continuo Exitoso</h1>

            <h2>Flask + GitHub + Azure</h2>

            <p>La aplicación se actualizó automáticamente.</p>

            <p>Versión 3.0</p>

            <hr style="width: 60%; margin: 40px auto;">

            <h2>Imagen del proyecto</h2>

            <img
                src="/images/logo.png"
                alt="Imagen del proyecto"
                style="
                    width: 500px;
                    max-width: 90%;
                    height: auto;
                    border-radius: 12px;
                    border: 3px solid white;
                    margin-top: 15px;
                "
            >

        </body>
    </html>
    """


if __name__ == "__main__":
    app.run()