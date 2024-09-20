'''Q.2)'''

def vowels_consonants(string):
    vowels= "aeiou"
    vowel= 0
    consonant= 0

    for word in string:
        if word.isalpha():
            if word in vowels:
                vowel += 1
            else:
                consonant += 1

    return vowel,consonant

a = input("Enter a string: ")

vowel,consonant= vowels_consonants(a)

print(f"Number of vowels:{vowel}")
print(f"Number of consonants:{consonant}")
