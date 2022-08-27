banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
students_file = open("nav.html", "w")
for student in banks_list:
    students_file.write("" + student + "\n")
students_file.write("\n")
students_file.close()