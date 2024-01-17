_string=input("Enter a string:\n")
flag=1
palindrome=""
for char in _string:
    palindrome=palindrome+char

for i in (0,len(palindrome)-1):
    for j in (0,len(_string)-1):
        if palindrome[i]!=_string[j]:
            flag=0
            break

if flag==1:
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")
        
            