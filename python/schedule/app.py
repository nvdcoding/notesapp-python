import notes as note
from gtts import gTTS
import speech_recognition
import playsound
def outputVoice(str):
	tts = gTTS(text = str, lang = 'vi')
	tts.save("voice.wav")
	playsound.playsound('voice.wav', True)

def inputVoice():
	robotEar = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		print('Apple: Listening')
		robotEar.adjust_for_ambient_noise(mic)
		audio = robotEar.listen(mic, timeout = 3, phrase_time_limit = 3)
	try:
		you = robotEar.recognize_google(audio, language='vi-VN')
	except:
		outputVoice('Tôi không hiểu')
		you = 'cant listen'
	return you
def menu():
	outputVoice('Tôi có thể giúp gì cho bạn, hãy yêu cầu tôi: ')
	print('\tNote App')
	print('1, Liệt kê công việc')
	print('2, Thêm công việc')
	print('3, Xóa công việc')
	print('4, Xem công việc')
def main():
	while True:
		you = inputVoice().lower()
		print(you)
		if you == 'bắt đầu':
			menu()
			choose  = inputVoice()
			outputVoice("Bạn chọn: " + choose)
			if choose == 'thêm công việc':
				print('Tên công việc')
				outputVoice('Tên công việc: ')
				title = inputVoice()
				if title == "dừng" or title == 'cant listen':
					break
				print('Ghi chú')
				outputVoice('Ghi chú: ')
				body = inputVoice()
				if body == "dừng" or body == 'cant listen':
					break
				note.addNote(title, body)
				outputVoice('Thêm xong')
			elif choose == 'liệt kê công việc':
				note.listNotes()
			elif choose == 'xóa công việc':
				print('Tên công việc')
				outputVoice('Tên công việc: ')
				title = inputVoice()
				if title == "dừng" or title == 'cant listen':
					break
				note.removeNote(title)
				outputVoice('Xóa xong')
			elif choose == 'xem công việc':
				title = inputVoice()
				if title == "dừng" or title == 'cant listen':
					break
				note.detailNote(title)
			elif choose ==	'tạm biệt':
				return
			print('Done')
		else:
			outputVoice("Chúc bạn vui vẻ")
main()
# 