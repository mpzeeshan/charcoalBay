#from crypt import methods
from flask import Flask, session, g, url_for
from flask import render_template
from flask import request
import os
import asyncio
from flask_sqlalchemy import SQLAlchemy
from datetime import date



app = Flask(__name__)

app.config.update(
    SECRET_KEY='shan',
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/charcoaldb',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)



class SOPcounter_staff(db.Model):
    __tablename__ = 'sopCounterStaff'

    id = db.Column(db.Integer, primary_key=True)
    sop = db.Column(db.String(), nullable=False)

    def __init__(self, sop):
        self.sop = sop

    def __repr__(self, sop):
        return sop 


class SOPkitchen(db.Model):
    __tablename__ = 'sopKitchen'

    id = db.Column(db.Integer, primary_key=True)
    sop = db.Column(db.String(), nullable=False,)

    def __init__(self, sop):
        self.sop = sop


class CleaningStaffChecklist(db.Model):
    __tablename__ = 'cleaningsChecklist'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(), nullable=False, unique = True)

    def __init__(self, item):
        self.item = item


class CounterStaffChecklist(db.Model):
    __tablename__ = 'countersChecklist'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(), nullable=False,  unique = True)

    def __init__(self, item):
        self.item = item


class KitchenStaffChecklist(db.Model):
    __tablename__ = 'kitchensChecklist'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(), nullable=False,)

    def __init__(self, item):
        self.item = item


class OnlineMeetings(db.Model):
    __tablename__ = 'onlineMeetings'

    id = db.Column(db.Integer, primary_key=True)
    magenda = db.Column(db.String(40), nullable=False)
    mhost = db.Column(db.String(40), nullable=False)
    time = db.Column(db.String(40), nullable=False)
    date = db.Column(db.String, nullable=False,)
    link = db.Column(db.String(),nullable=False)
    audience = db.Column(db.String(),nullable=False)

    def __init__(self, magenda, mhost, time, date, link, audience):
        self.magenda = magenda
        self.mhost = mhost
        self.time = time
        self.date = date
        self.link = link
        self.audience = audience


class OnlineTrainings(db.Model):
    __tablename__ = 'onlineTrainings'

    id = db.Column(db.Integer, primary_key=True)
    magenda = db.Column(db.String(40), nullable=False)
    mhost = db.Column(db.String(40), nullable=False)
    time = db.Column(db.String(40), nullable=False)
    date = db.Column(db.String, nullable=False,)
    link = db.Column(db.String(),nullable=False)
    audience = db.Column(db.String(),nullable=False)
    mode = db.Column(db.String())

    def __init__(self, magenda, mhost, time, date, link, audience, mode):
        self.magenda = magenda
        self.mhost = mhost
        self.time = time
        self.date = date
        self.link = link
        self.audience = audience
        self.mode = mode



class Register(db.Model):

    __tablename__ = 'register'
    
    name = db.Column(db.String(40),nullable=False)
    email = db.Column(db.String(40), primary_key=True)
    username = db.Column(db.String(40),unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    outlet = db.Column(db.String(40),nullable=False)
    role = db.Column(db.String(40),nullable=False)
    
    def __init__(self, name, email, username, password, outlet, role):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.outlet = outlet
        self.role = role


class ProdcutDevelopment(db.Model):
    __tablename__ = 'productDev'

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String, nullable = False)
    user = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    outlet = db.Column(db.String(5), nullable=False)

    def __init__(self, review, user, name, date, outlet):
        self.review = review
        self.user = user
        self.name = name
        self.date = date
        self.outlet = outlet

class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String, nullable = False)
    user = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    outlet = db.Column(db.String(5), nullable=False)

    def __init__(self, review, user, name, date, outlet):
        self.review = review
        self.user = user
        self.name = name
        self.date = date
        self.outlet = outlet

