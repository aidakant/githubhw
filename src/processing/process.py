def filter_by_state(operations_list: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтруем список операций по статусу.
    Возвращаем только те операции, у которых ключ 'state'
    соответствует указанному значению.
    """
    filtered_list = []

    for operation in operations_list:
        if operation.get('state') == state:
            filtered_list.append(operation)

    return filtered_list


def sort_by_date(operations_list: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список операций по дате.
    """
    sorted_list = operations_list.copy()
    sorted_list.sort(key=lambda x: x['date'], reverse=reverse)

    return sorted_list