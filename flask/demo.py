from flask import Flask,redirect,url_for, request, render_template
from flask_mail import Mail,Message
from flask import send_file
from forms import ContactForm
from flask import*
import MySQLdb

app= Flask(__name__)
app.secret_key="karthisree"
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


if __name__ == '__main__':
    app.run(debug=True)
