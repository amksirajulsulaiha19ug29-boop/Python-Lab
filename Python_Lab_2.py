#DAY 2
#Task 1

passenger_name = "Rahul Sharma"
passenger_age = 28
gender = "Male"
mobile_number = 9876543210

#print("Passenger Name:", passenger_name)
#print("Passenger Age:", passenger_age)
#print("Gender:", gender)
#print("Mobile Number:", mobile_number)


#Task 2

train_name = "Rajdhani Express"
seat_number = "B2-45"
ticket_price = 2450
journey_date = "25-May-2026"

#print("Train Nmae:", train_name)
#print("Seat Number:", seat_number)
#print("Ticket Price:", ticket_price)
#print("Journey Date:", journey_date)


#Task 3

number_of_passengers = 3
ticket_price = 2450

total_fare = number_of_passengers * ticket_price

#print("Total Fare:", total_fare)


#Task 4
gst_percentage = 5

gst_amount = (total_fare * gst_percentage)/100
#print("GST Amount:" , gst_amount)

final_amount = total_fare + gst_amount
#print("Final Payable amount:", final_amount)


#Task 5
print("-------------Indian Railway Ticket--------------")
print("Passenger Name\t:" , passenger_name)
print("Train Name\t:", train_name)
print("Seat Number\t:", seat_number)
print("Journey Date\t:", journey_date)
print("Passengers\t:", number_of_passengers)
print("Total Fare\t:", total_fare)
print("GST Amount\t:" , gst_amount)
print("Final Payable amount\t:", final_amount)
print("------------------------------------------------")


