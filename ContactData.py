import csv


with open('contact_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

contact = "contact_data.csv"
#contact_data = ['id','name','email','gender','dob','address','mobile']

def display_data():
   # print("----Contacts Record----")
    with open('contact_data.csv', mode="r") as csv_file:
      reader = csv.reader(csv_file) 

      for item in reader:
      #  print("......................................................................................................")
       print(item)
    input("\n""Press Enter To Continue")    

def add_data():
   
    print("Add Contact Details")
    contact_data=[]
    for field in contact_data:
        value = input("Enter " + field +": ")
        contact_data.append(value)   
      
    input("\n""Contact Added Successfully")    
       
def delete_data():
    print("-------------------------")
    updatedlist=[]
    with open("contact_data.csv",newline="") as f:
      reader=csv.reader(f)

      id=input("Enter the ID of Contact to Delete : ")
      contactid= False
      for row in reader:            
                if row[0]!=id: 

                    updatedlist.append(row)
                else:
                    contactid=True
      if contactid is True:
          updatefile(updatedlist)
      else:
          print("\n""ID Not Found")    
         
    
      input("\n""Press Continue")                 
    

def updatefile(updatedlist):
    with open("contact_data.csv","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(updatedlist)
        print("\n""Deleted")

    
while True:
   
    print("1. List Contacts")
    print("2. Add Contact")
    print("3. Delete Contact")
    print("4. Exit")
    print("Enter Number :- ")
    val = int(input())
    if val == 1:
        display_data()
    elif val == 2:
       add_data()
    elif val == 3:
        delete_data()
    elif val==4:
        exit()
       
        break
    else:
        print("Entered Invalid details data")

