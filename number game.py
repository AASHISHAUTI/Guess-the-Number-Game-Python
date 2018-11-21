print("\n\n\t\t\t******************************************************************")
print("\t\t\t||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||The Brainthinker Game |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("\t\t\t******************************************************************")
from random import randint

a=input('''
\n\t\t*$*$*$*$*$*$*$* WELCOME TO THE BRAINTHINKER GAME Developed By- Aashish Auti *$*$*$*$*$*$*$*
\n\n\n press 1 if YES  & press 0 for NO.\n''')
a=int(a)
if a==1:
    print('''
          |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                 Choose Any Number.
          |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
     '''
          )
else:
    print("\n\nChoose at least Number for playing Game.")

b=input("\n\n If you choose the number then,press 1 Or 0 for Next Process.\n")
b=int(b)
if b==1:
    print('''
          |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                Now double this Number.
          |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'''
          )
else:
    print("\n\nIf you choose the number ,then double it.")




c=input("\n\nIf you Double the number then,press 1 Or 0 for Next Process.\n")
c=int(c)
if c==1:
    choose=randint(1,100)


    print('''
            ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                  Now Add this Number in your value.
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
\n''',choose)
else:
    print("\n\n If you Double the number ,then add these number in your value.")



d=input("\n\nIf you Add the number then,press 1 Or 0 for Next Process.\n")
d=int(d)
if d==1:
   print('''
            ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                    Now divide this Number by 2.
            ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
''')
else:
    print("\n\nIf you add the number ,then divide by 2.")


e=input("\n\n If you Divide  the number by 2 then,press 1 Or 0 for Next Process.\n")
e=int(e)
if e==1:
    print('''
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                        Now Subtract your choose  Number by Given Value.
            ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                ''')
else:
    print("If you Divide the number by 2 ,then Subtract the choosen Number.")

f=input("\n\nIf you Subtract  the number then,press 1 Or 0 for Next Process.\n")
f=int(f)
if f==1:
    f=choose/2
    print('''
************************************
This is your Answer.'''
          )
    print(f)
    print("************************************")
    
else:
    print("\n\nI think this the answer.")



input("\n\nPress the Enter key to exit.")


print("\n\n\t\t\t******************************************************************")
print("\t\t\t|||||||||||||||||||||||||||||||||||||||||||||||||||THANK YOU FOR PLAYING GAME ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("\t\t\t\tDeveloped By  Aashish Auti - Python Programmer")
print("\t\t\t******************************************************************")



