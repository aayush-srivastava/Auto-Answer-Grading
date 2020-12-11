from flask import Flask, request, render_template
import re
import math

app = Flask("__name__")

q = ""

@app.route("/")
def loadPage():
	return render_template('index.html', question1="", question2="", question3="", question4="")

@app.route("/", methods=['POST'])
def cosineSimilarity():
	
	universal1 = []
	universal2 = []
	universal3 = []
	universal4 = []
	matchPercentage = 0

#############################QUESTION 1###############################################
	inputQ1 = request.form['question1']
	lowerQ1 = inputQ1.lower()

	wordList1 = re.sub("[^\w]", " ",lowerQ1).split()			#Replace punctuation by space and split
	# wordList1 = map(str, wordList1)					#This was causing divide by zero error

	for word in wordList1:
		if word not in universal1:
			universal1.append(word)
	######
	fd = open("question1.txt", "r")
	database1 = fd.read().lower()

	dbWord1 = re.sub("[^\w]", " ",database1).split()	#Replace punctuation by space and split
	# dbWord1 = map(str, dbWord1)			#And this also leads to divide by zero error

	for word in dbWord1:
		if word not in universal1:
			universal1.append(word)
	######
	q1TF = []
	db1TF = []

	for word in universal1:
		q1TFCounter = 0
		db1TFCounter = 0

		for word2 in wordList1:
			if word == word2:
				q1TFCounter += 1
		q1TF.append(q1TFCounter)

		for word2 in dbWord1:
			if word == word2:
				db1TFCounter += 1
		db1TF.append(db1TFCounter)

	dotProduct1 = 0
	for i in range (len(q1TF)):
		dotProduct1 += q1TF[i]*db1TF[i]

	question1Value = 0
	for i in range (len(q1TF)):
		question1Value += q1TF[i]**2
	question1Value = math.sqrt(question1Value)

	db1Value = 0
	for i in range (len(db1TF)):
		db1Value += db1TF[i]**2
	db1Value = math.sqrt(db1Value)

	if inputQ1 == "":
		matchPercentage1 = 0
	else:
		matchPercentage1 = (float)(dotProduct1/(question1Value * db1Value))*100

##############################QUESTION 2################################################

	inputQ2 = request.form['question2']
	lowerQ2 = inputQ2.lower()

	wordList2 = re.sub("[^\w]", " ",lowerQ2).split()			#Replace punctuation by space and split
	# wordList1 = map(str, wordList1)					#This was causing divide by zero error

	for word in wordList2:
		if word not in universal2:
			universal2.append(word)
	######
	fd = open("question2.txt", "r")
	database2 = fd.read().lower()

	dbWord2 = re.sub("[^\w]", " ",database2).split()	#Replace punctuation by space and split
	# dbWord1 = map(str, dbWord1)			#And this also leads to divide by zero error

	for word in dbWord2:
		if word not in universal2:
			universal2.append(word)
	######
	q2TF = []
	db2TF = []

	for word in universal2:
		q2TFCounter = 0
		db2TFCounter = 0

		for word2 in wordList2:
			if word == word2:
				q2TFCounter += 1
		q2TF.append(q2TFCounter)

		for word2 in dbWord2:
			if word == word2:
				db2TFCounter += 1
		db2TF.append(db2TFCounter)

	dotProduct2 = 0
	for i in range (len(q2TF)):
		dotProduct2 += q2TF[i]*db2TF[i]

	question2Value = 0
	for i in range (len(q2TF)):
		question2Value += q2TF[i]**2
	question2Value = math.sqrt(question2Value)

	db2Value = 0
	for i in range (len(db2TF)):
		db2Value += db2TF[i]**2
	db2Value = math.sqrt(db2Value)

	if inputQ2 == "":
		matchPercentage2 = 0
	else:
		matchPercentage2 = (float)(dotProduct2/(question2Value * db2Value))*100

############################QUESTION 3##################################################
	
	inputQ3 = request.form['question3']
	lowerQ3 = inputQ3.lower()

	wordList3 = re.sub("[^\w]", " ",lowerQ3).split()			#Replace punctuation by space and split
	# wordList1 = map(str, wordList1)					#This was causing divide by zero error

	for word in wordList3:
		if word not in universal3:
			universal3.append(word)
	#######
	fd = open("question3.txt", "r")
	database3 = fd.read().lower()

	dbWord3 = re.sub("[^\w]", " ",database3).split()	#Replace punctuation by space and split
	# dbWord1 = map(str, dbWord1)			#And this also leads to divide by zero error

	for word in dbWord3:
		if word not in universal3:
			universal3.append(word)
	######
	q3TF = []
	db3TF = []

	for word in universal3:
		q3TFCounter = 0
		db3TFCounter = 0

		for word2 in wordList3:
			if word == word2:
				q3TFCounter += 1
		q3TF.append(q3TFCounter)

		for word2 in dbWord3:
			if word == word2:
				db3TFCounter += 1
		db3TF.append(db3TFCounter)

	dotProduct3 = 0
	for i in range (len(q3TF)):
		dotProduct3 += q3TF[i]*db3TF[i]

	question3Value = 0
	for i in range (len(q3TF)):
		question3Value += q3TF[i]**2
	question3Value = math.sqrt(question3Value)

	db3Value = 0
	for i in range (len(db3TF)):
		db3Value += db3TF[i]**2
	db3Value = math.sqrt(db3Value)

	if inputQ3 == "":
		matchPercentage3 = 0
	else:
		matchPercentage3 = (float)(dotProduct3/(question3Value * db3Value))*100

#############################QUESTION 4#################################################

	inputQ4 = request.form['question4']
	lowerQ4 = inputQ4.lower()

	wordList4 = re.sub("[^\w]", " ",lowerQ4).split()			#Replace punctuation by space and split
	# wordList1 = map(str, wordList1)					#This was causing divide by zero error

	for word in wordList4:
		if word not in universal4:
			universal4.append(word)
	######
	fd = open("question4.txt", "r")
	database4 = fd.read().lower()

	dbWord4 = re.sub("[^\w]", " ",database4).split()	#Replace punctuation by space and split
	# dbWord1 = map(str, dbWord1)			#And this also leads to divide by zero error

	for word in dbWord4:
		if word not in universal4:
			universal4.append(word)
	####
	q4TF = []
	db4TF = []

	for word in universal4:
		q4TFCounter = 0
		db4TFCounter = 0

		for word2 in wordList4:
			if word == word2:
				q4TFCounter += 1
		q4TF.append(q4TFCounter)

		for word2 in dbWord4:
			if word == word2:
				db4TFCounter += 1
		db4TF.append(db4TFCounter)

	dotProduct4 = 0
	for i in range (len(q4TF)):
		dotProduct4 += q4TF[i]*db4TF[i]

	question4Value = 0
	for i in range (len(q4TF)):
		question4Value += q4TF[i]**2
	question4Value = math.sqrt(question4Value)

	db4Value = 0
	for i in range (len(db4TF)):
		db4Value += db4TF[i]**2
	db4Value = math.sqrt(db4Value)

	if inputQ4 == "":
		matchPercentage4 = 0
	else:
		matchPercentage4 = (float)(dotProduct4/(question4Value * db4Value))*100

###############################################################################
	totalMatch = (float)(((matchPercentage1 + matchPercentage2 + matchPercentage3 + matchPercentage4)/4)*20)/100

	output = "%0.02f out of 20."%totalMatch

	return render_template('index.html', question1=inputQ1, question2=inputQ2, question3=inputQ3, question4=inputQ4, output=output)

app.run()
