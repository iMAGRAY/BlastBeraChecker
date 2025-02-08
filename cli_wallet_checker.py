import requests
import threading
import time
import sys

spinner_running = True

def animate_spinner():
    """
    Анимация спиннера с использованием слова "CatoCut", выводящая сообщение во время поиска кошельков.
    """
    frames = [
        "CatoCut | Идет поиск кошельков...",
        "CatoCut / Идет поиск кошельков...",
        "CatoCut - Идет поиск кошельков...",
        "CatoCut \\ Идет поиск кошельков..."
    ]
    while spinner_running:
        for frame in frames:
            if not spinner_running:
                break
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(0.1)

def check_wallet_allocation(address):
    """
    Отправляет запрос к API для проверки аллокации указанного кошелька.
    Возвращает ответ в формате JSON или словарь с ключом "error" в случае ошибки.
    """
    base_url = "https://www.blastbera.fun/api/check-eligibility"
    params = {"address": address}
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def main():
    # Чтение адресов из файла wallets.txt
    try:
        with open("wallets.txt", "r", encoding="utf-8") as f:
            addresses = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Файл wallets.txt не найден в текущей папке.")
        return

    if not addresses:
        print("Файл wallets.txt пуст или не содержит адресов.")
        return

    global spinner_running
    spinner_running = True

    # Запускаем анимацию в отдельном потоке
    spinner_thread = threading.Thread(target=animate_spinner)
    spinner_thread.start()

    total_allocation = 0.0
    results = []
    
    # Перебор адресов и получение данных
    for address in addresses:
        result = check_wallet_allocation(address)
        if "error" in result:
            results.append(f"Адрес: {address} | Ошибка: {result['error']}")
        else:
            eligible = result.get("isEligible", False)
            allocation_raw = result.get("allocation", "0")
            try:
                allocation_num = float(allocation_raw.replace(",", ""))
            except Exception:
                allocation_num = 0.0
            total_allocation += allocation_num
            results.append(f"Адрес: {address} | isEligible: {eligible} | allocation: {allocation_raw}")
    
    # Останавливаем анимацию и очищаем строку
    spinner_running = False
    spinner_thread.join()
    sys.stdout.write("\r" + " " * 60 + "\r")
    sys.stdout.flush()

    print("Результаты:")
    for res in results:
        print(res)
    
    print(f"\nИтоговый общий баланс allocation: {total_allocation}")

if __name__ == "__main__":
    main() 