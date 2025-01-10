import evalang

while True:
	text = input('EvaLang > ')
	result, error = basic.run('<stdin>', text)

	if error: print(error.as_string())
	else: print(result)