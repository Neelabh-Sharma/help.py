"""
In this project we are going to create a timer quiz using python and also we are going to show the result
This project created by Neelabh sharma!
let's began:
"""

#importing time module for using its elements
import time

#this function use for taking basic user details
def user_details():
    global Name #for using in different function
    global id
    Name=input("Enter your name\t:")#user name
    id=int(input("Enter your id\t:"))#user id
    #a set of basic instruction for user
    print("1)Please Enter your answer in capital letter\n2)Please becarefull while answering\n3)You have 10 second for "
          "every Question to answered")
    print("____________________________________lets start_______________________________________________________!")


#we have define a function for checking the data from user is correct or not
def Answer_checking(userinput):
    a = 0
    b = 0
    c = 0
 #list contain all correct answer
    Anskey = ["C", "A", "A", "D", "A"]
    for i in userinput:#logic for answer checking
        if i in Anskey[c]:#camparing user input and anskey data for every position
            a += 1 #increment marks
        else:
            b += 1 #increment wrong ans
        c += 1#condition for every position
    print("___________________________________________________________________________________________!")
    print("Name:",Name,"\t ID",id)
    print("Your score is \t:", a)
    print("Wrong Answered\t:", b)


#It is the main function
def Main():
    #User detail function called here
    user_details()
    #listQ contain all the question in it and Option also in it
    listQ = [
        "Q1)What is the Name of python developer\n A)Neelabh \t\tB)Aakash \n C)Guido van Rossum \t D)None of the above"
        , "Q2)What is python \n A)Computer programming language \t B)Language\n C)snake \t\t\t D)None of the above",
        "Q3)What is C++ \n A)Computer programming language \t B)Language\n C)snake \t\t\t D)None of the above",
        "Q4)What is string \n A)Computer programming language \t B)Language\n C)snake \t\t\t D)None of the above",
        "Q5)What is xml \n A)Computer programming language \t B)Language\n C)snake \t\t\t D)None of the above"]

    #userinput is a empty list to take user input
    userinput = []



    #this is a for loop use for ask and taking input from user side
    for i in listQ: #we are going into listQ one by one using i

        print("Please enter the option in capital letters!") #user need to put the input in cap
        print(i) #print element of listQ
        userinput.append(input("Enter the Answer>"))#taking User input in list and storing that data
        time.sleep(10)
    Answer_checking(userinput) #now we are passing the element of userinput into function for checking answer


#we are use if condition for checking its is a main function or not
if __name__=="__main__":#if it is then program are going to excute
    Main()