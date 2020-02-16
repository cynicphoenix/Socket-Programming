# This is the client code
import socket 
import sys

ip = input('Enter ip of server : ')
port = input('Enter Port : ')
welcome_msg = ('-'*20) + 'WELCOME!' + ('-'*20)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((ip, int(port)))
    print('Connection Successful!\n')
    print(welcome_msg)
except:
    print("Connection Error!")
    sys.exit()
    

print("Enter 'EXIT' to terminate!")
username = input('Enter Username : ')
if username == 'EXIT':
    client_socket.send(("EXIT").encode())
    print(client_socket.recv(1024).decode())
else:
    client_socket.send(username.encode())
    print(client_socket.recv(1024).decode())
    password = input('Enter Password : ')
    if password == 'EXIT' :
        client_socket.send(("EXIT").encode())
        print(client_socket.recv(1024).decode())
    else:
        client_socket.send(password.encode())
        print(client_socket.recv(1024).decode())
        validate_bit = client_socket.recv(1024).decode()
        if validate_bit == '0':
            print('Access Denied!')
        else:
            print('Authentication Successful!')
client_socket.close()
print('Socket closed!')