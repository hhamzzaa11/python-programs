#Create a program to generate the table of any number

number = int(input('Enter any number to generate its table.'))

for i in range (1, 11):
    print(number,'*',i,'=',number * i)

