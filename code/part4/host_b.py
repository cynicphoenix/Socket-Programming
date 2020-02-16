import sys
import csv
import socket

ip = '127.0.0.1'
port = 1312
filename = 'login_credentials2.csv' # filename of csv file-name
data = {}


# Read CSV file
def file_read():
    with open(filename,'r') as login_file:
        reader = csv.reader(login_file)
        for row in reader:
            if row[0] != 'Username':
                data[row[0]] = row[1]


# Function to validate authentication
def validate_login(username, password):
    if (data.get(username)) is None:
        return '0'
    elif (data[username] == password):
        return '1'
    else:
        return '0'


# Main Function
def main():
    global ip, port
    file_read()
    # Create socket and bind
    host_b_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        host_b_socket.bind ((ip, port))
    except:
        print("Bind Failed! Error : " + str(sys.exc_info()))
        sys.exit()


    host_b_socket.listen(5)
    print('Socket is now listening!')
    print('-'*40)
    while True:
        try:
            # Connect to a client
            client_socket, address = host_b_socket.accept()
            ip, port = str(address[0]), str(address[1])
            print("Connected with " + ip + " : " + port)
        except:
            print("Connection failed!")
            continue

        # Get username and password
        username = client_socket.recv(1024).decode()
        client_socket.send(('ACK : Username received by Host-B!').encode())
        print('Username received!')
        password = client_socket.recv(1024).decode()
        client_socket.send(('ACK : Password received by Host-B!').encode())
        print('Password received!')
        client_socket.send((validate_login(username, password)).encode())

        client_socket.close()
        print("Connection " + ip + ":" + port + " Closed!")
        print('-'*40)

    host_b_socket.close()
    print('Socket Closed!')
    print('-'*40)

# Run the main function
main()
