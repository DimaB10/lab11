def write_powers_of_three(chisla, N):
    try:
        with open(chisla, 'w', encoding='utf-8') as file:
            for i in range(1, N + 1):
                file.write(f"3^{i} = {3**i}\n")

        print(f"Степені числа 3 від 1 до {N} записані у файл '{chisla}'.")

    except Exception as e:
        print(f"Виникла помилка: {e}")
try:
    N = int(input("Введіть число N: "))
    if N > 0:
        write_powers_of_three('chisla.txt', N)
    else:
        print("Будь ласка, введіть число більше 0.")
except ValueError:
    print("Введіть ціле число.")