class DailyUpdatesCallCenter(db.Model):
    __tablename__ = 'dailyUpdates'

    date = db.Column(db.String, primary_key=True)
    user = db.Column(db.String, nullable=False)
    callsDaily = db.Column(db.String, nullable=False)
    ordersDaily = db.Column(db.String, nullable=False)
    complaintsDaily = db.Column(db.String, nullable=False)
    onlineReviews = db.Column(db.String, nullable=False)
    participationofCC = db.Column(db.String, nullable=False)
    reviewResponse = db.Column(db.String, nullable=False)
    reviewSuggestions = db.Column(db.String, nullable=False)

    def __init__(self, date, user, callsDaily, ordersDaily, complaintsDaily, onlineReviews, participationofCC, reviewResponse, reviewSuggestions):
        self.date = date
        self.user = user
        self.callsDaily = callsDaily
        self.ordersDaily = ordersDaily
        self.complaintsDaily = complaintsDaily
        self.onlineReviews = onlineReviews
        self.participationofCC = participationofCC
        self.reviewResponse = reviewResponse
        self.reviewSuggestions = reviewSuggestions



class ManagerChecklist(db.Model):
    __tablename__ = 'managerChecklist'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(), nullable=False)
    outlet = db.Column(db.String(), nullable=False)

    def __init__(self, item, outlet):
        self.item = item
        self.outlet = outlet





meet_agenda = ['Daily Meeting',
               'Special Guests',
              ]

meet_time = ['10:00 A.M',
             '2:00 P.M',
            ]

meet_date = ['30/09/2022', 
             '01/10/2022',
            ]

meet_host = ['Manager',
             'Super Admin',
            ]


coordinator_menu_items = [
                          'TASK',
                          'CHECKLIST',
                          'MEETINGS',
                          'TRAININGS',
                          'PRODUCT DEVELOPMENT',
                          'REVIEWS',
                         ]



clstaff_menu_items = ['CLEANING',
                      'MEETINGS',
                      'TRAININGS',
                      'STOCKLIST',
                      'SOP',
                      'REVIEWS',
                     ]

counterStaff_menu_items = ['CLEANING',
                      'MEETINGS',
                      'TRAININGS',
                      'STOCKLIST',
                      'SOP',
                      'REVIEWS',
                      'PRODUCT DEVELOPMENT',
                     ]

pstaff_menu_items = [ 'CLEANING',
                      'MEETINGS',
                      'TRAININGS',
                      'STOCKLIST',
                      'SOP',
                      'REVIEWS',
                      'PRODUCT DEVELOPMENT',
                      'CHARCOAL USAGE',
                      'PREPARATION LIST',
                     ]

cl_menu_links = ["checklist",
                 "meetings",
                 "trainings",
                 "stocklist",
                 "sop",
                 "review",
                ]


counterStaff_menu_links = ["checklist",
                 "meetings",
                 "trainings",
                 "stocklist",
                 "sop",
                 "review",
                 "productDev",
                ]

pstaff_menu_links = ["checklist",
                 "meetings",
                 "trainings",
                 "stocklist",
                 "sop",
                 "review",
                 "productDev",
                 "charcoal",
                 "plist",
                ]




@app.route("/", methods=['POST', 'GET'])
async def index():
    if request.method == 'POST':
        session.pop('user', None)

        global userData
        global uname
        global menu
        global menu_links

        uname = request.form.get('uname')
        password = request.form.get('psw')
        userData = Register.query.filter_by(username=uname).one()
        if uname == userData.username and password == userData.password:
            
            session['user'] = request.form.get('uname')

            if userData.role == "Production Staff":
                menu = pstaff_menu_items
                menu_links = pstaff_menu_links
            elif userData.role == "Cleaning Staff":
                menu = clstaff_menu_items
                menu_links = cl_menu_links
            elif userData.role == "Counter Staff":
                menu = counterStaff_menu_items
                menu_links = counterStaff_menu_links
            elif userData.role == "Store Coordinator":
                return render_template('store-coordinator/coordinator-home.html',login_name = session['user'], login_category = userData.role)
            elif userData.role == "Call Center":
                return render_template('call-center/call-home.html',login_name = session['user'], login_category = userData.role)    
            elif userData.role == "Store Manager":
                return render_template('store-manager/manager-home.html',login_name = session['user'], login_category = userData.role)

            return render_template('home.html',login_name = userData.name, login_category = userData.role, menu = menu, menu_links = menu_links)
       
        else:
            
            return render_template('login.html',message = "Invalid Username or Password")
    else:
       
        uname = ""
        db.create_all()
        # reg = Register('John Doe','john@gmail.com', 'john', 'password', '4', 'Quality Assurance')
        # db.session.add(reg)
        # db.session.commit()
        
        
        

        # data = Register.query.all()
        # for i in data:
        #     print(i.name)

        return render_template('login.html')



