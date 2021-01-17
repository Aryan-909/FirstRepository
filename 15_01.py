import sqlite3
import re

conn=sqlite3.connect('email02.sqlite')
curhand=conn.cursor()

curhand.execute('DROP TABLE IF EXISTS Counts')
curhand.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fhand=open('mbox.txt')
x=fhand.read()
d=re.findall('From:.+\S+@(\S+)',x)
for domain in d:
    curhand.execute('SELECT count FROM Counts WHERE org = ? ',(domain,))
    r=curhand.fetchone()
    if r is None:
        curhand.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(domain,))
    else:
        curhand.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))
conn.commit()

sqlstr='SELECT*FROM Counts'

for row in curhand.execute(sqlstr):
    print(row[0],row[1])
curhand.close()
