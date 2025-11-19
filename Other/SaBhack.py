# Give's The Player Free Admin Commands in Steal a Brainrot.

Copy
import time
import pyautogui
import pyperclip

# Define constants for better readability
APP_NAME = "VulnerableApp.exe"
TXT_INPUT Loc = (200, 150)  # Coordinates of the 'txtInput' TextBox
BTN_EXECUTE_loc = (350, 150)  # Coordinates of the 'btnExecute' button
RTB_OUTPUT_loc = (100, 250)  # Coordinates of the 'rtbOutput' RichTextBox

def execute_injection(injection):
    # Copy the injection to the clipboard
    pyperclip.copy(injection)

    # Activate the C# application window
    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.write(APP_NAME)
    pyautogui.press('enter')
    time.sleep(1)

    # Paste the injection into the 'txtInput' TextBox
    pyautogui.click(TXT_INPUT_loc)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)

    # Click the 'btnExecute' button to trigger the injection
    pyautogui.click(BTN_EXECUTE_loc)
    time.sleep(1)

    # Get the output from the 'rtbOutput' control
    output = ""
    for i in range(10):  # Adjust the number of iterations based on output length
        output += pyautogui.locateOnScreen("output.png").get_text().strip() + "\n"
        time.sleep(0.5)

    return output.strip()

if __name__ == "__main__":
    injection = "System.Windows.Forms.MessageBox.Show(\"Brainrot injection successful with Python!\")"
    result = execute_injection(injection)
   
