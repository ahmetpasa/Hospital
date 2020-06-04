import mysql.connector
import hashlib
from flask import Flask, render_template, url_for, flash, redirect, request
from form import LoginForm, RoomForm, MeetingForm, MeetingUpdateForm, MeetingDeleteForm, AddDiagnosis

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

@app.route("/doctor", methods=['GET', 'POST'])
def doctor():
    username = request.args.get('username', default = "*", type = str)
    #Adding diagnosis
    form_diags = AddDiagnosis()
    fetch_diags = "SELECT Diagnosis_ID, Result FROM Diagnosis"
    mycursor.execute(fetch_diags)
    for x in mycursor:
        ind_diag = (str(x[0]), x[1])
        form_diags.diag.choices.append(ind_diag)
    fetch_pats = "select patient.Patient_ID, patient.Patient_Name from patient, doctor where patient.Doctor_ID = doctor.Doctor_ID and doctor.Doctor_Name = %(x)s"
    mycursor.execute(fetch_pats, {'x': username})
    for x in mycursor:
        ind_pat = (str(x[0]), x[1])
        form_diags.to_patient.choices.append(ind_pat)
    if form_diags.validate_on_submit():
        insert_stmt = "INSERT INTO Has(Diagnosis_ID, Patient_ID) VALUES(%(x)s, %(y)s)"
        mycursor.execute(insert_stmt,
                         {'x': form_diags.diag.data, 'y': form_diags.to_patient.data})
        mydb.commit()  # commit the changes
        print("Rows affected:", mycursor.rowcount)
        print("Statement:", mycursor.rowcount)
    return render_template('doctor.html',username=username, form_diags=form_diags)

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

