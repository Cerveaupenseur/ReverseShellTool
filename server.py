import socket
from threading import Thread


host = 'localhost'
port = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print(f"Serveur en ligne sur le port {host}, sur le port {port}.")

clients = []


def gestion(client):
    while True:
        for client in clients:
            try:
                action = input(">")
                client.send(action.encode('utf-8'))



            except:
                clients.remove(client)
                print(clients)
                client.close()
                break
                

def recoit():
    while True:

        client, address = server.accept()
        clients.append(client)
        print(client)
        


        thread = Thread(target=gestion, args=(client, ))
        thread.start()


recoit()
