# -*- coding: utf-8 -*-

# Később nem fogja kiírni a hibát, hanem egy logfile-ba jegyzi be
import traceback
from colorPrint import colorPrint
import json

class errorHandl:
	# Fancy módon írja ki, hogy mi a hiba
	# Megjegyzés: azért traceback, mert az megmutatja a sorszámot,
	# ahol a hiba keletkezett
	def errorHandling(self, clientIP):
		printObj = colorPrint()
		printObj.errPrint('Hiba történt egy kliensnél (%s):\n---------------traceback---------------' %(clientIP))
		print(traceback.format_exc())
		print('---------------traceback---------------')

	# Amennyiben egy http-hibát találunk, (szépen) írjuk ki, valamint küldjünk vissza egy választ a hibakóddal
	def RequestError(self, requestObj, errorCode, errorCodeToldalek = '-es'):
		colorPrint().errPrint('%s%s hiba nála: %s' %(str(errorCode), str(errorCodeToldalek), str(requestObj.remote_addr)))
		return json.dumps({'ERROR': str(errorCode) + ' ERROR'})
