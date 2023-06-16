import socket
import network

# Configurações do ponto de acesso Wi-Fi
SSID = 'MinhaRedeWiFI'  # Nome da rede Wi-Fi
PASSWORD = 'MinhaSenha123'  # Senha da rede Wi-Fi
HOST = '192.168.4.1'  # Endereço IP do servidor (ponto de acesso)

# Configura o ponto de acesso Wi-Fi
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, authmode=network.AUTH_WPA2_PSK, password=PASSWORD)

# Cria o socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao endereço IP e porta
server_socket.bind((HOST, 1234))

# Aguarda por conexões
server_socket.listen(1)

print(f"Aguardando conexões em {HOST}:1234...")

# Aceita uma nova conexão
client_socket, client_address = server_socket.accept()
print(f"Conexão estabelecida com {client_address[0]}:{client_address[1]}")

while True:
    # Recebe dados do cliente
    data = client_socket.recv(1024).decode()

    if not data:
        # Se não houver dados, a conexão foi encerrada
        break

    print(f"Recebido: {data}")

    # Envie uma resposta ao cliente
    response = f"Recebido: {data}"
    client_socket.send(response.encode())

# Encerra a conexão
client_socket.close()
server_socket.close()
