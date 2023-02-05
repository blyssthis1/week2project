# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

class Parking_Garage:

    def __init__(self, tickets, parking_spaces):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {None: False}
    

    def Taketickets(self):
        if self.tickets == []:
            print("Garage is full!")
            return
        elif self.parking_spaces == []:
            print("Garage has no spaces available!")
            return

        elif self.tickets :
            ticket = self.tickets.pop()
            print(self.current_ticket)
            self.parking_spaces.pop()
            print(f'Available parking space now:---> {self.parking_spaces}')
            self.current_ticket[ticket] = False
            print(f'Your ticket number is: {ticket}. Enjoy your stay.')
        else:
            print("The parking lot is full.")
        
    

    def payForParking(self):
        ticket_no = int(input("Enter your ticket no:"))
        if ticket_no in self.current_ticket:
            if self.current_ticket[ticket_no] == False :
                payment = int(input("How much would you like to pay today?: "))
                if payment >= 1:
                    print("Thank you! Your ticket has been paid. You have 15 minutes to leave.")
                    self.current_ticket[ticket_no] = True
                else:
                    print("Invalid amount. Please try again.")
            else:
                print("Your ticket has been paid!")
        else:
            print("Enter a valid ticket number")
    

    def leave_garage(self):
        ticket_no = int(input("Enter your ticket no:"))
        if ticket_no in self.current_ticket:
            if self.current_ticket[ticket_no] == True:
                print("Thank you have a nice day!")
                self.tickets.append(ticket_no)
                self.parking_spaces.append(ticket_no)
            else:
                payment = int(input("How much would you like to pay today?: "))
                if payment >= 1:
                    print("Thank you! Your ticket has been paid. You have 15 minutes to leave.")
                    self.current_ticket[ticket_no] = True
                    self.tickets.append(ticket_no)
                    self.parking_spaces.append(ticket_no)
                else:
                    print("Invalid amount. Please try again.")
                    # self.leave_garage()
        else:
            print("Enter a valid ticket number")
        print(f'Available parking space now:---> {self.parking_spaces}')


    def main(self):
        while True:
            print("1. Take Ticket")
            print("2. Pay for Parking")
            print("3. Leave Garage")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.Taketickets()
            elif choice == 2:
                self.payForParking()
            elif choice == 3:
                self.leave_garage()
            else:
                print("Invalid choice")
                break
user= Parking_Garage(list(range(1,10)), list(range(1,10)))
user.main()