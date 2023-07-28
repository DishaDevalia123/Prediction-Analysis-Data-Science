# Prediction-Analysis-Data-Science
This project aims to create a web application that predicts house prices based on various features such as city, number of bedrooms, number of bathrooms, and total square footage. The web application is built using Flask, a Python web framework, and it is deployed on an AWS EC2 instance for accessibility.

The application also includes a Tableau dashboard visualization that incorporates the machine learning model for house price prediction. Additionally, the dashboard provides an overview of the entire Arizona state's real estate data, such as the number of houses on rent, for sale, average price per square foot in each city, and more. The dashboard is interactive and includes features like a search bar for data exploration.

Features:-
Tableau dashboard visualization with real estate data overview for Arizona state.
House price prediction based on city, number of bedrooms, number of bathrooms, and total square footage.
Interactive elements on the dashboard, including a search bar for data exploration.
Comparison of tax-assessed value vs. house price.
Insights into the real estate market, trends, and patterns.

Technologies Used:-
Rapid API: To fetch real-time data for real estate metrics.
Flask: Python web framework for building the web application.
Python: The programming language used for implementing the machine learning model and backend logic.
AWS EC2: Cloud-based virtual machine used for deploying the web application.
Tableau: Data visualization tool used to create the interactive dashboard.
TabPy: TabPy is a Python server that allows you to execute Python code and models from Tableau.
HTML/CSS/JavaScript: Frontend technologies for designing the web pages and dashboard interface.
Machine Learning Libraries: Python libraries for creating and deploying the house price prediction model.
Data Manipulation Libraries: Python libraries for handling and processing real estate data.

Getting Started:-
To run the project locally or deploy it on your own AWS EC2 instance, follow these steps:
1. Clone the repository
2. Install the required Python packages: pip install -r requirements.txt
3. Run the Flask web application: python app.py
4. Access the web application in your browser

Deployment to AWS EC2:-
To deploy the web application on an AWS EC2 instance:
Create an AWS EC2 instance and obtain the instance's public IP address.
Connect to the EC2 instance via SSH: ssh -i your-key.pem ec2-user@your-ec2-public-ip
Upload the project files to the EC2 instance using SCP or Git.
Install necessary dependencies on the EC2 instance using the same steps as the local setup.
Run the Flask web application on the EC2 instance: python app.py
Access the web application in your browser using the EC2 instance's public IP.

Tableau Dashboard:-
The Tableau dashboard is accessible through the web application or directly via its URL. It provides various visualizations and insights into the Arizona real estate market. Users can interact with the dashboard, use the search bar to explore specific data, and gain valuable information for analysis and decision-making.

To enable the connection between the Flask web application and Tableau using TabPy:
Install TabPy on your system: pip install tabpy
Start TabPy server: tabpy
In the Tableau dashboard, connect to the TabPy server using the appropriate URL and port.
