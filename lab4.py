def LongestWord(wordList):
    longestSoFar = ""
    for x in wordList:
        if len(x) > len(longestSoFar):
            longestSoFar = x
    return longestSoFar

lista = ["hej", "Stefan", "sdadassdad", "Hejhoppsdfadf"]
print(LongestWord(lista))                


