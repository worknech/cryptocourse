import requests
from tkinter import *
from tkinter import ttk


def get_crypto_rate():
    """
        Получает текущий курс выбранной криптовалюты к указанной валюте через API CoinGecko
        и отображает результат в интерфейсе.

        Функция выполняет следующие действия:
        1. Получает выбранные значения криптовалюты и валюты из Combobox
        2. Формирует запрос к API CoinGecko
        3. Обрабатывает ответ и форматирует результат
        4. Обновляет текстовую метку result_label с полученным курсом

        Исключения:
            requests.RequestException: Возникает при проблемах с сетевым запросом
            KeyError: Возникает если API вернул неожиданную структуру данных
            ValueError: Возникает при проблемах с преобразованием данных

        Пример возвращаемого значения в result_label:
            "1 bitcoin = 50 123.45 USD"
            "Ошибка: timeout"
            "Выберите валюту и криптовалюту"

        Примечания:
            - Для работы требуется активное интернет-соединение
            - Использует API CoinGecko (https://www.coingecko.com/en/api)
            - Форматирует числа с разделением тысяч пробелами
        """
    crypto = crypto_combobox.get()
    currency = currency_combobox.get()
    if crypto and currency:
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}"
                                    f"&vs_currencies={currency}")
            response.raise_for_status()
            data = response.json()
            rate = data[crypto][currency]
            result_label.config(text=f"1 {crypto} = {rate:,.2f}".replace(",", " ") + f" {currency.upper()}")
        except requests.RequestException as e:
            result_label.config(text=f"Ошибка сети: {e}", fg="red")
        except KeyError:
            result_label.config(text="Ошибка: неверный формат данных от API", fg="red")
        except ValueError as e:
            result_label.config(text=f"Ошибка данных: {e}", fg="red")
        except Exception as e:
            result_label.config(text=f"Ошибка: {e}", fg="red")
    else:
        result_label.config(text="Выберите валюту и криптовалюту", fg="orange")


# Список криптовалют
cryptocurrencies = ["bitcoin", "ethereum", "ripple", "cardano", "solana"]

# Список валют
currencies = ["usd", "eur", "rub"]

# Создание интерфейса
root = Tk()
root.title("Курсы криптовалют")
root.geometry("400x300")

# Комбобокс выбора валюты
Label(text="Выберите валюту:").pack(pady=10)
currency_combobox = ttk.Combobox(root, values=currencies, state="readonly")
currency_combobox.pack(pady=10)
currency_combobox.set('rub')

# Комбобокс выбора криптовалюты
Label(text="Выберите криптовалюту:").pack(pady=10)
crypto_combobox = ttk.Combobox(root, values=cryptocurrencies, state="readonly")
crypto_combobox.pack(pady=10)
crypto_combobox.set('bitcoin')

# Кнопка запуска
Button(text="Обновить курс", command=get_crypto_rate).pack(pady=10)

# Вывод результата и ошибок
result_label = Label(text="", font=("Verdana", 11))
result_label.pack(pady=20)

root.mainloop()
