import os

os.mkdir("Homework_E10/DNA")
os.mkdir("Homework_E10/Prot")

for file_name in os.listdir("Homework_E10"):
    #print(file_name.find(".seq"))
    if file_name.find(".seq") == 1:
        #print(file_name)
        #print()
        file_content = open("Homework_E10/" + file_name)
        file_component = file_content.read()
        file_content.close()

        file_component = file_component.rstrip()
        file_component = file_component.rstrip("\n")
        #print(file_component)
        file_component = file_component.replace("A" , "")
        file_component = file_component.replace("T" , "")
        file_component = file_component.replace("C" , "")
        file_component = file_component.replace("G" , "")
        #print(file_component)
        #print("Homework_E10/" + file_name ,len(file_component))
        if len(file_component) != 0:
            os.rename("Homework_E10/" + file_name , "Homework_E10/Prot/" + file_name)
        else:
            os.rename("Homework_E10/" + file_name , "Homework_E10/DNA/" + file_name)