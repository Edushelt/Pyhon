def calculate_totall_bill(bill_amount, tip_percentage=15):
    tip=bill_amount*tip_percentage/100
    total = bill_amount + tip
    return total

#Test the function
total1 = calculate_totall_bill(100)
total2 = calculate_totall_bill(100,20)

print(f"Total with default tip: ${total1}")
print(f"Total with 20%: ${total2}")
