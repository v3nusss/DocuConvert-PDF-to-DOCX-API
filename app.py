from flask import Flask, render_template, request, send_file
import os
from converter import docx_to_pdf, pdf_to_docx, pdf_to_txt, docx_to_txt, pptx_to_pdf  # As funções de conversão

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    conversion_type = request.form['conversion_type']
    files = request.files.getlist('file')

    # Checa se o diretório de uploads existe, se não cria
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Loop para processar múltiplos arquivos
    for file in files:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        
        # Chama a função de conversão correspondente
        if conversion_type == 'pdf_to_docx':
            pdf_to_docx(filename)
            return send_file(filename.replace('.pdf', '.docx'), as_attachment=True)
        
        elif conversion_type == 'docx_to_pdf':
            docx_to_pdf(filename)
            return send_file(filename.replace('.docx', '.pdf'), as_attachment=True)
        
        elif conversion_type == 'pdf_to_txt':
            txt_file = pdf_to_txt(filename)
            return send_file(txt_file, as_attachment=True)
        
        elif conversion_type == 'docx_to_txt':
            docx_to_txt(filename)
            return send_file(filename.replace('.docx', '.txt'), as_attachment=True)
        
        elif conversion_type == 'pptx_to_pdf':
            pptx_to_pdf(filename)
            return send_file(filename.replace('.pptx', '.pdf'), as_attachment=True)

    return 'Conversion Completed'

if __name__ == '__main__':
    app.run(debug=True)
