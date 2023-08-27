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

    middle = word_variants // 2


    start_time_for_regularly = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:

        future1 = executor.submit(generate_word_regularly, word_len, use_simbols, 0, middle)
        future2 = executor.submit(generate_word_regularly, word_len, use_simbols, middle, word_variants)

        rez_for_regulary_part1 = future1.result()
        rez_for_regulary_part2 = future2.result()

    rez_for_regulary = rez_for_regulary_part1 + rez_for_regulary_part2
    end_time_for_regularly = time.time()



    elapsed_time_for_regularly = end_time_for_regularly - start_time_for_regularly
    save_in_file(rez_for_regulary, elapsed_time_for_regularly)

