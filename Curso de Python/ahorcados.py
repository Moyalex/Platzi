import random

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]


def display_board(hidder_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidder_word)
    print(' --- * --- * --- * --- * --- * --- * --- ')




def random_word():
    ldx = random.randint(0,len(WORDS)-1)
    return WORDS[ldx]


def run():
    word = random_word()
    hidder_word = ['-'] * len(word)
    tries = 0
    while True:
        display_board(hidder_word,tries)
        curren_letter = str(input("Escoge una letra"))

        letter_indexes = []
        for idx in range(len(word)):
            if word == curren_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0
            tries += 1

            if tries==7:
              display_board(hidder_word,tries )
              print("")
              print("¡Perdoste! La palabra correcta era {}".format(word))
              break

        else:
            for idx in letter_indexes:
                hidder_word[idx] = curren_letter

            letter_indexes  = []
        
        try:
            hidder_word.index('-')
        except expression as identifier:
            print("")
            print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
            break

        
           

       



if __name__ == "__main__":
    print("B I E N V E N I D O S  A  A H O R C A D O S")
    run()