import wikipedia

def soz_manosi(soz):
    wikipedia.set_lang("uz")

    try:
        result = wikipedia.summary(soz)
    except:
        result = "Topilmadi!"
    return result
print(soz_manosi(soz = "Alisher Navoiy"))