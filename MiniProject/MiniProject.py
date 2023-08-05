from flask import Flask,redirect,url_for, request, render_template
from flask_bcrypt import Bcrypt
import MySQLdb
from flask_mysqldb import MySQL
from flask import*
import re

app= Flask(__name__)
app.secret_key="karthisree"


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD'] ='root'
app.config['MYSQL_DB'] = 'PortFolioDB'
mysql =MySQL(app)


@app.route('/home')
def home():
    return render_template('homePage.html')

@app.route('/loginPage_index')
def loginPage_index():
    return render_template('loginPage.html')

#LOGIN SESSION
@app.route('/userlogin', methods=['GET','POST'])
def login():
    message=''
    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * from user where email =%s',(email,))
        user =cursor.fetchone()

        if user:
            hashed_password = user["password"]
            is_valid = bcrypt.check_password_hash(hashed_password,password)
        
        if is_valid:
            session['loggedin'] =True
            session['name'] =user['username']
            session['email'] = user['email']
            message='logged in successfully'
            return render_template("userHomePage.html",message = message)
        else:
            message ="PLease enter CORRECT"
    return render_template('loginPage.html', message = message)
#LOG OUT SESSION
@app.route('/logout')
def logout():
    session.pop("logged in", None)
    session.pop("email", None)
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route('/userRegister_index')
def userRegister_index():
    return render_template('registerPage.html')
@app.route('/userregister', methods=['POST','GET'])
def register():
    message =''
    if request.method == 'POST':
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * from user WHERE email = %s',(email,))
        account = cursor.fetchone()

        password= bcrypt_demo(password)

        if account:
            message = 'Account alerdy exists !'
        elif not re.match(".+@[a-z]+\.[a-z]+", email):
            message = 'invalid email address !'
        elif not userName or not password or not email:
            message = 'Please fillout the form !'
        else:
            cursor.execute('INSERT INTO user(username,email,password) VALUES (%s,%s,%s)',(userName,email,password))
            mysql.connection.commit()
            message = ' you have successfully register '
    elif request.method == "GET":
        message = 'please fill out the form!'
    return render_template('registerPage.html',message = message)

@app.route('/addAchievementDetail_index')
def addAchievementDetail_index():
    return render_template('addAchievementDetail.html')

@app.route('/addAchievementDetail', methods= ['POST', 'GET'])
def addAchievementDetail():
    if request.method =='POST':
        email = request.form['email']
        hobby  = request.form['hobby']
        studies = request.form['studies']
        city = request.form['city']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        cursor.execute("UPDATE user set hobby =%s,city= %s,studies=%s where email =%s",(hobby,city,studies,email))
        mysql.connection.commit()
        
        
    return render_template('userHomePage.html')

@app.route('/showAchievementDetail_index')
def showAchievementDetail_index():
    return render_template('showAchievementPage.html')

@app.route('/showAchievementDetail')
def showAchievementDetail():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * from user where user= %s ')
    user =cursor.fetchone()
    session['hobby'] =user['hobby']
    session['city'] = user['city']
    session['studies'] = user['studies']
    return redirect(url_for("showAchievementDetail_index"))
    
#bcrypt 

bcrypt = Bcrypt(app)

@app.route('/bcyrpt_demo')
def bcrypt_demo(password):
    passwordVAR = password
    hashed_password = bcrypt.generate_password_hash(passwordVAR).decode('utf-8')
    return hashed_password



if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

