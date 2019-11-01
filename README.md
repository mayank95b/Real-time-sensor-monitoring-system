# RaspberryPi_SqliteDB

From Sensor Data to Visualization:  Using Flask and SQLite with Raspberry Pi

Capturing real data (RPi/DHT11), saving them in a database (SQLite), creating graphs (Matplotlib) and presenting them on a web page (Flask).

### Installation:

Follow the below steps to create a database.

1. Install SQLite to Raspberry Pi using the command:

       sudo apt-get install sqlite3

2. Create a directory to develop the project:

       mkdir Sensors_Database

3. Move to this directory:

       cd mkdir Sensors_Database/

3. Give a name and create a database like databaseName.db (in my case “sensorsData.db”):

       sqlite3 sensorsData.db

### Creating a table:
 
To create a table, you can do it:

Directly on the SQLite shell, or Using a Python program.

#### 1. Using Shell:**

Open the database that was created in the last step:

    sqlite3 sensorsData.db

And entering with SQL statements:

    sqlite> BEGIN;

    sqlite> CREATE TABLE DHT_data (timestamp DATETIME,  temp NUMERIC, hum NUMERIC);

    sqlite> COMMIT;

#### 2. Using Python

        import sqlite3 as lite

        import sys

        con = lite.connect('sensorsData.db')

        with con: 

        cur = con.cursor() 

        cur.execute("DROP TABLE IF EXISTS DHT_data")

        cur.execute("CREATE TABLE DHT_data(timestamp DATETIME, temp NUMERIC, hum NUMERIC)")

Open the above code from my GitHub: createTable.py and Run it on your Terminal:

     python3 createTableDHT.py

Wherever the method used, the table should be created. You can verify it on SQLite Shell using the “.table” command. Open the database 

shell:
           
     sqlite3> sensorsData.db

In the shell, once you use the .table command, the created tables names will appear (in our case will be only one: “DHT_table”. Quit the 

shell after, using the .quit command.

     sqlite> .table
     DHT_data
     sqlite> .quit


#### Installing DHT Library

On your Raspberry, starting on /home, go to /Documents:

    cd Documents

Create a directory to install the library and move to there:
   
    mkdir DHT22_Sensor
    cd DHT22_Sensor

On your browser, go to Adafruit GITHub: https://github.com/adafruit/Adafruit_Python_DHT

Download the library by clicking the download zip link to the right and unzip the archive on your Raspberry Pi recently created folder. 

Then go to the directory of the library (subfolder that is automatically created when you unzipped the file), and execute the command:

    sudo python3 setup.py install
    
#### Capturing Data Automatically

Open a new Terminal window and enter with bellow Python code:

        import time
        import sqlite3
        import Adafruit_DHT
        dbname='sensorsData.db'
        sampleFreq = 1*60 # time in seconds ==> Sample each 1 min
        # get data from DHT sensor
        def getDHTdata():	
            DHT22Sensor = Adafruit_DHT.DHT22
            DHTpin = 16
            hum, temp = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)
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

Or get it from my GitHub: logDHT.py. Run it on the Terminal:

     python3 logDHT.py

What the main() function does is:

Call the function getDHTdata(), that will return the captured data by the DHT22 sensor. Take those data (temperature and humidity) and 

passing them to another function: logData(temp, hum) that insert them, together with actual date and time, to our table.And goes to 

sleep, waiting until the next scheduled time to capture data (defined by sampleFreq, which in this example is 1 minute).
    
    
