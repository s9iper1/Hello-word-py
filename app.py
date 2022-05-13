i = 1

while i <= 5:
    weight = int(input("Enter your weight: \n"))
    weight_unit = str(input("Enter unit of the weight pounds(L) or kilograms(k) \n"))
    if weight_unit.lower() == 'k':
        convert_to_pounds = weight // 0.45
        print(f"your weight is {convert_to_pounds} pounds")
    elif weight_unit.lower() == 'l':
        convert_to_kilograms = weight * 0.453592
        print(f"your weight is {convert_to_kilograms} kilograms")
    i = i+1

print("Loop ends here")
