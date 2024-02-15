user_age = int(input("Введите ваш возраст:  "))

def whoAreYou(age):
    if user_age in range(0, 6 + 1):
        print("Вы ребенок")
    elif user_age in range(7, 14 + 1):
        print("Вы подросток")
    elif user_age in range(14, 18 + 1):
        print("Вы юноша")
    elif user_age in range(18, 60 + 1):
        print("Вы взрослый")
    else:
        print("Вы пожилой")

whoAreYou(user_age)