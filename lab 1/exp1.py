import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\arshb\OneDrive\Desktop\sub\SEM VI\NLP\lab 1\employees.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

print(df.head(10))

summary_stats = df.groupby('DEPARTMENT_ID')['SALARY'].agg(['min', 'median', 'mean', 'max']).reset_index()

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
plt.subplots_adjust(wspace=0.4, hspace=0.4)

sns.barplot(x='DEPARTMENT_ID', y='min', data=summary_stats, ax=axes[0, 0])
axes[0, 0].set_title('Minimum Salary')

sns.lineplot(x='DEPARTMENT_ID', y='median', data=summary_stats, ax=axes[0, 1])
axes[0, 1].set_title('Median Salary')

sns.scatterplot(x='DEPARTMENT_ID', y='max', data=summary_stats, ax=axes[1, 0])
axes[1, 0].set_title('Average Salary')

summary_stat = df.groupby('JOB_ID')['SALARY'].agg(['min', 'median', 'mean', 'max']).reset_index()

axes[1, 1].pie(summary_stat['max'], labels=summary_stat['JOB_ID'], autopct='%1.1f%%', startangle=90)
axes[1, 1].set_title('Maximum Salary')

plt.show()
