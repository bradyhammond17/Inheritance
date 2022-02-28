import PersonClass as p


def main():
    generic_person = p.Person("John", "123 Baylor Ave", "111-1111")
    customer = p.Customer("John", "123 Baylor Ave", "111-1111", "01", True)
    print(generic_person.print_person())
    print(customer.print_person())


main()
