from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_api import status
import configparser
import psycopg2
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('padronapi.ini')
cnx=psycopg2.connect(dbname=config['DB']['name'], user=config['DB']['user'], password=config['DB']['password'], host=config['DB']['host'], port=config['DB']['port'])
cur=cnx.cursor()

app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/provincias')
def provincias():
    if request.method == 'GET':
        cur.execute("SELECT * FROM provincia;")
        dataJson = []
        for provincia in cur.fetchall():
            dataDict = {
                'codigo-provincia': provincia[0],
                'nombre-provincia': provincia[1]
            }
            dataJson.append(dataDict)
        flash('dataJson')
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincias'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED 

@app.route('/provincias/<string:codigo>')
def provincia(codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM provincia WHERE codigo=%s;",(codigo,))
        provincia=cur.fetchone()
        if provincia is None :
            content = {'Error de código': 'La provincia con el código {} no existe.'.format(codigo)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataDict = {
                'codigo-provincia': provincia[0],
                'nombre-provincia': provincia[1]
            }
            return jsonify(dataDict), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincia'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/cantones')
def cantones():
    if request.method == 'GET':
        cur.execute("SELECT * FROM canton;")
        dataJson = []
        for cantones in cur.fetchall():
            dataDict = {
                'codigo-provincia':cantones[0],
                'codigo-canton': cantones[1],
                'nombre-canton': cantones[2]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para cantones'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/cantones/<string:codigo>')
def canton(codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM canton WHERE codigo=%s;",(codigo,))
        dataJson = []
        for canton in cur.fetchall():
            dataDict = {
                'codigo-provincia': canton[0],
                'codigo-canton': canton[1],
                'nombre-canton': canton[2]
            }
            dataJson.append(dataDict)
        flash('dataJson')
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para Cantones'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED 

@app.route('/cantones/canton-provincia/<string:codigo>')
def canton_provincia(codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM canton WHERE provincia=%s;",(codigo,))
        dataJson = []
        for canton in cur.fetchall():
            dataDict = {
                'codigo-canton': canton[1],
                'nombre-canton': canton[2]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else:
        content = {'Error de método': 'Sólo se soporta GET para provincias'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED 
       
@app.route('/distritos')
def distritos():
    if request.method == 'GET':
        cur.execute("SELECT * FROM distrito;")
        dataJson = []
        for distritos in cur.fetchall():
            dataDict = {
                'codigo-provincia': distritos[0],
                'codigo-canton': distritos[1],
                'codigo-distrito': distritos[2],
                'nombre-distrito': distritos[3]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para distritos'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/distritos/<string:codigo>')
def distrito(codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM distrito WHERE codigo=%s;",(codigo,))
        distrito=cur.fetchone()
        if distrito is None :
            content = {'Error de código': 'El distrito con el código {} no existe.'.format(codigo)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataDict = {
                'codigo-provincia': distrito[0],
                'codigo-canton': distrito[1],
                'codigo-distrito': distrito[2],
                'nombre-distrito': distrito[3]
            }
            return jsonify(dataDict), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para distrito'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/distritos/distrito-canton/<string:codigo>')
def distrito_canton(codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM distrito WHERE canton=%s;",(codigo,))
        dataJson = []
        for distrito in cur.fetchall():
            dataDict = {
                'codigo-distrito': distrito[2],
                'nombre-distrito': distrito[3]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else:
        content = {'Error de método': 'Sólo se soporta GET para distritos'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED 

@app.route('/distritos/distrito-provincia/<string:codigo>')
def distrito_canton_provincia(codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM distrito WHERE provincia=%s;",(codigo,))
        dataJson = []
        for distrito in cur.fetchall():
            dataDict = {
                'codigo-distrito': distrito[2],
                'codigo-canton': distrito[1],
                'nombre-distrito': distrito[3]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else:
        content = {'Error de método': 'Sólo se soporta GET para distritos'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED 

if __name__ == '__main__':
    app.debug = True
    app.run()
