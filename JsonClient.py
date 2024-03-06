import socket
import json

serverHOST = '127.0.0.1'
serverPORT = 17829
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverHOST, serverPORT))

method = input("Enter method (Random, Add, Subtract): ")
tal1 = int(input("Enter first number (Tal1): "))
tal2 = int(input("Enter second number (Tal2): "))

request = json.dumps({"method": method, "Tal1": tal1, "Tal2": tal2})  
client.sendall(request.encode())

response = client.recv(1024).decode()
response_data = json.loads(response)  

if "result" in response_data:
    print(f"Result: {response_data['result']}")
else:
    print(f"Error: {response_data['error']}")

client.close()
