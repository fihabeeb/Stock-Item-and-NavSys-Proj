#Student ID:
#Creating the stock item class
class Stock_Item:
    #declaring a variable that stores the stock category
    item_Stock_Category = "Car accessories"

    #defining a constructor
    def __init__(self, stock_Code = "000A", stock_Quantity = 0, item_Price = 0.0):
        self.__stock_Code = stock_Code
        self.__stock_Quantity = stock_Quantity
        self.__item_Price = item_Price

    #Functions for setting and getting the stock code
    def set_Stock_Code(self, change_Value):
        self.__stock_Code = change_Value

    def get_Stock_Code(self):
        return self.__stock_Code

    #Functions for setting and getting the stock quantity
    def set_Stock_Quantity(self, change_Value):
        self.__stock_Quantity = change_Value

    def get_Stock_Quantity(self):
        return self.__stock_Quantity

    #Functions for setting and getting the item price
    def set_Item_Price(self, change_Value):
        self.__item_Price = change_Value

    def get_Item_Price(self):
        return self.__item_Price

    #Functions for getting the stock name
    def get_Stock_Name(self):
        return "Unknown Stock Name"

    #Functions for getting the stock description
    def get_Stock_Description(self):
        return "Unknown Stock Description"

    #Functions for increasing the stock price
    def increase_Stock(self, increase_Value: int):
        #Conditions and error handling of increasing the stock

        if (increase_Value <= 0):
            #Raises a value error if the increase value given by the user is 0 or less
            raise ValueError("Error: Cannot increase with a zero value")
        elif (self.__stock_Quantity > 100):
            #Raises a value error if the increase value given by the user is 100 or more
            raise ValueError("Error: Stock Quantity cannot go beyond 100")
        elif ((self.__stock_Quantity + increase_Value) > 100):
            #Raises a value error if the increasing the stock value by the amount the user gives
            #would make the stock value greater than 100
            raise ValueError("Error: Stock Quantity cannot go beyond 100")
        else:
            #Increases the stock if no conditional errors are present
            self.__stock_Quantity += increase_Value



    #Function to sell the stock
    def sell_Stock(self, decrease_Value: int):

        #Condition and error handling of stock selling
        if (decrease_Value >= 1):
            if (decrease_Value <= self.__stock_Quantity):
                self.__stock_Quantity -= decrease_Value
            else:
                return False
        else:
            #Raises an error if the user tries to decrease the stock value by zero
            raise ValueError("Error: Cannot decrease with a zero value")

    #Function that returns the VAT Value
    def get_VAT(self):
        return (17.5)

    #Function that sets the price value
    def set_Price(self, set_Value):
        self.__item_Price = set_Value

    #Functions that return the price value without or with the VAT applied respectively
    def get_Price_No_VAT(self):
        return self.__item_Price

    def get_Price_With_VAT(self):
        return round((self.__item_Price + self.get_VAT()), 2)

    #Function that prints out all the information of a stock item
    def __str__(self):
        return "Specifications of the Navigation system:" "\nStock Name:" + self.get_Stock_Name() + "\nStock Code: " + self.__stock_Code +"\nStock Description: " + self.get_Stock_Description() + "\nQuantity in stock: " + str(self.get_Stock_Quantity()) + "\nPrice Before VAT: " + str(self.get_Price_No_VAT()) + "\nPrice After VAT: " + str(self.get_Price_With_VAT())



#Creating the navigation system class as a child of the stock item class
class NavSys(Stock_Item):
    #The constructor
    def __init__(self, stock_Code="000A", stock_Quantity=0, item_Price=0, brand = None):
        #Overrides the constructor of the parent class
        super().__init__(stock_Code, stock_Quantity, item_Price)
        #Applies a value to the private variable "navSys_Brand"
        self.__navSys_Brand = brand

    #Function that overrides the parent "get_Stock_Name()" function and returns "Navigation System" instead
    def get_Stock_Name(self):
        return "Navigation System"

    #Function that overrides the parent "get_Stock_Description()" function and returns "GeoVision Sat Nav" instead
    def get_Stock_Description(self):
        return "GeoVision Sat Nav"

    #Overrides the parent class's "__str__()" function
    def __str__(self):
        return super().__str__() + "\nBrand: " + self.__navSys_Brand


#Code Example
test = NavSys("124B", 10, 20, "Nike")
print(test)
test.increase_Stock(10)
print(test)
test.sell_Stock(30)
print(test)