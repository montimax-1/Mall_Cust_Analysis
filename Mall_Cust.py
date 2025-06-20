import pandas as pd

#import dataset
df = pd.read_csv("Mall_Customers.csv")

#Preview_Data
print(df.head())


#Check Mising Values
print(df.isnull().sum())


#Remove duplicate rows using .drop_duplicates() 
df_cleaned = df.drop_duplicates()


#Standardize text values like gender, country names, etc.
#Gender
df['Genre'] = df['Genre'].str.strip().str.title()

#Rename column headers to be clean and uniform (e.g., lowercase, no spaces).
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

#Age By ascending Order 
df.sort_values(by='age', ascending=True, inplace=True)


# Convert 'age', 'annual_income_(k$)', 'spending_score_(1-100)' to int if needed
numeric_columns = ['age', 'annual_income_(k$)', 'spending_score_(1-100)']
for col in numeric_columns:
    if col.lower().replace(' ', '_') in df.columns:
        df[col.lower().replace(' ', '_')] = df[col.lower().replace(' ', '_')].astype(int)

# Final 
print("\nCleaned Shape:", df.shape)
print("\nCleaned Columns:\n", df.columns)


# Save cleaned dataset
df.to_csv("cleaned_mall_customers.csv", index=False)
print("\n Cleaned dataset saved as 'cleaned_mall_customers.csv'")

