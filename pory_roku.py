lista=("grudzien","styczeń","luty","marzec","kwiecien","maj","czerwiec","lipiec","sierpien","wrzesien","pazdziernik","listopad")
for i in range(0,len(lista),3):
    if(i==0):
        print("zima")
    elif (i==3):
       print("wiosna")
    elif(i==6):
        print("lato")
    elif(i==9):
        print("jesien")
    print(lista[i:i+3])