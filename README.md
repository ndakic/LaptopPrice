# Predict Laptop Price

<h4> Server API </h4>

- Language: Java 7
- Framework: Spring with MVC architecture
- Project management tool: Maven
- Database: Postgresql

<h4> Client API </h4>

- Angular App
- Some features:
    - Preview and filter all laptops
    - Choose your laptop specs
    - See predicited Laptop prices

<h4> Prediction API </h4>

- Django App in which API endpoints consumes JSON
- Machine Learning methods for prediction:
    - Multiple Linear Regression
    - K-Nearest neighbors
- Predicted price is based on laptop specifications

<h4> Data Scrapper </h4>

- Python scripts which:
    - Collects as many as possible laptops from website <a href="https://www.kupindo.com/" target="_blank"> kupindo.com</a>.
    - Insert collected data into DB

<h4> Deploy </h4>
 
- All Apps are dockerized and deployed on AWS EC2
