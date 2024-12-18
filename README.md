SafeScape-AI: Real-Time Instagram Event Analyzer

SafeScape-AI is a Python-based Flask application that integrates with Instagram's Webhooks API to capture, store, and analyze Instagram events in real time. It processes events such as comments, messages, reactions, and more, storing the data in an SQLite database. The tool includes a powerful analysis module to generate insights like top active users, event breakdowns, and trends.

Key Features 🚀

Webhook Integration: Captures real-time Instagram events (comments, reactions, messages, etc.) via webhooks.

SQLite Database Storage: Stores all incoming events persistently for analysis.

Event Handlers: Processes multiple types of events efficiently and categorizes them.

Data Analysis: Generates insights including:

Event counts by type.

Top users by activity.

Breakdown of comments, reactions, and messages.

Recent activity within specific date ranges.

Lightweight Setup: Designed to run seamlessly on local systems or cloud environments.

ngrok Integration: Enables local testing by exposing the Flask server to the internet securely.

Prerequisites 🛠️

Ensure you have the following tools installed before starting:

Python: Version 3.9 or later (Download Here)

Pip: Python's package installer

ngrok: For local testing of Instagram Webhooks (Install ngrok)

Setup Instructions ⚙️

Follow these steps to set up SafeScape-AI on your system:

Step 1: Clone the Repository

Clone the GitHub repository to your local machine:

git clone <repository_url>
cd SafeScape-AI

Step 2: Set Up a Virtual Environment

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

For Windows:

venv\Scripts\activate

For Mac/Linux:

source venv/bin/activate

Step 3: Install Dependencies

Install all required Python packages from the requirements.txt file:

pip install -r requirements.txt

Step 4: Initialize the Database

Run the database.py script to create the SQLite database and tables:

python database.py

Step 5: Start the Flask Application

Run the Flask server to start listening for Instagram webhook events:

python app.py

The Flask server will start running at:

http://127.0.0.1:5000

Step 6: Set Up ngrok for Webhook Testing

To expose your local Flask server to the internet:

Start ngrok to forward port 5000:

ngrok http 5000

Copy the public URL provided by ngrok (e.g., https://1234abcd.ngrok.io).

Go to the Instagram Webhook settings in your developer portal and set the webhook URL to:

https://<public_url>/webhook

Verify the webhook by ensuring the VERIFY_TOKEN in app.py matches the one configured in Instagram.

Step 7: View or Analyze Data

View All Database Contents:

python view_database.py

Analyze Data for Insights:

python analyze_data.py

Example Outputs 📝

1. Running app.py:

When Instagram sends a webhook event, the following JSON response is returned:

{
  "status": "success"
}

2. Sample Analysis Script Output:

Event Type Counts:

event_type
comments         5
messages         3
reactions        2
live_comments    1

Top Users by Activity:

username
test_user    6
demo_user    3

Comments Breakdown:

  username            data_text
0 test_user  This is a test comment!

Troubleshooting 🛠️

Common Issues and Solutions

Webhook Verification Fails:

Ensure the VERIFY_TOKEN in app.py matches the token configured in Instagram Webhook settings.

Confirm that the ngrok URL is correct and publicly accessible.

Database Not Found:

Run the database.py script to initialize the SQLite database.

Dependencies Missing:

Ensure all dependencies are installed:

pip install -r requirements.txt

ngrok Not Working:

Restart ngrok and ensure the correct public URL is being used.

Project Structure 📁

SafeScape-AI/
│
├── app.py              # Flask server to handle webhook events
├── database.py         # Initializes the SQLite database
├── handlers.py         # Event handlers for different Instagram events
├── analyze_data.py     # Analysis script to process stored events
├── view_database.py    # Script to view database contents
├── requirements.txt    # List of required Python packages
└── instagram_data.db   # SQLite database (created after initialization)

Future Improvements 🚀

Add support for additional Instagram events.

Enhance data visualization with charts and graphs.

Deploy the application to a cloud service like Heroku or AWS.

License 📜

This project is licensed under the MIT License. You are free to use, modify, and distribute this project.

Contributors 🙌

Your Name - Initial Development

Additional Contributors - Add here as needed

Thank you for using SafeScape-AI! 🎉
Happy Coding! 🚀

