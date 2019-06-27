import time
import sqlite3
import Adafruit_DHT
dbname='sensorsData.db'
sampleFreq = 5 # time in seconds ==> Sample each 1 min
# get data from DHT sensor
def getDHTdata():	
	DHT11Sensor = Adafruit_DHT.DHT11
	DHTpin = 4
	hum, temp = Adafruit_DHT.read_retry(DHT11Sensor, DHTpin)
	if hum is not None and temp is not None:
		hum = round(hum)
		temp = round(temp, 1)
	return temp, hum
# log sensor data on database
def logData (temp, hum):
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, hum))
	conn.commit()
	conn.close()
# main function
def main():
	while True:
		temp, hum = getDHTdata()
		logData (temp, hum)
		time.sleep(sampleFreq)
# ------------ Execute program 
main()
