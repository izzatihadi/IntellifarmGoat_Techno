import pandas as pd
import statsmodels.api as sm

# Load Excel file
data = pd.read_excel("C:/Users/Nor Sa'adah/Downloads/Technopreneurship/Machine Learning/.vscode/datasets.xlsx")
print("Successful Read Excel File")

# Generate Goat IDs
data['Goat ID'] = range(1, len(data) + 1)

# Extract the 'Temperature' and 'Heartbeat' columns from the Excel
X = data[['Temperature', 'Heartbeat']]

# Add a constant for the intercept
X = sm.add_constant(X)

# Load the coefficients for the regression model
a = -0.4870
b = 0.0600
intercept = 25.1534

# Calculate the 'Y' values using the regression formula
data['Y'] = intercept + (a * data['Temperature']) + (b * data['Heartbeat']) 

# Define the health status criteria
lower_limit = 10.0195 #Min range for healthy goats
upper_limit = 11.2039 #Max range for healthy goats

# Calculate health status based on Y values
data['Health Status'] = ['HEALTHY' if lower_limit <= y <= upper_limit else 'UNHEALTHY' for y in data['Y']]

# Extract values of Fever, DifficultyBreathing, Fatigue, and Cough
fever = data['Fever']
difficulty_breathing = data['DifficultyBreathing']
fatigue = data['Fatigue']
cough = data['Cough']

# Set conditions based on data for symptoms
def potential_disease(row):
    if row['Fever'] == 'Y' and row['DifficultyBreathing'] == 'Y' and row['Fatigue'] == 'Y' and row['Cough'] == 'Y':
        return 'Anthrax and Pneumonia'
    elif row['Fever'] == 'Y' and row['DifficultyBreathing'] == 'Y' and row['Fatigue'] == 'N' and row['Cough'] == 'N':
        return 'Anthrax or Pneumonia'
    elif row['Fever'] == 'Y' and row['DifficultyBreathing'] == 'N' and row['Fatigue'] == 'Y' and row['Cough'] == 'Y':
        return 'Anthrax or Pneumonia'
    elif row['Fever'] == 'Y' and row['DifficultyBreathing'] == 'Y' and row['Fatigue'] == 'Y' and row['Cough'] == 'N':
        return 'Anthrax'
    elif row['Fever'] == 'N' and row['DifficultyBreathing'] == 'Y' and row['Fatigue'] == 'Y' and row['Cough'] == 'N':
        return 'Anthrax'
    elif row['Fever'] == 'Y' and row['DifficultyBreathing'] == 'N' and row['Fatigue'] == 'Y' and row['Cough'] == 'N':
        return 'Anthrax'
    elif row['Fever'] == 'N' and row['DifficultyBreathing'] == 'N' and row['Fatigue'] == 'Y' and row['Cough'] == 'N':
        return 'Anthrax'
    elif row['Fever'] == 'Y' and row['DifficultyBreathing'] == 'Y' and row['Fatigue'] == 'N' and row['Cough'] == 'Y':
        return 'Pneumonia'
    elif row['Fever'] == 'Y' or row['DifficultyBreathing'] == 'Y' and row['Fatigue'] == 'N' and row['Cough'] == 'Y':
        return 'Pneumonia'
    elif row['Fever'] == 'Y' and row['DifficultyBreathing'] == 'N' and row['Fatigue'] == 'N' and row['Cough'] == 'Y':
        return 'Pneumonia'
    elif row['Fever'] == 'N' and row['DifficultyBreathing'] == 'N' and row['Fatigue'] == 'N' and row['Cough'] == 'Y':
        return 'Pneumonia'
    else:
        return ''

# Determine the potential disease for goats based on its symptoms
data['Potential Disease'] = data.apply(potential_disease, axis=1)

# Arrange the columns
column_order = ['Goat ID', 'Temperature', 'Heartbeat', 'Y', 'Health Status', 'Fever', 'DifficultyBreathing', 'Fatigue', 'Cough', 'Potential Disease']
data = data[column_order]

# Save the updated data with 'Y', 'Health Status' columns to a new Excel file
data.to_excel('Results.xlsx', index=False)

print("Data for goats monitoring has been saved to 'Results.xlsx'.")