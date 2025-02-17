# DocuConvert: PDF ↔ DOCX API 🚀

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)  
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)  
![License](https://img.shields.io/badge/License-MIT-yellow.svg)  

## 🔹 Description  
DocuConvert is a simple and efficient API for **PDF ↔ DOCX** file conversion, allowing automation via HTTP requests.  
Built with **Flask**, it uses `pdf2docx` for **PDF → DOCX** conversion and `docx2pdf` for **DOCX → PDF** conversion.  

---

## 🛠 Technologies Used  
- **Python 3.10+**  
- **Flask** (Backend API)  
- **pdf2docx** (PDF to DOCX conversion)  
- **docx2pdf** (DOCX to PDF conversion)  
- **Werkzeug** (File handling)  

---

## 🚀 Installation and Usage  

### 🔹 **1. Clone the repository**  
```sh
git clone https://github.com/your-username/docuconvert.git  
cd docuconvert
```

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
