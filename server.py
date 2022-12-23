import sys
import socket
#gets the socket and the address and uses the socket to send the address a messege that the request was illegal
def sendErrorMessage(s,addr):
    s.sendto(b'Illegal request',addr)
    return

#check if the user messege is valid according to the rules of the chat messege types
def isUserMessageValid(user_message):
    #if the user enters an empty messege or if he enters any messege in length of 2 will return false
    #any messsege in length of 2 will be illegal like '2 ' or '3 '    
    if((len(user_message) == 0) or (len(user_message) == 2)):
        return False
    #if the messege contains one character
    elif(len(user_message) == 1):
        #only legal messeges in length 1 is '4' or '5'
        if(user_message[0].isdigit()) and (user_message[0] == '4' or user_message[0]== '5'):
            return True
        #any other messege with one character is not legal
        else:
            return False
    #check if the messege is in format '1 $name' or '2 $message content' or '3 $newname'
    else:
        if((user_message[0] == '1' or user_message[0]== '2' or user_message[0] == '3') and user_message[1] == ' '):
            return True
    #if the message is not in any of those formats it is not legal
    return False
            
#gets a refrence to the users list of messeges,the address of the user and the clients socket

#                 
def sendPendingMessages(s, addr, user_pending_messages):
    #if the user has no pending messages it sends an empty messege to the given address with the given socket and returns
    if len(user_pending_messages) == 0 :
        s.sendto(b'',addr)
        return
    # joins all the messeges to the user in one string with \n delimiter after each message and convert it to bytes
    user_strings = '\n'.join(user_pending_messages)
    user_strings_in_bytes = bytes(user_strings, 'utf-8')
    #send the bytes to the user address with the given socekt
    s.sendto(user_strings_in_bytes,addr)
    #after the messages are sent we clear the messages list
    user_pending_messages.clear()
    return




# if port was not entered as an argument
if(len(sys.argv)<2):
    print("Illegal request")
    exit()
if not sys.argv[1].isnumeric():
    print("Illegal request")
    exit()
if(int(sys.argv[1])>65535):
    print("Illegal request")
    exit()
if(int(sys.argv[1])<1):
    print("Illegal request")
    exit()


#create a socket and bind it to the port number given as an argument    
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',int(sys.argv[1])))

#dictionary to map between addresses and usernames
user_ports={}

#dictionary to map between usernames and their list of strings waiting to be printed
mem ={}


while True:
    data,addr=s.recvfrom(1024)
    user_message=data.decode()

    #if the client sends invalid message, send error messege and finish iteration
    if (not isUserMessageValid(user_message)):
        sendErrorMessage(s,addr)
        continue
    
    type_of_message=int(user_message[0])
    text_message=user_message[2:]

    if type_of_message == 1:
        #if the user wants to register and he is not registered yet
        if text_message not in mem:
            user_names = ', '.join(reversed(mem.keys()))
            user_names_bytes=bytes(user_names, 'utf-8')
            
            #send user the list of all other users in the chat
            s.sendto(user_names_bytes,addr)

            #add the user to the dictionaries
            user_ports[addr]=text_message
            mem[text_message] =[]
            
            #notify the other users that there is a new user
            lst = [user for user in mem.keys() if (user != user_ports[addr])]
            for user in lst:
               mem[user].append(str(user_ports[addr]+" has joined"))
        
        #if the user wants to register but he is already registered
        else:
            sendErrorMessage(s,addr)

            
    elif type_of_message == 2:
        #if the user is not registered
        if addr not in user_ports:
            sendErrorMessage(s,addr)
            
        else:
            #notify all users the message user wrote
            lst = [user for user in mem.keys() if (user != user_ports[addr])]
            for user in lst:
                mem[user].append(str(user_ports[addr]+": "+ text_message))
            
            #send the user his pending messages
            sendPendingMessages(s,addr,mem[user_ports[addr]])
            
    elif type_of_message == 3:
        #if the user is not registered
        if addr not in user_ports:
            sendErrorMessage(s,addr)
        
        else:
            #notify all users the new name of the user
            lst = [user for user in mem.keys() if (user != user_ports[addr])]
            for user in lst:
               mem[user].append(str(user_ports[addr] + " changed his name to " + text_message))
               
            #send the user his pending messages, remove him from dictionary and add him again with the new name   
            sendPendingMessages(s,addr,mem[user_ports[addr]])
            mem.pop(user_ports[addr])
            user_ports[addr]=text_message
            mem[text_message]=[]

    elif type_of_message == 4:
        #if the user is not registered
        if addr not in user_ports:
            sendErrorMessage(s,addr)
        else:
            #notify all users the current user has left the group
            lst = [user for user in mem.keys() if (user != user_ports[addr])]
            for user in lst:
               mem[user].append(str(user_ports[addr]+" has left the group"))

            #remove user from dictionries
            mem.pop(user_ports[addr])
            user_ports.pop(addr)
            s.sendto(b'close',addr)   

    elif type_of_message == 5:
        #if the user is not registered
        if addr not in user_ports:
            sendErrorMessage(s,addr)
        else:
            #send the user his pending messages
            sendPendingMessages(s,addr,mem[user_ports[addr]])
    else:
        sendErrorMessage(s,addr)