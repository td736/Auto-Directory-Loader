import os

## Static fields
line_marker = '*'
prj_names = "Project_Names.txt"
prj_data = "Project_Data.txt"

#Static fields end

#Dynamic fields
project_names = {}
project_directories = {}
last = '000'
#Dynamic fields end


names = open(prj_names, 'r')
for line in names.readlines():
    if line.startswith(line_marker):
        project_names[line[1:4]] = line[5:-1]
        project_directories[line[1:4]] = []
        last = line[1:4]
    
names.close()


directories = open(prj_data)
for line in directories.readlines():
    if line.startswith(line_marker):
        project_directories[line[1:4]].append(line[5:-1]) 



def open_project(project):

    if project_directories.__contains__(project):
        for path in project_directories[project]:
            os.startfile(path)

        
def make_project(name, number_of_directories):
    global last
    last = ("%03d" % (int(last) + 1))

    with open(prj_names, "a") as myfile:
        myfile.write("%s%s-%s\n" %(line_marker, last, name))
        project_names[last] = name
        project_directories[last] = []

    for directory in range(number_of_directories):
        
            with open(prj_data, "a") as myfile: 
                directory = input("Enter directory: ")
                myfile.write("%s%s-%s\n" %(line_marker, last, directory))
                project_directories[last].append(directory)
            
def clear_data():
    print("The saved projects are:\n " + str(project_names))
    if input("Type 'DEL' to delete: ") == 'DEL':
        open(prj_names, 'w').close()
        open(prj_data, 'w').close()

    

