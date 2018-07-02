import os

os.mkdir("Quiz_E6/DNA")
os.mkdir("Quiz_E6/Prot")

for file_name in os.listdir("Quiz_E6"):
    #print(file_name.find(".seq"))
    if file_name.find(".seq") == 1:
        #print(file_name)
        #print()
        file_content = open("Quiz_E6/" + file_name)
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
        #print("Quiz_E6/" + file_name ,len(file_component))
        if len(file_component) != 0:
            os.rename("Quiz_E6/" + file_name , "Quiz_E6/Prot/" + file_name)
        else:
            os.rename("Quiz_E6/" + file_name , "Quiz_E6/DNA/" + file_name)