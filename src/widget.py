from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_or_card_info: str) -> str:
    account_or_card_info_number = account_or_card_info.split(" ")[-1]
    account_or_card_info_id = " ".join(account_or_card_info.split(" ")[:-1])

    result = account_or_card_info_id

    if len(account_or_card_info_number) == 16:
        result += get_mask_card_number(account_or_card_info_number)
    else:
        result += " " + get_mask_account(account_or_card_info_number)

    return result


def get_date(string_date: str) -> str:
    date = string_date.split("T")[0]
    date_list = date.split("-")
    date_list = date_list[::-1]
    result = ".".join(date_list)
    return result
