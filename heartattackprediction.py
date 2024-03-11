import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/manas/OneDrive/Desktop/Heart_health.csv")
print(data.head()) # printing first 5 rows to ensure our data is printing without errors

null_values = data.isnull().sum()
print("the count of null values:",null_values) # ensuring there are no null values in our data set


# first caluculate the number of smokers in our data
smoker_counts = data['Smoker'].value_counts()
# display them in our plot in pie chart
smoker_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)

# plot the labels and display the plot
plt.title('Distribution of Smokers')
plt.axis()
plt.show()

# Convert 'Yes' to 1 and 'No' to 0 in the 'Smoker' column
data['Smoker'] = data['Smoker'].map({'Yes': 1, 'No': 0})

# Filter the Dataset for individuals who smoke or have a risk of getting a heart attack
smokers_with_heart_attack = data[(data['Smoker'] == 1) | (data['Heart Attack'] == 1)]

# Select the desired columns: Name, Age, Smoker, Heart Attack
selected_columns = ['Name','Gender' ,'Age', 'Smoker', 'Heart Attack']
result = smokers_with_heart_attack[selected_columns]

# Print the result
print(result)