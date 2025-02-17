# DocuConvert-PDF-to-DOCX-API

This is a simple and efficient API for converting files between PDF, DOCX, PPTX, and TXT formats. It is built using **Flask** and provides a user-friendly interface to easily upload and convert files. It also supports various formats for both input and output, making it a versatile tool for document conversion.

## Features

- Convert **PDF to DOCX**.
- Convert **DOCX to PDF**.
- Convert **PPTX to PDF**.
- Convert **PDF to TXT**.
- Convert **DOCX to TXT**.
- Beautiful **UI** for easy use and multiple format selections.

## Tech Stack

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, JavaScript (using Flask's rendering system)
- **File Conversion**: `pdf2docx`, `python-pptx`, `python-docx`, `PyPDF2`
- **Storage**: Temporary file storage for uploaded documents
- **Libraries**: Flask, werkzeug, pdf2docx, python-pptx, python-docx, PyPDF2

## 🚀 Installation and Usage  

### 🔹 **1. Clone the repository**  
```sh
git clone https://github.com/<your_username>/DocuConvert-PDF-to-DOCX-API.git  
cd DocuConvert-PDF-to-DOCX-API


### 🔹 **2. Create a virtual environment and install dependencies**  
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 🔹 **3. Run the server**  
```sh
python app.py
```
The server will be available at **http://127.0.0.1:5000**.

---

## 📡 API Usage  

### 🔹 Convert PDF to DOCX (`/convert/pdf-to-docx`)  
- **Method:** `POST`  
- **Form-data:** `file` (PDF file to convert)  

#### Example using cURL:  
```sh
curl -X POST -F "file=@document.pdf" http://127.0.0.1:5000/convert/pdf-to-docx -o converted.docx
```

#### Example using Python (requests):  
```python
import requests

url = "http://127.0.0.1:5000/convert/pdf-to-docx"
files = {"file": open("document.pdf", "rb")}
response = requests.post(url, files=files)

if response.status_code == 200:
    with open("converted.docx", "wb") as f:
        f.write(response.content)
    print("Conversion completed!")
else:
    print("Error:", response.json())
```

---

### 🔹 Convert DOCX to PDF (`/convert/docx-to-pdf`)  
- **Method:** `POST`  
- **Form-data:** `file` (DOCX file to convert)  

#### Example using cURL:  
```sh
curl -X POST -F "file=@document.docx" http://127.0.0.1:5000/convert/docx-to-pdf -o converted.pdf
```

#### Example using Python (requests):  
```python
import requests

url = "http://127.0.0.1:5000/convert/docx-to-pdf"
files = {"file": open("document.docx", "rb")}
response = requests.post(url, files=files)

if response.status_code == 200:
    with open("converted.pdf", "wb") as f:
        f.write(response.content)
    print("Conversion completed!")
else:
    print("Error:", response.json())
```

---

## 📌 Future Improvements  
✅ Support for multiple file conversions per request  
✅ Cloud storage integration   

---

## 📜 License  
This project is licensed under the **MIT License**.
