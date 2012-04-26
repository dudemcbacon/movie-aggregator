import web

urls = {
	'/', 'index'
}

class index:
	deg GET(self):
		return "Hello, world!"
		
if __name__ = "__main__":
	app = web.application(urls, globals())
	app.run()