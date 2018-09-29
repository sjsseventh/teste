from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
import psycopg2
import tornado.web
import json

async def get_http_result():
   url = 'https://raw.githubusercontent.com/backstage/functions/master/package.json'
   response = await AsyncHTTPClient().fetch(url, validate_cert=False)
   data = json.loads(response.body)
   return {
       'heey': data['name'],
       'teste': data['author']
   }

class MainHandler(tornado.web.RequestHandler):
   async def get(self):
       result01, result02 = await gen.multi([
           get_http_result(),
           get_http_result(),
       ])
       self.write(json.dumps([result01, result02]))

class Application(tornado.web.Application):
   def __init__(self):
       handlers = [
           (r"/?", MainHandler)
       ]
       tornado.web.Application.__init__(self, handlers)

class ConexaoBd():
   def con(self):
       try:
           conn = psycopg2.connect("dbname='teste' user='postgres' host='localhost' password='postgres'")
           print("ok")
          
       except:
           print ("I am unable to connect to the database")

def main():
   app = Application()
   app.listen(80)
   IOLoop.instance().start()

if __name__ == '__main__':
   main()
