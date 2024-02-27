def main():
    #вводим кол-во списков
    n = input("Введите кол-во списков: ")
    n = int(n)

    #массив списков
    myList = []
    for i in range(n):

        #заполняем список
        print('Список №', i+1)
        curList = []
        for j in range(3):
            print('list[', j, '] = ', sep='', end='')
            el = input()
            el = int(el)
            curList.append(el)

        #добавляем в массив
        myList.append(curList)
        print()
    count = check_lists(myList)
    print('Кол-во одинаковых элементов =', count)


def check_lists(myList):
    # кол-во одинаковых элементов
    count = 0

    # перебираем элементы 1 списка
    for i in range(3):
        # кол-во списков (начиная со 2), где найден элемент
        a = 0

        # перебираем все списки начиная со 2
        for j in range(1, len(myList)):

            # если элемент есть в этом списке
            if myList[0][i] in myList[j]:
                a += 1

        # если элемент есть в каждом из списков
        if len(myList) - 1 == a:
            count += 1
    return count


if __name__ == '__main__':
    main()