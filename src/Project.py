import os

class Project():


    def __init__(self, names_folder, data_folder):
        
        self.names_folder = names_folder
        self.data_folder = data_folder
        self.line_marker = '*'
        
        self.project_names = {}
        self.project_directories = {}
        self.last = '000'

        self.load_names()
        self.load_directories()


    def load_names(self):
        with open(self.names_folder, "r") as myfile:
            for line in myfile.readlines():
                if line.startswith(self.line_marker):
                    self.project_names[line[1:4]] = line[5:-1]
                    self.project_directories[line[1:4]] = []
                    self.last = line[1:4]
                    

    def load_directories(self):
        with open(self.data_folder, "r") as myfile:
            for line in myfile.readlines():
                if line.startswith(self.line_marker):
                    self.project_directories[line[1:4]].append(line[5:-1])


    def open_project(self, project):
        if self.project_directories.__contains__(project):
            for path in self.project_directories[project]:
                os.startfile(path)


    def make_project(self, name, number_of_directories):
        
        self.last = ("%03d" % (int(self.last) + 1))

        with open(self.names_folder, "a") as myfile:
            myfile.write("%s%s-%s\n" %(self.line_marker, self.last, name))
            self.project_names[self.last] = name
            self.project_directories[self.last] = []

        for directory in range(number_of_directories):
                with open(self.data_folder, "a") as myfile: 
                    directory = input("Enter directory: ")
                    myfile.write("%s%s-%s\n" %(self.line_marker, self.last, directory))
                    self.project_directories[self.last].append(directory)

                    
    def clear_data(self):
        print("The saved projects are:\n " + str(self.project_names))
        if input("Type 'DEL' to delete: ") == 'DEL':
            open(self.names_folder, 'w').close()
            open(self.data_folder, 'w').close()
            self.project_names = {}
            self.project_data = {}
            self.last = '000'





                    
