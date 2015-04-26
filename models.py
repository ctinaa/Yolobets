from flask.ext.sqlalchemy import SQLAlchemy 

db = SQLAlchemy() 

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	userid = db.Column(db.Integer, db.ForeignKey('user.id'))
	firstname = db.Column(db.String(30))
	lastname = db.Column(db.String(30))
	username = db.Column(db.String(30), unique=True)
	email = db.Column(db.String(30), unique=True)
	password = db.Column(db.String(30), unique = True)
	pointvalue = db.Column(db.Integer)
	level = db.Column(db.Integer)
	image = db.Column(db.String(100))
	badge = db.Badge(db.Strint(100))

	def __init__(self, firstname, lastname, username, email, 
		password, pointvalue, level, image, badge):
		self.firstname = firstname
		self.lastname = lastname
		self.username = username
		self.email = email
		self.password = password 
		self.pointvalue = pointvalue 
		self.level = level
		self.image = image 
		self.badge = badge 


class  Goal(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	userid = db.Column(db.Integer, db.ForeignKey('user.id'))
	goal_one = db.Column(db.TEXT)
	goal_two = db.Column(db.TEXT)
	goal_three = db.Column(db.TEXT)
	duedate = db.Column(DATETIME)
	
	def __init__(self, userid, goal_one, goal_two, goal_three, duedate):
		self.userid = user_id
		self.goal_one =  goal_one
		self.goal_two = goal_two
		self.goal_three = goal_three 
		self.duedate = duedate

class  Challenge(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	challengerid = db.Column(db.Integer, db.ForeignKey('user.id'))
	opponentid = db.Column(db.Integer, db.ForeignKey('user.id'))
	isCompleted = db.Column(db.tinyint(1))
	
	def __init__(self, challengerid, opponentid, isCompleted):
		self.challengerid = challengerid 
		self.opponentid = opponentid
		self.isCompleted = isCompleted
