#!/usr/bin/env python3
import sqlite3
import datetime as DT
import os

sqlite_file = '/home/ubuntu/momCron/data.db'
day = DT.date.today().day
month = DT.date.today().month

week_from_now = DT.date.today() + DT.timedelta(days=7)
dayin7 = week_from_now.day
monthin7 = week_from_now.month

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('SELECT name FROM dates WHERE day = (?) AND month = (?)', (dayin7, monthin7))
for row in c.fetchall():
	rowString = ["".join(map(str,r)) for r in row]
	str1 = "".join(rowString)
	os.system('echo "Mom, this is your son writing to inform you that ' + str1 + ' is coming up in one week.\n\nLove,\nMatt" | mail -s "' + str1 + '" mjforeman@hotmail.com')
	os.system('echo "Email Sent" | mail -s "Alert!" mforeman12@gmail.com') 


conn.commit()
conn.close()
