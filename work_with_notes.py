

class WorkWithNotes:

    __fields=['id', 'Название заметки', 'Дата создания', 'Автор', 'Описание заметки']
    __column_sizes={'id': 10, 'Название заметки': 30, 'Дата создания': 15, 'Автор':40, 'Описание заметки':50}

    def print_notes(self, notes):
        # fields=['id:','Фамилия:', 'Имя:', 'Телефон:', 'Описание:']
        correct_size_for_print=lambda x,n:x+''.join([' ' for i in range(n-len(x))]) # функция добавляет недостающее количество пробелов до фиксированного размера n
        
        for k in self.__fields:
            print(correct_size_for_print(k,self.__column_sizes[k]),end='')
        print()
        for i in notes:
            for k,v in i.items():
                if k=='Описание заметки' and len(v)>self.__column_sizes[k]-1:
                    self.__print_long_description(v)
                else:
                    print(correct_size_for_print(v,self.__column_sizes[k]-1),end=' ')
            print()
        print('\n')


    def __count_spaces_num(self,key):
        spaces_number=0
        for i in self.__fields:
            if i==key:
                break
            else:
                spaces_number+=self.__column_sizes[i]
        return spaces_number

    def __print_long_description(self, descr):
        count=1
        for i in range(len(descr)):
            if (i!=(self.__column_sizes['Описание заметки']-1)*count):
                print(descr[i], end='')
            else:
                print(' ')
                print(''.join([' ']*self.__count_spaces_num('Описание заметки')), end='')
                print(descr[i], end='')
                count+=1