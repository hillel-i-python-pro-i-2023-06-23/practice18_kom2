import sys
from app.services.calk_max_variants import calk
from app.services.generate_world import generate_word_regularly, process_worker
from app.services.save import save_in_file
from app.services.use_simbol import use_simbols
import multiprocessing
import time
import os
from pathlib import Path

OUTPUT_PATH = Path.cwd().joinpath("output")

def main():
    print("Пароль состоит из _ елементов?")
    word_len = int(input())
    word_variants = calk(len(use_simbols), word_len)
    print(word_variants)

    start_time_for_regularly = time.time()

    lock = multiprocessing.Lock()
    num_cores = os.cpu_count()//2
    process_list = []
    start = 0
    end = int(word_variants / num_cores)

    for process in range(num_cores):
        if process == num_cores-1:
            end = word_variants

        word_generator = generate_word_regularly(word_len, use_simbols, start, end)
        future = multiprocessing.Process(target=process_worker, args=(word_generator, OUTPUT_PATH / f"output{process}.txt", lock),
                                         name=f"process{process}")
        process_list.append(future)
        future.start()
        start = end
        end += int(word_variants / num_cores)


    for i in process_list:
        i.join()

    end_time_for_regularly = time.time()


    elapsed_time_for_regularly = end_time_for_regularly - start_time_for_regularly

    print(elapsed_time_for_regularly)
    # save_in_file(rez_for_regulary, elapsed_time_for_regularly)

