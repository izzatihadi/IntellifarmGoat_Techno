import pandas as pd
import statsmodels.api as sm

# Load the Excel file into a DataFrame
data = pd.read_excel("C:/Users/Nor Sa'adah/Downloads/Technopreneurship/Machine Learning/.vscode/data.xlsx")
print(data)

# Extract the 'Temperature' and 'Heartbeat' columns from the Excel data
X = data[['Temperature', 'Heartbeat']]

# Add a constant for the intercept
X = sm.add_constant(X)

# Load the coefficients for the regression model
a = -0.4870
b = 0.0600
intercept = 25.1534

# Calculate the 'Y' values using the regression formula
data['Y'] = intercept + (a * data['Temperature']) + (b * data['Heartbeat']) + 47

# Define the health status criteria
lower_limit = 10.0195
upper_limit = 11.2039

# Calculate health status based on Y values
data['Health Status'] = ['HEALTHY' if lower_limit <= y <= upper_limit else 'UNHEALTHY' for y in data['Y']]

# Save the updated data with 'Y' and 'Health Status' columns to a new Excel file
data.to_excel('updated_goat_data.xlsx', index=False)
