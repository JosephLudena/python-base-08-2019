def menu():
    print('******MENU******')
    print('1.- Создать имя списка ')
    print('2.- Ввод с клавиатуры')
    print('3.- Поиск по каталогу')
    print('4.- Редактировать список')
    print('5.- Показать список')
    print('6.- Выход')
    print()
 
def menu2():
    print('a.- Поиск по имени')
    print('b.- поиск по телефон')
    print('c.- Поиск по адресу')
 
def menu3():
    print("Редактировать список")
    print('1.- Удалить контакт')
    print('2.- Изменить контакт')
 
directorio = []
telefonos = {}
nombres = {}
direcciones = {}
apodos = {}
opcionmenu = 0
menu()
x=0
while opcionmenu != 6:
    opcionmenu = int(input("Введите число, чтобы выбрать вариант: "))
    if opcionmenu == 1:
        print('Введите название списка: ')
        nombre_de_lista=input()
        menu()
 
 
    elif opcionmenu == 2:
        print("Добавить имя, телефон, адрес")
        nombre = input("Имя: ")
        telefono = input("Телефон: ")
        direccion = input("Адрес: ")
        telefonos[nombre] = telefono
        nombres[telefono] = nombre
        direcciones[direccion] = nombre
        directorio.append([nombre, telefono, direccion,])
        menu()
 
    elif opcionmenu == 3:
        print("поиск")
        menu2()
        opcionmenu2 = input("Вставьте номер, чтобы выбрать вариант: ")
        if opcionmenu2=="a":
            nombre = input("Имя: ")
            if nombre in telefonos:
                print("Телефои это", telefonos[nombre])
            else:
                print(nombre, "не найден")
 
        if opcionmenu2=="b":
            telefono = input("Tелефон: ")
            if telefono in nombres:
                print("Имя это", nombres[telefono])
            else:
                print(telefono, "не найден")
 
        if opcionmenu2=="c":
            direccion = input("адрес: ")
            for linea in direcciones:
                linea = linea.rstrip()
                if not linea.startswith(direccion) : continue
                palabras = linea.split()
                print()
            else:
                print(direccion, "не найден")
        menu()
    elif opcionmenu == 4:
        menu3()
        opcionmenu3 = input("введите номер, чтобы выбрать вариант: ")
        if opcionmenu3=="1":
            nombre = input("Имя: ")
            if nombre in directorio[0:10]:
                print('удалённый')
            else:
                print(nombre, "не найден")
        else:
            menu()
        menu()
 
    elif opcionmenu == 5:
 
        print("\nНазвание списка: ",nombre_de_lista)
        for e in directorio:
            print("\nСписок: ",directorio)
        menu()
 
 
    elif opcionmenu != 6:
        menu()
