#_______File Handling________#

#"a" Append open file for appending values, create file if not exists
#"r" read [Default value] open file for read and give error if file is not exists
#"w" write open file fo writing, create file if not exists
#"x" create create file, give error if file exists


#import os

#print(os.getcwd()) #cwd main current work directory
#print(os.path.dirname(os.path.abspath(__file__))) #directory for the opened file
#print(os.path.abspath(__file__)) #return abslute file path

#to change current working directory
#  os.chdir(os.path.dirname(os.path.abspath(__file__))) put the new path you want


# open("file", "mood")
#file = open("ahmed.txt")


# file handling (read file)
myFile = open("ahmed.txt","r")

print(myFile) # return data object <_io.TextIOWrapper name='ahmed.txt' mode='r' encoding='cp936'>
# to print each data object alone:
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)
print(myFile.read()) # to read the content of the file 
#you can select the limit of the chars you want it to read between the parentheses


print(myFile.readline()) # reads only one line and you can also give it limit
print(myFile.readlines()) # return llist i can also limit it 

#for line in myFile: print(line) i can also loop through the file 


#and at last we can close the file
myFile.close()

myfile = open("writing-file","w") # if file is not exists it will create it
myfile.write("hello my file from python\n")
myfile.write("Second line")
# you have to notice that write() delete what exists and write new data

myfile = open("fun.txt","w")
myfile.write("Ahmed is coding\n"*500)

mylist  = ["Ahmed\n", "Saleh\n" ,"Hanan\n"]

myfile = open("Ahmed.txt","w")

myfile.writelines(mylist)

#append add without delete the exists content
myfile = open("Ahmed.txt","a")
myfile.write("hello my file from python\n")
myfile.write("Second line") 

#myfile.truncate(5) cut only five chars and delelte the rest
#print(myfile.tell())
#myfile.seek(11)
#print(myfile.read())
