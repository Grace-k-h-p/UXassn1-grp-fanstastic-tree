name=(input("Enter Name:"))
admin=(input("Enter Admin Number:"))
age=(input("Enter age"))
gender=(input("Enter Gender(male/female):"))
weight=float(input("Enter weight(kg):"))
height=float(input("Enter height(m):"))
bmi=weight/height**2

print("\n Hello!",name)
print("Your admin no is",admin,"age is",age)
print("your gender is %s and bmi is %.2f"%(gender,bmi))

score1=int(input("What is your score for Test 1:"))
weight1=float(input("What is weightage for Test 1:"))
score2=int(input("What is your score for Test 2:"))
weight2=float(input("What is weightage for Test 2:"))
score3=int(input("What is your score for Test 3:"))
weight3=float(input("What is weightage for Test 3:"))
exam=int(input("What is your scorce for Exam:"))


final=(weight1*(score1/100))+(weight2*(score2/100))+(weight3*(score3/100))+(exam/2)
print("your final scoree is",final)

string1=input("Enter string 1 (< 5 chars):")
string2=input("Enter string 2 (< 5 chars):")
print(f"\n{string1}\t{string2}\n{string2}\t{string1}\n")