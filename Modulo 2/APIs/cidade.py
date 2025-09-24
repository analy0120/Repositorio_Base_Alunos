import requests 

usuario = {
    "name":"analy",
}

response = requests.post(
    'https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos',
      json=usuario)
'''response = requests.delete(
    'https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos/11')'''                                                         
     
print(response.status_code)
                                                                                     

                                                                                    