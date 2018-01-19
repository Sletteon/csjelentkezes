# -*- coding: utf-8 -*-

# Amikor valaki üzenetet küld, ez az osztály lesz  megfelelő függvénye lesz meghívva
import socket, os

from flask import Flask, request, Response, json, send_from_directory
from flask_cors import CORS

from fileIO import fileIO
from errorHandl import errorHandl
from colorPrint import colorPrint

class onReceiveReq(fileIO, errorHandl):
	def onReceivePageGet(self, clientIP):
		printObj = colorPrint()
		return send_from_directory('www', 'pass.html')

	def onReceiveGet(self, clientIP):
                # colorPrint().finePrint('Adatlekérés: %s' %(clientIP))
                return fileIO().readJSONFormFile('data/data.json')

	def onReceiveChange(self, clientIP):

		gotJSON = request.get_json()
		colorPrint().finePrint('Változtatás: %s' %(clientIP))

		try:
			self.writeJSONToFile('data/data.json', gotJSON)

		except KeyError:
			errorHandl().errorHandling(clientIP)
			return Response(json.dumps({'ERROR': 'JSON ERROR'}), status=422, mimetype='application/json')

		except TypeError:
			errObj.errorHandling(clientIP)
			return Response(json.dumps({'ERROR': 'ERROR READING RECEIVED MESSAGE'}), status=400, mimetype='application/json')

		return Response(json.dumps('SUCCESS'), mimetype='application/json')
	
	def onReceiveReg(self, clientIP):
		gotJSON = request.get_json()
		colorPrint().finePrint('Regisztráció: %s' %(clientIP))
		
		try:
			self.appendJSONToFile('data/data.json', gotJSON)

		except KeyError:
			errorHandl().errorHandling(clientIP)
			return Response(json.dumps({'ERROR': 'JSON ERROR'}), status=422, mimetype='application/json')

		except TypeError:
			errObj.errorHandling(clientIP)
			return Response(json.dumps({'ERROR': 'ERROR READING RECEIVED MESSAGE'}), status=400, mimetype='application/json')

		return Response(json.dumps('SUCCESS'), mimetype='application/json')

	def onReceivePass(self, clientIP, passw):
                gotJSON = request.get_json()
                if fileIO().checkIfPassExists(passw) == True:
                        colorPrint().okPrint('Sikeres bejelentkezés: %s' %(clientIP))
                        return send_from_directory('www', 'index.html')
                else:
                        colorPrint().warnPrint('Hibás próbálkozás: %s' %(clientIP))
                        return Response(json.dumps('Téves jelszó'), mimetype='application/json')


