import json
# some function
def addNote(title, body):
	data = loadNotes()
	duplicateNotes = [note for note in data if note['title'] == title]
	if len(duplicateNotes) == 0:
		f = open('text.json', 'a')
		data.append({'title':title, 'body': body})
		saveNotes(data);
		f.close()
		print('added note')
	else: 
		print('title has used')
def removeNote(title):
	notes = loadNotes()
	notesToKeep = [note for note in notes if note['title'] != title]
	if len(notesToKeep) == len(notes):
		print('No note removed')
	else:
		saveNotes(notesToKeep)
		print('removed')
def detailNote(title):
	notes = loadNotes();
	noteFound = [note for note in notes if note['title'] == title]
	if len(noteFound) > 0:
		result = noteFound[0]
		print(result['title'] + ": " + result['body'])
	else:
		print('not found')
def loadNotes():
	try:
		f = open('text.json', 'r')
		dataJSON = f.read()
		f.close()
		return json.loads(dataJSON)
	except:
		return []
def saveNotes(notes):
	dataJSON = json.dumps(notes)
	f = open('text.json', 'w')
	f.write(dataJSON)
	f.close()
def listNotes():
	f = open('text.json', 'r')
	notes = json.loads(f.read())
	i = 1
	for note in notes:
		print(str(i) + ", " + note['title'])
		i+=1
# save notes.py