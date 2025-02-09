import requests
import tkinter as tk
from tkinter import messagebox

class CurrencyConverter:
    def __init__(self):
        self.usd_to_uah_rate = self.get_usd_to_uah_rate()

    def get_usd_to_uah_rate(self):
        try:
            response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
            data = response.json()
            for currency in data:
                if currency['cc'] == 'USD':
                    return currency['rate']
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося отримати курс валют: {e}")
            return None

    def convert_uah_to_usd(self, uah_amount):
        if self.usd_to_uah_rate:
            return uah_amount / self.usd_to_uah_rate
        else:
            messagebox.showerror("Помилка", "Курс долара не доступний.")
            return None

def on_convert():
    try:
        uah_amount = float(entry_uah.get())
        usd_amount = converter.convert_uah_to_usd(uah_amount)
        if usd_amount is not None:
            label_result.config(text=f"{uah_amount:.2f} грн = {usd_amount:.2f} $")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректну числову суму.")

converter = CurrencyConverter()

root = tk.Tk()
root.title("Конвертер валют")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label_uah = tk.Label(frame, text="Сума в гривнях:")
label_uah.grid(row=0, column=0, pady=5)

entry_uah = tk.Entry(frame)
entry_uah.grid(row=0, column=1, pady=5)

button_convert = tk.Button(frame, text="Конвертувати", command=on_convert)
button_convert.grid(row=1, columnspan=2, pady=5)

label_result = tk.Label(frame, text="")
label_result.grid(row=2, columnspan=2, pady=5)

root.mainloop()
