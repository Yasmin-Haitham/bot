from rivescript import RiveScript
#unicode for Arabic language

Bot = RiveScript(utf8= True)

#load directories
Bot.load_directory("brain")
Bot.sort_replies()

#bot reply function
while True:
    msg = str(input("User: "))
    reply = str(Bot.reply('localuser' , msg)) 
    if msg =="quit":
       break
    else:
        print('Bot: ' + reply)