@app.route("/checklist", methods=['GET'])
async def checklist():
    
    if userData.role == "Cleaning Staff":
        checklist = CleaningStaffChecklist.query.all()
        clist = []
        for i in checklist:
            clist.append(i.item)
    elif userData.role == "Counter Staff":
        checklist = CounterStaffChecklist.query.all()
        clist = []
        for i in checklist:
            clist.append(i.item)
    elif userData.role == "Production Staff":
        checklist = KitchenStaffChecklist.query.all()

        clist = []
        for i in checklist:
            clist.append(i.item)

    
    return render_template('checklist.html',checklist = clist, login_name = userData.name, login_category = userData.role, menu = menu, menu_links= menu_links)



@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']


@app.route('/dropsession')
def dropSession():
    session.pop('user', None)
    return render_template('login.html')



@app.route("/meetings", methods=['GET'])
async def meetings():
    if g.user:
        return render_template('meetings.html', login_name = session['user'], login_category = userData.role, menu = menu, menu_links= menu_links)
   

@app.route("/trainings", methods=['GET'])
async def trainings():
    if g.user:  
        return render_template('trainings.html', login_name = userData.name, login_category = userData.role, menu = menu, menu_links= menu_links)



@app.route("/sop",methods=['GET'])
async def sop():

    if userData.role == "Cleaning Staff":
        sop_list = []
    elif userData.role == "Counter Staff":
        sop = SOPcounter_staff.query.all()
        sop_list = []
        for i in sop:
            sop_list.append(i.sop)
    elif userData.role == "Production Staff":
        sop = SOPkitchen.query.all()
        sop_list = []
        for i in sop:
            sop_list.append(i.sop)


    return render_template('sop.html',sop_list = sop_list, login_name = userData.name, login_category = userData.role, menu = menu, menu_links= menu_links)

   

@app.route("/onlinemeetings", methods=['GET'])
async def omeetings():
    res = OnlineMeetings.query.all()

    name = []
    mhost = []
    time = []
    date = []
    link = []

    for i in res:
        name.append(i.magenda)
        mhost.append(i.mhost)
        time.append(i.time)
        date.append(i.date)
        link.append(i.link)

    return render_template('omeeting.html',m_agenda= name, m_host = mhost, m_time = time, m_date = date, mlink = link, login_name = userData.name, login_category =userData.role,  menu = menu, menu_links= menu_links)


@app.route("/offlinemeetings", methods=['GET'])
async def fmeetings():
    
    res = OnlineMeetings.query.all()

    name = []
    mhost = []
    time = []
    date = []
    link = []

    for i in res:
        name.append(i.magenda)
        mhost.append(i.mhost)
        time.append(i.time)
        date.append(i.date)
        link.append(i.link)

    return render_template('omeeting.html',m_agenda= name, m_host = mhost, m_time = time, m_date = date, mlink = link, login_name = userData.name, login_category =userData.role,  menu = menu, menu_links= menu_links)

    


@app.route("/onlinetrainings", methods=['GET'])
async def otrainings():

    result = OnlineTrainings.query.all()

    name = []
    mhost = []
    time = []
    date = []
    link = []

    for i in result:
        name.append(i.magenda)
        mhost.append(i.mhost)
        time.append(i.time)
        date.append(i.date)
        link.append(i.link)

    return render_template('otraining.html',t_name= name, t_trainer = mhost, t_time = time, t_date = date, t_venue=link, login_name = userData.name, login_category =userData.role ,menu = menu, menu_links = menu_links)

    
    #return render_template('otraining.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date)

@app.route("/offlinetrainings", methods=['GET'])
async def ftrainings():
    
    result = OnlineTrainings.query.all()

    name = []
    mhost = []
    time = []
    date = []
    link = []

    for i in result:
        name.append(i.magenda)
        mhost.append(i.mhost)
        time.append(i.time)
        date.append(i.date)
        link.append(i.link)

    return render_template('otraining.html',t_name= name, t_trainer = mhost, t_time = time, t_date = date, t_venue=link, login_name = userData.name, login_category =userData.role ,menu = menu, menu_links = menu_links)

    
    #return render_template('ftraining.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date)

