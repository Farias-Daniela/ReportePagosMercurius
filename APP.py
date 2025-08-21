from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB (opcional)

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "txt"}  # ajusta a gusto
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return '''
    <h2>Subir un archivo</h2>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="archivo" />
        <input type="submit" value="Subir" />
    </form>
    '''

@app.route("/upload", methods=["POST"])
def upload_file():
    if "archivo" not in request.files:
        return "No seleccionaste ningún archivo", 400

    file = request.files["archivo"]
    if file.filename == "":
        return "Nombre de archivo vacío", 400

    if not allowed_file(file.filename):
        return "Tipo de archivo no permitido", 400

    save_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(save_path)
    return f"Archivo {file.filename} subido correctamente!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

