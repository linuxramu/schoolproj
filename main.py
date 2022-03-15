st_name = input("Please Enter Student Name : ")
att_date = input("Please Enter Date : ")
is_new_sheet = input("Do you want to create a new attandance sheet ? yes/no ")
if is_new_sheet=='yes':
    f = open("new_file.csv", 'w')
    f.write(st_name + "," + att_date )
    print (" *** Success ***")
    f.close()
else:
    is_existing_sheet = input("Do you want to write in existing in file ? yes/no ")
    if is_existing_sheet=='yes':
        file_name = input("Please Exact Name of the File : ")
        f = open(file_name, 'a')
        f.write("\n")
        f.write(st_name + "," + att_date )
        f.close()
        print (" *** Success ***")
    else:
        print (" *** File not Found ! Thank you for using my application. Bye !!! ***")
