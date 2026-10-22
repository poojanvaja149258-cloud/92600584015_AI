print("===============================================")
print("                  CAREER GUIDANCE SYSTEM                               ")
print("===============================================")

print("Answer the following question with yes or no.")
SU="Suggested Career :"
c =str(input("Do you like coding ?           : "))
m =str(input("Do you like mathematics ? : "))
b =str(input("Do you like biology ?          : "))
d =str(input("Do you like drawing ?         : "))
print("\n")
print("==============      Career Suggestion    ===============")

if c == "no" and m =="no" and b =="no" and d == "no":
    print(SU,"Explore your interests and career option further.")
elif  c == "no" and m =="no" and b =="no" and d == "yes":
    print(SU,"Grapgic Designer / Animator")
elif  c == "no" and m =="no" and b =="yes" and d == "no":
    print(SU,"Pharmacist / Nurse")
elif  c == "no" and m =="no" and b =="yes" and d == "yes":
    print(SU,"Medical illustrator / healthcare Educator")
elif  c == "no" and m =="yes" and b =="no" and d == "no":
    print(SU,"Engineer / Date Anlyst ")
elif  c == "no" and m =="yes" and b =="no" and d == "yes":
    print(SU,"Architect")
elif  c == "no" and m =="yes" and b =="yes" and d == "no":
    print(SU,"doctor")
elif  c == "no" and m =="yes" and b =="yes" and d == "yes":
    print(SU,"Suggested Career : Medical Illustrator / Biomedical Desginer")
elif  c == "yes" and m =="no" and b =="no" and d == "no":
    print(SU,"Programmer / Web Developer")
elif  c == "yes" and m =="no" and b =="no" and d == "yes":
    print(SU,"Web Designer / UI - UX Designer")
elif  c == "yes" and m =="no" and b =="yes" and d == "no":
    print(SU,"Health App Developer")
elif  c == "yes" and m =="no" and b =="yes" and d == "yes":
    print(SU,"Medical illustrator")
elif  c == "yes" and m =="yes" and b =="no" and d == "no":
    print(SU,"Software Engineer / Computer Scientist ")
elif  c == "yes" and m =="yes" and b =="no" and d == "yes":
    print(SU,"Game developer / UI Engineer ")
elif  c == "yes" and m =="yes" and b =="yes" and d == "no":
    print(SU,"Bioinformatics Scientist")
elif  c == "yes" and m =="yes" and b =="yes" and d == "yes":
    print(SU,"Biomedical Software Engineer / Medical Technology Specialist")
print("\n")
print("Thank you for using the career Guidance Expert System !")

