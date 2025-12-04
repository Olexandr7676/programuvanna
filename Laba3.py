# ====================== ЗБІР РЕЗУЛЬТАТІВ СТУДЕНТІВ ======================

# Створюємо словник для збереження імен та оцінок
results = {}

# Безкінечний цикл введення студентів
while True:
    name = input("Введіть ім'я (або 'stop' для завершення): ")

    if name.lower() == "stop":   # Завершення програми
        break

    # Перевірка оцінки
    while True:
        grade_in = input("Введіть оцінку (1–12): ")

        if grade_in:  # Перевіряємо, чи введено хоч щось
            try:
                grade = int(grade_in)  # Спроба перетворити у число

                if 1 <= grade <= 12:
                    results[name] = grade  # Додаємо результат
                    break
                else:
                    print("❗ Оцінка повинна бути від 1 до 12.")
            
            except ValueError:
                print("❗ Оцінка має бути числом.")
        else:
            print("❗ Ви нічого не ввели.")

# ====================== ВИВЕДЕННЯ РЕЗУЛЬТАТІВ ======================

if results:
    print("\n===== Список студентів та їх оцінок =====")
    for name, grade in results.items():
        print(f"{name}: {grade}")

    # Обчислення середнього бала
    avg = round(sum(results.values()) / len(results), 2)
    print(f"\nСередній бал: {avg}")

    # Класифікація студентів
    excellent = [n for n in results if 10 <= results[n] <= 12]
    good = [n for n in results if 7 <= results[n] <= 9]
    weak = [n for n in results if 4 <= results[n] <= 6]
    fail = [n for n in results if 1 <= results[n] <= 3]

    print("\n===== Класифікація студентів =====")
    print("Відмінники:", len(excellent), "→", ', '.join(excellent) if excellent else "немає")
    print("Хорошисти:", len(good), "→", ', '.join(good) if good else "немає")
    print("Відстаючі:", len(weak), "→", ', '.join(weak) if weak else "немає")
    print("Не здали:", len(fail), "→", ', '.join(fail) if fail else "немає")

else:
    print("Жодного студента не було введено.")
