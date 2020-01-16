import socket

sock = socket.socket(2, 1) #socket.AF_INET, SOCKET.SOCK_STREAM
#Define the variable. Create a socket object - socket socket.socket(socket_family, socket_kind) We use AF_INET for ipv4 and SOCK_STREAM because we are using TCP

target = input("[+] Enter Target IP: ")
#Defines a variable with user input

def scanner(port):
    try:
        sock.connect((target, port))
        return True
    except:
        return False
#Defines a new function. "try" will ensure that if we run into trouble it wont throw errors

for portNumber in range(1,100):
    print("Scanning Port", portNumber)
    if scanner(portNumber):
        print('[*] Port', portNumber, '/tcp', 'is open')

