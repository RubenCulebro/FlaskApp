# Flask Application

## 1. PyCharm Configuration:
   - Open PyCharm.
   - Load the project directory by selecting Open and navigating to the directory where your Flask application code resides.

## 2. Create a Virtual Environment:
   - Open a terminal or command prompt and navigate to the project directory.
   - Run `python -m venv venv`.
   - Activate the virtual environment:
     - Windows: `venv\Scripts\activate`
     - macOS/Linux: `source venv/bin/activate`

## 3. Install Dependencies:
   - Inside the activated virtual environment, install the necessary packages using pip:
     `pip install flask numpy scikit-learn`

## 4. Set up Flask Run Configuration:
   - In PyCharm, go to Run > Edit Configurations.
   - Click on the + and select Python.
   - Set the Script path to `app.py`.
   - Add `FLASK_APP=app` to Environment variables.
   - Set the Working directory to the Flask application root path.

## 5. Interpreter:
   - Confirm that the selected Python interpreter is correct, pointing to the virtual environment's Python executable if applicable.

## 6. Run the Application:
   - Use the green run button in PyCharm, or in the terminal, execute `flask run` ensuring the environment variables are set.

## 7. Access the Application:
   - Flask applications run by default at http://127.0.0.1:5000. Access this URL in a web browser.