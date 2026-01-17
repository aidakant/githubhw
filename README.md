# Processing Module

### Назначение
Модуль processing предназначен для обработки списков банковских операций. Он содержит функции для фильтрации операций по статусу и сортировки по дате.

### Функции

### `filter_by_state(operations_list, state='EXECUTED')`
Фильтрует список операций по указанному статусу.

**Параметры:**
- `operations_list`: список словарей с операциями
- `state`: статус для фильтрации (по умолчанию 'EXECUTED')

**Возвращает:** новый список словарей, отфильтрованный по статусу

**Пример:**
```
from src.processing.process import filter_by_state

operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-15'},
    {'id': 2, 'state': 'CANCELED', 'date': '2024-01-16'}
]

executed = filter_by_state(operations, 'EXECUTED')
```

### `sort_by_date(operations_list, reverse=True)`
Сортирует список операций по дате.

**Параметры:**
- `operations_list`: список словарей с операциями
- `reverse`: порядок сортировки (True - по убыванию, False - по возрастанию, по умолчанию True)

**Возвращает:** новый список словарей, отсортированный по дате

**Пример:**
```
from src.processing.process import sort_by_date

operations = [
    {'id': 1, 'date': '2024-01-15'},
    {'id': 2, 'date': '2024-01-10'}
]

sorted_desc = sort_by_date(operations)  # по убыванию
sorted_asc = sort_by_date(operations, reverse=False)  # по возрастанию
```

 Пример комбинированного использования
```
from src.processing.process import filter_by_state, sort_by_date

result = sort_by_date(filter_by_state(operations, 'EXECUTED'))
```