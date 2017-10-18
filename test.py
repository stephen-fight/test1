import random
number = random.randint(1,100)
running = True
i = 0
j = 100
while running:
    guess = int(input('Enter an integer{}-{}:'.format(i,j)))#猜数字初始从0-100
    if guess >=j or guess<=i:#避免输入无效数字
        continue
                            #print('Enter try agin')
    elif guess == number:
        print('Congratulations, you guessed it.')
        running = False#对了结束
    elif guess < number:#小于数字则替换i
        print('no ,it is alittle lower than that.')
        i = guess
    else:#大于数字则替换j
        print('no,it is a little higher than that.')
        j = guess
else:
    print('the while loop is over')
    print('添加一行输出。')
    print('添加一行输出。')
    print('添加一行输出。')



