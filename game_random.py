import random

def guess_the_number():
    secret_number = random.randint(1, 10)  
    attempts = 3  

    print("Я загадав число від 1 до 10. Спробуй вгадати!")

    while attempts > 0:
        try:
            user_guess = int(input(f"У тебе залишилося {attempts} спроб(и). Введи число: "))
            if user_guess < 1 or user_guess > 10:
                print("Будь ласка, введи число від 1 до 10.")
                continue

            if user_guess == secret_number:
                print("Вітаю! Ти вгадав число!")
                break
            elif user_guess > secret_number:
                print("Менше!")
            else:
                print("Більше!")

            attempts -= 1
        except ValueError:
            print("Будь ласка, введи ціле число.")

    if attempts == 0:
        print(f"Ти програв! Загадане число було {secret_number}.")

# Запуск гри
guess_the_number()
