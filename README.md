# Stock-Item-and-NavSys-Proj

## Project Description
This project was the first one we had in the first year of our degree.

The task was not very challenging, its to create 2 classes in python, a class for general stock items in a store, and then a child class from that specifically for a Navigation System item also sold in the store.


## Stock Item Class
The ```Stock_Item``` class serves as the base class for managing inventory items. It includes:
    -   Attributes to track stock code, quantity, and price.
    -   Methods for:
        -   Setting and getting stock details.
        -   Managing stock quantities (e.g., increasing and selling stock).
        -   Calculating prices with and without VAT.
        -   Error handling to ensure valid stock operations.


## NavSys Class
The ```NavSys``` class extends ```Stock_Item```, representing a specific stock item: a navigation system. It overrides base class methods to:
    -   Provide a specialized stock name and description.
    -   Add an attribute for the navigation system's brand.


## Other features
```NavSys``` uses encapsulation in the form of getters and setter methods, and private attributes.
It also has a ```__str__``` method to display detailed information about each object.

```NavSys``` extends from ```Stock_Item``` but overrides the ```get_Stock_Name``` and ```get_Stock_Description``` methods to return "Navigation System" and "GeoVision Sat Nav" respectively. It also extends t;he ```__str__``` method to display additional information that's specific to Navigation Systems.


## Skills Demonstrated

-   Object-Oriented Programming: Design and implementation of parent-child class relationships.

-   Error Handling: Validation of input values with conditional checks.

-   Practical Applications: Simulating real-world scenarios (e.g., managing inventory systems).


## UML and Testing

Featured also in this repo is some UML and testing done as part of the assessment.
In the file ```UML and Testing.pdf``` you will find 2 UML class diagrams, one for each class.

The UML diagrams show all the methods and attributes in both classes, completed with typing definitions as well as an arrow from parent to child showing inheritance.

There are some issues with the UML, such as the inheritance arrow pointing in the opposite direction. I have left those errors in the file for future reference when proving my progress.


There are a good number of test cases provided. Each function was tested and met the expected output, but they don't meet all requirements. The test cases failed to test the boundaries of the functions, meaning that logic errors can happen when values not intended during design are inputted.


## Improvements

Use one consistent naming convention. Here I use both camelCase and snake_case which is not necessary and makes writing the code take a little longer.

Better UML:
-   Fix present errors in the UML.
-   Make the diagrams smaller so they fit in one page.