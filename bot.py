from irc import *
from carddb import *
import os
import random


channellist = []
server = "irc.uriirc.org"
nickname = "botcheckingbot"

irc = IRC()
irc.connect(server, nickname)

def hssearch(word):
    nummode = 0
    thelist = []
    longnamelist = []
    if not word:
        return "usage: hs [num] <word>"
    if word[0] == "-":
        if word[1].numeric():
            word = word[1:]
    if word[0:2] == "+ ":
        print(len(word))
        if len(word) != len("+ 한"):
            return "한글 글자 1개만 허용됩니다."
        word = word[2:]
        for i in range(len(cardnamelist)):
            if cardnamelist[i][0:len("한")] == word:
                idx = cardnamelist[i].find("(")
                longnamelist.append(cardnamelist[i][0:idx].replace(" ","").strip())
        if len(longnamelist) == 0:
            return word + "(으)로 시작하는 하스스톤 카드는 없습니다."
        longnamelist.sort(key = lambda x: len(str(x)),reverse = True)
        if len(longnamelist) < 9:
            rtvalue = longnamelist[0]
            for i in longnamelist[1:]:
                rtvalue = rtvalue + ", " + i
            return rtvalue
        rtvalue = longnamelist[0]
        for i in longnamelist[1:9]:
            rtvalue = rtvalue + ", " + i
        return rtvalue + ",..."
    while word and word[0].isnumeric():
        nummode = nummode * 10 + int(word[0])
        word = word[1:]
    word = word.strip()
    for i in range(len(cardnamelist)):
        if (cardnamelist[i].lower()).find(word.lower()) != -1:
            thelist.append(i)
    if len(thelist) == 1:
        return cardlist[thelist[0]].name + " - " + cardlist[thelist[0]].description
    elif len(thelist) == 0:
        return "card not found"
    elif nummode > 0:
        if len(thelist) < nummode:
            nummode = len(thelist)
        return cardlist[thelist[nummode-1]].name + " - " + cardlist[thelist[nummode-1]].description
    elif len(thelist) > 9:
        rtvalue = cardnamelist[thelist[0]]
        for j in thelist[1:5]:
            rtvalue = rtvalue + ", "  + cardnamelist[j]
        return rtvalue + ", ... (+" + str(len(thelist)-5) + ") 너무 많아요 ㅇㅅㅇ"
    else:
        rtvalue = cardnamelist[thelist[0]]
        for j in thelist[1:]:
            rtvalue = rtvalue + ", "  + cardnamelist[j]
        return rtvalue
    
def innkeeper():
    inntxt = open("innkeeperdb.txt",'r')
    idx = random.randrange(50)
    for i in range(idx):
        ret = inntxt.readline()
    return ret

print ("Success")
 
while 1:
    text = irc.get_text()
    print(text)
    for channel in channellist:
        idx = text.find("PRIVMSG " + channel + " :")
        if idx != -1:
            msg = text[idx + len("PRIVMSG " + channel + " :"):len(text)]
            print (msg)
            if msg[0:3] == "hs ":
                irc.send(channel, str(hssearch((msg[3:len(msg)]).strip())))
            
            elif msg[0:5] == "echo ":
                irc.send(channel, str(msg[5:len(msg)]))
                
            elif msg[0:len("bayoen " + nickname)] == "bayoen " + nickname:
                break
            
            elif "하스스톤" in msg:
                irc.send(channel, innkeeper())
    idx2 = text.find("INVITE " + nickname)
    if idx2 != -1:
        msg = text[idx2 + len("INVITE " + nickname + " :"):len(text)]
        print (msg)
        irc.join(msg)
        msg = msg.replace("\r", "").replace("\n","")
        if msg not in channellist:
            channellist += [msg]
        print(channellist)
    
    # idx2 = text.find("JOIN :" + channel)
    # if idx2 != -1:
    #     pmidx = text.find("!")
    #     irc.opping(channel, text[1:pmidx])
        
