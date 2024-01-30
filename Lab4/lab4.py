# Author: Jose Tellez
import login


def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    bcit_id = input("Enter your BCIT ID: ")
    default_login = login.generate_password(first_name,last_name,bcit_id)
    print(default_login)
    new_password = login.change_password()


if __name__ == "__main__":
    main()