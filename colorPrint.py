# -*- coding: utf-8 -*-

# Kiírja az állapotnak megfelelő ikont, és utána a szöveget

class colorPrint:
	def errPrint(self, message):
		print('\n[&&&] ' + message)

	def warnPrint(self, message):
		print('\n[*] ' + message)

	def okPrint(self, message):
		print('\n[+] ' + message)

	def finePrint(self, message):
		print('\n[-] ' + message)


	def startPrint(self, IpAddress):
		print('[+] ' + 'Szerver fut: ' + IpAddress)
