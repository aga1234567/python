podaj_ilosc_pkt = int((input("Podaj ilość pkt")))
if podaj_ilosc_pkt<200*50/100:
    print("ocena 2")
elif podaj_ilosc_pkt>=200*50/100 and podaj_ilosc_pkt< 200*60/100:
    print("Ocena 3")
elif podaj_ilosc_pkt>=200*60/100 and podaj_ilosc_pkt< 200*70/100:
    print("Ocena 3.5")
elif podaj_ilosc_pkt>=200*70/100 and podaj_ilosc_pkt< 200*80/100:
    print("Ocena 4")
elif podaj_ilosc_pkt>=200*80/100 and podaj_ilosc_pkt<= 200*90/100:
    print("Ocena 4.5")
elif podaj_ilosc_pkt>=200*90/100:
    print("Ocena 5")