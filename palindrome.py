n=-13
s_n=str(n)
revered_sn=s_n[::-1]
print(revered_sn)

if n<0:
    print("false")
elif n==0 or len(n)==1:
    print("true")
elif int(revered_sn)==n:
    print("true")
else:
    print("false")