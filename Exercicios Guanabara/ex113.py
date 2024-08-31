import urllib
import urllib.request

try:
    urllib.request.urlopen("https://www.xvideos.com")
except:
    print('Não consegui acessar o site Xvideos.com')
else:
    print("Consegui acessar o Xvideos.com")