i = 1
secret_number = 9
while i < 4:
    guessed_number = int(input('enter the secret number \n'))
    if guessed_number != 9:
        print('Wrong guess')
    else:
        print('You win')
        break
print("Program ends here...")
