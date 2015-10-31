import web
from twitterTimeline import getTweets
        
urls = (
    '/index', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self):
        i = web.input()
        print i.name;
        return getTweets(i.name)["text"]
        #return 'Hello World!'

if __name__ == "__main__":
    app.run()
