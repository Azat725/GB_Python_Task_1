total_sum = 0

while True:
    number = float(input("Введите число: "))
    if number < 0:
        break
    if number > 0:
        total_sum += number

print(f"Сумма всех положительных чисел, которые вы ввели = {total_sum}")