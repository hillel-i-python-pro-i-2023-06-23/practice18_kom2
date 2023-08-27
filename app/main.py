import concurrent.futures

from app.services.calk_max_variants import calk
from app.services.generate_world import generate_word_regularly
from app.services.save import save_in_file
from app.services.use_simbol import use_simbols
import time



def main():
    print("Пароль состоит из _ елементов?")
    word_len = int(input())

    word_variants = calk(len(use_simbols), word_len)
    print(word_variants)

    # rez = generate_word_recursive(use_simbols, word_len, )

    with concurrent.futures.ThreadPoolExecutor() as executor:

        start_time_for_regularly = time.time()
        rez_for_regulary = generate_word_regularly(word_len, use_simbols, word_variants)
        print(len(rez_for_regulary))
        end_time_for_regularly = time.time()
        elapsed_time_for_regularly = end_time_for_regularly - start_time_for_regularly

    save_in_file(rez_for_regulary, elapsed_time_for_regularly)
