import sys
import socket
#checks if there are at least two arguments (one for ip address and one for port number) 
if(len(sys.argv)<3):
    print("Illegal request")
    exit()
#checks if the second argument is a number
if not sys.argv[2].isnumeric(): 
    print("Illegal request")
    exit()
#checks if the given port number is in the range of port numbers
if(int(sys.argv[2])>65535):
    print("Illegal request")
    exit()
if(int(sys.argv[2])<1):
    print("Illegal request")
    exit()
    

#create a socket that works in ipv4 and with udp protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address=sys.argv[1]
port_number=int(sys.argv[2])


while True:
    #get a message from the user
    user_input = input()

    #convert the string the user wrote to bytes
    userInputInBytes=bytes(user_input,'utf-8')
    
    #send the string to the wrote to the server
    s.sendto(userInputInBytes, (ip_address,port_number))

    #receive the response from the server to the client's request
    data,addr=s.recvfrom(1024)

    #if the client(user) wants to leave the group chat
    if(user_input == '4'):
        s.close()
        exit(0)

    #print the data from the server
    if(len(data)>0):
        print(data.decode())
