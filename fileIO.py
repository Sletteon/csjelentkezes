# -*- coding: utf-8 -*-

# Fájlokkal zsonglőrködik
import json, fileinput

class fileIO:
	def writeJSONToFile(self, file, JSON):
		with open(file, 'w', encoding='utf-8') as fileobj:
			fileobj.truncate()
			json.dump(JSON, fileobj, ensure_ascii=False)

	def appendJSONToFile(self, file, JSON):
		with open(file, 'w', encoding='utf-8') as fileobj:
			json.dump(JSON, fileobj, ensure_ascii=False)

	def readJSONFormFile(self, file):
		with open(file, 'r', encoding='utf-8') as file:
			return '\n'.join(file.readlines())

	def filetrunc(self):
		with open('debug/data.json', 'w', encoding='utf-8') as file:
			file.truncate()
			file.close()

	def checkIfPassExists(self, passw):
                with open('data/passwords.list', 'r', encoding='utf-8') as file:
                        for line in file:
                                if str(passw) in line:
                                        return True
	
	def readDataFromFile(self, file, email):
		with open(file, 'r', encoding='utf-8') as fileobj:
			for line in fileobj:
				if str(email) in line:
					return line

	def setDataToFileold(self, file, email, gotJSON):
		with open(file, 'r+', encoding='utf-8') as fileobj:
			for line in fileobj:
				if str(email) in line:
					gotJSONobj = json.dumps(gotJSON)
					print(line.rstrip().replace(line, gotJSONobj[0]))

	def setDataToFile(self, file, email, gotJSON):
		for line in fileinput.input('data/data.txt', inplace=True):
			print(line.replace(line, json.dumps(gotJSON)[0]))
