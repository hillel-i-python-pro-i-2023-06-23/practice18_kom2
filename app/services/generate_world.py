def generate_word_recursive(alphabet, word_len, current_word="", output_strings=None):
    if output_strings is None:
        output_strings = []

    if word_len == 0:
        output_strings.append(current_word)
        return output_strings

    for letter in alphabet:
        generate_word_recursive(
            alphabet,
            word_len - 1,
            current_word + letter,
            output_strings,
        )

    return output_strings


def generate_word_regularly(word_len, use_simbols, start, end):
    for i in range(start, end):
        indices = []
        remaining = i
        for _ in range(word_len):
            indices.append(remaining % len(use_simbols))
            remaining //= len(use_simbols)
        word = "".join([use_simbols[idx] for idx in reversed(indices)])
        yield word


def process_worker(word_len, use_simbols, process_id, start, end, num_word_in_one_file, output_path, lock):
    for sub_range_start in range(start, end, num_word_in_one_file):
        sub_range_end = min(sub_range_start + num_word_in_one_file, end)
        word_generator = generate_word_regularly(word_len, use_simbols, sub_range_start, sub_range_end)
        words = list(word_generator)

        filename = output_path / f"output_process{process_id}_range{sub_range_start}-{sub_range_end}.txt"

        with open(filename, "a") as f:
            with lock:
                f.write(f"'{words}', ")

        # with open(filename, "a") as f:
        #     for word in words:
        #         with lock:
        #             f.write(f"'{word}', ")
