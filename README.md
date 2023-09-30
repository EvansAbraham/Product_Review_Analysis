# Product Review Analysis Website


## Introduction

The **Product Review Analysis** project is a web application built using Flask, designed to perform sentiment analysis on user-generated product reviews. It utilizes the TextBlob library to analyze the textual content of reviews and provide users with a sentiment score on a scale of 1 to 5, helping them gauge the overall sentiment of a product or service based on aggregated user feedback.

This README file will guide you through setting up and running the project on your local machine.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Review Submission**: Users can input their product reviews through a user-friendly interface.

- **Sentiment Analysis**: The project employs TextBlob to perform sentiment analysis on user reviews.

- **Sentiment Score**: The website displays the sentiment score of each review on a scale of 1 to 5, with 1 being highly negative and 5 being highly positive.

- **Aggregated Ratings**: Users can view the average sentiment score based on all submitted reviews.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: The project requires Python to be installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

- **Virtual Environment (Optional but recommended)**: It's advisable to set up a virtual environment to isolate project dependencies. You can create a virtual environment using `virtualenv` or `venv`:

   ```bash
   python -m venv venv
   ```

- **Dependencies**: Install project dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Shalini171002/Product_Review_Analysis.git
   cd product-review-analysis
   ```

2. Set up a virtual environment (recommended) and install project dependencies (if you haven't already):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask development server:

   ```bash
   flask run
   ```

2. Open a web browser and navigate to `http://localhost:5000` to access the Product Review Analysis website.

3. Use the web interface to submit product reviews.

4. The website will display the sentiment score for each review and calculate the average sentiment score.

5. Explore the website to gain insights into the sentiment of product reviews.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the project on GitHub.

2. Create a new branch with a descriptive name for your feature or bug fix.

3. Make your changes and test thoroughly.

4. Create a pull request to submit your changes.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as needed.

---

Thank you for using the Product Review Analysis website! If you have any questions or encounter issues, please don't hesitate to contact us at [Shalini](mailto:shalinijayanthilal1@gmail.com).
