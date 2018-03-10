STATIC_ROOT_DIR = "/home/banban"

class Application(object):
	def __call__(self, env, start_response):
		path = env.get("PATH")
		# if path.startswith("/static"):
		# 	path_way = path[7:]
		file_name = STATIC_ROOT_DIR + path
		print(file_name)
		try:
			file = open(file_name, "rb")
		except:
			status = "404 CANT FOUND"
			headers = []
			start_response(status, headers)
			return("error name")
		else:
			status = "404 OK"
			headers = [
				("Content-Type", "text/plain")
			]
			start_response(status, headers)
			response_date = file.read().decode("utf-8")
			return response_date
app = Application()
