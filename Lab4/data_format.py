# Author: Jose Tellez

def get_book_info():
    """

    :return:
    """
    book_title = input("Enter book title: ").strip()
    book_isbn = input("Enter book ISBN: ").strip()
    author_last_name = input("Enter author last name: ").strip()
    book_publisher = input("Enter book publisher: ").strip()
    year_published = input("Enter year of publication: ").strip()
    book_price_usd = input("Enter book price in USD: ").strip()
    return_string = f"{book_title}/{book_isbn}/{author_last_name}/{book_publisher}/{year_published}/%.2f" % book_price_usd
    return return_string


def to_csv_format():
    """

    :return:
    """
    pass


def to_JSON_format():
    """

    :return:
    """
    pass
