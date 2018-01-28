# -*- coding: utf-8 -*-

# Amikor valaki üzenetet küld, ez az osztály lesz  megfelelő függvénye lesz meghívva
import socket, os

from flask import Flask, request, Response, json, send_from_directory
from flask_cors import CORS

from errorHandl import errorHandl
from colorPrint import colorPrint
from dbIO import dbIO

class onReceiveReq(errorHandl, dbIO):


	def onReceivePageGet(self, clientIP):
		printObj = colorPrint()
		return send_from_directory('www', 'index.html')

	def onReceiveChangeGET(self, clientIP, email):
		if '%' in email:
			return Response(json.dumps({'data':'Biztonsági okokból a "%" le van tiltva'}))
		if '@' not in email:
			return Response(json.dumps({'data':'Nem érvényes e-mail cím'}))
		colorPrint().finePrint('Adat lekérése |%s| e-mail címen: %s' %(email, clientIP))
		return Response(json.dumps({'data':self.searchAndReturnColumn(self.getdbIp(), email)}), mimetype='application/json')

	def onReceiveChangePOST(self, clientIP, email):
		gotJSON = request.get_json()
		colorPrint().finePrint('Adatváltoztatás |%s| e-mail címen: %s' %(email, clientIP))
		self.updateWithJSON(self.getdbIp(), email, gotJSON['data'])
		return Response(json.dumps('Sikeres változtatás'), mimetype='application/json')
