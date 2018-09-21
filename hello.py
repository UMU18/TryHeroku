import os
from flask import Flask, request
import psycopg2
import pandas as pd

app = Flask(__name__) #create an instance of the Flask library

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/hello') #whenever this webserver is called with <hostname:port>/hello then this section is called
def hello():
	df = pd.read_sql_table("data_latih", conn)
	#cur = conn.cursor()
	#cur.execute("SELECT * FROM data_latih;")
	#raw = cur.fetchone()
	return df
	

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000)) #The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
	app.run(host='0.0.0.0', port=port)  #Start listening