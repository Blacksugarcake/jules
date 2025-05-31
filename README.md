# Simple News Display Project (jules)

## Overview

This project fetches the top 10 news articles from the US using the NewsAPI and displays them on a simple webpage. The news data is stored locally in a JSON file, which the webpage then uses to render the articles.

## Features

- Fetches top 10 news headlines from NewsAPI.
- Stores news data (title, URL, summary) in a JSON file.
- Displays news articles on a clean, responsive HTML page.
- Includes instructions for scheduling daily updates.

## Project Structure

```
project/
├── data/
│   └── news_articles.json  # Stores fetched news articles
├── scripts/
│   ├── config.py           # Stores API key (must be created by user)
│   └── fetch_news.py       # Python script to fetch news
└── web/
    └── index.html          # HTML page to display news
.gitignore                  # Excludes config.py from git
README.md                   # This file
```

## Prerequisites

- Python 3 (3.6 or newer recommended)
- `pip` (Python package installer)
- A NewsAPI key (obtainable for free from [newsapi.org](https://newsapi.org/))

## Setup Instructions

1.  **Clone the Repository (if applicable)**
    If you have cloned this project from a Git repository, navigate to the project directory. If you downloaded it as a ZIP, extract and navigate into it.
    ```bash
    # Example if cloned:
    # git clone <repository_url>
    # cd <repository_name>
    cd project
    ```

2.  **Install Dependencies**
    The project requires the `requests` library to fetch data from the NewsAPI.
    ```bash
    pip install requests
    ```
    (Depending on your Python installation, you might need to use `pip3` instead of `pip`.)

3.  **Set Up API Key**
    You need to provide your NewsAPI key for the script to work.
    - Create a file named `config.py` inside the `project/scripts/` directory.
    - Add your API key to this file as follows:
      ```python
      # project/scripts/config.py
      API_KEY = "YOUR_ACTUAL_API_KEY"
      ```
    - Replace `"YOUR_ACTUAL_API_KEY"` with the API key you obtained from NewsAPI.
    *Note: `config.py` is included in `.gitignore` to prevent accidental commitment of your API key.*

## Running the Project

1.  **Fetch News Articles Manually**
    To fetch the latest news articles, run the `fetch_news.py` script. The articles will be saved in `project/data/news_articles.json`.

    The **only recommended way** to run this script is as a Python module from the `project` directory (the parent directory of `scripts`). This ensures that imports within the script work correctly.

    - Navigate to the `project` directory (e.g., the directory containing the `scripts`, `data`, and `web` folders):
      ```bash
      # If you are in the repository root, and your project files are in a 'project' subdirectory:
      cd project
      # If your 'scripts', 'data', 'web' folders are directly in the repository root, you are already there.
      ```
    - Then, execute the script as a module:
      ```bash
      python -m scripts.fetch_news
      ```
    You should see a confirmation message if the news is fetched and saved successfully.

2.  **View the Webpage**
    Open the `project/web/index.html` file in your web browser.

    **Important:** For the webpage to fetch and display the `news_articles.json` data correctly, you might need to serve the files using a local HTTP server due to browser security restrictions (CORS policy for `fetch` API when using `file:///` URLs).

    A simple way to start an HTTP server (if you have Python 3):
    - Navigate to the `project` directory in your terminal.
    - Run one of the following commands:
      ```bash
      # For Python 3.x
      python -m http.server
      # or
      python3 -m http.server
      ```
    - Then, open your browser and go to `http://localhost:8000/web/index.html`. The port number (e.g., 8000) might vary depending on your system or if the port is already in use.

## Scheduling News Updates

To ensure the news articles displayed on the webpage are always up-to-date, it's recommended to schedule the `project/scripts/fetch_news.py` script to run automatically on a daily basis. This will fetch the latest news and update the `project/data/news_articles.json` file.

**Common Scheduling Tools:**

*   **Linux/macOS:** You can use `cron`. A cron job can be set up to execute the Python script at a specified time each day.
    Example crontab entry to run the script daily at 7 AM (ensure paths are correct):
    ```bash
    0 7 * * * /usr/bin/python3 /path/to/your/project/scripts/fetch_news.py
    ```
    *(Remember to replace `/usr/bin/python3` with the actual path to your Python interpreter and `/path/to/your/project/` with the absolute path to the project directory).*

*   **Windows:** You can use the Task Scheduler. You would create a new task that runs the Python script (e.g., `C:\path\to\python.exe C:\path\to\your\project\scripts\fetch_news.py`) daily.

**General Instruction:**

Configure your chosen scheduling tool to execute the `project/scripts/fetch_news.py` script once a day. This will keep your news feed current.