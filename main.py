import json

jsonbook = '{"tytul":"Hobbit","autor":"J.R.R. Tolkien","oprawa":"twarda","lstron":245,"cena":23.77}'
print(jsonbook)
print(type(jsonbook))

book = json.loads(jsonbook)
print(book)
print(type(book))

print(book['autor'])

kolor = {
    "id":23423,
    "nazwa_koloru":"zółty ciemny",
    "paleta":"UC567",
    "lodcieni":3,
    "odcienie":["jasny","standard","ciemny"]
}

jsonkolor = json.dumps(kolor,indent=4)
print(jsonkolor)

with open("kolor.json","w",encoding="utf-8") as f:
    f.write(jsonkolor)

with open("kolor.json","r",encoding="utf-8") as f:
    kolor_dict = json.load(f)

print(kolor_dict)
print(kolor_dict['odcienie'][0])

print("____________________________________________")