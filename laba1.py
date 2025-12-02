# ---- ЧИСЛОВІ ТИПИ ----
age = 17
height = 1.78
big_number = 1000000
# ---- ЛОГІЧНИЙ ТИП ----
is_student = True
# ---- РЯДКИ ----
username = "Egnatik"
# ---- СПИСКИ ----
scores = [10, 9, 12]
# ---- МНОЖИНА ----
unique_numbers = {1, 2, 3, 3, 2}
# ---- СЛОВНИК ----
student = {
    "name": "Egnatik",
    "age": 17,
    "grade": 11
}
# Виведення типів і значень
print(f"age, {type(age)} : {age}")
print(f"height, {type(height)} : {height}")
print(f"big_number, {type(big_number)} : {big_number}")
print(f"is_student, {type(is_student)} : {is_student}")
print(f"username, {type(username)} : {username}")
print(f"scores, {type(scores)} : {scores}")
print(f"unique_numbers, {type(unique_numbers)} : {unique_numbers}")
print(f"student, {type(student)} : {student}")
# ---- АРИФМЕТИЧНІ ОПЕРАТОРИ ----
a = 10
b = 3
print(a + b)    # додавання
print(a - b)    # віднімання
print(a * b)    # множення
print(a / b)    # ділення
print(a // b)   # цілочисельне ділення
print(a % b)    # остача
print(a ** b)   # степінь
# ---- ОПЕРАТОРИ ПОРІВНЯННЯ ----
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
# ---- ЛОГІЧНІ ОПЕРАТОРИ ----
x = True
y = False
print(x and y)
print(x or y)
print(not x)
# ---- ОПЕРАТОРИ ПРИСВОЄННЯ ----
n = 5
n += 2
n -= 1
n *= 3
n /= 2
n %= 3
print(n)