@app.route("/patient", methods=['GET', 'POST'])
def patient():
    username = request.args.get('username', default="*", type=str)
    #Patient's profile
    select_stmt_p1 = "SELECT Patient_ID, Patient_Name, Phone_No, Gender, Address, Age FROM Patient WHERE Patient_Name = %(x)s"
    mycursor.execute(select_stmt_p1, {'x': username})
    profile = {}
    for x in mycursor:
        # print(x)
        profile['Patient_ID'] = str(x[0])
        profile['Patient_Name'] = x[1]
        profile['Phone_No'] = x[2]
        profile['Gender'] = 'Male' if x[3] == 1 else 'Female'
        profile['Address'] = x[4]
    # Adding meeting
    select_stmt_m1 = "SELECT count(*) from Meeting"
    mycursor.execute(select_stmt_m1)
    for x in mycursor:
        newMeetingID = x[0] + 1
    select_stmt_m2 = "SELECT Patient_ID from Patient WHERE Patient_Name = %(x)s"
    mycursor.execute(select_stmt_m2, {'x': username})
    for x in mycursor:
        PatientId = x[0]
    select_stmt_m3 = "SELECT count(Record_No) from Meeting WHERE Patient_ID = %(x)s"
    mycursor.execute(select_stmt_m3, {'x': PatientId})
    for x in mycursor:
        newRecordNo = x[0] + 1
    form = MeetingForm()
    if form.validate_on_submit():
        insert_stmt = "INSERT INTO Meeting(Meeting_ID, Patient_ID, Record_No, DescriptionColumn, Appointment) VALUES(%(x)s, %(y)s, %(z)s, %(a)s, %(b)s)"
        mycursor.execute(insert_stmt,
                            {'x': newMeetingID, 'y': PatientId, 'z': newRecordNo, 'a': form.description.data,
                              'b': form.appointment.data})
        mydb.commit()  # commit the changes
        print("Rows affected:", mycursor.rowcount)
        print("Statement:", mycursor.rowcount)
    #Updating and deleting the meeting
    form2 = MeetingUpdateForm()
    if form2.validate_on_submit():
        update_stmt = "UPDATE Meeting SET Appointment = %(x)s WHERE Patient_ID = %(y)s AND Record_No = %(z)s"
        mycursor.execute(update_stmt,
                         {'x': form2.appointmentupd.data, 'y': PatientId, 'z': form2.recordID.data})
        mydb.commit()  # commit the changes
        print("Rows affected:", mycursor.rowcount)
        print("Statement:", mycursor.rowcount)
    form3 = MeetingDeleteForm()
    if form3.validate_on_submit():
        delete_stmt = "DELETE FROM Meeting WHERE Patient_ID = %(x)s AND Record_No = %(y)s"
        mycursor.execute(delete_stmt,
                         {'x': PatientId, 'y': form3.recordIDdel.data})
        mydb.commit()  # commit the changes
        print("Rows affected:", mycursor.rowcount)
        print("Statement:", mycursor.rowcount)
    # Patient's doctor's profile
    select_stmt_p2 = "SELECT Doctor_Name, Speciality, d.Phone_No, d.Gender, d.Address FROM Doctor as d, Patient as p WHERE d.Doctor_ID = p.Doctor_ID AND p.Patient_Name = %(x)s"
    mycursor.execute(select_stmt_p2, {'x': username})
    doctorprofile = {}
    for x in mycursor:
        # print(x)
        doctorprofile['Doctor_Name'] = x[0]
        doctorprofile['Speciality'] = x[1]
        doctorprofile['Phone_No'] = x[2]
        doctorprofile['Gender'] = 'Male' if x[3] == 1 else 'Female'
        doctorprofile['Address'] = x[4]
    # Patient's previous meetings
    select_stmt_p3 = "SELECT Record_No, DescriptionColumn, Appointment FROM Meeting, Patient WHERE Meeting.Patient_ID = Patient.Patient_ID AND Patient_Name = %(x)s"
    mycursor.execute(select_stmt_p3, {'x': username})
    meetings = []
    for x in mycursor:
        # print(x)
        meeting = {}
        meeting['Record_No'] = str(x[0])
        meeting['DescriptionColumn'] = x[1]
        meeting['Appointment'] = str(x[2])
        meetings.append(meeting)
    # Patient's previous medicines
    select_stmt_p4 = "SELECT m.MedicineName, m.Quantity, m.Price FROM Medicine as m,Given as g, Patient WHERE g.Patient_ID = Patient.Patient_ID AND g.Medicine_ID = m.Medicine_ID AND Patient_Name = %(x)s"
    mycursor.execute(select_stmt_p4, {'x': username})
    medicines = []
    for x in mycursor:
        # print(x)
        medicine = {}
        medicine['MedicineName'] = x[0]
        medicine['Quantity'] = str(x[1])
        medicine['Price'] = str(x[2])
        medicines.append(medicine)
    # Patient's previous records
    select_stmt_p5 = "SELECT Record_ID, Date_Admitted, Date_Discharged FROM Record, Patient WHERE Record.Patient_ID = Patient.Patient_ID AND Patient_Name = %(x)s"
    mycursor.execute(select_stmt_p5, {'x': username})
    records = []
    for x in mycursor:
        # print(x)
        record = {}
        record['Record_ID'] = str(x[0])
        record['Date_Admitted'] = str(x[1])
        record['Date_Discharged'] = str(x[2])
        records.append(record)
    # Patient's previous diagnoses
    select_stmt_p6 = "SELECT d.Diagnosis_ID, d.Result FROM Diagnosis as d, Has, Patient WHERE Has.Diagnosis_ID = d.Diagnosis_ID AND Patient.Patient_ID = Has.Patient_ID AND Patient_Name = %(x)s"
    mycursor.execute(select_stmt_p6, {'x': username})
    diagnoses = []
    for x in mycursor:
        # print(x)
        diagnosis = {}
        diagnosis['Diagnosis_ID'] = str(x[0])
        diagnosis['Result'] = x[1]
        diagnoses.append(diagnosis)
    #Patient's room(if there is)
    select_stmt_p7 = "SELECT Room_ID, RoomType, Nurse_Name, Phone_No FROM room, nurse where nurse.Nurse_ID = room.Nurse_ID and Patient_ID = %(x)s;"
    mycursor.execute(select_stmt_p7, {'x': PatientId})
    roominfo = []
    for x in mycursor:
        # print(x)
        room = {}
        room['Room_ID'] = str(x[0])
        room['RoomType'] = x[1]
        room['Nurse_Name'] = x[2]
        room['Phone_No'] = x[3]
        roominfo.append(room)

    return render_template('patient.html', username=username, profile=profile, doctorprofile=doctorprofile, meetings=meetings, medicines=medicines, records=records, diagnoses=diagnoses, form=form, form2=form2, form3=form3, roominfo=roominfo)



if __name__ == '__main__':
    app.run(debug=True)
