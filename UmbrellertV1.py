# -*- coding:utf-8 -*- 
import RPi.GPIO as gpio
import time
import urllib2 
from xml.dom.minidom import parse, parseString
import gzip
import StringIO
import json

gpio.setwarnings(False)

gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)
#gpio.setup(13,gpio.OUT)

config = open("config.json").read()
json_data = json.loads(config)
city = json_data["city"].encode('utf8')
print city

def get_weather(city):
	data = urllib2.urlopen("http://wthrcdn.etouch.cn/WeatherApi?city=" + city).read()
	data = StringIO.StringIO(data)
	gzipper = gzip.GzipFile(fileobj=data)
	html = gzipper.read()
	weather = html.decode('utf8')
	 
	print weather
		     
	return weather

def set_allert(weather):
     if weather.find(u"不带伞") <>  -1:
#         print 'No Rain'
		 gpio.output(11, gpio.LOW)
     elif weather.find(u"带伞") <> -1:
#		 print 'Take Your Umbrella!'
		 gpio.output(11, gpio.HIGH)


#city = "%e8%a5%bf%e5%ae%89"
#city = "%E4%B8%8A%E6%B5%B7"
#city = "上海"
#city = "西安"

weather = get_weather(city)
set_allert(weather)



#print urllib2.urlopen("http://wthrcdn.etouch.cn/WeatherApi?city=%E4%B8%8A%E6%B5%B7").read().decode(htmlCharsetEncoding)
#上海
#data = urllib2.urlopen("http://wthrcdn.etouch.cn/WeatherApi?city=%E4%B8%8A%E6%B5%B7").read()
#西安
#data = urllib2.urlopen("http://wthrcdn.etouch.cn/WeatherApi?city=%e8%a5%bf%e5%ae%89").read()
#data = StringIO.StringIO(data)
#gzipper = gzip.GzipFile(fileobj=data)
#html = gzipper.read()

#result = html.decode('utf8')
#print result
#if result.find(u"不带伞") <>  -1:
#	print 'No Rain'
#elif result.find(u"带伞") <> -1:
#	print 'Take Your Umbrella!'

#print time.timezone
#print time.strftime("%H:%M:%S", time.localtime())
#while 1:

	#gpio.output(11,True)
	#gpio.output(13,True)
	#time.sleep(2)
	#gpio.output(11,False)
	#gpio.output(13,False)
#	time.sleep(2)
#	gpio.setup(13,gpio.IN)
#	time.sleep(2)
#	gpio.setup(13,gpio.OUT)

#gpio.cleanup()
#gpio.cleanup()
