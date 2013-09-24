#!/usr/bin/python
from gmusicapi import Webclient
import sys

api = Webclient()

api.login(sys.argv[1],sys.argv[2])

rsongs = api.get_all_songs()
fsongs = ""
addstr = ''
for rsong in rsongs:
	if 'year' in rsong and 'albumArtUrl' in rsong:
		addstr = rsong['title'] + ';' + rsong['artist'] + ';' + rsong['album'] + ';' + rsong['genre'] + ';' + str(rsong['year']) + ';' + rsong['id'] + ';' + str(rsong['durationMillis']) + ';' + rsong['albumArtUrl']
	elif 'albumArtUrl' in rsong:	
		addstr = rsong['title'] + ';' + rsong['artist'] + ';' + rsong['album'] + ';' + rsong['genre'] + ";Unknown;" + rsong['id'] + ';' + str(rsong['durationMillis']) + ';' + rsong['albumArtUrl']
	addstr = addstr.encode('utf-8','replace')
	fsongs = fsongs + addstr + "<>"


fsongs = fsongs[0:len(fsongs) - 2]
print(fsongs)

api.logout()
