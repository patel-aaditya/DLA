# Digital Literacy Assistant (DLA)

A desktop GUI application designed to help elderly users operate their smartphones with confidence. The app provides step-by-step instructions for common phone tasks and includes a threat detection feature to help users identify potential scams.

## Features

### 📱 Question & Answer System
Ask plain-language questions about how to use your phone and receive clear, step-by-step instructions. Supported topics include:

- Unlocking your phone
- Making and receiving calls
- Sending messages
- Browsing the internet
- Adjusting volume and brightness
- Changing your password or wallpaper
- Copying and pasting text
- Changing screen rotation
- Turning on the flashlight
- Setting alarms
- Taking pictures and recording videos
- Installing and deleting apps
- Deleting messages
- Finding locations using Google Maps
- Connecting to Wi-Fi
- Making emergency calls
- Powering off your phone
- Taking screenshots

### 🚨 Threat Detection
Enter a phone number, email address, and message to check for signs of scams or threats. The app uses case-insensitive substring matching to flag:

- **Phone numbers** containing "anonymous" or "unknown"
- **Emails** containing "phishing" or "fraud"
- **Messages** containing "threatening" or "danger"

## Requirements

- Python 3.10.x
- No additional packages required — the application uses only Python's built-in `tkinter` library.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/patel-aaditya/DLA.git
   cd DLA
   ```

2. *(Optional)* **Install dependencies with Poetry:**
   ```bash
   poetry install
   ```
   > Since there are no external dependencies, you can also run the app directly with Python 3.10.

## Usage

Run the application from the project root:

```bash
python main.py
```

A window titled **"Digital Literacy Assistant"** will open.

### Getting an Answer

1. Type your question into the **"Enter your question:"** field (e.g., *"How do I take a screenshot?"*).
2. Click **"Get answer 🤖"**.
3. The step-by-step instructions will appear in the text box below.

### Checking for Threats

1. Enter a **phone number**, **email address**, and **message** in the respective fields.
2. Click **"Check for threats 🚨"**.
3. A pop-up will display whether any threats were detected based on the inputs.

## Project Structure

```
DLA/
├── main.py          # Main application source code
├── pyproject.toml   # Poetry project configuration
├── poetry.lock      # Dependency lock file
└── README.md        # Project documentation
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements such as:

- Additional phone task instructions
- More comprehensive threat detection patterns
- UI/UX enhancements for accessibility
- Support for other languages
