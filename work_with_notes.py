

class Work_with_notes:

    def __init__(self, fields):
        self.__fields=fields


    def print_notes(self, notes):
        # fields=['id:','Фамилия:', 'Имя:', 'Телефон:', 'Описание:']
        correct_size_for_print=lambda x,n:x+''.join([' ' for i in range(n-len(x))]) # функция добавляет недостающее количество пробелов до фиксированного размера n
        for k in self.__fields:
            if k=='id':
                print(correct_size_for_print(k,10),end='')
            elif k=='Описание заметки':
                print(correct_size_for_print(k,40),end='')
            elif k=='Дата создания':
                print(correct_size_for_print(k,20),end='')
            else:
                print(correct_size_for_print(k,30),end='')
        print('\n')
        for i in notes:
            for k,v in i.items():
                if k=='id':
                    print(correct_size_for_print(v,9),end=' ')
                elif k=='Описание заметки':
                    if (len(v)>49):
                        # print('cirrent'+v)
                        self.print_long_data(v)
                    else:
                        print(correct_size_for_print(v,39),end=' ')
                elif k=='Дата создания':
                    print(correct_size_for_print(v,19),end=' ')
                else:
                    print(correct_size_for_print(v,29),end=' ')
            print()
        print('\n')



    def print_long_data(self, descr):
        # spaces = [' ']*36
        count=1
        for i in range(len(descr)):
            if (i!=39*count):
                print(descr[i], end='')
            else:
                print(' ')
                print(''.join([' ']*90), end='')
                print(descr[i], end='')
                count+=1