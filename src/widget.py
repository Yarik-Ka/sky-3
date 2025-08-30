import typing

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(value: str) -> str:
    """функция принимает номер счета или номер карты"""
    value_splited = value.split(" ")
    new_list = []
    for symbols in value_splited:
        if symbols.isalpha():
            the_first_part = symbols
            new_list.append(the_first_part)
            """ условие записывает первую буквенную часть в список """
        else:
            if len(symbols) == 16:
                formatted_number = get_mask_card_number(symbols)
                new_list.append(formatted_number)
            elif len(symbols) == 20:
                formatted_number = get_mask_account(symbols)
                new_list.append(formatted_number)
                """ побочное условие форматирует номер в зависимости от кол-ва цифр """
            else:
                return "Error: invalid number or account format"
    return " ".join(new_list)


if __name__ == "__main__":
    result_1 = mask_account_card(input("Enter account card: "))
    print(result_1)


def get_date(date: typing.Any) -> typing.Any:  #
    """принимаем дату"""
    if isinstance(date, str):
        if len(date) >= 10 and date[4] == "-" and date[7] == "-":
            if int(date[8:10]) <= 31 and int(date[5:7]) <= 12:
                date_used = date[8:10] + "." + date[5:7] + "." + date[:4]
                return date_used
            else:
                return "This date doesn't exist"
        else:
            return "Please, enter the date in the 'year-month-day' format"
    else:
        if isinstance(date, list):
            filter_date = []
            for item in date:
                if len(item) >= 10 and item[4] == "-" and item[7] == "-":
                    if int(item[8:10]) <= 31 and int(item[5:7]) <= 12:
                        date_used = item[8:10] + "." + item[5:7] + "." + item[:4]
                        filter_date.append(date_used)
                        return " ".join(filter_date)
                else:
                    return "Please, enter the date in the 'year-month-day' format"
        else:
            return "Please, enter the date in the 'year-month-day' format"


if __name__ == "__main__":
    result_2 = get_date(input("Enter date: "))
    print(result_2)