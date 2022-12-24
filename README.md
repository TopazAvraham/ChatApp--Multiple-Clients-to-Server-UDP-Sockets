<h4 align="center">


![](https://github.com/TopazAvraham/IntroductionToCS-University-C-programming/blob/master/Screenshots/31.png?raw=true)

</h4>

<h4 align="center">Implementation of client & server code which acts similar to WhatsApp groups!</h4>

<p align="center">
  <a href="##Introduction">Introduction</a> •
  <a href="#Screenshots">Implementation</a> •
   <a href="#Screenshots">Example</a> •
  <a href="#Installation">Installation</a> •
  <a href="#Author">Author</a> •
  <a href="#Support">Support</a> 

</p>

<p align="center">
  <img width="600" height="500" src="Images/12.gif">
</p>


## Introduction

This Server & Client code is the final product of computer-networks course assignment, which I took in the 1st semester of my 2nd year at Bar Ilan University.  
I created WhatsApp-like implementation of groups, where each user (client) can:


💥 Join the group

💥 Send messages to all other members of the group.

💥 Change his name for future messages

💥 Get notifications about other people's activity in the group- when someone else has joined, sent a message, left the group, etc.


## Implementation

Our chat will act similar to a Whatsapp group, in which each member can write a message, and every message someone writes is sent to all other memebers <br>
When someone is sending a message, the message is being sent to the server immediately. Yet, the server sents the message to the clients only when they reach out the server. <br>

For example: Alice, Bob, and Charlie are members in the group. Alice sent a message. The message needs to be sent to Bob and Charlie, <br>
but they will receive Alice's messgae only when they ask for it explicitly from the server, or if they will send a message to the server so he will send them back all their waiting messages. <br>

Our server is establishing a socket and listens on the port which he receives as an argument from CLI.<br>
<b>The server can receive 5 different types of messages:</b><br> <br>

1. <b>Register- Client which sends this message, wants to join the group chat.</b> <br>
    The message will be in the following format: 1 [Name]<br>
    
    The server keeps details of the client's name and socket details, and sends all other members the message: [Name] has joined.<br>
    Also, the server sends to the client who asked to join all names of the existing members in the group. <br><br><br>
       
2. <b>Sending a message-  Client wants to send a message to all other members in the group.</b><br>
    The message will be in the following format: 1 [Name]: [Message]<br><br><rb>
  
3. <b>Change of name- Client which sends this message, wants to change his name in the group.</b><br>
    The message will be in the following format: 3 [Name]<br>
    
    When the server recieves this type of message, it sends all other members the message: [Old Name] changed his name to [New Name].<br><br>
  
4. <b>leaving the group- Client which sends this message, wants to leave the group.</b><br>
    The message will be in the following format: 4<br>
    
    When the server recieves this type of message, it sends all other members the message: [Name] has left the group.<br><br>
  
 5. <b>Get new info- Client which sends this message, wants to get notification abut all new messages since his last update. </b><br>
    The message will be in the following format: 5<br>
    
    When the server recieves this type of message, it sends the client 1 message that contain all the messages <br> 
  that were supposed to be sent to him since the last time <br><br>
    

## Example
  <b>
    1. Alice registered. <br>
    2. Bob registered. <br>
    3. Bob sent a message.<br>
    4. Display so far:<br>
    <p align="left">
  <img width="600" height="600" src="Images/2.png">
</p>
    5. Charlie registered.<br>
    6. Charlie sent 2 messages.<br>
    7. Display so far:<br>
    
    8. Alice asked for update.<br>
    9. Display so far:<br>
    
    10. Alice sent a message.<br>
    11. Alice sent invalid message.<br>
    12. Charlie changed his name.<br>
    13. Charlie sent a message.<br>
    14. Display so far:<br>
    
    15. Charlie left.<br>
    16. Bob sent a message.<br>
    17. Alice asked for update.<br>
    18. Display so far:<br>
    
    
  <p align="left">
  <img width="600" height="600" src="Images/2.png">
</p>
  

## Installation
### Option 1 - Without Ant
1. Clone the repository:
    ```
    git clone https://github.com/TopazAvraham/Arkanoid.git
    ```

2. Open the project from an IDE such as Intellij, Eclipse, etc.
3. Add the biu-oop.jar file as a global library to the Arkanoid project.
4. Make sure an updated JDK is set in the configuration, and the src folder of Arkanoid is set as the source root.
5. Create a configuration with Ass6.java as the Main Class, run it, and enjoy!



### Option 2 - With Ant
1. Clone the repository:
    ```
    git clone https://github.com/TopazAvraham/Arkanoid.git
    ```
2. Install [Apache Ant](https://ant.apache.org/bindownload.cgi) 
 
   if you're having difficulties with the Ant installation proccess, you can click [here](https://www.youtube.com/watchv=3eaW81yYIqY&t=353s&ab_channel=xscourse) for help. 

<br /> 

3. Open CMD in the cloned directory and run this command:
    ```
    ant run
    ```

## Built With

- Java

<br />

## Author

**Topaz Avraham**

- [Profile](https://github.com/TopazAvraham?tab=repositories )
- [Email](mailto:topazavraham9@gmail.com?subject=Hi "Hi!")
- [LinkedIn](https://www.linkedin.com/in/topaz-avraham-68b340208/ "Welcome")

## 🤝 Support

Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!
