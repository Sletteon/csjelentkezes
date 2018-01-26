# -*- coding: utf-8 -*-

# Elküldi/lekéri az adatokat egy külső adatbázisba (mysql)
import json, pymysql, pymysql.cursors

class dbIO:
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

		return curs.fetchall()

	def searchAndReturnColumn(self, dbIp, email):
		return self.executeQuery(dbIp, 'SELECT * FROM `jelentkezok` WHERE `csvLines` LIKE "%' + email + '%"')[0]
