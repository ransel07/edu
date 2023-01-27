import requests
import webbrowser

url = "https://oficinavirtual.edeeste.com.do/Login.aspx?ReturnUrl=%2f"
session = requests.Session()

d = webbrowser.open(url)

payload = {'username': 'ransel07@hotmail.es', 'password': ''}
response = session.post(url, data=payload)

if response.status_code == 200:
    print('Inicio de sesión exitoso')
else:
    print('Error al iniciar sesión')

response = session.get('https://example.com/protected-page')
print(response.content)

