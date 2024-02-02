# Author: Jose Tellez
def main():
    book_info = get_book_info()
    csv_string = to_csv_format(book_info)
    print("The CSV format string: \n"+csv_string)
    json_string = to_JSON_format(csv_string)
    print("The JSON format string: \n"+json_string)


def get_book_info():
    """
    Receives user input and formats it properly
    :return:returns concatenated string joining with /
    """
    book_title = input("Enter book title: ").strip()
    book_isbn = input("Enter book ISBN: ").strip()
    author_last_name = input("Enter author last name: ").strip()
    book_publisher = input("Enter book publisher: ").strip()
    year_published = input("Enter year of publication: ").strip()
    book_price_usd = float(input("Enter book price in USD: ").strip())
    return_string = (f"{book_title}/{book_isbn}/{author_last_name}/{book_publisher}/{year_published}/%.2f"
                     % book_price_usd)
    return return_string


def to_csv_format(string):
    """
    Formats an input string in csv style
    :param string:
    :return:formatted string in CSV style
    """
    csv_list = string.split("/")
    csv_string = ",".join(csv_list)
    return csv_string


def to_JSON_format(csv_string):
    """
    Converts a csv style string to a json format string
    :param csv_string: csv formatted string
    :return:JSON style formatted string
    """
    csv_comma_indexes = get_separator_indexes(csv_string,",")
    book_title = csv_string[:csv_comma_indexes[0]]
    book_isbn = csv_string[csv_comma_indexes[0]+1:csv_comma_indexes[1]]
    author_last_name = csv_string[csv_comma_indexes[1]+1:csv_comma_indexes[2]]
    book_publisher = csv_string[csv_comma_indexes[2]+1:csv_comma_indexes[3]]
    year_of_publication = csv_string[csv_comma_indexes[3]+1:csv_comma_indexes[4]]
    book_price_in_usd = csv_string[csv_comma_indexes[4]+1:csv_comma_indexes[5]]
    JSON_string = f'{{"Book Title":"{book_title}",'\
                  f'"Book ISBN":"{book_isbn}",'\
                  f'"Author Last Name":"{author_last_name}",'\
                  f'"Publisher":"{book_publisher}",'\
                  f'"Year of Publication":"{year_of_publication}",'\
                  f'"Price in USD":"{book_price_in_usd}"}}'
    return JSON_string


def get_separator_indexes(string,character):
    """
    Finds all the positions in which a specific character can be found in a specific string
    :param string: input string
    :param character: target character
    :return:List of indexes in which the target character was found in the string
    """
    indexes = []
    start_index = 0
    comma_index = string.find(character)
    indexes.append(comma_index)
    while comma_index != -1:
        start_index = comma_index+1
        comma_index = string.find(character, start_index)
        indexes.append(comma_index)

    return indexes


if __name__ == "__main__":
    main()
