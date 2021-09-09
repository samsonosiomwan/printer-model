from assets.art import *
from printer.coloured import *
from printer.greyscale import *
#display message and logo
print(logo)
print("You are welcome")
print('+++++++++++++++++++++++++++++++++++++++++++++\n')

def Print_document():
    """funtion to  collect users printing format and process the printing"""
    print_format = input("What format would you like? ( coloured or greyscale ): ")
    while True:
        try:
            if print_format == "coloured":
                pages_number = int(input('Enter Number of Pages: '))
                print_doc = coloured(pages_number)
                print(print_doc.check_ink())
                return print_again()

            elif print_format == "greyscale":
                pages_number = int(input('Enter Number of Pages: '))
                print_doc = greyscale(pages_number)
                print(print_doc.check_ink())
                return print_again()

            elif print_format == "report":
                report_doc = Printer()
                print(report_doc.report())
                return print_again()

            elif print_format == "off":
                print('you have turned off the printer successfully')
                quit()
            else:
                print("Invalid format: type ('coloured' or 'greyscale')")
                return Print_document()
        except ValueError:
            return 'invalid input: restart printer and enter a number for pages no'

def print_again():
    """function exits or restarts the program, with yes or no response"""
    print('thank you for using our service')
    something_else = input('would you like to do something else (yes or no): ')
    if something_else == 'yes':
        return Print_document()
    else:
        exit()

#main entry point to the application
if __name__ == '__main__':
    print(Print_document())
    
