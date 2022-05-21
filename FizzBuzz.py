for num in range(1, 101):
    string = ''

#----------ここから記述----------

    if num % 15  == 0:      # 15の倍数の時
        print("FizzBuzz")

    elif num % 3 == 0:      # 3の倍数のの時
        print("Fizz")

    elif num % 5 == 0:     # 5の倍数の時
        print("Buzz")

    else:                   # それ以外の時
        print(num)

#----------ここまで記述----------
    print(string)
