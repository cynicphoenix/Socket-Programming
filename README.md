# SOCKET PROGRAMMING
There are four parts corresponding to section 2.<br/>
To execute, open the terminal and go to a specific directory.
<br/>
<br/>
### Part 1 :
How to run ?<br/>
Go to part1 directory and open terminal in that directory.
```bash
python server.py
```
Enter port number(e.g. 1024)<br/><br/>

Open another terminal in the same location.
```bash
python client.py
```
Enter the hostname of server and port number to which server is listening.<br/>
(e.g. hostname = StarkHUB, port = 1024)<br/>
Enter username and password.<br/>
<br/>
<br/>
### Part 2 :
This program allows multiple clients to feature.<br/>
I have implemented it using threads.<br/>
<br/>
How to run ?<br/>
Go to part2 directory and open terminal in that directory.<br/>
```bash
python server.py
```
Enter port number(e.g. 1024)<br/>
<br/>
Open two terminals in the same location.
Run python client.py in both.
```bash
python client.py
```
(Enter the following data in any order.)<br/>
Enter the hostname of server and port number to which server is listening.<br/>
(e.g. hostname = StarkHUB, port = 1024)<br/>
Enter username and password.<br/>
<br/>
<br/>
### Part 3 :
This program allows the client and server programs at two different machines.<br/>
Assumption : Server will be hosted on wifi network. Client will connect to the IP of the server.<br/>
e.g. IP = '172.21.5.133' : Wifi IP of my laptop<br/>
This IP will be printed when server.py will run. Clients need to enter this IP in hostname.<br/>
<br/>
To calculate the medium bandwidth :<br/>
Open the server (e.g. IP = '172.21.5.133')<br/>
Ping this IP with another system and calculate avg-RTT.<br/>
56(84) Bytes data sent and 64 Bytes data received.<br/>
data =  148 Bytes<br/>
avg RTT = 10.7ms<br/>
Bandwidth = data/avg-RTT i.e. nearly 13 MBps<br/>
<br/>
How to run ?<br/>
Go to part3 directory and open terminal in that directory.<br/>
```bash
python server.py
```
Enter port number(e.g. 1024)<br/>
<br/>
Open another terminal in the same location on another machine.<br/>
Run python client.py<br/>
Enter hostname of server and port number to which the server is listening.<br/>
(e.g. hostname = 172.21.5.133, port = 1024)<br/>
Enter username and password.<br/>
<br/>
<br/>
### Part 4 :
Assumption 1 : IP and port of host A,B,C,D are defined at the top in their files.<br/>
If we are changing StarkHUB.rtl file then we need to manually change IP and port at the top.<br/>
Assumption 2 : Exclusive access means only access to some people that is whose attendance > 80%. <br/>
<br/>
How to run ?<br/>
Go to part4 directory and open terminal in that directory.<br/>
To split the file run python splitter.py<br/>
It will split login_credentials.csv in three files login_credentials1.csv,<br/>
login_credentials2.csv, login_credentials3.csv. Host A, B, C will read from these files.<br/>
So if these hosts are running on different machines, we need to provide them with csv files too.<br/>
 <br/>
To calculate percentage run python calculate_attendance.py<br/>
It will store username, percentage in attendance_percentage.csv<br/>
<br/>
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
Enter port number(e.g. 1024)<br/>
<br/>
Open another terminal in the same location on the same/another machine.<br/>
```bash
python client.py
```
Enter the hostname of server and port number to which server is listening.<br/>
(e.g. hostname = 172.21.5.133, port = 1024)<br/>
Enter username and password.<br/>
To quit enter 'EXIT'.<br/>
