#!/usr/bin/python
from gmusicapi import Webclient
import sys


api = Webclient()

api.login(sys.argv[1],sys.argv[2])

if sys.argv[3] != '':
	streamurl = api.get_stream_urls(sys.argv[3])[0]
	print streamurl

