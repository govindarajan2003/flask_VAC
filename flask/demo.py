from flask import Flask,redirect,url_for, request, render_template

app= Flask(__name__)

from flask_wtf import CSRFProtect
app.secret_key="karthisree"
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

if __name__ == '__main__':
    app.run(debug=True)
