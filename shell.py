import evalang

while True:
    start = input('EvaLang > ')
    result,error = evalang.Run('<stdin>',start)

    if error: print(error.as_string())
    else: print(result)