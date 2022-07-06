import time
import math
matematika = float(input("Unesi svoju ocenu iz matematike: "))
srpski = float(input("Unesi ocenu iz srpskog: "))
fizika = float(input("Unesi ocenu iz fizike: "))
fizicko = float(input("Unesi ocenu iz fizickog: "))
engleski = float(input("Unesi ocenu iz engleskog: "))
muzicko = float(input("Unesi ocenu iz muzickog: "))
drugi_jezik = float(input("Unesi ocenu iz ruskog/francuskog jezika: "))
istorija = float(input("Unesi ocenu iz istorije: "))
likovno = float(input("Unesi ocenu iz likovnog: "))
hemija = float(input("Unesi ocenu iz hemije: "))
geografija = float(input("Unesi ocenu iz geografije: "))
biologija = float(input("Unesi ocenu iz biologije: "))
tehnicko = float(input("Unesi ocenu iz tehnickog: "))
informatika = float(input("Unesi ocenu iz informatike: "))
broj_ocena = float("14.0")



print("Racunanje:[                    ] 0% ")
time.sleep(1)
print("Racunanje:[=====               ] 25%")
time.sleep(1)
print("Racunanje:[==========          ] 50%")
time.sleep(1)
print("Racunanje:[===============     ] 75%")
time.sleep(1)
print("Racunanje:[====================] 100%")
time.sleep(2)


prosek = (matematika + srpski + fizika + fizicko + engleski + drugi_jezik + istorija + hemija + geografija + biologija + tehnicko + informatika + likovno + muzicko) / broj_ocena


print("Zakljucna ocena je: "  + str(prosek))
print("Zakljuceno ti je: ", round(prosek))