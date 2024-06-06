import tkinter as tk
from tkinter import messagebox

class DigitalLiteracyAssistant:
    def __init__(self, master):
        self.master = master
        master.title ("Digital Literacy Assistant")

        self.label = tk.Label(master, text="Welcome to the Digital Literacy Assistant!", font=("Arial", 14, "bold"))
        self.label.pack()

        self.entry_label = tk.Label(master, text="Enter your question:")
        self.entry_label.pack()

        self.user_entry = tk.Entry(master)
        self.user_entry.pack()

        self.instruction_button = tk.Button(master, text="Get answer 🤖", command=self.get_answer, font=("Arial", 12), bg="#3498db", fg="white")
        self.instruction_button.pack()

        self.response_text = tk.Text(master, height=10, width=40, font=("Arial", 12))
        self.response_text.pack(pady=10)

        self.phone_entry = tk.Entry(master, width=40, font=("Arial", 12))
        self.phone_entry.pack()

        self.email_entry = tk.Entry(master, width=40, font=("Arial", 12))
        self.email_entry.pack()

        self.message_entry = tk.Entry(master, width=40, font=("Arial", 12))
        self.message_entry.pack()

        self.threat_detection_button = tk.Button(master, text="Check for threats 🚨", command=self.check_for_threats, font=("Arial", 12), bg="#e74c3c", fg="white")
        self.threat_detection_button.pack()

    def get_answer(self):
        user_question = self.user_entry.get().lower()
        if "unlock" in user_question and "phone" in user_question:
            response = "To unlock your phone, press the power button."
        elif "call" in user_question or "make a call" in user_question:
            response = "To make a call, open the Phone app and dial the number."
        elif "message" in user_question or "send a message" in user_question:
            response = "To send a message, open the Messages app and compose a new message."
        elif "browse" in user_question or "internet" in user_question:
            response = "To browse the internet, open the Safari or Chrome app and enter a website URL."
        elif "volume" in user_question or "adjust the volume" in user_question:
            response = "To adjust the volume, use the physical volume buttons on the side of your phone."
        elif "password" in user_question or "change the password" in user_question:
            response = "To change the password, go to the Settings app, scroll to the password category, enter your old password then set a new one."
        elif "copy" in user_question or "copy text" in user_question:
            response = "To copy text, double tap on the text until it becomes highlighted in blue and select the copy option right above it."
        elif "paste" in user_question or "paste text" in user_question:
            response = "To paste text, you first need to make sure that you have copied it. Then, double click on the typing box and select the paste option."
        elif "brightness" in user_question or "increase brightness" in user_question:
            response = "To increase the brightness of your screen, place your finger at the top of your screen then slide down. After, slide your finger upwards the sun-like icon."
        elif "rotation" in user_question or "change rotation" in user_question:
            response = "To change your screen rotation, place your finger at the top of your screen, slide down and click on the lock icon."
        elif "flashlight" in user_question or "turn on flashlight" in user_question:
            response = "To turn on flashlight, go to your lock screen and press on the bottom left icon."
        elif "wallpaper" in user_question or "change wallpaper" in user_question:
            response = "To change your wallpaper, go to Settings, scroll down to the wallpaper category and set a new wallpaper."
        elif "alarm" in user_question or "set an alarm" in user_question:
            response = "To set an alarm, go to the Clock app, click on the alarm category and set an alarm using the plus sign on the upper right corner."
        elif "picture" in user_question or "take a picture" in user_question:
            response = "To take a picture, go to the Camera app, situate your phone for the picture and click on the white circular button on the bottom of your screen."
        elif "video" in user_question or "record a video" in user_question:
            response = "To record a video, go to Camera app, swipe to the left to get the red button on the bottom of your screen and press on it to record."
        elif "install" in user_question or "install an app" in user_question:
            response = "To install an app, go the App Store app, type the name of the app you wish to install and click on the 'Get' icon to begin the installation."
        elif "delete" in user_question or "delete an app" in user_question:
            response = "To delete an app, press and hold on it until it starts to wiggle. Then tap on the 'X' icon to confirm deletion."
        elif "discard" in user_question or "delete message" in user_question:
            response = "To delete a message, press and hold on it and click the option 'delete'. If the option is not available, then the message cannot be deleted."
        elif "location" in user_question or "find location" in user_question:
            response = "To find the location of certain place, go to the Google Map app and type the name of the place in the search bar."
        elif "internet" in user_question or "connect to the internet" in user_question:
            response = "To connect to the internet, go to Settings, scroll up to the Wi-Fi category, click on the network you wish to connect to and enter the necessary information."
        elif "emergency" in user_question or "emergency call" in user_question:
            response = "To make an emergency call, press on the the power and the volume button on the sides of your phone at the same time until the 'Emergency SOS' category pops up and slide your finger to the right."
        elif "off" in user_question or "power off" in user_question:
            response = "To shut your phone down, press on the the power and the volume up button on the sides of your phone at the same time until the 'Slide to Power Off' category pops up and slide your finger to the right. "
        elif "screenshot" in user_question or "take a screenshot" in user_question:
            response = "To take a screenshot, simultaneously press the power and volume up button on the sides of your phone, then release your fingers quickly."


        else:
            response = "I'm sorry. I couldn't understand your question. Please ask again."

        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, response)

    def check_for_threats(self):
        phone_number = self.phone_entry.get()
        email_address = self.email_entry.get()
        message = self.message_entry.get()

        if not phone_number or not email_address or not message:
            messagebox.showwarning("Input Error", "Please enter phone number, email address, and message.")
            return

        is_phone_threat = self.check_for_threat(phone_number, ["anonymous", "unknown"])
        is_email_threat = self.check_for_threat(email_address, ["phishing", "fraud"])
        is_message_threat = self.check_for_threat(message, ["threatening", "danger"])

        self.show_threat_results(phone_number, email_address, message, is_phone_threat, is_email_threat, is_message_threat)

    def check_for_threat(self, text, threat_patterns):
        return any(pattern in text.lower() for pattern in threat_patterns)

    def show_threat_results(self, phone_number, email_address, message, is_phone_threat, is_email_threat, is_message_threat):
        result_message = f"Results: \n\nPhone Number: {phone_number}\nEmail Address: {email_address}\nMessage: {message}\n\n"

        if is_phone_threat:
            result_message += "Threat Alert: Be cautious with anonymous or unknown phone numbers.\n"

        if is_email_threat:
            result_message += "Threat Alert: Be cautious with emails related to phishing or fraud.\n"

        if is_message_threat:
            result_message += "Threat Alert: Be cautios with threatening or dangerous messages.\n"

        if not any([is_phone_threat, is_email_threat, is_message_threat]):
            result_message += "No specific threats detected."

        messagebox.showinfo("Threat Detection Results", result_message)

def run_digital_literacy_assistant():
     root = tk.Tk()
     app = DigitalLiteracyAssistant(root)
     root.mainloop()

if __name__ == "__main__":
     run_digital_literacy_assistant()
