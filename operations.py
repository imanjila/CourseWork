class Property:
    def __init__(self, kittaNumber: int, location: str, direction: str, anna: int, price: float, status: str):
         self.kittaNumber = kittaNumber #initializing/ setting the value of an instance variable
         self.location = location
         self.direction = direction
         self.anna = anna
         self.price = price
         self.status = status
         
    def __repr__(self):
        return f"Property( \nkittaNumber={self.kittaNumber}, \nlocation='{self.location}', \ndirection='{self.direction}', \nanna='{self.anna}', \nprice='{self.price}', \nstatus='{self.status}'\n)"
    