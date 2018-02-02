# -*- coding: utf-8 -*-

# Elküldi/lekéri az adatokat egy külső adatbázisba (mysql)
import json, pymysql, pymysql.cursors
from colorPrint import colorPrint

class dbIO:
	def getdbIp(self):
		with open('DBIp.txt', 'r') as file:
			return file.readline()

	def executeQuery(self, dbIp, query):

		conn = pymysql.connect(
			host=dbIp,
			user='cserk',
			password='1111CScsapat',
			db='cserk',
			charset='utf8mb4',
            # cursorclass=pymysql.cursors.DictCursor
		)
		curs = conn.cursor()
		curs.execute(query)
		conn.commit()

		fetchedResp = curs.fetchall()
		if len(fetchedResp) > 1:
			return None
		else:
			return fetchedResp

	def searchAndReturnColumn(self, dbIp, email):
		selectQueryResp = self.executeQuery(dbIp, 'SELECT csvLines FROM `jelentkezok` WHERE `csvLines` LIKE "%email:' + email + '%"')

		if selectQueryResp != None:
			try:
				return selectQueryResp[0]
			except IndexError:
				return 'Nincs ilyen adat az adatbázisban'
		else:
			return 'Több ilyen felhasználónak adatai egyeznek meg a megadott email címmel'

	def updateWithJSON(self, dbIp, email, changeTo):
		self.executeQuery(dbIp, 'UPDATE `jelentkezok` SET csvLines = "' + changeTo + '" WHERE csvLines LIKE "%' + email + '%"')
