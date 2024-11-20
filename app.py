qual=(input("Write your Qualification:")).lower()
yos=eval(input("Enter your years of service:")) 
if qual=="masters" and yos>=10:
    print("Your salary is 150,000")
elif qual=="bachelors" and yos>=10:
    print("Your salary is 100,000")
elif qual=="masters" and yos<10:
    print("Your salary is 100,000")
elif qual=="bachelors" and yos<10:
    print("Your salary is 70,000")
else:
    print("You are not Eligible")