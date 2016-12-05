#!/usr/bin/env python3
"""

Author: aabuinc
Version: 0.2
Contacts: aabu.inc@gmail.com

"""
def sign():
    print("""

,--------.       ,------.   v.0.2
'--.  .--',---.  |  .-.  \  ,---.
   |  |  | .-. | |  |  \  :| .-. |
   |  |  ' '-' ' |  '--'  /' '-' '
   `--'   `---'  `-------'  `---'
       Tool for To-Do tasks

""")
# Список комманд + Переобразователь комманды
def getcmd():
    print("""
    Возможные функции:

    1) Вывести все To-Do task'и
    2) Добавить To-Do task
    3) Удалить To-Do task
    4) Очистить файл todo.txt

    99) Обновить файл и выйти
    """)
    command = input("    todo.py >   Выберите:  ")
    try:
        command = int(command)
        return command
    except Exception as e:
        print("\n\n    Неверная команда! Введите снова\n\n")
        return getcmd()

def addtask():
    while 8==8:
        newitem = input("    Введите To-Do Task:  ")
        if newitem.find("[^splitter$$]")==-1:
            break
        else:
            print("[ ! ] Простите, но \"[^splitter$$]\" используется в программе как разделитель. Измените на дргую подстроку :)")
    while 8==8:
        newitemt = input("    Введите тип(для показа типов list):")
        if newitemt=="list":
            print("""    1) + - Сделанное задание
    2) ? - Под вопросом
    3) (пустое) - простое задание
    4) W - Важное
    5) T - ограниченное временем""")
        elif (newitemt=="+")or(newitemt=="W")or(newitemt=="T")or(newitemt=="?")or(newitemt==""):
            if newitemt=="":
                newitemt=" "
            newitem = "\n[ "+newitemt+" ] "+newitem+"\n"
            break
        else:
            print("\nНеверный тип. Для просмотра типов введите list")
    return newitem

def getall():
    print(todoa)

def main():
    todof = open("todo.txt","r")
    todoa = ""
    for line in todof:
        todoa = todoa + line

    sign()
    while 8==8:
        cmdd = getcmd()

        if cmdd ==1: print(todoa)
        if cmdd ==2: todoa = todoa + addtask()
        if cmdd ==3:
            while 8==8:
                tdlst = todoa.replace("\n\n","[^splitter$$]")
                tdlst = tdlst.replace("\n","")
                tdlst = tdlst.split("[^splitter$$]")
                i=1
                for elem in tdlst:
                    print("    " + str(i) + " ) " + elem)
                    i=i+1
                todel = input("Введите номер(a) (через пробел) To-Do task'a для удаления (099 в меню): ")
                if todel == "099":
                    break
                todel = int(todel)
                if todel < i:
                    tdlst = tdlst[:todel-1] + tdlst[todel:]
                    todoa = ""
                    for elem in tdlst:
                        todoa = todoa +"\n" + elem + "\n"
                    break
                else:
                    print("Неверный ввод!")
        if cmdd ==4:
            todof.close
            todof = open("todo.txt","w")
            todof.write("")
            exit()
        if cmdd ==99:
            todof.close
            todof = open("todo.txt","w")
            todof.write(todoa)
            exit()
if __name__ == '__main__':
    main()
