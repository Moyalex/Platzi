def palindrome2(word):
    reversed_word = word[::-1]

    if reversed_word == word :
      return True

    return False


def palindrome(word):
    reversed_letters = []
    
    for item in word:
        reversed_letters.insert(0,item)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
      return True
    
    return False


if __name__ == "__main__":
    word = str(input("Escribe una palabra: "))
    
    result = palindrome2(word)
    
    if result:
        print('{} si es un palindromo.'.format(word))
    else:
        print("{} no es un palindromo.".format(word))