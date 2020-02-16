import sys
import csv
import socket

ip = '127.0.0.1'
port = 3103
filename = 'attendance_percentage.csv' # filename of csv file-name
data = []
ex = 80


# Read CSV file
def file_read():
    with open(filename,'r') as login_file:
        reader = csv.reader(login_file)
        fields = reader.__next__() 
        for row in reader:
            data.append(row)


# Calculate attendance
def attendance(username) :
    att = 0
    for row in data:
        if(row[0] == username):
            att = float(row[1])
            break
    if att >= ex:
        return '1'
    return '0'


# Main Function
def main():
    global ip, port
    file_read()
    # Create socket and bind
    host_d_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        host_d_socket.bind ((ip, port))
    except:
        print("Bind Failed! Error : " + str(sys.exc_info()))
        sys.exit()


    host_d_socket.listen(5)
    print('Socket is now listening!')
    print('-'*40)
    while True:
        try:
            # Connect to a client
            client_socket, address = host_d_socket.accept()
            ip, port = str(address[0]), str(address[1])
            print("Connected with " + ip + " : " + port)
        except:
            print("Connection failed!")
            continue

        # Get username and password
        username = client_socket.recv(1024).decode()
        client_socket.send(('ACK : Username received by Host-D!').encode())
        print('Username received!')
        client_socket.send((attendance(username).encode()))

        client_socket.close()
        print("Connection " + ip + ":" + port + " closed!")
        print('-'*40)

    host_d_socket.close()
    print('Socket Closed!')
    print('-'*40)


# Run main
main()

        

