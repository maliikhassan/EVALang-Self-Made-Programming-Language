import evalang

while True:
	text = input('EvaLang > ')
	result, error = evalang.run('<stdin>', text)

	if error: print(error.as_string())
	else: print(result)