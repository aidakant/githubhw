from src.masks import get_mask_card_number, get_mask_account
from src.processing.process import filter_by_state, sort_by_date


def main() -> None:
    """Основная функция приложения."""
    print("Примеры маскировки карт:")
    print(get_mask_card_number("7000792289606361"))  # 7000 79** **** 6361

    print("\nПримеры маскировки счетов:")
    print(get_mask_account("73654108430135874305"))  # **4305

    operations = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    print("Пример использования функции для обработки словарей:")
    executed_ops = filter_by_state(operations)
    for op in executed_ops:
        print(f"  ID: {op['id']}, Дата: {op['date']}, Статус: {op['state']}")

if __name__ == "__main__":
    main()