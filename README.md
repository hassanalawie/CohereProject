Hey! I recently made this project to experiment with Sentiment analysis, so I decided, why not use cohere? The process was really smooth and to see this in action, just input your own cohere API key!!

# Customer Success Dashboard

## Overview
The Customer Success Dashboard is a web application designed to visualize customer sentiment and various performance metrics in real-time. It aims to provide clear insights into customer feedback and support ticket analysis, allowing businesses to make data-driven decisions to enhance customer satisfaction.

## Features
- **Sentiment Analysis**: Visual representation of customer sentiment through positive and negative support tickets.
- **Net Promoter Score (NPS)**: An index ranging from -100 to 100 reflecting customers' willingness to recommend a company's products or services.
- **Customer Satisfaction Score (CSAT)**: A measure of how products and services meet or surpass customer expectation.
- **Other Metrics**: Includes Customer Effort Score (CES), churn rate, retention rate, average resolution time, and first contact resolution rate, all vital for understanding and improving customer experience.

## Technologies Used
- **Frontend**: React, Chart.js, Axios
- **Backend**: Flask, NLTK for sentiment analysis

## Setup and Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory and install dependencies:
npm install
3. Start the Flask backend server:
python app.py
4. Run the React frontend in development mode:
npm start

Open [http://localhost:3000](http://localhost:3000) to view it in the browser.