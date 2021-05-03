from flask import Flask ,render_template,request,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)
app.secret_key = 'a'
app.config['MYSQL_HOST'] = "remotemysql.com"
app.config['MYSQL_USER'] = "HAIxhNBolo"
app.config['MYSQL_PASSWORD'] = "Sq1REro6fT"
app.config['MYSQL_DB'] = "HAIxhNBolo"

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template("apply.html")

@app.route('/uploaddata',methods =["POST"])
def uploaddata():
    if request.method =="POST":
        name = request.form["name"]
        e-mail = request.form["e-mail"]
        stream = request.form["gender"]
        address = request.form["address"]
        mobile = request.form["mobile"]
        session['username']  = name
      
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO DetailsTable VALUES(NULL,% s,% d,% s,% s,% s)',(name,mobile,gender,address,e-mail))
        mysql.connection.commit()
        msg = "you have sucessfully got registered"
    return render_template("apply.html",msg = msg)
@app.route('/display')
def display():
    print(session['name'])
    print(type(session['name']))
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM newtable WHERE name = %s', (session['username'],))
    account = cursor.fetchone()
    print(account)
    session.pop('username')
    return render_template("apply.html",account = account)
    


if __name__ == '__main__':
    app.run(debug = True)