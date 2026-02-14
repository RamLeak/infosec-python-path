def calculate_compound_interest(start: float,bet: float,age: int) -> float:
    if start < 0 or bet < 0 or age < 0:
        raise ValueError("Сумма, ставка и срок не могут быть отрицательными.")
    summa = start
    for i in range(1,age+1):
        summa = summa * (1 + bet/100)
    return round(summa,2)

if __name__ == '__main__':
    print("Программа запущена")

    while True:
        try:
            user_start = float(input("Введите начальную сумму: "))
            user_bet = float(input("Введите годовую ставку (%): "))
            user_age = int(input("Введите срок (лет): "))

            result = calculate_compound_interest(user_start, user_bet, user_age)

            print(f"Через {user_age} лет сумма составит: {result} рублей")
            break
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")