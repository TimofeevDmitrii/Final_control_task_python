# Что это за проект

    Данное консольное приложение создано в соответствии с условиями, изложенными в файле "Задание 1.pdf" (прикреплен в репозитории). Главная задача приложения - обеспечить работу человека заметками. Программа имеет следующий функционал: создание, редактирование, удаление заметки, печать заметок в консоль, осуществление поиска заметок по идентификатору или по дипазаону дат. Программно приложение производит чтение и запись (хранение) данных в файл. Взаимодействие с пользователем осуществляется через консоль посредством вывода меню команд и предложения ввести номер команды из спсиска, а также предложения осуществить ввод определенных данных взависимости от выбранной операции. Приложение написано на языке python.  

## Запуск приложения

    Струтктурно проект состоит из трех рабочих модулей: app_notes.py, all_menu_operations.py и auxilary.py; также в состав входит файл Notes.csv, используемый для хранения заметок. Файл Notes.csv, прикрепленный в репозитории, уже содержит в себе данные - примеры заметок. Главным, стартовым модулем с исполняемым кодом является app_notes.py. Остальные необходимы для его работы.

    Для запуска приложения необходимо, чтобы на машине был установлен интерпретатор кода на языка python. Далее необходимо иметь программную среду, которая может запускать проекты, написанные на данном языке. Для этого, например, подойдет программа Microsoft VSCode с установленным виртуальным окружением python venv в директории, где будет находится приложение для работы с заметками. 
    
    Для работы проекта прежде всего необходимо поместить в директорию с виртуальным окружением три файла-модуля - app_notes.py, all_menu_operations.py и auxilary.py. Файл Notes.csv для правильной работы также должен находиться в одной директории с этими тремя модулями. Но он не обязателен к установке, т.к. в случае его отсутствия после добавления первой заметки программа создаст экземпляр файла Notes.csv и поместит эту заметку в него. Если же Вы установите Notes.csv с примерами заметок из репозитория, то приложение в дальнейшем будет работать с ним. 

    Для удобства можно воспользоваться программой git и через терминал в VSCode склонировать репозиторий с этими четырьмя файлами в директорию с виртуальным окружением. 

    После того, как все три модуля скопированы, в терминале VSCode необходимо переместиться в директорию, где они находятся, и ввести следующую команду: 
        python app_notes.py
    Таким образом мы запускаем файл app_notes.py. В результате в консоли появится меню программы с предложением ввести номер команды. Приложение запущено. Для выхода из приложения в главном меню необходимо ввести число '8'. 

## Устройство приложения и логика работы

