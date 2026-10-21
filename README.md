# AI Support Ticket Classifier and Troubleshooting Assistant

## About the Project

I built this project to explore how machine learning and AI can be used to handle technical support tickets.

The application takes a support issue as input, predicts its category and priority, and suggests troubleshooting steps. I used a machine learning model for classification and integrated the Google Gemini API to generate suggestions based on the ticket description.

I also added an SQLite database to store submitted tickets and a fallback mechanism so the application can still provide predefined troubleshooting steps when the Gemini API is unavailable.

## Features

- **Ticket Classification:** Predicts categories such as Login, Application Error, Database, and API.
- **Priority Prediction:** Predicts the priority of a ticket using a machine learning model.
- **AI Troubleshooting:** Uses the Gemini API to generate issue-specific troubleshooting suggestions.
- **Fallback Mechanism:** Returns predefined troubleshooting steps if the AI request fails.
- **Ticket Storage:** Saves ticket descriptions, categories, priorities, and statuses in SQLite.
- **Ticket History:** Displays previously submitted tickets through the Streamlit interface.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web interface |
| pandas | Working with the ticket dataset |
| scikit-learn | Machine learning-based ticket classification |
| Google Gemini API | Generating troubleshooting suggestions |
| SQLite | Storing submitted tickets |
| python-dotenv | Loading the Gemini API key from environment variables |

## Project Structure

```text
ai-support-ticket-assistant/
│
├── Data/
│   └── tickets.csv
│
├── app.py
├── classifier.py
├── database.py
├── troubleshooting.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

### What Each File Does

- `app.py` — Runs the Streamlit application and connects the ticket submission, classification, troubleshooting, and history features.
- `classifier.py` — Contains the machine learning logic used to predict ticket categories and priorities.
- `database.py` — Creates the SQLite table and handles saving and retrieving tickets.
- `troubleshooting.py` — Generates troubleshooting suggestions using Gemini and provides predefined steps if the API call fails.
- `Data/tickets.csv` — Contains the sample ticket dataset used by the classifier.
- `requirements.txt` — Lists the Python packages needed to run the project.
- `.gitignore` — Excludes files such as `.env`, the virtual environment, and the local database from Git tracking.
- `.env` — Stores the Gemini API key locally. This file should not be uploaded to GitHub.
- `README.md` — Contains project documentation and setup instructions.

The `.env` file is created locally during setup and is intentionally excluded from the repository.

## How It Works

1. The user enters a technical support issue in the Streamlit interface.
2. The classifier predicts the ticket category and priority.
3. The ticket is saved in the SQLite database.
4. The Gemini API generates troubleshooting suggestions based on the issue description.
5. If the Gemini request fails, the application returns predefined troubleshooting steps for the predicted category.
6. The results are displayed in the interface, and saved tickets can be viewed in Ticket History.

## Getting Started

### Prerequisites

- Python installed on your computer
- A Google Gemini API key for AI-generated troubleshooting suggestions

### 1. Clone the Repository

```bash
git clone https://github.com/syamsantosh0905/ai-support-ticket-assistant.git
cd ai-support-ticket-assistant
```

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project root and add your API key:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the example value with your own key. Never commit or share your real API key.

### 5. Run the Application

```powershell
python -m streamlit run app.py
```

Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Testing

I tested the application with sample tickets covering:

- Login problems
- Application crashes
- Database connection failures
- API authentication and permission errors

I also simulated a Gemini API failure and verified that the application returned the predefined troubleshooting steps.

These tests check the main functionality. A more detailed evaluation of classification and priority prediction accuracy is still a possible improvement.

## What I Learned

Building this project gave me practical experience with:

- Text classification using scikit-learn.
- Integrating an external AI API into a Python application.
- Working with SQLite for data persistence.
- Building an interactive application using Streamlit.
- Managing API keys with environment variables.
- Handling API errors and implementing fallback logic.

## Future Improvements

- Evaluate and improve ticket priority prediction.
- Add automated tests for the main features.
- Improve the formatting of troubleshooting suggestions.
- Add ticket status updates and search functionality.
- Deploy the application so others can try it online.