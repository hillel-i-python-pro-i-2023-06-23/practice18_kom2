# import concurrent.futures

# with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
#
#     future1 = executor.submit(generate_word_regularly, word_len, use_simbols, 0, middle)
#     future2 = executor.submit(generate_word_regularly, word_len, use_simbols, middle, word_variants)
#
#     rez_for_regulary_part1 = future1.result()
#     rez_for_regulary_part2 = future2.result()
