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