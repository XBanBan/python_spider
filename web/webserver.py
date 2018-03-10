from socket import *
from multiprocessing import *
import re
import sys

WSGI_PYTHON_DIR = "/home/banban/web"

class HTTP(object):
	def __init__(self, app):
		self.server_socket = socket(AF_INET, SOCK_STREAM)
		self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.app = app

	def start(self):
		self.server_socket.listen(128)
		client_socket, client_addr = self.server_socket.accept()
		print("newcommer" + str(client_addr))
		client_process = Process(target = self.handle_client, args = (client_socket,))
		client_process.start()
		client_socket.close()

	def bind(self, port):
		self.server_socket.bind(("",port))

	def handle_client(self, client_socket):
		client_date = client_socket.recv(1024)
		client_line = client_date.splitlines()
		client_start_line = client_line[0].decode("utf-8")
		require_name = re.match(r"\w+ +(/[^ ]*) ", client_start_line).group(1)
		env = {
			"PATH" : require_name
		}
		response_body = self.app(env, self.start_response)
		response = self.response_headers  + "\r\n" + response_body
		client_socket.send(bytes(response, "utf-8"))
		client_socket.close()

	def start_response(self, status, heraders):
		response_headers = "HTTP/1.1 " + status + "\r\n" 
		for header in heraders:
			response_headers += "%s:%s\r\n"%header
		self.response_headers = response_headers

def main():
	sys.path.insert(1, WSGI_PYTHON_DIR)
	module_name, app_name = sys.argv[1].split(":")
	m = __import__(module_name)
	app = getattr(m, app_name)
	http = HTTP(app)
	http.bind(8888)
	http.start()

if __name__ == '__main__':
	main()		
