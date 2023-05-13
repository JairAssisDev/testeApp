import os
from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

# carrega o modelo
model = tf.keras.models.load_model('model')

# configuração das dimensões da imagem
image_width = 160
image_height = 160
image_color_channel = 3
image_size = (image_width, image_height)
image_shape = image_size + (image_color_channel,)

# função para fazer a previsão do modelo
def predict(image_file):
    image = tf.keras.preprocessing.image.load_img(image_file, target_size=image_size)
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.expand_dims(image, 0)
    prediction = model.predict(image)[0][0]
    return {'prediction': prediction, 'class': 'cat' if prediction < 0.5 else 'dog'}

# rota para fazer a previsão
@app.route('/predict', methods=['POST'])
def predict_route():
    if 'image' not in request.files:
        print(request.files)
        return jsonify({'error': 'no image file'})
        
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'no image file'})
    image_file = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(image_file)
    prediction = predict(image_file)
    return jsonify(prediction)

# rota para verificar se a API está funcionando
@app.route('/health')
def health_check():
    return 'API está funcionando'

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = './uploads'
    app.run(debug=True)


