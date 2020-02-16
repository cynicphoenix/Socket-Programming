# SOCKET PROGRAMMING
There are four parts corresponding to section 2.
To execute, open the terminal and go to a specific directory.


### Part 1 :
How to run ?
Go to part1 directory and open terminal in that directory.
```bash
python server.py
```
Enter port number(e.g. 1024)

Open another terminal in the same location.
```bash
python client.py
```
Enter the hostname of server and port number to which server is listening.
(e.g. hostname = StarkHUB, port = 1024)
Enter username and password.


### Part 2 :
This program allows multiple clients to feature.
I have implemented it using threads.

How to run ?
Go to part2 directory and open terminal in that directory.
```bash
python server.py
```
Enter port number(e.g. 1024)

Open two terminals in the same location.
Run python client.py in both.
```bash
python client.py
```
(Enter the following data in any order.)
Enter the hostname of server and port number to which server is listening.
(e.g. hostname = StarkHUB, port = 1024)
Enter username and password.


### Part 3 :
This program allows the client and server programs at two different machines.
Assumption : Server will be hosted on wifi network. Client will connect to the IP of the server.
e.g. IP = '172.21.5.133' : Wifi IP of my laptop
This IP will be printed when server.py will run. Clients need to enter this IP in hostname.

To calculate the medium bandwidth :
Open the server (e.g. IP = '172.21.5.133')
Ping this IP with another system and calculate avg-RTT.
56(84) Bytes data sent and 64 Bytes data received.
data =  148 Bytes
avg RTT = 10.7ms
Bandwidth = data/avg-RTT i.e. nearly 13 MBps

How to run ?
Go to part3 directory and open terminal in that directory.
```bash
python server.py
```
Enter port number(e.g. 1024)

Open another terminal in the same location on another machine.
Run python client.py
Enter hostname of server and port number to which the server is listening.
(e.g. hostname = 172.21.5.133, port = 1024)
Enter username and password.


### Part 4 :
Assumption 1 : IP and port of host A,B,C,D are defined at the top in their files.
If we are changing StarkHUB.rtl file then we need to manually change IP and port at the top.
Assumption 2 : Exclusive access means only access to some people that is whose attendance > 80%. 

How to run ?
Go to part4 directory and open terminal in that directory.
To split the file run python splitter.py
It will split login_credentials.csv in three files login_credentials1.csv,
login_credentials2.csv, login_credentials3.csv. Host A, B, C will read from these files.
So if these hosts are running on different machines, we need to provide them with csv files too.
 
To calculate percentage run python calculate_attendance.py
It will store username, percentage in attendance_percentage.csv

Now run in terminal run on same/different machines :
```bash
python host_a.py
python host_b.py
python host_c.py
python host_d.py
````

After that, open another terminal in the same location on the same/another machine.
```bash
python server.py
```
Enter port number(e.g. 1024)

Open another terminal in the same location on the same/another machine.
```bash
python client.py
```
Enter the hostname of server and port number to which server is listening.
(e.g. hostname = 172.21.5.133, port = 1024)
Enter username and password.
To quit enter 'EXIT'.
