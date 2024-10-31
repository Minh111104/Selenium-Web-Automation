# Selenium Web Automation Project

This project demonstrates how to use Selenium WebDriver to automate various web interactions, including locating elements by different methods, filling out forms, and navigating websites. It consists of three scripts—`main.py`, `interaction.py`, and `challenge.py`—each showcasing different Selenium functionalities with Python.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Script Descriptions](#script-descriptions)

## Features

- **Automated Browser Interaction**: Controls a web browser using Selenium for tasks like form filling and navigation.
- **Element Location**: Demonstrates different methods for locating elements, such as by `ID`, `Name`, `Class Name`, `CSS Selector`, and `XPath`.
- **Data Extraction**: Extracts and prints content from specified elements on a webpage.
- **Keyboard Simulation**: Sends keyboard commands (e.g., `Enter`) to interact with elements.

## Setup

### Prerequisites

- [Python 3](https://www.python.org/)
- [Google Chrome](https://www.google.com/chrome/) (or update driver path if using another browser)
- ChromeDriver (Ensure ChromeDriver matches the installed Chrome version)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/selenium-web-automation.git
    cd selenium-web-automation
    ```

2. Install the required Python packages:
    ```bash
    pip install selenium
    ```

3. [Download ChromeDriver](https://chromedriver.chromium.org/downloads) and place it in the project directory or specify the path in the code if different from the default.

## Script Descriptions

### `main.py`
- **Purpose**: Demonstrates different ways to locate and interact with elements on a webpage.
- **Functionality**:
    - Opens the Python website and navigates to event listings.
    - Extracts and prints upcoming event names and times.
    - Interacts with elements by different locators like `ID`, `CSS Selector`, and `XPath`.

### `interaction.py`
- **Purpose**: Shows additional interaction methods, such as navigating to a link, performing a search, and sending keyboard inputs.
- **Functionality**:
    - Opens Wikipedia’s main page.
    - Clicks on "Content portals" using link text.
    - Searches for "Python" using the search bar and submits the query with `Keys.ENTER`.

### `challenge.py`
- **Purpose**: Automates form filling and submission on a sample website.
- **Functionality**:
    - Fills out a signup form on the example website with a first name, last name, and email.
    - Locates the "Sign Up" button and submits the form.