@app.route("/review",methods=['GET'])
async def review():
    return render_template('review.html', login_name = userData.name, login_category = userData.role, user = userData.username, outlet = userData.outlet, menu = menu, menu_links= menu_links)



@app.route("/staffreviewSubmit/<user>/<name>/<outlet>/<role>",methods=['GET','POST'])
async def staffreview(user, name, outlet, role):
    if request.method == 'POST':
        rev_obj = Review(request.form.get('review'),user=user, name=name, date=date.today(), outlet = outlet)
        db.session.add(rev_obj)
        db.session.commit()
        # return render_template('store-coordinator/Creview.html',login_name = name, login_category = role, outlet = outlet, user = user )
        return render_template('review.html',login_name = name, login_category = role, outlet = outlet, user = user, menu = menu, menu_links= menu_links)




@app.route("/productDevelopment", methods=["GET"])
async def productDev():
    return render_template('productDevelopment.html', login_name = userData.name, login_category = userData.role, user = userData.username, outlet = userData.outlet, menu = menu, menu_links= menu_links)


@app.route("/submitstaffPD/<user>/<name>/<outlet>/<role>", methods=['POST', 'GET'])
async def submitstaffPD(user, name, outlet, role):
    if request.method == 'POST':
        pd_obj = ProdcutDevelopment(request.form.get('pd'),user=user, name=name, date=date.today(), outlet = outlet)
        db.session.add(pd_obj)
        db.session.commit()
        return render_template('productDevelopment.html',login_name = name, login_category = role, outlet = outlet, user = user, menu = menu, menu_links= menu_links )






@app.route("/stocklist",methods=["GET"])
async def stocklist():
    return render_template('stocklist.html', login_name = userData.name, login_category = userData.role, menu = menu, menu_links= menu_links)


@app.route("/charcoalUsage", methods=["GET"])
async def charcoal():
    return render_template('charcoalUsage.html', login_name = userData.name, login_category = userData.role, menu = menu, menu_links= menu_links)
    

@app.route("/preparationList",methods=["GET"])
async def plist():
    return render_template('plist.html', login_name = userData.name, login_category = userData.role, menu = menu, menu_links= menu_links)


@app.route("/tasks",methods=["GET"])
async def tasks():
    return render_template('store-coordinator/coordinator-tasks.html',login_name = userData.name, login_category = userData.role)



@app.route("/task",methods=["GET"])
async def task():
    return render_template('store-coordinator/coordinator-task.html',login_name = userData.name, login_category = userData.role)

@app.route("/coordinatorMeetings",methods=["GET"])
async def cordMeetings():
    return render_template('store-coordinator/coordinator-meetings.html',login_name = userData.name, login_category = userData.role)

@app.route("/addmeetings",methods=["GET"])
async def addmeetings():
    result = OnlineMeetings.query.all()
    m_id = []
    m_name = []
    for i in result:
        m_id.append(i.id)
        m_name.append(i.magenda.split(' ')[0])
    
    return render_template('store-coordinator/add-meetings.html',login_name = userData.name, login_category = userData.role, m_id = m_id, m_name = m_name)

@app.route("/coordinatorTrainings",methods=["GET"])
async def cordTrainings():
    return render_template('store-coordinator/coordinator-trainings.html',login_name = userData.name, login_category = userData.role)


@app.route("/addtrainings",methods=["GET"])
async def addtrainings():
    result = OnlineTrainings.query.all()
    t_id = []
    t_name = []

    for i in result:
        t_id.append(i.id)
        t_name.append(i.magenda.split(' ')[0])

    return render_template('store-coordinator/add-trainings.html',login_name = userData.name, login_category = userData.role, t_id = t_id, t_name = t_name)



@app.route("/newtraining/<mode>",methods=['GET','POST'])
async def newtraining(mode):
    if request.method == 'POST':
        try:
            train = OnlineTrainings(request.form.get('tname'),request.form.get('trainer'),request.form.get('ttime'),request.form.get('tDate'),request.form.get('tVenue'),request.form.get('audience'),mode)
            db.session.add(train)
            db.session.commit()

            return render_template('store-coordinator/new-training.html',login_name = userData.name, login_category = userData.role)
        except Exception as e:
            print(e)

    return render_template('store-coordinator/new-training.html',login_name = userData.name, login_category = userData.role)



