class car:  
   
  def_init_(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

 
def get_descriptive_name(self):
    """Return a neatly formated describe name."""
    long_name = f"{self.make} {self.model}" 
    return long_name.title()

class truck (car):

   def setName(self, name):
       self.truck_name = name

   def displayOption(self):
       print(f" The bed length is: {self.bed_length}")

inputBed_length = input("Please enter your bed lenght:")
input_car = input("Please inter what kind of  )