

from flask import Flask, render_template, request
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image
import os

# Create Flask app FIRST
app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "prescription" not in request.files:
        return "No file uploaded"

    file = request.files["prescription"]

    if file.filename == "":
        return "No selected file"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    img = Image.open(filepath)
    text = pytesseract.image_to_string(img)

    print("Extracted Text:", text)

    return render_template("result.html", extracted_text=text, filename=file.filename)


if __name__ == "__main__":
    app.run(debug=True)