@app.route("/training-content/<t_id>",methods=["GET"])
async def trainingContent(t_id):
    try:
        res = OnlineTrainings.query.filter_by(id=t_id).one()
    except Exception as e:
        print(e)

    return render_template('store-coordinator/training-content.html',login_name = userData.name, login_category = userData.role,t_name = res.magenda, t_host = res.mhost, t_time = res.time, t_date = res.date, t_link = res.link, t_aud = res.audience)



@app.route("/new-meeting",methods=['POST', 'GET'])
async def newmeeting():
    if request.method == 'POST':
        try:
            meet_obj = OnlineMeetings(request.form.get('magenda'),request.form.get('mhost'),request.form.get('mtime'),request.form.get('mDate'),request.form.get('mlink'),request.form.get('audience'))
            db.session.add(meet_obj)
            db.session.commit()    
        except Exception as e:
            print(e)
        return render_template('store-coordinator/new-meeting.html',login_name = userData.name, login_category = userData.role)
    else:
        
        return render_template('store-coordinator/new-meeting.html',login_name = userData.name, login_category = userData.role)


@app.route("/coordinatorPD", methods=['POST', 'GET'])
async def coordinatorPD():
    return render_template('store-coordinator/prodDevelop.html',login_name = userData.name, login_category = userData.role, outlet= userData.outlet, user = session['user'])



@app.route("/coordinatorReview", methods=['POST', 'GET'])
async def coordinatorReview():
    return render_template('store-coordinator/Creview.html',login_name = userData.name, login_category = userData.role, outlet= userData.outlet, user = session['user'] )

@app.route("/callcenterReview", methods=['POST', 'GET'])
async def callcenterReview():
    return render_template('call-center/call-reviews.html',login_name = userData.name, login_category = userData.role, outlet= userData.outlet, user = session['user'] )




@app.route("/submitPD/<user>/<name>/<outlet>/<role>", methods=['POST', 'GET'])
async def submitPD(user, name, outlet, role):
    if request.method == 'POST':
        pd_obj = ProdcutDevelopment(request.form.get('pd'),user=user, name=name, date=date.today(), outlet = outlet)
        db.session.add(pd_obj)
        db.session.commit()
        return render_template('store-coordinator/Creview.html',login_name = name, login_category = role, outlet = outlet, user = user )




@app.route("/submitReview/<user>/<name>/<outlet>/<role>", methods=['POST', 'GET'])
async def submitReview(user, name, outlet, role):
    if request.method == 'POST':
        rev_obj = Review(request.form.get('review'),user=user, name=name, date=date.today(), outlet = outlet)
        db.session.add(rev_obj)
        db.session.commit()
        return render_template('store-coordinator/Creview.html',login_name = name, login_category = role, outlet = outlet, user = user )

@app.route("/submitcallcenterReview/<user>/<name>/<outlet>/<role>", methods=['POST', 'GET'])
async def submitcallReview(user, name, outlet, role):
    if request.method == 'POST':
        rev_obj = Review(request.form.get('review'),user=user, name=name, date=date.today(), outlet = outlet)
        db.session.add(rev_obj)
        db.session.commit()
        return render_template('call-center/call-reviews.html',login_name = name, login_category = role, outlet = outlet, user = user )



@app.route("/meeting-content/<m_id>",methods=["GET"])
async def meetingContent(m_id):
    print(m_id)
    res = OnlineMeetings.query.filter_by(id=m_id).one()
    return render_template('store-coordinator/meeting-content.html',login_name = userData.name, login_category = userData.role, m_agenda = res.magenda, m_host = res.mhost, m_time = res.time, m_date = res.date, m_link = res.link, m_aud = res.audience)


