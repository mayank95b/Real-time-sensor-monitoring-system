# RaspberryPi_SqliteDB

From Sensor Data to Visualization:  Using Flask and SQLite with Raspberry Pi

Capturing real data (RPi/DHT11), saving them in a database (SQLite), creating graphs (Matplotlib) and presenting them on a web page (Flask).

Installation:

Follow the below steps to create a database.

1. Install SQLite to Raspberry Pi using the command:

sudo apt-get install sqlite3

2. Create a directory to develop the project:

mkdir Sensors_Database

3. Move to this directory:

cd mkdir Sensors_Database/

3. Give a name and create a database like databaseName.db (in my case “sensorsData.db”):

sqlite3 sensorsData.db

Creating a table:

To create a table, you can do it:

Directly on the SQLite shell, or

Using a Python program.

1. Using Shell:

Open the database that was created in the last step:

sqlite3 sensorsData.db

And entering with SQL statements:

sqlite> BEGIN;

sqlite> CREATE TABLE DHT_data (timestamp DATETIME,  temp NUMERIC, hum NUMERIC);

sqlite> COMMIT;

2. Using Python

import sqlite3 as lite

    import sys

    con = lite.connect('sensorsData.db')

    with con: 

    cur = con.cursor() 
    
    cur.execute("DROP TABLE IF EXISTS DHT_data")
    
    cur.execute("CREATE TABLE DHT_data(timestamp DATETIME, temp NUMERIC, hum NUMERIC)")
