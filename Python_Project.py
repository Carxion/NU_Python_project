#Project: Strong Password Checker
#Names: Alexander Anicete, Shaun Turner, Erik Jewell, Jose Diaz, Dominick Bolanos
#Class: Programming for Cybersecurity 216 
#Instructor: Donald Smith
import re
print('Please enter prospective password. Include 16 characters, uppercase and lowercase letters, numbers, and special characters(!@#):')
def Agoodpassword():
     
            while True:
                strongpassword = input()
            
                uppercase = []  # uppercase
                lowercase = []  # lowercase
                number = []  # number
                specialcharacter = [] #special character

                if len(strongpassword) < 16:
                    print('Password must have 16 characters or more:')
                    return Agoodpassword() # We added the return function because we didnt want the prompt to close until the password was set

# This section of code is to make sure there is an uppercase

                uppercaseRegex = re.compile(r'[A-Z]')
                uppercase = uppercaseRegex.findall(strongpassword)
                if uppercase == []:
                    print('Yeah sorry, you will need an uppercase letter in there, buddy:')
                    return Agoodpassword()


 # This section is to make sure there is a lowercase

                lowercaseRegex = re.compile(r'[a-z]')
                lowercase = lowercaseRegex.search(strongpassword)
                if lowercase == []:
                    print('I do not seem to see a lowercase letter, try again:')
                    return Agoodpassword()

# This section is to make sure the user adds a number to the password
                numberRegex = re.compile('[0-9]')
                number = numberRegex.findall(strongpassword)
                if number == []:
                    print('Add a number silly goose!:')
                    return Agoodpassword()

 #This section is to make sure the user enters a special character

                specialcharacterregex = re.compile('[!@_#$%^&*()<>?/\|}{~:;]')
                specialcharacter = specialcharacterregex.findall(strongpassword)
                if specialcharacter == []:
                    print('you need a special character!:')
                    return Agoodpassword()                        

                else:
                    print('You did it buddy! Password looks good to me! ')
                    break
           

Agoodpassword()   

# This section was to add a little fun
print ("Is there anything else I can do for you?:") 

while True:

     messingwiththeuser: input()
     break

print("Just kidding, you're done, get outta here!")
