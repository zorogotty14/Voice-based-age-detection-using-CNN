import psycopg2
from flask import Flask,render_template,request,session,redirect,url_for
import re,glob,os
from song_prediction.recom import recommend_songs

connection=psycopg2.connect(user="postgres",
							password="postgres",
							host="127.0.0.1",
							port="5432",
							database="SongRec")

cursor=connection.cursor()
print ( connection.get_dsn_parameters(),"\n")
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")

app=Flask(__name__)
DEBUG=True
app.secret_key="Chandan_Bhat"

@app.route('/', methods=['GET', 'POST'])
def login():

    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        username = request.form['username']
        password = request.form['password']

        connection=psycopg2.connect(user="postgres",password="postgres",host="127.0.0.1",port="5432",database="SongRec")
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM registration WHERE username =%s AND password = %s', (username, password,))

        registration = cursor.fetchone()

        if registration:

            session['loggedin'] = True
            session['username'] = registration[0]

            return redirect(url_for('record'))
        else:

            msg = 'Incorrect username/password!'

    return render_template('index.html', msg=msg)

@app.route('/logout')
def logout():

   session.pop('loggedin', None)
   session.pop('username', None)

   return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():

    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']


        connection=psycopg2.connect(user="postgres",password="postgres",host="127.0.0.1",port="5432",database="SongRec")
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM registration WHERE username = %s', (username,))
        account = cursor.fetchone()

        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:

            cursor.execute('INSERT INTO registration VALUES (%s, %s, %s)',(username, password, email,))
            connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':

        msg = 'Please fill out the form!'

    return render_template('register.html', msg=msg)


@app.route('/record')
def record():

    if 'loggedin' in session:

        return render_template('recording.html', username=session['username'])

    return redirect(url_for('login'))
@app.route('/record',methods=['GET','POST'])
def recorded():
    if(request.method == 'POST'):
        return redirect(url_for('upload'))

    else:
        return redirect(url_for('upload'))



@app.route("/upload")
def upload():
	with open("age.txt") as file:
		data = file.read()
	dataTransformed = AgeClasses(data)
	user_id = "b80344d063b5ccb3212f7pg6538f3d9e43d87dca9e"
	#add to data database
	username=session['username']
	connection=psycopg2.connect(user="postgres",password="postgres",host="127.0.0.1",port="5432",database="SongRec")
	cursor=connection.cursor()
	cursor.execute("UPDATE registration SET user_id=%s,age=%s WHERE username=%s",(user_id,dataTransformed,username,))
	connection.commit()
	songs = recommend_songs(user_id, dataTransformed)
	list_songs = songs.values.tolist()
	return render_template('home.html', username=username,list_of_songs=list_songs,age=dataTransformed)

def AgeClasses(data:str):
    if(data == "teens"):
        return 15
    elif(data == "twenties"):
        return 25
    elif(data == "thirties"):
        return 35
    elif(data == "forties"):
        return 45
    elif(data == "fifties"):
        return 55
    elif(data == "sixties"):
        return 65
    elif(data == "seventies"):
        return 75
    elif(data == "eighties"):
        return 85
    elif(data == "nineties"):
        return 95
    else:
        return 25



if __name__ == "__main__":
    app.run()
