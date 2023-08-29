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


def process_worker(word_generator, filename, lock):
    words = list(word_generator)

    with open(filename, "a") as f:
        for word in words:
            with lock:
                f.write(f"'{word}', ")
