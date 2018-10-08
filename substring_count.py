

string1="aaabbabbab"
string2="aabbabbbaaaababaaab"

substring="ab"

print("The number of", substring,"present in ", string1," is",string1.count('ab'),"and in",string2," is",string2.count('ab'))

#User input
#infinite loop
while(1):
    check=input("Do you want to check more?(yes/no)")

    if check=='yes':
        string=input("Enter the string: ")
        sub=input('Enter the substring: ')

        cou=string.count(sub)

        print("The number of", sub,"present in ",string ,"is ",cou)
    
    elif check=='no':
        print("It's ok")
        break

    else:
        print("Please enter the correct input")
    
    
    



