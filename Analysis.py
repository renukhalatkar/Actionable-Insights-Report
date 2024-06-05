import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore


# Load the dataset
data = pd.read_csv('complaints data.csv')


# Drop rows with missing critical values
critical_columns = ['Date received', 'Product', 'Issue', 'Company']
data_cleaned = data.dropna(subset=critical_columns)

# Fill missing values in less critical columns with 'Unknown'
less_critical_columns = ['Sub-product', 'Sub-issue', 'Consumer complaint narrative', 'Company public response',
                         'State', 'ZIP code', 'Tags', 'Consumer consent provided?', 'Submitted via',
                         'Date sent to company', 'Company response to consumer', 'Timely response?', 
                         'Consumer disputed?', 'Complaint ID']

for column in less_critical_columns:
    data_cleaned[column] = data_cleaned[column].fillna('Unknown')

# Standardize date formats
data_cleaned['Date received'] = pd.to_datetime(data_cleaned['Date received'], errors='coerce')
data_cleaned['Date sent to company'] = pd.to_datetime(data_cleaned['Date sent to company'], errors='coerce')

# Drop rows where date conversion failed
data_cleaned = data_cleaned.dropna(subset=['Date received', 'Date sent to company'])


# Standardize date formats
data_cleaned['Date received'] = pd.to_datetime(data_cleaned['Date received'], errors='coerce')


# Extract year and month
data_cleaned['Year'] = data_cleaned['Date received'].dt.year
data_cleaned['Month'] = data_cleaned['Date received'].dt.month




output_file_path_excel = 'cleaned_complaints_data.xlsx'
data_cleaned.to_excel(output_file_path_excel, index=False)
