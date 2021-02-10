#jump_n.py

n=int(input('Please enter jump number(2~9):'))
while n<=1 or n>=10:
    print('Out of range,try again')
    n=int(input('Please enter jump number(2~9):'))

for i in range(1,101):
    if i%n==0 or i%10==n or i//10==n:
        continue
    else:
        print(i)
