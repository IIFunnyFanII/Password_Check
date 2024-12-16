import math

def calculate_entropy(password):
    length = len(password)
    if length == 0:
        return 0, "Пароль пустой."
    
    # Количество возможных символов в пароле
    R = 0
    if any(i.islower() for i in password):
        R += 26  # Строчные буквы
    if any(i.isupper() for i in password):
        R += 26  # Заглавные буквы
    if any(i.isdigit() for i in password):
        R += 10  # Цифры
    if any(i in "!@#$%^&*()-_=+[]{}|;:',.<>?/`~" for i in password):
        R += 32  # Специальные символы
    
    # Энтропия
    if R > 0:
        entropy = length * math.log2(R)
        return entropy, ""
    else:
        return 0, "Набор символов не распознан."

def evaluate_strength(entropy):
    if entropy < 28:
        return "Слабый пароль"
    elif entropy < 36:
        return "Средний пароль"
    elif entropy < 60:
        return "Сильный пароль"
    else:
        return "Очень сильный пароль"

def main():
    password = input("Введите пароль для оценки: ")
    entropy, message = calculate_entropy(password)
    if message:
        print(message)
    else:
        print(f"Энтропия: {entropy:.2f} бит.")
        strength = evaluate_strength(entropy)
        print(f"Сложность пароля: {strength}")

if __name__ == "__main__":
    main()
