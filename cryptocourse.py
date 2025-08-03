import requests
import json
from tkinter import *
from tkinter import messagebox as mb, ttk

def get_crypto_rate():
    crypto = crypto_combobox.get()
    if crypto:
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd")
            response.raise_for_status()
            data = response.json()
            rate = data[crypto]['usd']
            result_label.config(text=f"1 {crypto} = {rate} USD")
        except Exception as e:
            result_label.config(text=f"Ошибка: {e}")
    else:
        result_label.config(text="Выберите криптовалюту")

# Список криптовалют
cryptocurrencies = ["bitcoin", "ethereum", "ripple", "cardano", "solana"]

# Создание интерфейса
window = Tk()
window.title("Курсы криптовалют")
window.geometry("400x200")

Label(text="Выберите криптовалюту:").pack(pady=10)
crypto_combobox = ttk.Combobox(values=cryptocurrencies)
crypto_combobox.pack(pady=10)

Button(text="Обновить курс", command=get_crypto_rate).pack(pady=10)
result_label = Label(text="")
result_label.pack(pady=20)

window.mainloop()