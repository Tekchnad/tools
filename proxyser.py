import SocketServer
from SocketServer import StreamRequestHandler
import re
import urllib2
import time
from time import sleep
from urllib2 import urlopen
import bs4
from bs4 import BeautifulSoup

class Bypass(SocketServer.BaseRequestHandler):

	def setup(self):
		print("Proxy Server Connected with client")

	def handle(self):
		self.clientrequest=self.request.recv(1024)
		print("client request is==> %s" % (self.clientrequest))
		self.url=str(self.clientrequest).strip()
		re.findall("'^http|https|www|^\d','\Z[a-z]|[0-9]|\S'",self.url)
		self.proxysend=urllib2.urlopen(self.url).read()
		print("sending response to client..")
		sleep(1)
		if self.request.send(str(self.proxysend)):
			self.linkconnector=BeautifulSoup(self.proxysend,features="html5lib")
			with open("link.txt","w+") as fp:
				fp.write(str(self.proxysend))
			self.linkhandler=BeautifulSoup(self.proxysend,feature="xhtml")
			print(self.linkhandler.find_all("<a>"))
			print("good buy")

	def finish(self):
		self.request.send("Client disconnected")

if __name__ == "__main__":

	ADDR,PORT="10.0.2.15",6500
	remote=SocketServer.TCPServer((ADDR,PORT),Bypass,True)
	remote.serve_forever()
	remote.allow_reuse_address()





