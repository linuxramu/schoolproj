st_name = input("Please Enter Student Name : ")
att_date = input("Please Enter Date : ")
is_new_sheet = input("Do you want to create a new attandance sheet ? yes/no ")
f = open("new_file.csv", 'w')
f.write(st_name + "," + att_date )

