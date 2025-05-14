JS Quiz Pro 🚀
JS Quiz Pro is an interactive, web-based JavaScript quiz application built with Streamlit. It helps developers test and improve their JavaScript knowledge through a premium, modern interface. With a 30-minute timer, engaging confetti animations for correct answers, and a sleek design, this quiz is perfect for beginners and experts alike to master JavaScript concepts in a fun and challenging way.
Features

Ready Button: Start the quiz when you're ready with a dedicated starting screen.
30-Minute Timer: A client-side timer gives you 30 minutes to complete the quiz, adding a sense of urgency.
Premium UI: Dark theme with purple-blue gradients, neumorphic containers, and smooth animations.
Progress Circle: SVG-based visual indicator showing quiz completion percentage.
Confetti Animation: Celebrate correct answers with colorful confetti bursts.
Leaderboard: Compare your score and time with simulated top performers.
Instant Feedback: Immediate correct/incorrect feedback after each answer.
Responsive Design: Optimized for both desktop and mobile devices.
Shareable Results: Share your score on social media with a single click.

Prerequisites
To run JS Quiz Pro, you need:

Python 3.8+: Download Python
Streamlit: Version 1.30.0 or higher
Internet Connection: Required for Google Fonts and confetti animations (optional for offline use)

Installation

Clone the Repository (or copy the code to your local machine):
git clone https://github.com/your-username/js-quiz-pro.git
cd js-quiz-pro

Alternatively, save main.py in C:\Users\lenovo\OneDrive\Desktop\quz.

Install Dependencies:
pip install streamlit

Verify Streamlit version:
streamlit --version


(Optional) Offline Setup:

Remove the Google Fonts link (<link href="https://fonts.googleapis.com/...">) and confetti script (<script src="https://cdn.jsdelivr.net/...">) from main.py if you lack internet access.
Replace with local font files or skip confetti.



Usage

Run the App:Navigate to the project directory:
cd C:\Users\lenovo\OneDrive\Desktop\quz
streamlit run main.py

If port 8501 is in use, try:
streamlit run main.py --server.port 8502


Access the Quiz:

Open your browser and go to http://localhost:8501 (or the specified port).
You’ll see a "Ready" screen with quiz instructions.


Start the Quiz:

Click the Ready button to begin.
The 30-minute timer starts, and the first question appears.


Take the Quiz:

Select an answer from the options (A, B, C, D).
Receive instant feedback (✅ Correct or ❌ Wrong).
Navigate using Previous and Next buttons, or click Finish to end early.
Correct answers trigger confetti animations.


View Results:

After finishing or when the timer expires, view your score, accuracy, time taken, and leaderboard.
Check correct/incorrect answers in the detailed review section.
Share your score using the Share Score button.



Customizing Quiz Data
To modify or add quiz questions, edit the quiz list in main.py:
quiz = [
    {
        'question': 'Your question here?',
        'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
        'answer': 'Correct option'
    },
    # Add more questions
]


Ensure each question has a question (string), options (list of strings), and answer (string matching one option).
Save and rerun the app to load updated questions.

Screenshots
Add screenshots of the app to showcase the UI. Example placeholders:

Ready Screen: screenshots/ready_screen.png
Quiz Interface: screenshots/quiz_interface.png
Results Page: screenshots/results_page.png

To include screenshots, capture images of the app and place them in a screenshots/ folder in your repository.
Troubleshooting

UI Not Displaying:

Check the terminal for errors after running streamlit run main.py.
Ensure Streamlit is installed: pip install --force-reinstall streamlit.
Clear browser cache or use Incognito mode.
Verify Python version (3.8+): python --version.


Timer Issues:

The timer runs client-side via JavaScript. Ensure your browser allows scripts.
Check browser console (F12 → Console) for errors if the timer doesn’t start.


No Confetti/Fonts:

Internet connection is needed for canvas-confetti and Google Fonts. For offline use, remove these from main.py or host locally.



License
This project is licensed under the MIT License - see the LICENSE file for details.
Contact
For feedback, suggestions, or contributions:

Email: [your-email@example.com]
GitHub: your-username
Project Link: [your-app-link]


Happy quizzing! 🚀 Master JavaScript with JS Quiz Pro!
