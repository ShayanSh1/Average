numbers = []

user_number = int(input('enter your number:'))

while user_number != -1:
    numbers.append(user_number)
    user_number = int(input('enter your next number:'))


user_next_number = 0

for num in numbers:
    user_next_number += num

result = user_next_number / len(numbers)


print(f'your result is {result}')

