from app.services.calk_max_variants import calk
from app.services.generate_world import generate_word_recursiv, generate_word_regularly
import time

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

    start_time_for_recursiv = time.time()
    rez = generate_word_recursiv(use_simbols, word_len)
    end_time_for_recursiv = time.time()
    elapsed_time_for_recursiv = end_time_for_recursiv - start_time_for_recursiv
    print(f"Рекурсивная функция выполнилась за {elapsed_time_for_recursiv:.6f} секунд")


    start_time_for_regularly = time.time()
    rez1 = generate_word_regularly(word_len, use_simbols, word_variants)
    end_time_for_regularly = time.time()
    elapsed_time_for_regularly = end_time_for_regularly - start_time_for_regularly
    print(f"Обычная функция выполнилась за {elapsed_time_for_regularly:.6f} секунд")



    with open('output.txt', 'w') as file:
        file.write(f"{str(rez)}\n\n\n\n\n\n\n\n\n")
        file.write(f"{str(rez)}\n")
        file.write(f"Рекурсивная функция выполнилась за {elapsed_time_for_recursiv:.6f} секунд\n")
        file.write(f"Обычная функция выполнилась за {elapsed_time_for_regularly:.6f} секунд")


