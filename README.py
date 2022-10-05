# conex-o-cliente-e-servidor-parte-cliente
Conexão cliente e sevidor parte cliente
import socket

# Server address
ip = '0.0.0.0'
# Server port
port = 8888


# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
sock.connect((ip, port))

# Message
message = '...'.encode()

# Send message
sock.send(message)

# Receiving response from the server
reply = sock.recv(9000)
print(reply)
