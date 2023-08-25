from app.services.calk_max_variants import calk
from app.services.generate_world import generate_word

def main():
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    #            '_', '+', '-', '=', '[', ']', '{', '}', ';', ':',
    #            '"', "'", ',', '.', '<', '>', '/', '?']

    use_simbols = alphabet

    print("Пароль состоит из _ елементов?")
    word_len = int(input())
    word_variants = calk(len(use_simbols), word_len)
    print(word_variants)
    rez = generate_word(word_len, use_simbols, word_variants)
    print(rez)
    print(len(rez))
