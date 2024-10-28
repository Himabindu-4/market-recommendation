from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Load the dataset
data = pd.read_csv('path/to/modcloth.csv')  # Replace with actual path if necessary

# Initialize WebDriver (use the path to your ChromeDriver)
driver = webdriver.Chrome(executable_path='C:\Users\nanna\market-recommendation')

# Open the locally running Flask app
driver.get("http://127.0.0.1:5000")  # Assuming Flask is running locally

# Check that the home page is loaded
assert "Lung Cancer Prediction API" in driver.page_source

# Navigate to the prediction route (if it's a form-based interface)
driver.get("http://127.0.0.1:5000/predict")

# Get the first row of data as input values
sample_data = data.iloc[0]
rating = sample_data['rating']
size = sample_data['size'] if pd.notnull(sample_data['size']) else 'N/A'
fit = sample_data['fit'] if pd.notnull(sample_data['fit']) else 'N/A'
category = sample_data['category']

# Find the input fields for prediction (assuming you have a form)
input_element = driver.find_element(By.NAME, 'features')  # Adjust input field name if necessary

# Enter data into the form field
input_element.send_keys(f"{rating}, {size}, {fit}, {category}")

# Submit the form (assuming there's a submit button)
submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()

# Wait for the response and print it
time.sleep(2)  # Adjust as necessary for loading time
response = driver.page_source
print(response)

# Validate if the prediction response appears on the page
assert "prediction" in response

# Close the browser
driver.quit()
