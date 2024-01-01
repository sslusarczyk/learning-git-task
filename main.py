lista_zakupow = {
 "Piekarnia": ['Chleb','Paczek','Bulki'],
 "Warzywniak": ['Marchew','Seler','Rukola']
}

count0 = 0
count1 = 0
for sklep, produkt in lista_zakupow.items():
    uppercase_tekst1 = "Ide do"
    uppercase_tekst2 = "i kupuje tam"

    print (uppercase_tekst1.upper(), sklep.upper(), uppercase_tekst2.upper(), ', '.join([produkt.upper() for produkt in produkt]))


count0 = len (lista_zakupow['Piekarnia'])
count1 = len(lista_zakupow['Warzywniak'])

print (f"W sumie kupuje {count0+count1} produktow")
print ("Zmiana 1 Github")
print ("Zmiana 1 Github - zmiana 2")
print ("Specialne pozdrowienia")