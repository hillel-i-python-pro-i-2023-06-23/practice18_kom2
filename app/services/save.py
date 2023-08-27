def save_in_file(data, timer):
    with open("output.txt", "w") as file:
        file.write(f"{str(data)}\n\n\n\n\n\n\n\n\n")
        file.write(f"Обычная функция выполнилась за {timer:.6f} секунд")
