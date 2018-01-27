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

		return curs.fetchall()

	def searchAndReturnColumn(self, dbIp, email):
		try:
			return self.executeQuery(dbIp, 'SELECT csvLines FROM `jelentkezok` WHERE `csvLines` LIKE "%' + email + '%"')[0]
		except IndexError:
			return 'Nincs adat az adatbázisban'

	def updateWithJSON(self, dbIp, email, changeTo):
		self.executeQuery(dbIp, 'UPDATE `jelentkezok` SET csvLines = "' + changeTo + '" WHERE csvLines LIKE "%' + email + '%"')
