def IsMyndig(age):
    if age >= 18:
        return True
    return False

age = int(input("Ange ålder"))
txt = "myndig"
if IsMyndig(age):
    txt = "ej " + txt
print(f"Om du är {age} år är du {txt}")    
