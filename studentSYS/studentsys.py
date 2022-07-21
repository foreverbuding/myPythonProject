# Author: Dawei Xu
# Version:
# CreateTime: 2022/7/18 23:55
import os.path

file_name = 'student.txt'


def mainEntry():
    while True:
        menu()
        choice = int(input("please choose:"))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                confirm = input("Are you sure to exit? y/n")
                if confirm == 'y' or confirm == 'Y':
                    print("Thank you!")
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()

# function menu shown to user
def menu():
    print("==================STUDENT INFORMATION MANAGEMENT SYSTEM===================")
    print('-------------------MENU------------------------')
    print('\t 1.ADD STUDENT INFORMATION')
    print('\t 2.SEARCH STUDENT INFORMATION')
    print('\t 3.DELETE STUDENT INFORMATION ')
    print('\t 4.CHANGE STUDENT INFORMATION')
    print('\t 5.SORT')
    print('\t 6.SHOW TOTAL STUDENT NUMBER')
    print('\t 7.SHOW ALL STUDENT INFORMATION')
    print('\t 0.EXIT')
    print('----------------------------------------------------')


# function to add student information
def insert():
    student_list = []
    while True:
        id = input('please input your id(ex:1001)')
        if not id:
            break
        name = input('please input your name')
        if not name:
            break
        try:
            English_score = int(input('please input english score'))
            Python_score = int(input('please input python score'))
        except:
            print('invalid input, please input a number')
            continue
        student = {'id': id, 'name': name, 'English': English_score, 'Python': Python_score}
        student_list.append(student)
        isContinue = input('continue to insert? y/n')
        if isContinue == 'y' or isContinue == 'Y':
            continue
        else:
            break
    save(student_list)


# function to save the list into file
def save(lst):
    try:
        student_txt = open(file_name, 'a')
    except:
        student_txt = open(file_name, 'w')
    for item in lst:
        student_txt.write(str(item) + '\n')
    student_txt.close()


# function to search student by ID or student name
def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(file_name):
            mode = input("input 1 to search by ID, input 2 to search by name")
            if mode == '1':
                id = input('please input student ID:')
            elif mode == '2':
                name = input('please input student name:')
            else:
                print('invalid input, please try again')
                search()
            with open(file_name, 'r') as read_file:
                student = read_file.readlines()
                for item in student:
                    temp_dict = dict(eval(item))
                    if id != '':
                        if temp_dict['id'] == id:
                            student_query.append(temp_dict)
                    if name != '':
                        if temp_dict['name'] == name:
                            student_query.append(temp_dict)
            show_result(student_query)
            student_query.clear()
            isContinue = input('continue to search? y/n\n')
            if isContinue == 'y' or isContinue == 'Y':
                continue
            else:
                break
        else:
            print('there is no student records')
            return


# function to format the print style of all record
def show_result(lst):
    if len(lst) == 0:
        print('there is no student record')
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^8}'
    print(format_title.format('ID', 'NAME', 'ENGLISH', 'PYTHON', 'TOTAL'))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('English'),
                                 item.get('Python'),
                                 int(item.get('English')) + int(item.get('Python'))))


# function to delete the student record by student ID
def delete():
    while True:
        student_old = []
        flag = False
        student_id = input('please input student ID you want to delete: ')
        if student_id != '':
            if os.path.exists(file_name):
                with open(file_name, 'r') as file:
                    student_old = file.readlines()
            ''' if student_old is not empty, then open the file in write way which will cover the 
                original file'''
            if student_old:
                with open(file_name, 'w') as write_file:
                    for item in student_old:
                        temp_dict = dict(eval(item))
                        # if the temp_dict id is not same with student_id to be deleted, then write to the file
                        if temp_dict['id'] != student_id:
                            write_file.write(str(temp_dict))
                        else:
                            flag = True
                    # flag to determine if the student is successfully deleted
                    if flag:
                        print(f'the student with id: {student_id} has been deleted')
                    else:
                        print(f'the student id: {student_id} does not exist')
            else:
                print('There is no student record')
                break
            show()
            isContinue = input('continue to delete? y/n')
            if isContinue == 'y' or isContinue == 'Y':
                continue
            else:
                break


# function to show total number of students restored
def total():
    if os.path.exists(file_name):
        with open(file_name, 'r') as read_file:
            students = read_file.readlines()
            if students:
                print(f'Total number of student is: {len(students)}')
            else:
                print('there is no record')
    else:
        print('there is no record')


# function to show all student records
def show():
    student_lst = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as read_file:
            students = read_file.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_result(student_lst)
            else:
                print('there is no student record')
    else:
        print('there is no record')


# function to sort in descend or ascend by English score. Python score or total score
def sort():
    show()
    if os.path.exists(file_name):
        with open(file_name, 'r') as read_file:
            student_list = read_file.readlines()
            student_new = []
            for item in student_list:
                temp_dict = dict(eval(item))
                student_new.append(temp_dict)
    else:
        return
    asc_or_desc = input('choose o to ascend, 1 to descend: ')
    if asc_or_desc == '0':
        # false means ascend
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        # true means descend
        asc_or_desc_bool = True

    else:
        print('invalid input, please try again')
        sort()
    mode = input("choose 1 to sort by English score, 2 by Python score, 3 by total score: ")
    if mode == '1':
        student_new.sort(key=lambda x: int(x['English']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['Python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['English']) + int(x['Python']), reverse=asc_or_desc_bool)
    else:
        input('invalid input, please retry')
        sort()
    show_result(student_new)


# function to modify student record by student ID
def modify():
    show()
    if os.path.exists(file_name):
        with open(file_name, 'r') as read_file:
            student_old = read_file.readlines()
    else:
        return
    student_id = input("please input student ID you want to modify:")
    with open(file_name, 'w') as write_file:
        for item in student_old:
            temp_dict = dict(eval(item))
            if temp_dict['id'] == student_id:
                while True:
                    try:
                        temp_dict['name'] = input("please input the name:")
                        temp_dict['English'] = input('please input English score')
                        temp_dict['Python'] = input('please input Python score')

                    except:
                        print('invalid input, please input again')
                    else:
                        break
                write_file.write(str(temp_dict) + '\n')
                print('modify succeed!!!!!')
            else:
                write_file.write(str(temp_dict) + '\n')

        isContinue = input('continue to modify other students? y/n ')
        if isContinue == 'y' or isContinue == 'Y':
            modify()


if __name__ == '__main__':
    mainEntry()
