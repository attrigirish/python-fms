#Flight Management


import dl
from flight import Flight
from booking import Booking
from user import User

def AddFlight(userid):
        flightno=int(input("Enter Flight Number : "))
        name=input("Enter Flight Name : ")
        source=input("Enter Source : ")
        destination=input("Enter Destination : ")
        fare=float(input("Enter Fare : "))
        print("Enter 1 for Availability and 0 for Unavailability")
        availability=""
        
        availability+=input("Sunday : ") + ","
        availability+=input("Monday : ") + ","
        availability+=input("Tuesday : ") + ","
        availability+=input("Wednesday : ") + ","
        availability+=input("Thursday : ") + ","
        availability+=input("Friday : ") + ","
        availability+=input("Saturday : ")

        flight=Flight(flightno,name,source,destination,fare,availability)
        
        if(dl.SaveFlight(flight)>0):
            print("Record Saved Successfully")
        else:
            print("Failed!")


def SearchFlight():
    flightno=int(input("Enter Flight Number : "))
    flight=dl.GetFlightDetail(flightno)
    if(flight!=None):
        print("Flight Number : " + str(flight.GetFlightNo()))
        print("Name : " + flight.GetName())
        print("Source : " + flight.GetSource())
        print("Destination : " + flight.GetDestination())
        print("Fare : " + str(flight.GetFare()))
    else:
        print("No Record Found")


def DeleteFlight():
    flightno=int(input("Enter Flight Number : "))
    if(dl.DeleteFlight(flightno)>0):
        print("Record Deleted Successfully")
    else:
        print("Record Not Found")


def UpdateFlightName():
    flightno=int(input("Enter Flight Number : "))
    name=input("Enter Flight Name : ")
    if(dl.UpdateFlightName(flightno,name)>0):
        print("Record Updated Successfully")
    else:
        print("Record Not Found")


        
def FlightMenu():
    print("1. Add New Flight")
    print("2. Update Flight Name")
    print("3. Update Flight Source")
    print("4. Update Flight Destination")
    print("5. Update Flight Fare")
    print("6. Update Flight Availability")
    print("7. Delete Flight")
    print("8. Search Flight")
    print("9. Print Flight Details")
    print("10. Check Booked Flights")
    print("11. Check Cancelled Flights")
    print("12. Update Profile")
    print("0. Exit")

    option=int(input("Enter Choice : "))

    if(option==1):
        AddFlight()
    elif(option==2):
        UpdateFlightName()
    elif(option==7):
        DeleteFlight()
    elif(option==8):
        SearchFlight()
    elif(option==0):
        return False
    return True


#Booking Module

def AddBooking(userid):    
    source=input("Enter Source Location : ")
    destination=input("Enter Destination Location : ")
    flights=list(filter(lambda x: x.GetSource()==source and x.GetDestination()==destination, dl.GetFlightDetails()))

    print("Available Flights from ",source," to ",destination," are:")
    print()
    print("Flight No.\t\tName\t\tSource\t\tDestination\t\tFare\t\tAvailability")
    print("-"*100)
    for flight in flights:
        print(flight.GetFlightNo(),end="\t\t\t")        
        print(flight.GetName(),end="\t\t")        
        print(flight.GetSource(),end="\t\t")        
        print(flight.GetDestination(),end="\t\t\t")        
        print(flight.GetFare(),end="\t\t")        
        availability=flight.GetAvailability().split(',')
        days=['S','M','T','W','T','F','S']
        for i in range(availability.__len__()):
            if(availability[i]=='1'):
                print(days[i],end=' ')



    bookingid=int(input("Enter Booking Id : "))
    flightno=int(input("Enter Flight Number : "))
    bookingdate=input("Enter Booking Date (Y-M-D) : ")

    booking=Booking(bookingid,userid,flightno,bookingdate)
    if(dl.SaveBooking(booking)):
        print("Flight Booked Successfull")
    else:
        print("Please Try Again!!")



def BookingMenu(userid):
    print("1. Book Flight")
    print("2. Check Your Bookings")
    print("3. Cancel Booking")
    print("4. Check Cancelled Bookings")
    print("5. Update Profile")
    print("0. Exit")

    option=int(input("Enter Choice : "))

    if(option==1):
        AddBooking(userid)
    elif(option==2):
        DisplayBookings()
    elif(option==0):        
        return false
    
        



#USER

from user import User

def AddUser():
        userid=input("Enter User Id : ")
        name=input("Enter User Name : ")
        password=input("Enter Password : ")
        type=input("Enter Type (1: Admin, 0: User) : ")

        user=User(userid,name,password,type)
        
        if(dl.SaveUser(user)>0):
            print("Record Saved Successfully")
        else:
            print("Failed!")
    
def Login():
    userid=input("Enter User Id : ")
    password=input("Enter Password : ")
    user=dl.Login(userid,password)
    print(user.GetType())
    if(user!=None):
        if(user.GetType()=="1"):      #User is Admin
            while FlightMenu(userid.GetUserId()):
                pass
        else:                       #User is User
            while BookingMenu(userid.GetUserId()):
                pass
    else:
        print("Login Failed")


def UserMenu():
    print("1. Register")
    print("2. Login")
    print("0. Exit")

    option=int(input("Enter Choice : "))

    if(option==1):
        AddUser()
    elif(option==2):
        Login()
    elif(option==0):
        return false




#Main Program

while UserMenu():
    pass









