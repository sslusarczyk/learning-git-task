lista_zakupow = {
 "Piekarnia": ['Chleb'],
 "Warzywniak": ['Marchew']
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
