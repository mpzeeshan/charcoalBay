#from crypt import methods
from flask import Flask
from flask import render_template
from flask import request
import os
import asyncio


app = Flask(__name__)


menu = []

sop_counterStaff = ['Customer Walks in',
                    'Hi Sir, Greeting with hands up',
                    'Menu Introduction As per Co; Priority Strater main dish & Fizzy Explain the taste of food',
                    'Take the Order',
                    'Reconfirm the Order',
                    'Issue the bill',
                    'Sanitize the token',
                    'Handover the buzzer and token to the customer',
                    'Collect cash/Card',
                    'Pay back the change',
                    'Handover the bill to work table',
                    'Pick up the tikka from display & handover to work table',
                    'Collect the order from work table in 10 minutes',
                    'Re-confirm the order delivered from work table',
                    'Re-confirm the sides (Mayonnaise, Chutney, Onion, Tikkasalad etc, are enclosed)',
                    'Confirm drinks are included if any',
                    'Press the token Buzzer',
                    'Handover the food tray/parcel to the customer',
                    'Take back the buzzer from customer and sanitize',
                    'Greet the customer with thank you'
                    ]


sop_kitchen = ['Order placed on KDS',
               'Pick the KOT and keep it on the KOT holder',
               'Pick the Tikka from the counter staff if any',
               'Pick the grill chicken from work table if any',
               'check the KDS for new order',
               'Keep it in the Combi oven',
               'Take the Tikka/Grill chicken from the combi oven and keep it on Charcoal',
               'Check the KDS for new order',
               'Turn the grill on charcoal',
               'Check the KDS for more orders',
               'Check the Tikka/Grill on charcoal to see if cooked well',
               'Check the KDS for more orders',
               'Keep the Kubboos/Rice ready for packing',
               'Keep the sides(Mayo, chatni, salad etc) in the tray or pack',
               'Take the Tikka/Grill from charcoal nd pack it',
               'Reconfirm if the food in the pack or on the tray',
               'Paste the KOT on the tray or parel cover',
               'Cancel the ticket from KDS screen',
               'Hand over teh cover/tray to billing staff',
               'Check and inform the non-available item to the counter staff',
               'Check if the all masala marinated grill/tikka is ready and available for cooking for the next order',
               'Wait for the next order on KDS',
              ]

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

cleaning_staff_checklist = ['Glass Cleaning 58*2*1 minutes',
                            'Tables Inside',
                            'Chairs Inside',
                            'Wash Basin Mirror',
                            'Wash Basin Wall',
                            'Inside Floor Moping 1.00pm',
                            'Inside Floor Moping 6.00pm',
                            'Inside Floor Moping 10.00pm',
                            'Tissue Refill',
                            'Hand wash Refill',
                            'Tables Outside Cleaning and Setting',
                            'Chair Outside Cleaning and Setting',
                            'Plant Watering',
                            'Outside Floor Cleaning',
                            'Sign Board Grill Cleaning',
                            'Ceiling Grill Cleaning',
                            'Toilet Full Cleaning',
                            'Waste disposal to Insonator',
                            'Oil Filtering from Treatment Plant 1 & 2',
                            'Paper on Floor Cleaning @ 12.00 pm & 6.00 pm',
                            'Sewage Plant Chemical Mixing @ 12.00 pm',
                           ]

counter_staff_checklist = ['Cash counter top & counter area',
                           'Display freezer 2 nos top and sides',
                           'Behind the counter walls cleaning',
                          ]

