#imprimindo arquivo da internet 

from urllib.request import urlopen
import json

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]


print('Titulo:', data['title'])
print('URL:', data ['url'])
print('Duralçao:', data['duration'])
print('Número de visualizações:', data['stats_number_of_plays'])

