import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv('/content/transactions.csv')

# Data Cleaning
data.drop_duplicates(inplace=True)
data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')
data['Amount (INR)'] = pd.to_numeric(data['Amount (INR)'], errors='coerce')
data['Status'] = data['Status'].str.strip().str.upper()
data.dropna(subset=['Transaction ID', 'Timestamp', 'Amount (INR)', 'Status'], inplace=True)

# Feature Engineering
data['Date'] = data['Timestamp'].dt.date
data['Month'] = data['Timestamp'].dt.to_period('M').astype(str)
data['Hour'] = data['Timestamp'].dt.hour

# Key Metrics
total_transactions = len(data)
successful = (data['Status'] == 'SUCCESS').sum()
failed = (data['Status'] == 'FAILED').sum()

success_rate = successful / total_transactions * 100 if total_transactions else 0
failure_rate = failed / total_transactions * 100 if total_transactions else 0

print("Total Transactions:", total_transactions)
print("Successful Transactions:", successful)
print("Failed Transactions:", failed)
print(f"Success Rate: {success_rate:.2f}%")
print(f"Failure Rate: {failure_rate:.2f}%")
print("Total Amount (INR):", data['Amount (INR)'].sum())
print("Average Amount (INR):", data['Amount (INR)'].mean())

# Status Analysis
print("\nStatus Summary:")
print(data.groupby('Status')['Amount (INR)'].agg(['count', 'sum', 'mean']))

sns.countplot(data=data, x='Status')
plt.title('Transaction Status')
plt.show()

# Transaction Amount Distribution
sns.histplot(data=data, x='Amount (INR)', bins=30, kde=True)
plt.title('Transaction Amount Distribution')
plt.show()

# Daily Transactions
daily = data.groupby('Date').agg(
    Transactions=('Transaction ID', 'count'),
    Total_Amount=('Amount (INR)', 'sum')
)

daily['Transactions'].plot(figsize=(10, 5), marker='o')
plt.title('Daily Transaction Volume')
plt.ylabel('Number of Transactions')
plt.show()

# Monthly Transactions
monthly = data.groupby('Month').agg(
    Transactions=('Transaction ID', 'count'),
    Total_Amount=('Amount (INR)', 'sum')
)

print("\nMonthly Analysis:")
print(monthly)

monthly['Transactions'].plot(kind='bar', figsize=(10, 5))
plt.title('Monthly Transaction Volume')
plt.ylabel('Number of Transactions')
plt.show()

# Hourly Transactions
hourly = data.groupby('Hour')['Transaction ID'].count()

hourly.plot(kind='bar', figsize=(10, 5))
plt.title('Transactions by Hour')
plt.xlabel('Hour')
plt.ylabel('Number of Transactions')
plt.show()

# Top Senders and Receivers
print("\nTop Senders:")
print(data['Sender UPI ID'].value_counts().head(5))

print("\nTop Receivers:")
print(data['Receiver UPI ID'].value_counts().head(5))

# Save Cleaned Dataset
data.to_csv('cleaned_transactions.csv', index=False)

print("\nAnalysis Completed Successfully!")
