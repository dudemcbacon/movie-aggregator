import web

urls = (
    '/', 'index'
)

render = web.template.render('templates/')

class index:
    def GET(self):
        return render.index("blah!")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()