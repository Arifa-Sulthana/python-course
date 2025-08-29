n=120
s_n=str(n)
revered_sn=s_n[::-1]
print(revered_sn)

if int(revered_sn)==n:
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome")
