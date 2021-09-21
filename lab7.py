def IsVowel(letter):
    vowels = ["a", "o", "u", "å", "e", "i", "y", "ä", "ö"]
    return letter in vowels


def Translate(txt):
    s = ""
    for ch in txt:
        if IsVowel(ch):
            s += ch
        else:
            s += ch + "o" + ch
    return s

print(Translate("Stefan"))
