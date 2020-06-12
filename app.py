import notes as note
from gtts import gTTS
import pyttsx3
import speech_recognition
robotMouth = pyttsx3.init()
def inputVoice():
	robotEar = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		print('Apple: Listening')
		robotEar.adjust_for_ambient_noise(mic)
		audio = robotEar.listen(mic)
	try:
		you = robotEar.recognize_google(audio, language='vi-VN')
	except:
		you = 'cant listen'
	return you
def menu():
	print('\tNote App')
	print('1, Liệt kê công việc')
	print('2, Thêm công việc')
	print('3, Xóa công việc')
	print('4, Xem công việc')
def main():
	while True:
		you = inputVoice().lower()
		print(you)
		if you == 'xin chào':
			menu()
			choose  = inputVoice()
			print(choose)
			if choose == 'thêm':
				print('Tên công việc: ')
				title = inputVoice()
				if title == "dừng" or title == 'cant listen':
					break
				print('Ghi chú: ')
				body = inputVoice()
				if body == "dừng" or body == 'cant listen':
					break
				note.addNote(title, body)
			elif choose == 'liệt kê công việc':
				note.listNotes()
			elif choose == 'xóa công việc':
				print('Tên công việc: ')
				title = inputVoice()
				if title == "dừng" or title == 'cant listen':
					break
				note.removeNote(title)
			elif choose == 'xem công việc':
				title = inputVoice()
				if title == "dừng" or title == 'cant listen':
					break
				note.detailNote(title)
			elif choose ==	'tạm biệt':
				break;
		print('Done')
	else:
		print(1)
main()
# 