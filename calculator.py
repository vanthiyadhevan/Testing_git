# This testing comment test merge conflict
# Get first and second number
fnum = int(input("Enter The first_number:"))
snum = int(input("Enter The second_number:"))

# main function 
def cal(fnum,snum):
    add = fnum + snum
    sub = fnum - snum
    mul = fnum * snum
    div = fnum % snum
    print("Addition of:",fnum,"+",snum,"=",add)
    print("Subtraction of:",fnum,"-",snum,"=",sub)
    print("Multiplication of:",fnum,"*",snum,"=",mul)
    print("Division of:",fnum,"%",snum,"=",div)

while True:
    cal(fnum,snum)
    # Ask if the user wants to continue
    choice = input("Do You Want Perform the Action Again?")
    if choice != 'yes':
        break
    # allow the user to enter new numbers
    fnum = int(input("Enter The first number: "))
    snum = int(input("Enter The second number: "))




