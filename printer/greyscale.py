from printer.printing_machine import *
class greyscale(Printer):
    """check availabilty of greyscale resources, checks for price,processes the recieved amount and updates resources"""
      
    def check_ink(self):
        """method to check both ink and paper resources"""
        ink_type = self.estimated_resources(self.greyscale)
        try:
            if (ink_type > self.ink_resources) or (self.no_of_pages > self.paper_resources):
                raise ValueError
            else:
                printing_cost = self.price_transaction(self.greyscale_price) 
                print (f'your price is N{printing_cost} \n +++++++++++++++++++++++++++++++++')
        except ValueError:
            return 'sorry there is no enough ink or papper'
        try:
            self.recieved_amount()
        except ValueError:
            print('invalid entry: numbers only')
        return 'processing payment............updating resource......complete(100%) \n\n +++++++++++++++++++++++++++++++++'
    
    def recieved_amount(self):
        """method to process the recived amount and return update on resources used and profit"""
        try:
            #price variable holding cost of print per page
            price = self.price_transaction(self.greyscale_price) 
            print('Please pay the printing cost')
            self.biyar = int(input('Enter Biyar: ')) * 5
            self.faiba = int(input('Enter Faiba: ')) * 10
            self.muri = int(input('Enter Muri: ')) * 20
            self.wazobia = int(input('Enter Wazobia: ')) * 50
            self.amount_recieved = self.biyar + self.faiba + self.muri + self.wazobia
            
            if self.amount_recieved < price:
                print('sorry that\'s not enough money: money rufunded')
            elif self.amount_recieved == price:
                print("your money has been recieved \n\n +++++++++++++++++++++++++++++++++")
                return self.resource_update()
            elif self.amount_recieved > price:
                customers_change = self.amount_recieved - price
                self.profit_recieved = self.amount_recieved - customers_change
                print(f'you paid: {self.amount_recieved}')
                print(f'here is your balance N{customers_change} in change \n\n +++++++++++++++++++++++++++++++++')
                return self.resource_update()
        except ValueError:
            print('invalid entry: numbers only')
    
    def resource_update(self):
        """method to hold greyscale resource and profit update returned after calculate recieved payement"""
        resources['ink'] = self.ink_resources - self.estimated_resources(self.greyscale)
        resources['paper'] = self.paper_resources - self.no_of_pages
        resources['profit'] = self.profit_recieved