import requests
import json
from tkinter import *
from tkinter import messagebox as mb, ttk


def get_crypto_rate():
    crypto = crypto_combobox.get()
    currency = currency_combobox.get()
    if crypto and currency:
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}"
                                    f"&vs_currencies={currency}")
            response.raise_for_status()
            data = response.json()
            rate = data[crypto][currency]
            result_label.config(text=f"1 {crypto} = {rate} {currency.upper()}")
        except Exception as e:
            result_label.config(text=f"Ошибка: {e}")
    else:
        result_label.config(text="Выберите валюту и криптовалюту")


# Список криптовалют
cryptocurrencies = ["bitcoin", "ethereum", "ripple", "cardano", "solana"]

# Список валют
currencies = ["usd", "eur", "rub"]

# Создание интерфейса
root = Tk()
root.title("Курсы криптовалют")
root.geometry("400x300")

Label(text="Выберите валюту:").pack(pady=10)
currency_combobox = ttk.Combobox(root, values=currencies)
currency_combobox.pack(pady=10)
currency_combobox.set('rub')

Label(text="Выберите криптовалюту:").pack(pady=10)
crypto_combobox = ttk.Combobox(values=cryptocurrencies)
crypto_combobox.pack(pady=10)
crypto_combobox.set('bitcoin')

Button(text="Обновить курс", command=get_crypto_rate).pack(pady=10)
result_label = Label(text="")
result_label.pack(pady=20)

root.mainloop()
