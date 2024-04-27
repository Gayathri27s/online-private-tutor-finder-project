from flask import Flask, render_template, request, session, flash, send_file
import mysql.connector

app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = 'aaa'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/AdminLogin')
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route('/TutorLogin')
def TutorLogin():
    return render_template('TutorLogin.html')


@app.route('/StudentLogin')
def StudentLogin():
    return render_template('StudentLogin.html')


@app.route('/NewTutor')
def NewTutor():
    return render_template('NewTutor.html')


@app.route('/NewStudent')
def NewStudent():
    return render_template('NewStudent.html')


@app.route('/AdminHome')
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tutortb")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/alogin", methods=['GET', 'POST'])
def alogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
            cur = conn.cursor()
            cur.execute("SELECT * FROM tutortb")
            data = cur.fetchall()
            return render_template('AdminHome.html', data=data)

        else:
            flash('Username or Password is wrong')
            return render_template('AdminLogin.html')


@app.route("/newTutor", methods=['GET', 'POST'])
def newTutor():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        uname = request.form['uname']
        education = request.form['education']
        about = request.form['about']
        password = request.form['password']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tutortb VALUES ('','" + name + "','" + mobile + "','" + email + "','" + address
            + "','" + education + "','" + about + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        flash('Tutor Register successfully')
        return render_template('NewTutor.html')


@app.route("/tlogin", methods=['GET', 'POST'])
def tlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['tname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
        cursor = conn.cursor()
        cursor.execute("SELECT * from tutortb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('TutorLogin.html')
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
            cur = conn.cursor()
            cur.execute("SELECT * FROM tutortb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('TutorHome.html', data=data)


@app.route('/TutorHome')
def TutorHome():
    sname = session['tname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tutortb where username='" + sname + "' ")
    data = cur.fetchall()

    return render_template('TutorHome.html', data=data)


@app.route('/TProfile')
def TProfile():
    return render_template('TProfile.html')


@app.route('/TAddSchedule')
def TAddSchedule():
    return render_template('TAddSchedule.html')


@app.route("/profileupdate", methods=['GET', 'POST'])
def profileupdate():
    if request.method == 'POST':
        sname = session['tname']

        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        education = request.form['education']
        about = request.form['about']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
        cursor = conn.cursor()
        cursor.execute(
            "update  tutortb set  email = '" + email + "',mobile='" + mobile + "',address='" + address
            + "',education='" + education + "',about='" + about + "' where Username='" + sname + "'")
        conn.commit()
        conn.close()
        flash('Profile Update successfully')
        return render_template('TProfile.html')


@app.route("/newschedule", methods=['GET', 'POST'])
def newschedule():
    if request.method == 'POST':
        sname = session['tname']
        Class = request.form['Class']
        SubjectName = request.form['SubjectName']
        Schedule = request.form['Schedule']
        Duration = request.form['Duration']
        Amount = request.form['Amount']
        Info = request.form['Info']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
        cursor = conn.cursor()
        cursor.execute("SELECT * from schdtb where TName='" + sname + "' and Schedu='" + Schedule + "'")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO schdtb VALUES ('','" + sname + "','" + Class + "','" + SubjectName + "','" + Schedule
                + "','" + Duration + "','" + Amount + "','" + Info + "')")
            conn.commit()
            conn.close()

            flash('New Tuition Info Save successfully')
            return render_template('TAddSchedule.html')
        else:
            flash('Please  Change Schedule Time')
            return render_template('TAddSchedule.html')


@app.route("/TScheduleInfo")
def TScheduleInfo():
    sname = session['tname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM schdtb where Tname='" + sname + "'  ")
    data = cur.fetchall()
    return render_template('TScheduleInfo.html', data=data)


@app.route("/TSRemove")
def TSRemove():
    id = request.args.get('id')
    sname = session['tname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cursor = conn.cursor()
    cursor.execute(
        "delete from schdtb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash(' Tuition  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM schdtb where Tname='" + sname + "'  ")
    data = cur.fetchall()
    return render_template('TScheduleInfo.html', data=data)


@app.route('/TBookInfo')
def TBookInfo():
    sname = session['tname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM jointb where Tname='" + sname + "' ")
    data = cur.fetchall()
    return render_template('TBookInfo.html', data=data)


@app.route("/newStudent", methods=['GET', 'POST'])
def newStudent():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO studenttb VALUES ('','" + name + "','" + email + "','" + mobile + "','" + address + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        flash('NewStudent successfully')

    return render_template('NewStudent.html')


@app.route("/stlogin", methods=['GET', 'POST'])
def stlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['sname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
        cursor = conn.cursor()
        cursor.execute("SELECT * from  studenttb where username='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('StudentLogin.html')
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
            cur = conn.cursor()
            cur.execute("SELECT * FROM  studenttb where username='" + username + "' and password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('StudentHome.html', data=data)


@app.route('/SProfile')
def SProfile():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tutortb ")
    data = cur.fetchall()
    return render_template('SProfile.html', data=data)


@app.route('/SSchedule')
def SSchedule():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM schdtb ")
    data = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT distinct SubjectName from schdtb ")
    data1 = cur.fetchall()
    return render_template('SSchedule.html', data=data,data1=data1)


@app.route("/Search", methods=['GET', 'POST'])
def Search():
    if request.method == 'POST':
        SubjectName = request.form['SubjectName']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
        cur = conn.cursor()
        cur.execute("SELECT * from  schdtb where SubjectName='" + SubjectName + "' ")
        data = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
        cur = conn.cursor()
        cur.execute("SELECT distinct SubjectName from schdtb  ")
        data1 = cur.fetchall()
        return render_template('SSchedule.html', data=data,data1=data1)




@app.route("/Book")
def Book():
    id = request.args.get('id')
    session['id'] = id

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM schdtb where  id='" + id + "'")
    data1 = cursor.fetchone()
    if data1:
        Amount = data1[6]
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM schdtb  where  id='" + id + "' ")
    data = cur.fetchall()

    return render_template('SBook.html', amt=Amount, data=data)


@app.route("/Sbook", methods=['GET', 'POST'])
def Sbook():
    if request.method == 'POST':
        id = session['id']
        sname = session['sname']
        cname = request.form['cname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM schdtb where  id='" + id + "'")
        data = cursor.fetchone()
        if data:
            Tname = data[1]
            Clname = data[2]
            Subname = data[3]
            Sch = data[4]
            Duration = data[5]
            Amount = data[6]


        else:
            return 'Incorrect username / password !'

        dd = int(Duration) * 30

        from datetime import timedelta
        from datetime import date

        Begindatestring = date.today()

        # print begin date
        print("Beginning date")
        print(Begindatestring)

        # calculating end date by adding 4 days
        Enddate = Begindatestring + timedelta(days=int(dd))

        # printing end date
        print("Ending date")
        print(Enddate)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
        cur = conn.cursor()
        cur.execute(
            "SELECT *  FROM  jointb where Tname='" + Tname + "' and Sch='" + Sch + "' and  '" + str(
                Begindatestring) + "' between   SDate  and  Edate  ")
        data2 = cur.fetchone()
        if data2:
            flash('Already Book this  Date')

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
            cursor = conn.cursor()
            cursor.execute("SELECT  *  FROM schdtb where  id='" + id + "'")
            data1 = cursor.fetchone()
            if data1:
                Amount = data1[6]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
            cur = conn.cursor()
            cur.execute("SELECT * FROM schdtb  where  id='" + id + "' ")
            data = cur.fetchall()

            return render_template('SBook.html', amt=Amount, data=data)

        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO jointb VALUES ('','" + sname + "','" + Tname + "','" + Subname + "','" + Sch + "','" + Duration
                + "','" + Amount + "','" + str(Begindatestring) + "','" + str(Enddate) + "','" + cname + "')")
            conn.commit()
            conn.close()
            flash('Tutor Book  successfully')
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
            cur = conn.cursor()
            cur.execute("SELECT * FROM jointb   where  id='" + id + "' ")
            data = cur.fetchall()

            return render_template('SBookInfo.html', data=data)


@app.route('/SBookInfo')
def SBookInfo():
    sname = session['sname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM jointb where Sname='" + sname + "' ")
    data = cur.fetchall()
    return render_template('SBookInfo.html', data=data)


@app.route('/SFeedBack')
def SFeedBack():
    sname = session['sname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT Distinct Tname FROM jointb where Sname='" + sname + "' ")
    data = cur.fetchall()
    return render_template('SFeedBack.html', data=data)


@app.route('/SFeedBackInfo')
def SFeedBackInfo():
    sname = session['sname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT *  from feedtb where Sname='" + sname + "' ")
    data = cur.fetchall()
    return render_template('SFeedBackInfo.html', data=data)


@app.route('/TFeedBack')
def TFeedBack():
    sname = session['tname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT *  from feedtb where Tname='" + sname + "' ")
    data = cur.fetchall()
    return render_template('TFeedBack.html', data=data)


@app.route("/down")
def down():
    id = request.args.get('id')
    print(id)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cursor = conn.cursor()
    cursor.execute("SELECT * from doctb where id ='" + id + "'   ")
    data = cursor.fetchone()
    if data is None:

        return 'Assingment Not Upload'
    else:

        filename = data[4]

        return send_file('static/upload/' + filename, as_attachment=True)


@app.route("/newfeed", methods=['GET', 'POST'])
def newfeed():
    if request.method == 'POST':
        sname = session['sname']
        tname = request.form['tname']
        feedbac = request.form['FeedBack']

        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO feedtb VALUES ('','" + sname + "','" + tname + "','" + feedbac + "','" + date + "')")
        conn.commit()
        conn.close()
        flash('New Feedback Register successfully')
        return render_template('SFeedBack.html')


@app.route('/AStudentInfo')
def AStudentInfo():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  studenttb  ")
    data = cur.fetchall()
    return render_template('AStudentInfo.html', data=data)


@app.route('/AScheduleInfo')
def AScheduleInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM schdtb  ")
    data = cur.fetchall()
    return render_template('AScheduleInfo.html', data=data)

@app.route('/AJoinInfo')
def AJoinInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM jointb  ")
    data = cur.fetchall()
    return render_template('AJoinInfo.html', data=data)

@app.route('/AFeedBackInfo')
def AFeedBackInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2privatetutor')
    cur = conn.cursor()
    cur.execute("SELECT * FROM feedtb  ")
    data = cur.fetchall()
    return render_template('AFeedBackInfo.html', data=data)
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
