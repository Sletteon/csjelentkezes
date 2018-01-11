# -*- coding: utf-8 -*-

# Fájlokkal zsonglőrködik
import json

class fileIO:
	# JSON adatok mentése
	def writeJSONToFile(self, file, JSON):
		with open(file, 'w', encoding='utf-8') as fileobj:
			fileobj.truncate()
			json.dump(JSON, fileobj, ensure_ascii=False)

	def readJSONFormFile(self, file):
		with open(file, 'r', encoding='utf-8') as file:
			return '\n'.join(file.readlines())

	def filetrunc(self):
		with open('debug/data.json', 'w', encoding='utf-8') as file:
			file.truncate()
			file.close()
