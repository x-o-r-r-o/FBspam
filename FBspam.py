import os, time, fbchat
from fbchat import Client
from getpass import getpass

def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear')

def main():

	print ('''

Наш уютный Телеграм: @Termuxtop
·▄▄▄▄▄▄▄· .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. 
▐▄▄·▐█ ▀█▪▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪
██▪ ▐█▀▀█▄▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·
██▌.██▄▪▐█▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌
▀▀▀ ·▀▀▀▀  ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀

	''')

	username = input ('Твой логин:')
	client = fbchat.Client (username, getpass('Твой пароль:'))

	name = str (input('Имя жертвы:'))

	friends = client.searchForUsers (name)
	friend = friends[0]
	msg = str (input('Сообщение:'))

	while True:

		try:
			sent = client.send (fbchat.models.Message(msg), friend.uid)
			print ('Отправлено пользователю ' + name)
			time.sleep (4)

		except:
			print ('Сообщение не отправлено :(')

if __name__ == '__main__':
	clear()
	main()
