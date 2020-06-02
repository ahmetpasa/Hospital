import mysql.connector
import hashlib
from flask import Flask, render_template, url_for, flash, redirect, request
from form import LoginForm, RoomForm

#mysql connection
#!!!parameters must be changed according to the server !!!
mydb = mysql.connector.connect(user='root',
                              host='127.0.0.1',
                              password='123',
                              auth_plugin='mysql_native_password',
                              database = 'hospital'
                              )

mycursor = mydb.cursor(buffered=True)

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

@app.route("/nurse", methods=['GET', 'POST'])
def nurse():
    username = request.args.get('username', default = "*", type = str)
    ##get nurseID
    select_nurse = 'SELECT Nurse_ID FROM Nurse WHERE Nurse_Name = %(x)s'
    mycursor.execute(select_nurse, { 'x': username})
    nurse_id = 0
    for x in mycursor:
            nurse_id = x[0]
    ##updating rooms
    form = RoomForm()
    if form.validate_on_submit():
        ## Check if patient exist
        patient_id = -1
        select_stmt3 = 'SELECT Patient_ID FROM Patient WHERE Patient_Name = %(x)s'
        mycursor.execute(select_stmt3, { 'x': form.patient.data})
        flagP = False
        for x in mycursor:
            flagP = True
            patient_id = x[0]
        if form.patient.data == 'null':
            patient_id = None
            flagP = True
        if flagP == False:
            flash('There is something wrong about patient, I can feel it', 'danger')
        
        ## Check if nurse exist
        nurse_id = -1
        select_nurse = 'SELECT Nurse_ID FROM Nurse WHERE Nurse_Name = %(x)s'
        mycursor.execute(select_nurse, { 'x': form.nurse.data})
        flagN = False
        for x in mycursor:
            nurse_id = x[0]
            flagN = True
        if form.nurse.data == 'null':
            nurse_id = None
            flagN = True
        if flagN == False:
            flash('There is something wrong about nurse, I can feel it', 'danger')
        ##update
        if flagN and flagP:
            select_stmt4 = 'UPDATE Room SET Patient_ID=%(x)s, Nurse_ID=%(y)s WHERE Room_ID=%(z)s'
            #mycursor.execute('UPDATE Room SET Patient_ID=44, Nurse_ID=152 WHERE Room_ID=3')
            mycursor.execute(select_stmt4, {'x': patient_id,'y':nurse_id,'z':form.roomID.data})
            #mycursor.fetchall()
            mydb.commit()  # commit the changes
            print("Rows affected:", mycursor.rowcount)
            print("Statement:", mycursor.rowcount)
        #mycursor.fetchall()

    ##Fetching the profile
    select_stmt1 = "SELECT * FROM Nurse WHERE Nurse_Name = %(x)s"
    mycursor.execute(select_stmt1, { 'x': username})
    profile = {}
    for x in mycursor:
        #print(x)
        profile['Nurse_ID'] = str(x[0])
        profile['Nurse_Name'] = x[1]
        profile['Phone_No'] = x[2]
        profile['Gender'] = 'Male' if x[3]==1 else 'Female'
        profile['Address'] = x[4]
    ##Fetching the patients
    select_stmtP = "SELECT Patient_Name,Gender,Age FROM Patient"
    mycursor.execute(select_stmtP)
    patients = []
    for x in mycursor:
        patient = {}
        patient['Patient_Name'] = x[0]
        patient['Gender'] = 'Male' if x[1]==1 else 'Female'
        patient['Age'] = str(x[2])
        patients.append(patient)
    ##Fetching rooms
    rooms = []
    select_stmt2 = """SELECT Room_ID,Nurse_Name,Patient_Name,RoomType,Result
                     FROM Room, Nurse, Patient, Has, Diagnosis
                     WHERE Patient.Patient_ID = Room.Patient_ID and
                           Room.Nurse_ID = Nurse.Nurse_ID and
                           Has.Patient_ID = Patient.Patient_ID and
                           Has.Diagnosis_ID = Diagnosis.Diagnosis_ID"""
    mycursor.execute(select_stmt2)
    for x in mycursor:
        room = {}
        room['Room_ID'] = str(x[0])
        room['Nurse_Name'] = x[1]
        room['Patient_Name'] = x[2]
        room['RoomType'] = x[3]
        room['Result'] = x[4]
        rooms.append(room)
    print(len(rooms))
    return render_template('nurse.html',profile=profile,rooms=rooms,username=username,form=form,patients=patients)

@app.route("/patient")
def patient():
    username = request.args.get('username', default = "*", type = str)
    return render_template('patient.html',username=username)


if __name__ == '__main__':
    app.run(debug=True)