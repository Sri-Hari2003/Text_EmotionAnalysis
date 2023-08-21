# Text_EmotionAnalysis

# Emotion Analysis Web Application
This is a Flask-based web application that performs emotion analysis on text using the IBM Watson SDK. The application provides a user-friendly interface for analyzing text and retrieving emotions detected within the text.

# Features
Analyze emotions in text using the IBM Watson Emotion Analysis service.
User-friendly interface to input text and receive emotion analysis results.
Error handling for various scenarios, such as short text, invalid input, and API errors.

# Prerequisites
Python 3.x
Flask
IBM Watson SDK

# Other dependencies (specified in requirements.txt)
Getting Started
Clone this repository to your local machine.
Install the required dependencies by running:
Copy code
pip install -r requirements.txt
Configure the IBM Watson SDK with your API credentials (consult the SDK documentation for instructions).
Run the application using:
Copy code
python app.py
Open your web browser and go to http://localhost:5000 to access the web interface.
Usage
Access the home page by navigating to the root URL (/) to interact with the web interface.
Enter text in the provided input field and submit to receive emotion analysis results.
Alternatively, you can use the /analyze_emotion route to make a POST request with JSON data containing the text to analyze.
The /emotionDetector route can be accessed via a GET request with the textToAnalyze query parameter to retrieve emotion analysis results.

# Error Handling
The application includes error handling for scenarios such as empty input, short text, API errors, and invalid input.
Error messages are designed to be informative and user-friendly.
Deployment
For production deployment, it's recommended to use a production-grade server such as Gunicorn instead of the built-in Flask development server.
Ensure that you configure appropriate environment variables and security settings.
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.
