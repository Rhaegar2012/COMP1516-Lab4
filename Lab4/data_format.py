# Author: Jose Tellez
def main():
    book_info = get_book_info()
    csv_string = to_csv_format(book_info)
    print("The CSV format string: \n"+csv_string)
    json_string = to_JSON_format(csv_string)
    print("The JSON format string: \n"+json_string)


def get_book_info():
    """

    :return:
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

    :param string:
    :return:
    """
    csv_list = string.split("/")
    csv_string = ",".join(csv_list)
    return csv_string


def to_JSON_format(csv_string):
    """

    :param csv_string:
    :return:
    """
    csv_string_list = csv_string.split(",")
    book_title = csv_string_list[0]
    book_isbn = csv_string_list[1]
    author_last_name = csv_string_list[2]
    book_publisher = csv_string_list[3]
    year_of_publication = csv_string_list[4]
    book_price_in_usd = csv_string_list[5]
    JSON_string = f'{{"Book Title":"{book_title}",'\
                  f'"Book ISBN":"{book_isbn}",'\
                  f'"Author Last Name":"{author_last_name}",'\
                  f'"Publisher":"{book_publisher}",'\
                  f'"Year of Publication":"{year_of_publication}",'\
                  f'"Price in USD":"{book_price_in_usd}"}}'
    return JSON_string


def get_separator_index(string):
    """

    :param string:
    :return:
    """
    pass





if __name__ == "__main__":
    main()
