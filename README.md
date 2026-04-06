# 📊 Code Complexity Analyzer

A simple web application built using Streamlit and Python that analyzes Python code to estimate time complexity and provide basic metrics.

## 🚀 Features

- Count lines of code
- Count loops (for, while)
- Count conditions (if statements)
- Count functions
- Estimate time complexity (basic heuristic)

## 🛠️ Technologies Used

- Python
- Streamlit

## 📂 Project Structure

app.py      -> Frontend (UI)
model.py    -> Complexity analysis logic
utils.py    -> Helper functions
requirements.txt

## ▶️ How to Run

1. Install dependencies:

   pip install -r requirements.txt

2. Run the app:

   streamlit run app.py

3. Open browser:

   http://localhost:8501

## 📌 Limitations

- Complexity estimation is heuristic-based.
- Works primarily for Python code.
- Does not deeply analyze nested structures.

## 🔮 Future Improvements

- Detect nested loop depth properly
- Use AST parsing for accurate analysis
- Support multiple programming languages
- Show visualization charts
- Add cyclomatic complexity calculation