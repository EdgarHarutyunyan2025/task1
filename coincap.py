#!/usr/bin/env python3

"""
Модуль для конвертации валют с использованием API обменных курсов.
В данном скрипте реализована функция для конвертации указанной суммы в другую валюту
с помощью обменного курса, получаемого через API.
"""

import requests

def convert_currency(amount, base_currency, target_currency):
    """
    Функция для конвертации валют.

    :param amount: Сумма для конвертации (float или int)
    :param base_currency: Базовая валюта (например, 'USD')
    :param target_currency: Валюта для конвертации (например, 'EUR')
    :return: Конвертированная сумма или None в случае ошибки
    """
    try:
        # Устанавливаем таймаут для запроса, чтобы избежать зависания
        response = requests.get(
            f'https://v6.exchangerate-api.com/v6/217936093d74ee1fb37fa8f7/latest/{base_currency}',
            params={'APPID': '217936093d74ee1fb37fa8f7'},
            timeout=10  # Таймаут 10 секунд
        )
        response.raise_for_status()  # Если статус-код != 200, вызовет исключение
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None

    try:
        data = response.json()
        conversion_rate = data['conversion_rates'].get(target_currency)
        if conversion_rate is None:
            print(f"Курс для валюты {target_currency} не найден.")
            return None
        return amount * conversion_rate
    except (ValueError, KeyError) as e:
        print(f"Ошибка обработки данных: {e}")
        return None

def main():
    """
    Главная функция, которая запускает процесс конвертации валют.
    """
    amount = 100
    base_currency = "USD"
    target_currency = "AMD"

    converted_amount = convert_currency(amount, base_currency, target_currency)
    if converted_amount is not None:
        print("\nКонвертированная сумма:")
        print(f"{amount} {base_currency} эквивалентно {converted_amount:.2f} {target_currency}")

if __name__ == '__main__':
    main()
