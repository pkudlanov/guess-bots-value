from random import randint

bot_num = randint(1, 100)

print('\nThe unbiased number bot chose a number between 1 and 100. Guess its value.')

try_count = 1
deviation = 0
while True:
    try:
        user_guess = int(
            input('\nWhat is your guess? >> '))
    except ValueError:
        print('     !!! THAT IS NOT A NUMBER !!!')
        continue

    if 1 > user_guess or 100 < user_guess:
        print('     OUT OF Bounds')
        continue
    elif user_guess == bot_num:
        print(f'\nYou guessed correctly. The Bots number was {bot_num}')
        if try_count == 1:
            print('Congratulations!!! You guessed the bots value on the first try!!')
        else:
            print(f'It took you {try_count} tries to get the right number.')       
        break
    elif try_count == 1:
        if abs(bot_num - user_guess) <= 10:
            print('   WARM')
            deviation = abs(bot_num - user_guess)
            try_count += 1
        else:
            print('   COLD')
            deviation = abs(bot_num - user_guess)
            try_count += 1
        continue
    else:
        if abs(bot_num - user_guess) <= deviation:
            print('   WARMER')
            deviation = abs(bot_num - user_guess)
            try_count += 1
        else:
            print('   COLDER')
            deviation = abs(bot_num - user_guess)
            try_count += 1
        continue
