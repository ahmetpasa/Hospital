import mysql.connector
import hashlib
from flask import Flask, render_template, url_for, flash, redirect, request
from form import LoginForm

#mysql connection
#!!!parameters must be changed according to the server !!!
mydb = mysql.connector.connect(user='root',
                              host='127.0.0.1',
                              password='123',
                              auth_plugin='mysql_native_password',
                              database = 'hospital'
                              )

mycursor = mydb.cursor()

app = Flask(__name__)

app.config['SECRET_KEY'] = '226e42e17768b4531ea8bebd49dc1ab7'

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        select_stmt = "SELECT Username, Typ FROM Users WHERE Username = %(x)s and Pass = %(y)s"
        hashed_password = hashlib.sha256(str(form.password.data).encode('utf-8')).hexdigest()
        mycursor.execute(select_stmt, { 'x': form.username.data, 'y' : hashed_password})
        flag = False
        for x in mycursor:
            flag = True
            #flash(f'Welcome again {x[0]}! {x[1]}', 'success')
            if x[1] == 'doctor':
                username = "?username="+str(x[0])
                return redirect(url_for('doctor') + username)
            if x[1] == 'nurse':
                username = "?username="+str(x[0])
                return redirect(url_for('nurse') + username)
            if x[1] == 'patient':
                username = "?username="+str(x[0])
                return redirect(url_for('patient') + username)
            
        
        if flag == False:
            flash('There is something wrong, I can feel it', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/doctor")
def doctor():
    username = request.args.get('username', default = "*", type = str)
    return render_template('doctor.html',username=username)

@app.route("/nurse")
def nurse():
    username = request.args.get('username', default = "*", type = str)
    return render_template('nurse.html',username=username)

@app.route("/patient")
def patient():
    username = request.args.get('username', default = "*", type = str)
    return render_template('patient.html',username=username)


if __name__ == '__main__':
    app.run(debug=True)