#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# [+] Hiba nélkül történt valami (zöld)
# [-] Semmi extra (kék)
# [*] Nem végzetes hiba (sárga)
# [&&&] Végzetes hiba (piros, alig látszik)

# Standard könyvárak
import os, logging, socket, sys

# Hozzáadott könyvárak
from flask import Flask, request, Response
from flask_cors import CORS

# Saját osztáyok
from fileIO import fileIO
from reqHandl import onReceiveReq
from colorPrint import colorPrint
from errorHandl import errorHandl

# Ne látszódjanak a werkzeug (többek között HTTP-log) cuccai
logging.getLogger('werkzeug').setLevel(logging.WARNING)

app = Flask(__name__)
# Kell, ha nincs akkor kliens hibát kap
CORS(app, resources={r'/*': {'origins': '*'}})

@app.errorhandler(404)
def badRequest(e):
	return Response(errorHandl().RequestError(request, 404), status=404, mimetype='application/json')

@app.errorhandler(400)
def badRequest(e):
	return Response(errorHandl().RequestError(request, 400, errorCodeToldalek = '-as'), status=400, mimetype='application/json')

@app.errorhandler(500)
def badRequest(e):
	return Response(errorHandl().RequestError(request, 500, errorCodeToldalek = '-as'), status=500, mimetype='application/json')


@app.route('/', methods=['GET'])
def index():
	# Csatlakozott kliens IP-címe
	clientIP = request.remote_addr
	return onReceiveReq().onReceivePageGet(clientIP)

@app.route('/valtoztat/<email>', methods=['GET', 'POST'])
def valtoztat(email):
	clientIP = request.remote_addr
	if request.method == 'GET':
		return onReceiveReq().onReceiveChangeGET(clientIP, email)
	else:
		return onReceiveReq().onReceiveChangePOST(clientIP, email)

# Lokális Ip-t (hálózaton belülit) ad vissza
# Ha nem vagyunk online, OSError-t dob fel
def getlocalIp():
	return (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]


if __name__ == '__main__':
	# Ha bennhagyjuk, a rögzített bejegyzések újraindításkor törlődnek
	#fileIO().filetrunc()

	colorPrint().startPrint('%s:%s' %(getlocalIp(), str(1111)))
	app.run(host='0.0.0.0', port=1111)
