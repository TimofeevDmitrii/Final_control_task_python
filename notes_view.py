

class NotesView:

    __fields=['id','Дата создания','Дата изменения','Название заметки','Описание заметки'] 
    __column_sizes={'id': 8, 'Дата создания': 18, 'Дата изменения': 18, 'Название заметки': 40, 'Описание заметки':50}


    
    def print_notes(self, notes_lst):
        correct_size_for_print=lambda x,n:x+''.join([' ' for i in range(n-len(x))]) # функция добавляет недостающее количество пробелов до фиксированного размера n
        
        for k in self.__fields:
            print(correct_size_for_print(k,self.__column_sizes[k]),end='')
        print()
        for i in notes_lst:
            for k,v in i.items():
                if k=='Описание заметки' and len(v)>self.__column_sizes[k]-1:
                    self.__print_long_description(v)
                else:
                    print(correct_size_for_print(v,self.__column_sizes[k]-1),end=' ')
            print('\n')
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