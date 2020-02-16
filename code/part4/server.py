# This is the server code
import csv
import socket 
import sys
import traceback
from threading import Thread


# filename of csv-file
filename = 'StarkHUB.rtl'
data = {}


# Function to get IP of wifi 
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def validate_host(ip, port, username, password):
    new_port = str(int(port))
    host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        host_socket.connect((ip, int(port)))
        print("Connected to host "+ip+":"+new_port)
    except:
        print("Connection to host "+ip+":"+new_port+" failed.")
        return 0
    host_socket.send(username.encode())
    print(host_socket.recv(1024).decode())
    host_socket.send(password.encode())
    print(host_socket.recv(1024).decode())
    valid = host_socket.recv(1024).decode()
    host_socket.close()
    print("Connection to host "+ip+":"+new_port+" closed.")
    print('-'*40)
    return valid


# Function to validate authentication
def validate_login(username, password):
    file_reader = open(filename, "r")
    lines = file_reader.readlines()
    flag = 0
    count = 0
    print('-'*40)
    for line in lines:
        host = line[0:line.find('|')]
        ip = line[line.find('|') + 1: line.find('|', line.find('|') + 1)]
        port = line[line.find('|', line.find('|') + 1) + 1:]
        port_new = str(int(port))
        count = count + 1
        if count == 4 :
            break
        flag = flag or int(validate_host(ip, port, username, password))
    file_reader.close()

    if flag == 1:
        # Check attendance
        host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            host_socket.connect((ip, int(port)))
            print("Connected to host "+ip+":"+port_new)
        except:
            print("Connection to host "+ip+":"+port_new+" failed.")
            return '0'
        host_socket.send(username.encode())
        print(host_socket.recv(1024).decode())
        valid = host_socket.recv(1024).decode()
        if valid == '1': 
            return '1'
        else:
            return '0' 
    else:
        return '0'


# Function to start the server
def start_server():
    # Create socket and bind
    host = get_ip_address()
    port = input('Enter Port : ')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind ((host, int(port)))
    except:
        print("Bind failed! error : " + str(sys.exc_info()))
        sys.exit()
    
    
    server_socket.listen(5)
    print("Hostname : " + host)
    print('Socket is now listening...')
    print('*'*40)

    while True:
        # Connect to a client
        client_socket, address = server_socket.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)

        try:
            Thread(target = client, args=(client_socket, ip, port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()
        
    server_socket.close()


# Function to interact with client
def client(client_socket, ip, port):
    # Get username and password
    username = client_socket.recv(1024).decode()
    if username == 'EXIT':
        client_socket.send(('ACK : EXIT received!').encode()) 
        print("EXIT received from "+ip+" : "+port)
    else:
        client_socket.send(('ACK : Username received!').encode())
        print("Username received from "+ip+" : "+port)
        password = client_socket.recv(1024).decode()
        if password == 'EXIT':
            client_socket.send(('ACK : EXIT received!').encode())
            print("EXIT received from "+ip+" : "+port)
        else :
            client_socket.send(('ACK : Password received!').encode())
            print("Password received from "+ip+" : "+port)
            # Validate authentication
            if validate_login(username, password) == '1':
                client_socket.send(('1').encode())
            else:
                client_socket.send(('0').encode())
    # Close client socket
    client_socket.close()
    print("Connection " + ip + " : " + port + " closed!")
    print('*'*40)


# Main function
def main():
    start_server()

# Run the main function
main()