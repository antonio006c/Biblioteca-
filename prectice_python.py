#BLACK LIST OF NUMBERS 

#definición de conjuntos
list_of_numbers = set()


#First Question
while True:
    first_option = int(input("""
    what do you want to do ? please select an option \n
                             
    1- enter a new number to the list?
    2- delete number \n"""))

  ###MAIN PROGRAM###
    if first_option == 1:
        number_entered = int(input("enter the new number to the list: "))
        if number_entered in list_of_numbers:
            print("the number already exists in the list")
        else:
            list_of_numbers.add(number_entered)
            print("the number was added")
            print(list_of_numbers)

    elif first_option == 2:
        looking_for_number = int(input("enter the number you want to delete"))
        if looking_for_number in list_of_numbers:
            list_of_numbers.remove(looking_for_number)
            print("the number was deleted: ")
        else:    
            print("the number does not exist in the list")
            print(list_of_numbers)


# Descubriendo las funciones :: Aqui va a ir el código alternativo simplificado::



