class convert:
    def __init__(self):
        # self.conversionType = int(input("Press 1 to convert to Miles to Km or Press 2 to convert to KM to miles: "))
        # self.amountValue = int(input("Enter the amount of values you want to convert: "))
        # self.DeleteStatus = int(input("Press 3 if you want to delete a saved value or press 4 to move on "))
        # self.ValuetoDelete = int(input("Enter the number of values youd like to delete "))
        # self.miles = miles
        # self.km = km
        # self.j = 1
        # self.e = 1
        self.convert = "conversion"
        
   
    def convert_km(self, miles):
        km = miles * 1.6
        print(miles, "in Km = ", km)
        # return(km)
         
    def convert_miles(self, km):
        miles = km * 0.621371
        print(km, "in Miles = ", miles)
        # return(miles)
    

savedValues = []
# Create a Convert object
convert_value = convert()


# Prompt user for input.
ConversiontType = int(input("""Press 1 if you'll like to convert from KG to Grams or
Press 2 if you want to convert from Grams to KG """))

AmountOfvalues = int(input("Enter the amount of values you want to convert: "))

castValue = str(AmountOfvalues)
#controle value
j = 1
e = 1

#logic for cast value 
if castValue.isnumeric:
    while j <= AmountOfvalues:
        ValuetoConvert = float(int(input("Enter the value/values you want to convert: ")))
        savedValues.append(ValuetoConvert)
        j += 1
       
       
DeleteStatus = int(input("Press 3 if you want to delete a saved value or press 4 to move on "))

#get input for delete option
if DeleteStatus == 3:
    ValueTodelete = int(input("Enter the number of values youd like to delete "))
    while e <= ValueTodelete:
        selectValuestoDelete = int(input("Select the value/values you want to delete "))
        savedValues.append(selectValuestoDelete)
        e += 1       
elif DeleteStatus == 4:
    print("Moving on")

if ConversiontType == 1:
    for d in savedValues:
        convert_value.convert_miles(d)  ### calling the convert class 
elif ConversiontType == 2:
    for d in savedValues:
        convert_value.convert_km(d)  ### calling the convert class 
else:
    print("you have entered the wrong value")

    

    




