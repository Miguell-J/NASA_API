import requests
import json
import webbrowser

# fazer um request na api da nasa com a biblioteca requests
API_key = 'fly44jxvZPU9d383v527pNZefOCy8quIuiI5wmho' # api_key da api da nasa
url = 'https://api.nasa.gov/planetary/apod' # url do site da "apod" da nasa (astronomic picture of the day)

# paremetros do request
parametros = {
    'api_key':API_key, # chave da api
    'hd':'True', # qualidade da foto (True)
    'date':'2023-10-03' # data da foto
}

# captar a resposta com base no url e nos paremetros criados
resposta = requests.get(url,params=parametros)
# pegar os dados em json
json_data = json.loads(resposta.text)
url_imagem = json_data['hdurl']
# abrir a url da imagem
webbrowser.open(url_imagem)

