import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
       json_data=open("config.json").read()
       data = json.loads(json_data)
       city = data["city"]
       self.render("index.html",city_name=city)
      # data["city"]= "eheh"
      # out_file = open('config.json', 'wb')
      # out_file.write(str(data))
      # out_file.close
       #data["city"]= "dsjhdj"
       #with open('config.json', 'w') as outfile:
              #json.dump(data, outfile)
 
    def post(self):
        #self.write("You wrote " + self.get_argument("city_name")) 
        #self.render("index.html")
        city = self.get_argument("na_city_name")
        json_data=open("config.json").read()
        data = json.loads(json_data)
        data["city"]= city
        with open("./%s" % ('config.json'), 'w') as outfile:
               json.dump(data, outfile)
        self.render("index.html",city_name = city)

application = tornado.web.Application([
    (r"/", MainHandler),
])
 
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

