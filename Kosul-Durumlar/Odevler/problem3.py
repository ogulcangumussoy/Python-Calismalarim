

vize = float(input("Vize Notunuzu giriniz: "))
final = float(input("Final Notunuzu giriniz: "))

note = vize*0.3 + final*0.7

if(note >=90):
    print("AA")
elif(note >=85):
    print("BA")
elif(note >=80):
    print("BB")
elif(note >=75):
    print("CB")
elif(note >=70):
    print("CC")
elif(note >=65):
    print("DC")
elif(note>=60):
    print("DD")
else:
    print("FF")
