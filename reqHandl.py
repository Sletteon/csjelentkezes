# -*- coding: utf-8 -*-

# Amikor valaki üzenetet küld, ez az osztály lesz  megfelelő függvénye lesz meghívva
import socket, os

from flask import Flask, request, Response, json, send_from_directory
from flask_cors import CORS

from fileIO import fileIO
from errorHandl import errorHandl
from colorPrint import colorPrint
from dbIO import dbIO

class onReceiveReq(fileIO, errorHandl, dbIO):

	def onReceivePageGet(self, clientIP):
		printObj = colorPrint()
		return send_from_directory('www', 'index.html')

	def onReceiveChangeGET(self, clientIP, email):
		colorPrint().finePrint('Adat lekérése %s e-mail címen: %s' %(email, clientIP))
		# return fileIO().readDataFromFile('data/data.txt', email)
		return self.searchAndReturnColumn('192.168.1.137', email)

	def onReceiveChangePOST(self, clientIP, email):
		gotJSON = request.get_json()
		colorPrint().finePrint('Adatváltoztatás %s e-mail címen: %s' %(email, clientIP))
		fileIO().setDataToFile('data/data.txt', email, gotJSON)
		return Response(json.dumps('Sikeres változtatás'), mimetype='application/json')
