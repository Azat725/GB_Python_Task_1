name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
user_height = input("Введите ваш рост")
user_weight = input("Введите ваш вес: ")

def calc_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

print(f"Здраствуйте {name}, вам {age} лет, ваш индекс массы тела = {calc_bmi(user_weight, user_weight)}")