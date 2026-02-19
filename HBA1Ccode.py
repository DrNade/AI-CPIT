# Function to calculate HbA1c from average glucose (mg/dL)
def calculate_hba1c(eag_mgdl):
    # Using the ADAG formula: HbA1c = (eAG + 46.7) / 28.7
    hba1c = (eag_mgdl + 46.7) / 28.7
    return round(hba1c, 2)

# Main program
try:
    # Take input from user
    sugar_input = float(input("Enter your average blood sugar value (mg/dL): "))
    
    # Perform calculation
    result = calculate_hba1c(sugar_input)
    
    # Display result
    print(f"\nYour estimated HbA1c is: {result}%")
    
    # Interpretation
    if result < 5.7:
        print("Category: Normal")
    elif 5.7 <= result <= 6.4:
        print("Category: Prediabetes")
    else:
        print("Category: Diabetes")

except ValueError:
    print("Please enter a valid numeric value.")