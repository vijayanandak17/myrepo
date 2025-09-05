import pyautogui
import time

# Constants
TARGET_GLUCOSE = 100  # mg/dL
CORRECTION_FACTOR = 50  # 1 unit of insulin drops glucose by 50 mg/dL

def calculate_insulin_dose(glucose_level):
    if glucose_level <= 150:
        return 0
    return round((glucose_level - TARGET_GLUCOSE) / CORRECTION_FACTOR, 1)

def main():
    # Give user time to focus
    pyautogui.alert("Click OK to start insulin calculator.", "Insulin Dose Calculator")
    time.sleep(1)

    # Step 1: Get glucose level
    glucose_input = pyautogui.prompt(text="Enter current blood glucose level (mg/dL):", title="Glucose Level Input", default="")

    if glucose_input is None:
        pyautogui.alert("No input provided. Exiting.", "Cancelled")
        return

    try:
        glucose_level = int(glucose_input)
        insulin_dose = calculate_insulin_dose(glucose_level)

        if insulin_dose == 0:
            msg = f"Glucose level is {glucose_level} mg/dL. No insulin needed."
        else:
            msg = f"Glucose level is {glucose_level} mg/dL.\nRecommended insulin dose: {insulin_dose} units."

        pyautogui.alert(msg, "Insulin Recommendation")

    except ValueError:
        pyautogui.alert("Invalid input. Please enter a numeric glucose level.", "Error")

if __name__ == "__main__":
    main()
