from src.masks import get_mask_card_number, get_mask_account


def main() -> None:
    """Основная функция приложения."""
    print("Примеры маскировки карт:")
    print(get_mask_card_number("7000792289606361"))  # 7000 79** **** 6361

    print("Примеры маскировки счетов:")
    print(get_mask_account("73654108430135874305"))  # **4305


if __name__ == "__main__":
    main()
