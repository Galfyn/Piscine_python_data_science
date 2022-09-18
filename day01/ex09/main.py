import sys


def caesar(code, word, nb):
    if code == 'decode':
        nb *= -1
    new_word = ''
    lower_alfa = 'abcdefghijklmnopqrstuvwxyz'
    upper_alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(word)):
        if word[i] in lower_alfa:
            m = lower_alfa.find(word[i])
            new_word += lower_alfa[(nb + m) % len(lower_alfa)]
        elif word[i] in upper_alfa:
            m = upper_alfa.find(word[i])
            new_word += upper_alfa[(nb + m) % len(upper_alfa)]
        else:
            new_word += word[i]

    print(new_word)


if __name__ == '__main__':
    if len(sys.argv) != 4 or (sys.argv[1] != 'encode' and sys.argv[1] != 'decode'):
        raise Exception("Error argument")
    if not sys.argv[2].isascii():
        raise Exception("Error: str not from ascii")
    try:
        nb = int(sys.argv[3])
    except ValueError:
        raise Exception("Error: shift is not int")
    caesar(sys.argv[1], sys.argv[2], nb)

