from decorators import check_types

@check_types
def greet(name: str, age: int):
    print(f"Hello {name}, you are {age} years old.")

# Приклади виклику:
greet("Alice", 25)   # Коректно
greet("Bob", "30")   # Викличе TypeError
