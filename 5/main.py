# Імпортуємо 10 бібліотек
import requests #для HTTP-запитів
import numpy as np #математичні операції і робота з масивами
import pandas as pd #таблиці
import matplotlib.pyplot as plt #побудова графіків
from bs4 import BeautifulSoup #витягує дані з веб-сторінок
from PIL import Image # для роботи з зображеннями
from faker import Faker # створює фейкові дані
from tqdm import tqdm # індикатор прогресу 
import datetime # дата час 
import json # зчитує та зберігає дані


# --- 1. Використання requests ---
try:
    response = requests.get("https://api.github.com")
    print(" Requests успішно отримав статус:", response.status_code)
except Exception as e:
    print(" Помилка у requests:", e)


# --- 2. Використання numpy ---
try:
    arr = np.array([1, 2, 3, 4, 5])
    print(" NumPy середнє значення:", np.mean(arr))
except Exception as e:
    print(" Помилка у numpy:", e)


# --- 3. Використання pandas ---
try:
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    print(" Pandas таблиця:\n", df)
except Exception as e:
    print(" Помилка у pandas:", e)


# --- 4. Використання matplotlib ---
try:
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title("Простий графік")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig("plot.png")
    plt.close()  # закриваємо, щоб не завис процес
    print(" Matplotlib графік збережено у plot.png")
except Exception as e:
    print(" Помилка у matplotlib:", e)


# --- 5. Використання faker ---
try:
    fake = Faker()
    for _ in range(3):
        print(" Faker ім'я:", fake.name())
except Exception as e:
    print(" Помилка у faker:", e)
