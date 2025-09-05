# Step 1: Get blood glucose input from the user
try:
    glucose_level = float(input("Enter the patient's current blood glucose level (mg/dL): "))

    # Step 2: Check the glucose level and determine insulin dose
    if glucose_level < 70:
        dose = 0
        message = "Warning: Hypoglycemia! No insulin. Give fast-acting carbs (juice, glucose tabs)."
    elif 70 <= glucose_level <= 130:
        dose = 0
        message = "Glucose is in target range. No insulin needed."
    elif 131 <= glucose_level <= 180:
        dose = 2
        message = "Mildly elevated. Give 2 units of insulin."
    elif 181 <= glucose_level <= 240:
        dose = 4
        message = "Moderately elevated. Give 4 units of insulin."
    elif 241 <= glucose_level <= 300:
        dose = 6
        message = "High. Give 6 units of insulin."
    else:  # glucose_level > 300
        dose = 8
        message = "Very high! Give 8 units of insulin and consider contacting a healthcare provider."

    # Step 3: Output the result
    print(f"\nPatient's Blood Glucose Level: {glucose_level} mg/dL")
    print(f"Recommended Insulin Dose: {dose} unit(s)")
    print(f"Note: {message}")

except ValueError:
    print("Invalid input! Please enter a numeric value for blood glucose.")
