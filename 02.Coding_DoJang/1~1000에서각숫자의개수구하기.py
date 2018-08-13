while True:
    number = str(input('범위를 가정할 숫자 두개를 입력하세요:'))
    number_range = number.split()
    index = [0,0,0,0,0,0,0,0,0,0,]

    for i in range(int(number_range[0]),int(number_range[1])+1):
        for num_count in str(i):
            index[int(num_count)] += 1

    for i in range(10):
        print(i,':',index[i],'개')




    # number_sort = list(number_count)
    # number_insert = sorted(number_sort)
    # number_insert = map(int, number_insert)
    #
    # print(number_insert)



