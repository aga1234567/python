podajrok = int((input("Podaj rok, sprawdze czy przestepny")))
if (podajrok % 4 == 0 and podajrok % 100 != 0) or (podajrok % 400 == 0):
    print("rok przestepny")
else:
    print("nieprzestepny")
