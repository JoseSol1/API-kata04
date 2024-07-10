import requests

url = 'http://localhost:5000/convert'
matrix_data = "4 4\n*...\n....\n.*..\n....\n3 3\n*.*\n**.\n.*.\n0 0"

response = requests.post(url, data=matrix_data)
if response.status_code == 200:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
