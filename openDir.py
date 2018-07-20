import requests
response = requests.post('https://brandonaxellruiz.ml/ecgpnProyects/index.php', data={'Value':'value3'});

if response.text > '0':
 print("Actualizacion exitosa "+response.text) 
else:
 print("Lo sentimos no pudimos actualizar")
