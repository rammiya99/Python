class multiplefunctions():
    def Subfields():
        list=("Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing")
        print("Sub-fields in AI are:")
        for x in list:
            print(x)
    def OddEven():
        num = int(input("Enter the number"))
        if(num%2==0):
            print(num,"is Even number")
        else:
            print(num,"is odd number")
    def Elegible():
        gender = input("your Gender: ")
        age    = int(input("your age:"))
        if(gender=='Male' and age>=21) | (gender=='Female' and age>=18):
            print("Eligible")
        else:
            print("Not Eligible")        
    def Findper():
        sub1 = int(input("Subject1= "))
        sub2 = int(input("Subject2= "))
        sub3 = int(input("Subject3= "))
        sub4 = int(input("Subject4= "))
        sub5 = int(input("Subject5= "))
        Tot  = sub1+sub2+sub3+sub4+sub5
        print("Total:",Tot)
        per = Tot/5
        print("Percentage:",per)
    def Triangle():
        h = int(input("Height: "))
        b1 = int(input("Breadth: "))
        Area = (h*b1)/2
        print("Area of Triangle:",Area)
        h1 = int(input("Height1: "))
        h2 = int(input("Height2: "))
        b2 = int(input("Breadth: "))
        Peri = h1+h2+b2
        print("Perimeter formula: Height1+Height2+Breadth",)
        print("Perimeter of Triangle:", Peri) 
