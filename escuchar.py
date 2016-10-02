import speech_recognition as spr
rg=spr.Recognizer()
with spr.Microphone() as source:
	rg.adjust_for_ambient_noise(source)
	print 'Escuchando'
	audio=rg.listen(source)
	try:
		print rg.recognize_sphinx(audio)
	except spr.UnknownValueError:
		print 'error'

