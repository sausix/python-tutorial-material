#!/usr/bin/python
import time
import sys
import cowsay

rotate_chars = "|/-\\"

stacktrace = '''Traceback (most recent call last):
  File "loader.py", line 45, in javakiller
PermissionError: [Errno 13] Permission denied: C:\\Python3.8\\java_remove.py'''

stacktrace2 = '''Traceback (most recent call last):
  File "loader.py", line 55, in FoodFactory
FoodException: [Errno 345] Snake rejected food:
C:\\Python3.8\\FoodFactory.py'''

def print(text="\n"):
	sys.stdout.write(text)
	sys.stdout.flush()

def delete(number=1):
	sys.stdout.write('\b'*number)
	sys.stdout.write(' '*number)
	sys.stdout.write('\b'*number)
	sys.stdout.flush()


def showmsg(text, rotation, count):
	c = 0
	ticks = count
	print(text+" ")
	while(ticks>0):
		ticks = ticks - 1

		if rotation:
			print(rotate_chars[c])
			c = (c + 1) % len(rotate_chars)
		time.sleep(0.1)
		if rotation:
			delete()
	if rotation:
		print("✓\n")
	else:
		print("\n\n")

if "pause" in sys.argv:
	while(1):
		showmsg("Starte Pausensequenz", True, 50)
		showmsg('home.find("Badezimmer")', True, 50)
		showmsg("kaffee.flush()", True, 40)
		showmsg("Ersetze müde alte Giftschlange", True, 40)
		showmsg("Füttere Schlange", True, 30)
		showmsg(stacktrace2, False, 80)
		showmsg("Lade lehrreiche Pausen-Kuh", True, 50)
		cowsay.cow('print("Hello World!")')
		time.sleep(8)
		showmsg("Fülle Quasselwasser nach.", True, 40)
		showmsg("Defragmentiere Gedächtnis", True, 40)
		showmsg("Fixe Bugs", True, 40)
		showmsg("Entferne Folgefehler durch Bugfix", True, 40)
		showmsg("kaffee = Kaffeemaschine.getCoffee()", True, 50)

else:
	while (1):
		showmsg("Lade Programm", True, 50)
		showmsg("Prüfe Kaffee-Füllstand", True, 30)
		showmsg("Warte auf Teilnehmer", True, 50)
		showmsg("Justiere Python-Bibliotheken", True, 70)
		showmsg("Deinstalliere Java", True, 50)
		showmsg(stacktrace, False, 30)
		showmsg("Hole Hilfe", True, 50)
		showmsg("Schöpfe Schlangenöl", True, 60)
		showmsg("Kalkuliere Restzeit", True, 30)
		showmsg("Lade Spruch aus dem Ostfriesland", True, 60)
		showmsg('"Er würgte eine Klapperschlang\\\' bis ihre Klapper schlapper klang\\\' (Otto Walkes)"', False, 80)
		showmsg("Starte Server neu", True, 80)

