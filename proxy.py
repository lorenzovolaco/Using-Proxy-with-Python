import requests

proxies = {
    'https': 'https://2.139.62.85:3128' #insira o tipo de proxy, o ip do proxy junto com o port(ip:port).

}

response = requests.get("https://ipinfo.io/json", proxies=proxies)
print(response.json()['country'])#informações
print(response.json()['region'])
print(response.text)





