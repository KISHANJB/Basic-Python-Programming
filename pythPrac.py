print("LEAP YEAR")
y=int(input("Enter the year:"))
if(y%4==0):
    print("This is a leap year")
else :
     print("Not a leap year")
    
print("Palindrome String")
s=input("Enter Your String: ")
if(s==s[::-1]):
     print("Palindrome string")
else:
     print("Not a Palindrome")

print("Armstrong No.")
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

   print("Alphabetical Order")
lis=["Kishan","Athul","Prakash"]
for i in range(len(lis)-1):
  for j in range(i+1,len(lis)):
    if(lis[i]>lis[j]):
      lis[i],lis[j]=lis[j],lis[i]
    
print(lis)


     


