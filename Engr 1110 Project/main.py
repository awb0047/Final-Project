#imports
import pickle
import os

#Class Arrays
class1 = []
class2 = []
class3 = []
class4 = []
classes = [class1, class2, class3, class4]

#Gets File Location
dir_path = os.path.dirname(os.path.realpath(__file__))
fileLocation = str(dir_path) + "\dist\main\Data"

#Functions
def addName(nameIn, classInputIn):
   if classInputIn == 1:
      class1.append(nameIn)
   elif classInputIn == 2:
      class2.append(nameIn)
   elif classInputIn == 3:
      class3.append(nameIn)
   elif classInputIn == 4:
      class4.append(nameIn)
   else:
      print("Please enter a valid Class (1-4)")
      print("-----Press r to restart-----")
      restartKey = input()
      if restartKey == "r":
         addMenu()
   mainMenu()
    
def addMenu():
   print("Please Enter the First Name")
   firstName = input()
   print("Please Enter the Last Name")
   lastName = input()
   name = firstName + " " + lastName
   print("What Class would you like to add the student too?")
   classInput = int(input())
   addName(name, classInput)
    
def printClasses():
   #Class 1
   print("Class 1: ", end = '')
   print(', '.join(class1))
   #Class 2
   print("Class 2: ", end = '')
   print(', '.join(class2))
   #Class 3
   print("Class 3: ", end = '')
   print(', '.join(class3))
   #Class 4
   print("Class 4: ", end = '')
   print(', '.join(class4))
   #Menu Options
   print("\n\nReturn to main menu. 1")
   print("Quit Program. 2")
   exitCase = True
   while exitCase == True:
      inputValue = int(input())
      if inputValue != 1 or inputValue != 2:
         exitCase == True
      if inputValue == 1:
         mainMenu()
         break
      if inputValue == 2:
         quitProgram()
         break
         
def editClassMenu():
   print("Which class would you like to edit?")
   exitCase = True
   while exitCase == True:
      inputValue = int(input())
      if inputValue == 1 or inputValue == 2 or inputValue == 3 or inputValue == 4:
         editClass(inputValue)
         break
      else:
         print("Please enter valid class")
      
def editClass(classNumIn):
   classNum = classNumIn - 1
   print("Class ", classNumIn, ": ", end = '')
   print(', '.join(classes[classNum]), "\n")
   print("What would you like to do?")
   print("1. Edit Name")
   print("2. Delete Name")
   print("3. Return to Main Menu")
   exitCase = True
   while exitCase == True:
      inputValue = int(input())
      if inputValue != 1 or inputValue != 2 or inputValue != 3:
         print("Please enter valid option")
      if inputValue == 1:
         editName(classNum)
         break
      if inputValue == 2:
         deleteName(classNum)
         break
      if inputValue == 3:
         mainMenu()
         break
         
def editName(classNumIn):
   print("Which name would you like to edit?")
   nameInput = input()
   index = classes[classNumIn].index(nameInput) 
   if nameInput in classes[classNumIn]:
      print("Please Enter the new first name")
      newFirst = input()
      print("Please Enter the new last naem")
      newLast = input()
      newName = newFirst + " " + newLast
      classes[classNumIn][index] = newName
      print("Class ", classNumIn + 1, ": ", classes[classNumIn], "\n")
   else:
      print("Name not found")
   print("\n\nReturn to main menu. 1")
   print("Quit Program. 2")
   exitCase = True
   while exitCase == True:
      inputValue = int(input())
      if inputValue != 1 or inputValue != 2:
         exitCase == True
      if inputValue == 1:
         mainMenu()
         break
      if inputValue == 2:
         quitProgram()
         break
   

def deleteName(classNumIn):
   print("Which name would you like to delete?")
   nameInput = input()
   if nameInput in classes[classNumIn]:
      classes[classNumIn].remove(nameInput)
      print("Deleted!")
   elif nameInput not in classes[classNumIn]:
      print("Name not found")
   print("\n\nReturn to main menu. 1")
   print("Quit Program. 2")
   exitCase = True
   while exitCase == True:
      inputValue = int(input())
      if inputValue != 1 or inputValue != 2:
         exitCase == True
      if inputValue == 1:
         mainMenu()
         break
      if inputValue == 2:
         quitProgram()
         break

def quitProgram():
    print("Goodbye!")
    print("----------------------------------------------------------")

def searchName():
   print("What name would you like to look for?")
   nameSearched = input()
   for num in classes:
      for names in num:
         if str(names) == str(nameSearched):
            print(str(names) + " is in class", classes.index(num) + 1)
         else:
            print("Name Not Found")
   print("\n\nReturn to main menu. 1")
   print("Quit Program. 2")
   exitCase = True
   while exitCase == True:
      inputValue = int(input())
      if inputValue != 1 or inputValue != 2:
         exitCase == True
      if inputValue == 1:
         mainMenu()
         break
      if inputValue == 2:
         quitProgram()
         break
      
def saveData():
    pickle.dump(class1, open(fileLocation+"\class1.dat", "wb"))
    pickle.dump(class2, open(fileLocation+"\class2.dat", "wb"))
    pickle.dump(class3, open(fileLocation+"\class3.dat", "wb"))
    pickle.dump(class4, open(fileLocation+"\class4.dat", "wb"))
    print("Data Saved!")
    mainMenu()
    
def mainMenu():
   print("----------------------------------------------------------")
   print("Welcome to StudentIO! What would you like to do?")
   print("1. Add name")
   print("2. View Class")
   print("3. Edit Class")
   print("4. Search For Name")
   print("5. Save Data")
   print("6. Quit")
   print("----------------------------------------------------------")
   optionIn = int(input())
   if optionIn == 1:
      addMenu()
   if optionIn == 2:
      printClasses()
   if optionIn == 3:
      editClassMenu()
   if optionIn == 4:
      searchName()
   if optionIn == 5:
      saveData()
   if optionIn == 6:
      quitProgram()

def loadData():
   global class1
   global class2
   global class3
   global class4
   global classes
   class1 = pickle.load(open(fileLocation+"\class1.dat", "rb"))
   class2 = pickle.load(open(fileLocation+"\class2.dat", "rb"))
   class3 = pickle.load(open(fileLocation+"\class3.dat", "rb"))
   class4 = pickle.load(open(fileLocation+"\class4.dat", "rb"))
   classes = [class1, class2, class3, class4]
   

#Start
loadData()
mainMenu()