kitchen_staff_checklist = ['Kitchen Back area Floor Washing @ 06.00 pm & 11.00 pm',
                           'Back Kitchen floor Cleaning @ 06.00 pm & 11.00 pm',
                           'Main kitchen Floor cleaning @ 06.00 pm & 11.00 pm',
                           'Kitchen tables cleaning @ 06.00 pm & 11.00 pm',
                           'Combi oven cleaning @ 11.00 pm',
                           'Combi oven washer cleaning 04.00, 06.00, 08.00 & 10.00',
                           'Sauce Dispencer Cleaning',
                           'Sauce Dispencer Filling @ 12.00 pm',
                           'Switch Off All Lights at Closing time',
                           'Check freezer switched On',
                           'Waste disposal before closing @ 11.30 pm',
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

uname = ""


@app.route("/", methods=['POST', 'GET'])
async def index():
    if request.method == 'POST':
        global uname
        uname = request.form.get('uname')
        if uname == "Carmela" or uname == "CARMELA" or uname == "carmela":
            return render_template('home.html',login_name = "Carmela", login_category ="Cleaning Staff",menu = clstaff_menu_items, menu_links = cl_menu_links)
        elif uname == "Divya" or uname == "divya" or uname == "DIVYA":
            return render_template('home.html',login_name = "Divya", login_category ="Counter Staff",menu = counterStaff_menu_items, menu_links = counterStaff_menu_links)
        elif uname == "Abdul" or uname == "abdul" or uname == "ABDUL":
            return render_template('home.html',login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)

        else:
            return render_template('login.html',message = "Invalid Username")
    else:
        uname = ""
        return render_template('login.html')



@app.route("/checklist", methods=['GET'])
async def checklist():
    if uname == "Carmela" or uname == "CARMELA" or uname == "carmela":
        return render_template('checklist.html', checklist =cleaning_staff_checklist, login_name = "Carmela", login_category ="Cleaning Staff",menu = clstaff_menu_items, menu_links = cl_menu_links)
    elif uname == "Divya" or uname == "divya" or uname == "DIVYA":
        return render_template('checklist.html', checklist = counter_staff_checklist, login_name = "Divya", login_category ="Counter Staff",menu = counterStaff_menu_items, menu_links = counterStaff_menu_links)
    elif uname == "Abdul" or uname == "abdul" or uname == "ABDUL":
        return render_template('checklist.html', checklist = kitchen_staff_checklist, login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)







@app.route("/meetings", methods=['GET'])
async def meetings():
    if uname == "Carmela" or uname == "CARMELA" or uname == "carmela":
        return render_template('meetings.html',login_name = "Carmela", login_category ="Cleaning Staff",menu = clstaff_menu_items, menu_links = cl_menu_links)
    elif uname == "Divya" or uname == "divya" or uname == "DIVYA":
        return render_template('meetings.html',login_name = "Divya", login_category ="Counter Staff",menu = counterStaff_menu_items, menu_links = counterStaff_menu_links)
    elif uname == "Abdul" or uname == "abdul" or uname == "ABDUL":
        return render_template('meetings.html',login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)
    
   



@app.route("/trainings", methods=['GET'])
async def trainings():
    if uname == "Carmela" or uname == "CARMELA" or uname == "carmela":
        return render_template('trainings.html',login_name = "Carmela", login_category ="Cleaning Staff",menu = clstaff_menu_items, menu_links = cl_menu_links)
    elif uname == "Divya" or uname == "divya" or uname == "DIVYA":
        return render_template('trainings.html',login_name = "Divya", login_category ="Counter Staff",menu = counterStaff_menu_items, menu_links = counterStaff_menu_links)
    elif uname == "Abdul" or uname == "abdul" or uname == "ABDUL":
        return render_template('trainings.html',login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)





@app.route("/sop",methods=['GET'])
async def sop():
    if uname == "Carmela" or uname == "CARMELA" or uname == "carmela":
        return render_template('sop.html',sop_list = [],login_name = "Carmela", login_category ="Cleaning Staff",menu = clstaff_menu_items, menu_links = cl_menu_links)
    elif uname == "Divya" or uname == "divya" or uname == "DIVYA":
        return render_template('sop.html',sop_list = sop_counterStaff, login_name = "Divya", login_category ="Counter Staff",menu = counterStaff_menu_items, menu_links = counterStaff_menu_links)
    elif uname == "Abdul" or uname == "abdul" or uname == "ABDUL":
        return render_template('sop.html',sop_list = sop_kitchen,login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)

    



@app.route("/onlinemeetings", methods=['GET'])
async def omeetings():
    if uname == "Carmela" or uname == "CARMELA" or uname == "carmela":
        return render_template('omeeting.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date, login_name = "Carmela", login_category ="Cleaning Staff",menu = clstaff_menu_items, menu_links = cl_menu_links)
    elif uname == "Divya" or uname == "divya" or uname == "DIVYA":
        return render_template('omeeting.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date,  login_name = "Divya", login_category ="Counter Staff",menu = counterStaff_menu_items, menu_links = counterStaff_menu_links)
    elif uname == "Abdul" or uname == "abdul" or uname == "ABDUL":
        return render_template('omeeting.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date,login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)



@app.route("/offlinemeetings", methods=['GET'])
async def fmeetings():
    if uname == "Carmela" or uname == "CARMELA" or uname == "carmela":
        return render_template('fmeeting.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date, login_name = "Carmela", login_category ="Cleaning Staff",menu = clstaff_menu_items, menu_links = cl_menu_links)
    elif uname == "Divya" or uname == "divya" or uname == "DIVYA":
        return render_template('fmeeting.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date,  login_name = "Divya", login_category ="Counter Staff",menu = counterStaff_menu_items, menu_links = counterStaff_menu_links)
    elif uname == "Abdul" or uname == "abdul" or uname == "ABDUL":
        return render_template('fmeeting.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date,login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)

    # return render_template('fmeeting.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date)

@app.route("/onlinetrainings", methods=['GET'])
async def otrainings():
    if uname == "Carmela" or uname == "CARMELA" or uname == "carmela":
        return render_template('otraining.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date, login_name = "Carmela", login_category ="Cleaning Staff",menu = clstaff_menu_items, menu_links = cl_menu_links)
    elif uname == "Divya" or uname == "divya" or uname == "DIVYA":
        return render_template('otraining.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date,  login_name = "Divya", login_category ="Counter Staff",menu = counterStaff_menu_items, menu_links = counterStaff_menu_links)
    elif uname == "Abdul" or uname == "abdul" or uname == "ABDUL":
        return render_template('otraining.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date,login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)

    
    #return render_template('otraining.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date)

@app.route("/offlinetrainings", methods=['GET'])
async def ftrainings():
    if uname == "Carmela" or uname == "CARMELA" or uname == "carmela":
        return render_template('ftraining.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date, login_name = "Carmela", login_category ="Cleaning Staff",menu = clstaff_menu_items, menu_links = cl_menu_links)
    elif uname == "Divya" or uname == "divya" or uname == "DIVYA":
        return render_template('ftraining.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date,  login_name = "Divya", login_category ="Counter Staff",menu = counterStaff_menu_items, menu_links = counterStaff_menu_links)
    elif uname == "Abdul" or uname == "abdul" or uname == "ABDUL":
        return render_template('ftraining.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date,login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)

    
    #return render_template('ftraining.html',m_agenda= meet_agenda, m_host = meet_host, m_time = meet_time, m_date = meet_date)

@app.route("/review",methods=['GET'])
async def review():
    if uname == "Carmela" or uname == "CARMELA" or uname == "carmela":
        return render_template('review.html',login_name = "Carmela", login_category ="Cleaning Staff",menu = clstaff_menu_items, menu_links = cl_menu_links)
    elif uname == "Divya" or uname == "divya" or uname == "DIVYA":
        return render_template('review.html',login_name = "Divya", login_category ="Counter Staff",menu = counterStaff_menu_items, menu_links = counterStaff_menu_links)
    elif uname == "Abdul" or uname == "abdul" or uname == "ABDUL":
        return render_template('review.html',login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)

    #return render_template('review.html')


@app.route("/productDevelopment", methods=["GET"])
async def productDev():
    if uname == "Divya" or uname == "divya" or uname == "DIVYA":
        return render_template('productDevelopment.html',login_name = "Divya", login_category ="Counter Staff",menu = counterStaff_menu_items, menu_links = counterStaff_menu_links)
    elif uname == "Abdul" or uname == "abdul" or uname == "ABDUL":
        return render_template('productDevelopment.html',login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)


@app.route("/stocklist",methods=["GET"])
async def stocklist():
    if uname == "Carmela" or uname == "CARMELA" or uname == "carmela":
        return render_template('stocklist.html',login_name = "Carmela", login_category ="Cleaning Staff",menu = clstaff_menu_items, menu_links = cl_menu_links)
    elif uname == "Divya" or uname == "divya" or uname == "DIVYA":
        return render_template('stocklist.html',login_name = "Divya", login_category ="Counter Staff",menu = counterStaff_menu_items, menu_links = counterStaff_menu_links)
    elif uname == "Abdul" or uname == "abdul" or uname == "ABDUL":
        return render_template('stocklist.html',login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)

@app.route("/charcoalUsage", methods=["GET"])
async def charcoal():
    return render_template('charcoalUsage.html',login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)

@app.route("/preparationList",methods=["GET"])
async def plist():
    return render_template('plist.html',login_name = "Abdul", login_category ="Production Staff",menu = pstaff_menu_items, menu_links = pstaff_menu_links)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)