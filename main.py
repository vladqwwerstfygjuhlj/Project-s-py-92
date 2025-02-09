result = []

def divider(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Один із аргументів не є числом")
        if a < b:
            raise ValueError("Число 'a' менше за 'b'")
        if b > 100:
            raise IndexError("Значення 'b' більше 100")
        return a / b
    except Exception as e:
        print(f"Помилка у divider({a}, {b}): {e}")
        return None


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"Помилка обробки ключа {key}: {e}")

print("Результат:", result)

