from flask import Flask, request, jsonify
from main import teste
import os

app = Flask(__name__)

@app.route('/analise', methods=['POST'])
def analisar_imagem():
    # Verifica se um arquivo de imagem foi enviado na requisição
    if 'imagem' not in request.files:
        return jsonify({'error': 'Nenhum arquivo de imagem enviado'})

    imagem = request.files['imagem']
    
    # Verifica se o arquivo é uma imagem
    if not allowed_file(imagem.filename):
        return jsonify({'error': 'Arquivo inválido. Apenas imagens são permitidas'})

    # Salva a imagem temporariamente em um local
    caminho_temporario = save_temporary_image(imagem)
    
    # Executa a função de teste com a imagem
    resultado = teste(caminho_temporario)
    
    # Remove a imagem temporária após o processamento
    remove_temporary_image(caminho_temporario)
    
    return jsonify(resultado)

def allowed_file(filename):
    # Verifica a extensão do arquivo permitida (por exemplo, apenas imagens JPEG ou PNG)
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_temporary_image(imagem):
    # Verifica se o diretório temporário existe, se não, crie-o
    diretorio_temporario = '/home/jair/Documentos/testeApp/temp/'
    os.makedirs(diretorio_temporario, exist_ok=True)

    # Gera um nome único para o arquivo de imagem temporário
    nome_arquivo_temporario = 'imagem_temp.jpg'
    caminho_temporario = os.path.join(diretorio_temporario, nome_arquivo_temporario)

    # Salva a imagem no diretório temporário
    imagem.save(caminho_temporario)

    return caminho_temporario

def remove_temporary_image(caminho_temporario):
    # Remove a imagem temporária após o processamento
    # Por exemplo, exclui o arquivo do diretório 'temp'
    os.remove(caminho_temporario)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
