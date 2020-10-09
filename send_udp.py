import socket
msgFromClient       = '{"trace.id":"1234533-555","id":"udp01"}'
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 5160)
bufferSize          = 1024
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
print('END')
