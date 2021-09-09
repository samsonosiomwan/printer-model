from data.data import *
class Printer:
    """this class holds template for format and resources attrbute, estimated resources(calculates resources to be used) and report"""
    color,greyscale = FORMAT['coloured']['materials']['ink'],FORMAT['greyscale']['materials']['ink']
    colored_price,greyscale_price = FORMAT['coloured']['price'], FORMAT['greyscale']['price']
    def __init__(self,no_of_pages = None, coloured = color, greyscale = greyscale, ink_resources = resources['ink'], paper_resources = resources['paper']):

        self.no_of_pages = no_of_pages
        self.ink_resources= ink_resources
        self.paper_resources = paper_resources
        self.coloured = coloured
        self.greyscale = greyscale
  
    def estimated_resources(self,resources):
        """method serves as template to calculate resources used for ink, it pass resources type as argument"""
        total_materials = self.no_of_pages * resources
        return total_materials

    def price_transaction(self,price_per_page):
        """method to calucate cost or print, multipies no of pages by the price per page"""
        printing_cost = self.no_of_pages * price_per_page
        return printing_cost

    def report(self): 
        """method returns the report of after printing is completed"""
        ink = resources['ink']
        paper = resources['paper']
        profit = resources['profit']
        resource = f'Ink Level: {ink}ml\nPaper Level:{paper}pc\nProfit:₦{profit}'
        return resource