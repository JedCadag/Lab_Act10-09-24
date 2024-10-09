def calculate_fitness_fee(age, is_member):
    if age <= 18:
        if is_member:
            fee = 450.00
        else:
            fee = 650.00
    elif 18 <= age <= 65:
        if is_member:
            fee = 550.00
        else:
            fee = 750.00
    else:
        if is_member:
            fee = 400.00
        else:
            fee = 600.00
    return fee

age = int(input("Enter the attendee's age: "))
membership_status = input("Is the attendee a member? (yes/no): ").lower()

is_member = membership_status == "yes"

fee = calculate_fitness_fee(age, is_member)
print(f"The registration fee is: {fee} pesos.")