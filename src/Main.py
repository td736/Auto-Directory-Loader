import os
from Project import Project

names_folder = "Project_Names.txt"
data_folder = "Project_Data.txt"
page_break = "%s" % ('-'*30)

def run():
    project_loader = Project(names_folder, data_folder)

    while input("Press any key to continue or 'q' to quit: ") != 'q':

        print(page_break + "\nCurrent projects are: " + str(project_loader.project_names))
                
        menu_choice = input("\n1. Open project" +
                            "\n2. Make project" +
                            "\n3. Clear data\n"   +
                            page_break       +
                            "\nWhat would you like to do: ")
        
        if menu_choice == '1':
            project_loader.open_project(input(page_break +"\nEnter project ID: "))
            print(page_break)

        elif menu_choice == '2':
            project_loader.make_project(input(page_break + "\nName of project: "), int(input("Number of directories: ")))
            print(page_break)
            
        elif menu_choice == '3':
            print(page_break)
            project_loader.clear_data()
            print(page_break)

        elif menu_choice == 'q':
            break

        else:
            print("Command not recognised.")
            print(page_break)

if __name__ == '__main__':
    run()
