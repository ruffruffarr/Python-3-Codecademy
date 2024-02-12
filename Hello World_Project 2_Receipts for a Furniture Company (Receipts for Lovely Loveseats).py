#create two variable to represent Lovely Loveseat: Description and Price
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

#create two variable to represent Stylish Settee: Description and Price 
stylish_settee_description = "Stylish Setee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_setee_price = 180.50 

#create two variable to represent Luxuious Lamp: Description and Price
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

#create a variable for Sales Tax
sales_tax = .088

#add purchases and find out the total for the First Customer 
customer_one_total = 0
customer_one_itemization = ""
customer_one_total+= lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total +=luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)




