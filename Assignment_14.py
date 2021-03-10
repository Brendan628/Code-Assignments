def main():
    user_str = input('Enter a string of characters: ')
    print('That string has', vowels(user_str), 'vowels and', \
    consonants(user_str), 'consonants.')
def vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    totalVowels = 0
    for ch in s:
        if ch.lower() in vowels:
            totalVowels += 1
    return totalVowels
def consonants(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    totalConsonants = 0
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            totalConsonants += 1
    return totalConsonants
main()