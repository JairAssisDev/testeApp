import requests

url = 'http://localhost:5000/predict'
files = {'file': open('/home/jair/Documentos/testeApp/img1.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())