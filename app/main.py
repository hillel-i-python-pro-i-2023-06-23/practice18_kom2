from app.services.calk_max_variants import calk
from app.services.generate_world import generate_word_recursive, generate_word_regularly
from app.services.save import save_in_file
import time
import threading





def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+', '-', '=', '<', '>', '/', '?']

    use_simbols = alphabet + numbers + symbols

    print("Пароль состоит из _ елементов?")
    word_len = int(input())

    word_variants = calk(len(use_simbols), word_len)
    print(word_variants)

    # rez = generate_word_recursive(use_simbols, word_len, )

    start_time_for_regularly = time.time()
    rez1 = generate_word_regularly(word_len, use_simbols, word_variants)
    print(len(rez1))
    end_time_for_regularly = time.time()
    elapsed_time_for_regularly = end_time_for_regularly - start_time_for_regularly

    save_in_file(rez1, elapsed_time_for_regularly)