from flask import Flask,redirect,url_for, request, render_template
from flask_mail import Mail,Message
from flask import send_file
from forms import ContactForm
from flask import*
import MySQLdb
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
app= Flask(__name__)
app.secret_key="karthisree"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/mikey'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

'''
from flask_wtf import CSRFProtect

csrf = CSRFProtect(app)

#BASIC
@app.route('/kcet')
def index():
    return "welcome"

@app.route('/karthi')
def karthi():
    return "Karthi"	

@app.route('/name/<name>')
def name(name):
    return "hey %s" %name

#USER SWITCHING
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_gust',gust=name))

#ODD OR EVEN CALCULATOR
@app.route('/oddeven/<int:n>')
def oddeven(n):
    if(n%2 ==0):
        return " n is even"
    else:
        return " n is odd"

#URL BUILDING
def demo3():
    return "Welcome to url buillding"
app.add_url_rule("/demo3/","",demo3)


@app.route('/demo4')
def demo4():
    return render_template("demo.html",anime="Tokyo Revengers",character={1:"Micky",2:"drago"}, n=-6)


    

#LOGIN_PAGE GET<POST:
@app.route('/success/<name>')
def success(name):
    return "Welcome %s" %name

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for("success",name = user))
    else:
      user = request.args.get('nm')
      return redirect(url_for("success",name = user))

#student reselt
@app.route('/input')   
def input():
    return render_template("input.html")

@app.route('/inputprocess',methods=['post','get'])
def inputprocess():
    name=request.form['n1']
    gender = request.form['r1']
    city = request.form['city']
    return render_template("show.html", name = name , gender = gender, city= city)

@app.route("/styles")
def styles():
    return render_template("demo_static.html")

#MAIL
mail= Mail(app)

app.config['MAIL_SERVER'] ='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] ='customerproject404nf@gmail.com'
app.config['MAIL_PASSWORD'] ='nowdlnospvmgsoth'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] =True


@app.route('/mail_demo')
def mail_demo():
    msg = Message('HELLO',sender= 'customerproject404nf@gmail.com',recipients=['karthikeyan96883@gmail.com'])
    msg.body = "Hello"
    mail.send(msg)
    return "SENT"

#upload
@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploader',methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename )
        return 'uploaded successfuly'

#download

@app.route('/download_index')
def download():
    return render_template("download.html")

@app.route('/download')
def download_file():
    path = "tokyo-revengers-2.jpg"
    return send_file(path,as_attachment=True)


#flash

@app.route('/flash_index')
def flash_index():
    return render_template('flash_index.html')

@app.route('/flash_login', methods=['GET','POST'])
def flash_login():
    error=None
    if request.method == 'POST':
        
        if request.form['username'] != 'govind' or request.form['password'] != 'govind':
            error = 'invalid user password'
        else:
            flash('Successfully login')
            flash('example for flash')
            flash('vasi')
    return render_template('flash_login.html',error=error)'''
'''
#dbms

@app.route('/contact',methods=['POST','GET'])
def contact():
    form =ContactForm()

    if request.method == 'POST':
        if form.validate():
            flash('ALL FIELDS ARE REQUIRED')
            return render_template('contact.html', form= form)
        else:
            return render_template('success.html', form = form)
    else:
        return render_template('contact.html', form = form )

@app.route('/enternew')
def new_student():
    return render_template("student.html")

@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method =='POST':
        regno = int(request.form['t1'])
        name = request.form['t2']
        degree = request.form['t3']
        cgp = float(request.form['t4'])

        db = MySQLdb.connect("localhost","root","","mikey")
        c1 = db.cursor()
        c1.execute("insert into students(regno,name,degree,cgp) values('%d','%s','%s','%f')"%(regno,name,degree,cgp))
        db.commit()
        msg = "successfully added"
        return render_template("result.html", msg=msg)


@app.route('/list')
def list():
    db = MySQLdb.connect("localhost","root","","mikey")
    c1 = db.cursor()
    c1.execute("select * from students")
    rows = c1.fetchall()
    return render_template("list.html",rows =rows)

@app.route('/')
def home():
    return render_template("home.html")

#sqlite

@app.route('/')
@app.route('/s_home')
def index():
    return render_template('sqlite_index.html')

connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS PARTICIPANTS(name TEXT,email TEXT,city TEXT,country TEXT,phone TEXT)')

@app.route('/join',methods=['GET','POST'])
def join():
    if request.method =='POST':
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        country = request.form['country']
        phone = request.form['phone']

        with sqlite3.connect("database.db")as user:
            cursor = user.cursor()
            cursor.execute("INSERT INTO PARTICIPANTS(name,email,city,country,phone) VALUES(?,?,?,?,?)",(name,email,city,country,phone))
            user.commit()
        return render_template("sqlite_index.html")
    else:
        return render_template("join.html")

@app.route('/participants')
def participants():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM PARTICIPANTS')

    data = cursor.fetchall()
    return render_template("participants.html",data = data)



class Employees(db.Model):
    id = db.Column('employee_id', db.Integer, primary_key =True) #use to make the name of feild to 'employee_id'
    name = db.Column(db.String(100))
    job = db.Column(db.String(100)) 
    salary =db.Column(db.Float)

    def __init__(self, name,job,salary):
        self.name =name
        self.job = job
        self.salary = salary

@app.route('/')
def show_all():
    return render_template('show_all.html', employees = Employees.query.all())

@app.route('/new',methods=['POST','GET'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['job'] or not request.form['salary']:
            flash('please enter all the feilds','error')
        else:
            e1 =Employees(request.form['name'],request.form['job'],request.form['salary'])
            db.session.add(e1)
            db.session.commit()
            flash('record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')
'''

@app.route('/add_data')
def add_data():
    #TO Create mongo db
    client = MongoClient('localhost',27017)

    #Getting the database instance
    db = client['mydb']

    #create a cllection
    coll =db['example']

    #insert docs into a collection
    doc1 = {"_id":"104","name":"Arsadh","age":"20","city":"Madurai"}
    coll.insert_one(doc1)
    print(coll.find_one())
    return 'data added to MangoDB'

@app.route('/add_multiple_data')
def add_multiple_data():
     #TO Create mongo db
    client = MongoClient('localhost',27017)

    #Getting the database instance
    db = client['mydb']

    #create a cllection
    coll =db['example']
    
    data =[
        
             {"_id":"96",
             "name":"Vasee",
             "age":"19",
             "city":"Theni"
             },

            {"_id":"69",
            "name":"Navanee",
            "age":"20",
            "city":"Sivagasi"
            }
        
    ]

    res = coll.insert_many(data)
    return 'multiple data added to Mongo DB'

@app.route('/show_data')
def show_data():
    client = MongoClient('localhost',27017)
    db = client['mydb']
    coll =db['example']
    return render_template("show_data.html",data = coll.find())
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
