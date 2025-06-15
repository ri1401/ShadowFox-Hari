# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
tips = sns.load_dataset('tips')

# Matplotlib - Bar Chart
avg_tip = tips.groupby('day')['tip'].mean()
plt.figure()
plt.bar(avg_tip.index, avg_tip.values, color='skyblue')
plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Tip Amount")
plt.savefig("avg_tip_by_day.png")
plt.close()

# Matplotlib - Pie Chart
gender_counts = tips['sex'].value_counts()
plt.figure()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Gender Distribution")
plt.axis('equal')
plt.savefig("Gender_distribution.png")
plt.close()

# Seaborn - Boxplot
plt.figure()
sns.boxplot(x='day', y='tip', data=tips, palette='Set2')
plt.title("Tip Distribution by Day")
plt.savefig("tip_distribution.png")
plt.close()

# Seaborn - Scatterplot
plt.figure()
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex')
plt.title("Tip vs. Total Bill")
plt.savefig("Tip_vs_total.png")
plt.close()
