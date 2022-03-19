k = (input("Podaj PESEL"))
# Sprawdzenie sumy kontrolnej...
if(len(k)!=11):
    print("PESEL nieprawidłowy")
else:
  l = int(k[10])
  suma = ((1 * int(k[0])) + (3 * int(k[1])) + (7 * int(k[2])) + (9 * int(k[3])) + ((1 * int(k[4]))) + (3 * int(k[5])) + (
            7 * int(k[6])) + (9 * int(k[7])) + (1 * int(k[8])) + (3 * int(k[9])))
  kontrolka = 10 - (suma % 10)
  print("Cyfra kontrolna",kontrolka)
  print("l",l)
  if kontrolka == 10:
    kontrolka = 0
  else:
    kontrolka = kontrolka

  # kontrolka i sprawdzenie zgodnosci
  if ((l== kontrolka)):
    print("l",l)
    print("Suma kontrolna poprawna")
    plec = int(k[10]) % 2
    rok = int(k[0:2])
    miesiac = (k[2:4])
    dzien = (k[4:6])
    lat = 100 - rok + 22
    # print("Ilość znaków sie zgadza")
    if ((plec == 0)):
        print("Pesel kobiety", "miesiac:", miesiac, "dzien:", dzien, "rok", rok, "lat:", lat)
    else:
        print("PESEL męższczyzny""miesiac:", miesiac, "dzien:", dzien, "rok", rok, "lat:", lat)
  else:
    print("Suma kontrolna niepoprawna")

