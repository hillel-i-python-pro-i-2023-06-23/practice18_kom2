import psutil


def get_available_memory():
    mem = psutil.virtual_memory().available / (1024 * 1024) * 0.05
    return mem


def estimate_memory_usage(word_len):
    bytes_per_char = 1
    word_size_bytes = (word_len + 3) * bytes_per_char

    return word_size_bytes / (1024 * 1024)


def calculate_max_words(num_cores, word_len):
    word_size_mb = estimate_memory_usage(word_len)
    max_words = int(get_available_memory() / (num_cores * word_size_mb))
    return max_words
