This script creates an interactive multiple-choice quiz application using PyQt5, a popular GUI framework for Python. The application loads questions from a formatted text file and presents them in a visually engaging window with images, animations, and user interaction elements.

Main Components
1. Quiz Class (Quiz)
- Inherits from QWidget, serving as the main application window.
- Loads and shuffles questions from a file named quiz_creator_questions.txt.

Displays:

- A banner image (banner.jpg)
- The current quiz question
- Four radio buttons for answer options
- A "Submit" button to check the answer
- Feedback is shown using animated GIFs (correct.gif and wrong.gif) in a pop-up dialog.

2. Result Dialog (ResultDialog)
- Displays whether the selected answer was correct or wrong.
- Shows an animated GIF and a message in a popup dialog.

3. Final Dialog (FinalDialog)
- Shown when all questions have been answered.
- Indicates quiz completion with a congratulatory message and animation (finish.gif).
