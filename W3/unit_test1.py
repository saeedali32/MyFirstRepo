
#CAITLAND WAS HERE

def add_two_num_together(num1, num2):
    return num1 + num2


def test_add_two_num_success():
#Arrange
    num1 = 10
    num2 = 5
    expected = 15

#Act
    actual = add_two_num_together(num1, num2)

#Assert
    assert expected == actual 

test_add_two_num_success()



def add_people(new_name,people_list):

   # new_name = input("Please enter new name: ")
    people_list.append(new_name)
    return print(f'"{new_name}" has been added')

#people_list = []

#add_people("Saeed",people_list)

#print(people_list)

def add_people_test():
#Arrange
    apple = []
    new_name = "Saeed"
    expected = apple + [new_name]

#Act
    add_people(new_name,apple)

#Assert
    assert expected == apple

add_people_test()

