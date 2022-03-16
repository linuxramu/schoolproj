from datetime import date, datetime

curr_date_time = datetime.now().strftime("%d%m%Y%H%M%S")

st_name = input("Please Enter Student Name : ")
att_date = input("Please Enter Date : ")
is_new_sheet = input("Do you want to create a new attandance sheet ? yes/no ")
if is_new_sheet=='yes':
    file_name = "new_file_" + curr_date_time + ".csv"
    f = open(file_name, 'w')
    f.write(st_name + "," + att_date )
    print (" *** Success ***")
    f.close()
else:
    is_existing_sheet = input("Do you want to write in existing in file ? yes/no ")
    if is_existing_sheet=='yes':
        existing_file_name_e = input("Please Exact Name of the File : ")
        f = open(existing_file_name_e, 'a')
        f.write("\n")
        f.write(st_name + "," + att_date )
        f.close()
        print (" *** Success ***")
    elif is_existing_sheet=='no':
        print (" *** Wrong Choice : Try again please *** ")
    else:
        print (" *** File not Found ! Thank you for using my application. Bye !!! ***")
