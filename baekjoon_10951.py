while True:
    try:
        input_num = input().split(' ')
        print(int(input_num[0]) + int(input_num[1]))

    except EOFError:
        break