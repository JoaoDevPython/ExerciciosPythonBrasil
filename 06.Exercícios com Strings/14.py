
leet_speak = {'A': 4,
              'B': '|3',
              'C': '[',
              'D': '|)',
              'E': 3,
              'F': '|=',
              'G': 6,
              'H': '#',
              'I': 1,
              'J': ']',
              'K': '|<',
              'L': 1,
              'M': '/\\/\\',
              'N': '|\\|',
              'O': 0,
              'P': '|>',
              'Q': '0_',
              'R': '|2',
              'S': 5,
              'T': 7,
              'U': '(_)',
              'V': '\\/',
              'W': '\\/\\/',
              'X': '><',
              'Y': 'j',
              'Z': 2}
frase = input('Frase: ').upper()
print('Gerador Leet Speak')
for i in frase:
    if i.isalpha():
        print(leet_speak[i], end='')
    else:
        print(' ')
