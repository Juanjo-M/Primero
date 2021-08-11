palabra=input("Escriba una una palabra :")
palabra= palabra.upper()
word_without_vowels = ""
for letter in palabra: 
    if letter=="A":
        continue
    elif letter=="E":
        continue
    elif letter=="I":
        continue
    elif letter=="O":
        continue
    elif letter=="U":
        continue
    else:  word_without_vowels += letter #print(letter)     
print(word_without_vowels)

print("Fin del programa")