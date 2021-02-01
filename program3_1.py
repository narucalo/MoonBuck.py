
#pseudocode
#prompt user for the amount of roses and assign to variable
#assign discount for 1 dozen roses by multiply 'rose' variable to 1.39
#assign discount for 2 dozen roses by multiply 'rose' variable to 1.19
#assign discount for 3 dozen roses by multiply 'rose' variable to 0.89
#print for total 

def main():
    #prompt user for the amount
    rose = (int(input('How many roses would you like: ')))
    #the logic condition is set 
    if rose >1:
        total = rose + 1.69
    elif rose >=12:
        total = rose * 1.39 
    elif rose >=24:
        total = rose * 1.19
    elif rose >=36:
        total = rose * 0.89
    else:
         rose = 1.69

    

    print(f'Cost for rose:${total:.2f}')
   
main()
