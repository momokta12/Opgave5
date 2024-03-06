import socket
import threading
import json
import random

serverHOST = '127.0.0.1'
serverPORT = 17829
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((serverHOST, serverPORT))
server.listen(5)

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    data = conn.recv(1024).decode()
    try:
        request = json.loads(data) 
        method = request.get("method")
        tal1 = request.get("Tal1")
        tal2 = request.get("Tal2")

        if method and tal1 is not None and tal2 is not None:
            if method == 'Random':
                result = random.randint(tal1, tal2)
            elif method == 'Add':
                result = tal1 + tal2
            elif method == 'Subtract':
                result = tal1 - tal2
            else:
                raise ValueError("Invalid method")
            response = json.dumps({"result": result})  
        else:
            raise ValueError("Missing data in request")

    except (ValueError, json.JSONDecodeError) as e:
        response = json.dumps({"error": str(e)})

    conn.sendall(response.encode())
    conn.close()

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
