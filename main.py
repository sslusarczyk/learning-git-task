lista_zakupow = {
 "Piekarnia": ['Chleb','Paczek','Bulki'],
 "Warzywniak": ['Marchew','Seler','Rukola']
}

count0 = 0
count1 = 0
for key, value in lista_zakupow.items():
    uppercase_tekst1 = "Ide do"
    uppercase_tekst2 = "i kupuje tam"
    uppercase_value = value
    print (uppercase_tekst1.upper(), key.upper(), uppercase_tekst2.upper(), uppercase_value)

count0 = len (lista_zakupow['Piekarnia'])
count1 = len(lista_zakupow['Warzywniak'])

print (f"W sumie kupuje {count0+count1} produktow")
print ("Zmiana 1 Github")
print ("Zmiana 1 Github - zmiana 2")
print ("Specialne pozdrowienia")