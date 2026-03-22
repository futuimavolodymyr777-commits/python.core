# try:
#     number = float(input('Enter number: '))
# except ValueError:
#     print('Incorrect value')
# except Exception:
#     print('Unknown exception')

file_path = "test.txt"

file = open(file_path, "a")

file.close()