ДЛЯ ИСПОЛЬЗОВАНИЯ:
1.  Открыть папку со скриптом в терминале
2.  Запустить команду: pip install -r requirements.txt
3.  Указать в Wallet.txt желаемые кошельки для проверки (списком).
4.  Запустить скрипт с помощью команды: python cli_wallet_checker.py


- Скрипт читает список кошельков из файла wallets.txt (он должен лежать в одной папке с cli_wallet_checker.py).
- Скрипт проверяет аллокацию кошельков через API (https://www.blastbera.fun/api/check-eligibility?address=) и выводит только поля "isEligible" и "allocation", а также вычисляет общий баланс allocation.
- Добавлена "смешная" анимация в консоли во время поиска кошельков, теперь с использованием слова "CatoCut".
- Добавлен файл requirements.txt для быстрой установки зависимостей.
