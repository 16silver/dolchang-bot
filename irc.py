import socket
import sys
import ssl
import datetime

class IRC:
 
    irc = socket.socket()
  
    def __init__(self):
        self.irc = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
 
    def send(self, chan, msg):
        self.irc.send(bytes("PRIVMSG " + chan + " :" + msg + "\n","utf-8"))
 
    def connect(self, server, botnick):
        #defines the socket
        print ("connecting to:"+server)
        self.irc.connect((server, 16664))  #connects to the server
        self.irc.send(bytes("PASS PASS\n","utf-8"))
        self.irc.send(bytes("USER " + botnick + " " + "0" +" " + "*" + " :Dolchang-bot\n","utf-8")) #user authentication
        self.irc.send(bytes("NICK " + botnick + "\n","utf-8"))
        
    def quit(self, message):
        self.irc.send("QUIT " + message)
        
    def join(self, chan):
        self.irc.send(bytes("JOIN " + chan + "\n", "utf-8"))
 
    def get_text(self):
        text=self.irc.recv(2048)  #receive the text
        if text.strip():
            text=text.decode("utf-8")
 
        if text.find('PING') != -1:                      
            self.irc.send(bytes('PONG ' + text.split() [1] + '\n',"utf-8"))
            print (datetime.datetime.now())
 
        return text
        
    def opping(self, chan, name):
        self.irc.send(bytes("MODE " + chan + " +o " + name + "\n","utf-8"))
