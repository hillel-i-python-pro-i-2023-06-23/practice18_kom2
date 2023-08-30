from app.services.calk_max_variants import calk
from app.services.generate_world import process_worker
from app.services.use_simbol import use_simbols
from app.services.memory_check import calculate_max_words, get_available_memory
import multiprocessing
import time
import os
from pathlib import Path


OUTPUT_PATH = Path.cwd().joinpath("files_output")


def main():
    print("Пароль состоит из _ елементов?")
    # word_len = int(input())
    word_len = 5
    word_variants = calk(len(use_simbols), word_len)
    print(word_variants)

    start_time_for_regularly = time.time()

    lock = multiprocessing.Lock()
    num_cores = os.cpu_count()
    process_list = []
    start = 0
    end = int(word_variants / num_cores)
    num_word_in_one_file = calculate_max_words(num_cores, word_len)
    print(num_word_in_one_file)
    print(get_available_memory())
    print(num_cores)
    for process in range(num_cores):
        if process == num_cores - 1:
            end = word_variants

        future = multiprocessing.Process(
            target=process_worker,
            args=(word_len, use_simbols, process, start, end, num_word_in_one_file, OUTPUT_PATH, lock),
            name=f"process{process}",
        )
        process_list.append(future)
        future.start()
        start = end
        end += int(word_variants / num_cores)

    for i in process_list:
        i.join()

    end_time_for_regularly = time.time()
    elapsed_time_for_regularly = end_time_for_regularly - start_time_for_regularly
    print(elapsed_time_for_regularly)
