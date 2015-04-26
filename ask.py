from flask import render_template, request, Blueprint, session, redirect, url_for 
from models import Goal, db 
from utilities import login_required

import datetime 

ask = Blueprint('ask', __name__, template_folder='templates') 

@ask.route('/addgoal', methods=['POST')  
#@login_required
def add_goals(): 
	if request.method == 'POST': 
		new_goal = Goal(session['userid'],
			request.form['goal_one'],
			request.form['goal_two'],
			request.form['goal_three'],
			request.form['duedate']
			#request.form[''],
			#request.form['email'],  
			datetime.datetime.now(), 
			datetime.datetime.now())

		db.session.add(new_goal)
		db.session.commit() 

	return 
		#user_id = get_goal_id(new_goal, db)

		#return redirect(url_for('questions.show_question', question_id=question_id))

	#elif request.method == 'GET': 
	#	return render_template('ask.html')


# Helper Functions 

def get_question_id(record, db): 
	db.session.refresh(record)
	return record.ID