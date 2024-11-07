def count_letter_frequency(texas):
    letter_count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    try:
        with open(texas, 'r', encoding='utf-8') as file:
            for line in file:
                for char in line.lower():
                    if char in letter_count:
                        letter_count[char] += 1
        letter_count = {k: v for k, v in letter_count.items() if v > 0}
        print("Частота появи літер:")
        print(letter_count)
        return letter_count
    except FileNotFoundError:
        print(f"Файл '{texas}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
count_letter_frequency('texas.txt')