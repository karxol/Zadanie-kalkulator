import logging
logging.basicConfig(level=logging.DEBUG)

print("kalkulaotr !")
print("Wybierz opcje : ")
print(" ")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie \n")

choice = input("Wybieram: ")

pierwsza_liczba = float(input("Podaj pierwszą liczbe: "))
druga_liczba = float(input("Podaj drugą liczbe: "))

if choice == '1':
  wynik = pierwsza_liczba + druga_liczba 
  logging.info("Wynik działania to : ",wynik)
elif choice == '2':
  wynik = pierwsza_liczba - druga_liczba 
  logging.info("Wynik działania to : ",wynik)
elif choice == '3':
  wynik = pierwsza_liczba * druga_liczba 
  logging.info("Wynik działania to : ",wynik)
elif choice == '4':
  wynik = pierwsza_liczba / druga_liczba 
  logging.info("Wynik działania to : ",wynik)

  

