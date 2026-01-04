def get_mask_card_number(card_number: str) -> str:
    masked = ""
    split_masked = ""
    for i in range(len(card_number)):
        if 5 < i < 12:
            masked += "*"
        else:
            masked += card_number[i]

    for i in range(len(masked)):
        if i % 4 == 0:
            split_masked += " " + masked[i]
        else:
            split_masked += masked[i]

    return split_masked


def get_mask_account(account_number: str) -> str:
    masked = ""
    for i in range(14, len(account_number)):
        if 14 <= i < 16:
            masked += "*"
        else:
            masked += account_number[i]

    return masked
