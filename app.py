# from flask import Flask , render_template
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return "AI Prescription Analyzer is running!"

# if __name__== "__main__":
#     app.run(debug=True)

# import pytesseract
# import os
# from PIL import Image

# pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

# img = Image.open("test.png")

# text = pytesseract.image_to_string(img)

# print("Extracted Text:")
# print(text)

from flask import Flask , render_template, request
import pytesseract
import cv2
import os
os.makedirs("static/uploads", exist_ok=True)
app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "prescription" not in request.files:
        return "No file selected"

    file = request.files["prescription"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    text = pytesseract.image_to_string(filepath)
    return render_template("result.html", filename=file.filename, text=text)
if __name__== "__main__":
    app.run(debug=True)