@app.route("/call-center-meetings",methods=["GET"])
async def callCenterMeetings():
    meet_obj = OnlineMeetings.query.all()
    name = []
    mhost = []
    time = []
    date = []
    link = []

    for i in meet_obj:
        name.append(i.magenda)
        mhost.append(i.mhost)
        time.append(i.time)
        date.append(i.date)
        link.append(i.link)


    return render_template('call-center/call-meetings.html',login_name = userData.name, login_category = userData.role,m_agenda = name, m_host = mhost, m_time = time, m_date = date, m_link = link)


@app.route("/qaAudit",methods=["GET"])
async def qaAudit():
    return render_template('quality-assurance/qa-audit.html',login_name = userData.name, login_category = userData.role)

@app.route("/qaReview",methods=["GET"])
async def qaReview():
    return render_template('quality-assurance/qa-review.html',login_name = userData.name, login_category = userData.role)


@app.route("/call-dailyUpdates",methods=["GET","POST"])
async def callDailyUpdates():
    if request.method == 'POST':
        res = DailyUpdatesCallCenter(date.today(),session['user'], request.form.get('ncalls'),request.form.get('norders'),request.form.get('complaints'),request.form.get('oreviews'),request.form.get('participation'),request.form.get('responce'),request.form.get('reviewsuggestions'))
        db.session.add(res)
        db.session.commit()
        return render_template('call-center/call-dailyUpdates.html',login_name = userData.name, login_category = userData.role)

    return render_template('call-center/call-dailyUpdates.html',login_name = userData.name, login_category = userData.role)



########################### Store Manager Routes #################################


@app.route("/managerChecklist",methods=["GET"])
async def managerChecklist():
    result = ManagerChecklist.query.all()
    item = []

    for i in result:
        item.append(i.item)

    return render_template('store-manager/manager-checklist.html',login_name = userData.name, login_category = userData.role, mancheck=item)

    


@app.route("/managerTrainings",methods=["GET"])
async def managerTrainings():
    result = OnlineTrainings.query.all()
    name = []
    mhost = []
    time = []
    date = []
    link = []

    for i in result:
        name.append(i.magenda)
        mhost.append(i.mhost)
        time.append(i.time)
        date.append(i.date)
        link.append(i.link)
    return render_template('store-manager/manager-training.html',login_name = userData.name, login_category = userData.role, t_name = name, t_host = mhost, t_time = time, t_date = date, t_link = link)


@app.route("/manager-meetings",methods=["GET"])
async def managerMeetings():
    meet_obj = OnlineMeetings.query.all()
    name = []
    mhost = []
    time = []
    date = []
    link = []

    for i in meet_obj:
        name.append(i.magenda)
        mhost.append(i.mhost)
        time.append(i.time)
        date.append(i.date)
        link.append(i.link)


    return render_template('store-manager/manager-meetings.html',login_name = userData.name, login_category = userData.role,m_agenda = name, m_host = mhost, m_time = time, m_date = date, m_link = link)


@app.route("/managerPD", methods=['POST', 'GET'])
async def managerPD():
    return render_template('store-manager/manager-prodev.html',login_name = userData.name, login_category = userData.role, outlet= userData.outlet, user = session['user'])



@app.route("/managerReview", methods=['POST', 'GET'])
async def managerReview():
    return render_template('store-manager/manager-review.html',login_name = userData.name, login_category = userData.role, outlet= userData.outlet, user = session['user'] )




@app.route("/submitcallcenterReview/<user>/<name>/<outlet>/<role>", methods=['POST', 'GET'])
async def submitmanagerReview(user, name, outlet, role):
    if request.method == 'POST':
        rev_obj = Review(request.form.get('review'),user=user, name=name, date=date.today(), outlet = outlet)
        db.session.add(rev_obj)
        db.session.commit()
        return render_template('store-manager/manager-review.html',login_name = name, login_category = role, outlet = outlet, user = user )


@app.route("/submitmanagerPD/<user>/<name>/<outlet>/<role>", methods=['POST', 'GET'])
async def submitmanagerPD(user, name, outlet, role):
    if request.method == 'POST':
        pd_obj = ProdcutDevelopment(request.form.get('pd'),user=user, name=name, date=date.today(), outlet = outlet)
        db.session.add(pd_obj)
        db.session.commit()
        return render_template('store-manager/manager-prodev.html',login_name = name, login_category = role, outlet = outlet, user = user )


######################### end manager routes ######################################


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)