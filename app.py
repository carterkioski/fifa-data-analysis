from flask import Flask,render_template
from sqlalchemy import inspect, create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import text
import numpy as np
import os
import sqlalchemy
import psycopg2


engine = create_engine(os.environ['DATABASE_URL']) 
connection = engine.connect()
#Reflect an existing database and tables
Base = automap_base()
Base.prepare(engine, reflect=True)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)