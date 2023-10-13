# This is a sample Python script.
import datetime


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(datetime.datetime.now().strftime("%A"))
    print(datetime.datetime.now().weekday())
    print(datetime.datetime.strptime("30-09-2023", "%d-%m-%Y").strftime("%A"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
