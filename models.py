from flask.ext.sqlalchemy import SQLAlchemy 

db = SQLAlchemy() 

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	userId = db.Column(db.Integer, db.ForeignKey('user.id'))
	firstName = db.Column(db.String(30))
	lastName = db.Column(db.String(30))
	userName = db.Column(db.String(30), unique=True)
	email = db.Column(db.String(30), unique=True)
	password = db.Column(db.String(30), unique = True)
	pointValue = db.Column(db.Integer)
	totalPoints = db.Column(db.Integer)
	quote = db.Column(db.String(30))
	level = db.Column(db.Integer)
	image = db.Column(db.String(100))
	badge = db.Column(db.String(100))

	def __init__(self, firstName, lastName, username, email, 
		password, pointValue, totalPoints, quote, level, image, badge):
		self.firstName = firstname
		self.lastName = lastname
		self.username = username
		self.email = email
		self.password = password 
		self.pointValue = pointvalue 
		self.level = level
		self.totalPoints = totalPoints
		self.quote = quote
		self.image = image 
		self.badge = badge 


class  Goal(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	userId = db.Column(db.Integer, db.ForeignKey('user.id'))
	goalOne = db.Column(db.TEXT)
	goalTwo = db.Column(db.TEXT)
	goalThree = db.Column(db.TEXT)
	duedate = db.Column(db.DateTime)
	timeStamp = db.Column(db.DateTime)
	def __init__(self, userId, goalOne, goalTwo, goalThree, dueDate):
		self.userId = userId
		self.goalOne =  goalOne
		self.goalTwo = goalTwo
		self.goalThree = goalThree 
		self.dueDate = dueDate

class  Challenge(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	challengerId = db.Column(db.Integer, db.ForeignKey('user.id'))
	opponentId = db.Column(db.Integer, db.ForeignKey('user.id'))
	isCompleted = db.Column(db.Boolean(1))
	
	def __init__(self, challengerid, opponentid, isCompleted):
		self.challengerid = challengerid 
		self.opponentid = opponentid
		self.isCompleted = isCompleted
