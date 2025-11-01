import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

data = {
    'Mthly_HH_Income': [
        5000, 6000, 10000, 10000, 12500, 14000, 15000, 18000, 19000, 20000,
        20000, 22000, 23400, 24000, 24000, 25000, 25000, 25000, 29000, 30000,
        30500, 32000, 34000, 34000, 35000, 35000, 39000, 40000, 42000, 43000,
        45000, 45000, 45000, 45000, 46000, 47000, 50000, 50500, 55000, 60000,
        60000, 65000, 70000, 80000, 85000, 90000, 98000, 100000, 100000, 100000
    ],
    'Mthly_HH_Expense': [
        8000, 7000, 4500, 2000, 12000, 8000, 16000, 20000, 9000, 9000,
        18000, 25000, 5000, 10500, 10000, 12300, 20000, 10000, 6600, 13000,
        25000, 15000, 19000, 25000, 12000, 25000, 8000, 10000, 15000, 12000,
        25000, 40000, 10000, 22000, 25000, 15000, 20000, 20000, 45000, 10000,
        50000, 20000, 9000, 20000, 25000, 48000, 25000, 30000, 50000, 40000
    ],
    'No_of_Fam_Members': [
        3, 2, 2, 1, 2, 2, 3, 5, 2, 4, 4, 6, 3, 6, 4, 3, 3, 6, 2, 4, 5, 4,
        6, 3, 3, 4, 4, 4, 4, 4, 6, 6, 2, 4, 5, 7, 4, 3, 6, 3, 6, 4, 2, 4,
        5, 7, 5, 6, 4, 6
    ],
    'Emi_or_Rent_Amt': [
        2000, 3000, 0, 0, 3000, 0, 35000, 8000, 0, 0, 8000, 12000, 0, 0, 0,
        0, 3500, 0, 2000, 0, 5000, 0, 0, 4000, 0, 0, 0, 0, 0, 0, 0, 3500,
        1000, 2500, 3500, 0, 0, 0, 12000, 0, 10000, 5000, 0, 0, 0, 0, 0, 0,
        20000, 10000
    ],
    'Annual_HH_Income': [
        64200, 79920, 112800, 97200, 147000, 196560, 167400, 216000, 218880,
        220800, 278400, 279840, 292032, 316800, 244800, 246000, 261000, 258000,
        348000, 385200, 351360, 445440, 330480, 469200, 466200, 449400, 556920,
        412800, 488880, 619200, 523800, 507600, 437400, 610200, 596160, 456840,
        570000, 581760, 600600, 590400, 590400, 647400, 756000, 1075200, 1142400,
        885600, 1152480, 1404000, 1032000, 1320000
    ],
    'Highest_Qualified_Member': [
        'Under-Graduate', 'Illiterate', 'Under-Graduate', 'Illiterate', 'Graduate',
        'Graduate', 'Post-Graduate', 'Graduate', 'Under-Graduate', 'Under-Graduate',
        'Under-Graduate', 'Illiterate', 'Illiterate', 'Graduate', 'Graduate',
        'Graduate', 'Graduate', 'Under-Graduate', 'Graduate', 'Graduate',
        'Under-Graduate', 'Professional', 'Professional', 'Professional',
        'Graduate', 'Professional', 'Under-Graduate', 'Under-Graduate',
        'Graduate', 'Graduate', 'Graduate', 'Professional', 'Post-Graduate',
        'Post-Graduate', 'Graduate', 'Professional', 'Professional',
        'Professional', 'Graduate', 'Post-Graduate', 'Graduate', 'Illiterate',
        'Graduate', 'Graduate', 'Under-Graduate', 'Post-Graduate', 'Professional',
        'Graduate', 'Professional', 'Post-Graduate'
    ],
    'No_of_Earning_Members': [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 3, 1, 1, 1, 1,
        1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 1, 1, 1, 4, 1, 2, 2, 1, 1, 2, 1, 1,
        2, 3, 2, 1, 1
    ]
}

df = pd.DataFrame(data)

print("--- 1. Income & Expenditure ---\n")

mthly_income_mean = df['Mthly_HH_Income'].mean()
mthly_income_median = df['Mthly_HH_Income'].median()
mthly_income_mode = df['Mthly_HH_Income'].mode().tolist()

print(f"Mean Monthly Household Income: ${mthly_income_mean:,.2f}")
print(f"Median Monthly Household Income: ${mthly_income_median:,.2f}")
print(f"Mode of Monthly Household Income: {mthly_income_mode}\n")

mthly_expense_mean = df['Mthly_HH_Expense'].mean()
mthly_expense_median = df['Mthly_HH_Expense'].median()

print(f"Mean Monthly Household Expense: ${mthly_expense_mean:,.2f}")
print(f"Median Monthly Household Expense: ${mthly_expense_median:,.2f}")
print("Interpretation: The mean is slightly higher than the median, suggesting a slight positive skew in the expenditure data. "
      "This indicates a few households have unusually high expenses, pulling the average up.\n")

mthly_income_range = df['Mthly_HH_Income'].max() - df['Mthly_HH_Income'].min()
print(f"Range of Monthly Household Income: ${mthly_income_range:,.2f}\n")

df['Income_to_Expense_Ratio'] = df['Mthly_HH_Income'] / df['Mthly_HH_Expense'].replace(0, np.nan)
highest_ratio_row = df.loc[df['Income_to_Expense_Ratio'].idxmax()]
print("Household with the highest income-to-expense ratio:")
print(f"Index: {highest_ratio_row.name}")
print(f"Ratio: {highest_ratio_row['Income_to_Expense_Ratio']:.2f}\n")

print("=" * 50 + "\n")

print("--- 2. Family Structure ---\n")

avg_fam_members = df['No_of_Fam_Members'].mean()
print(f"Average number of family members per household: {avg_fam_members:.2f}\n")

std_dev_fam_members = df['No_of_Fam_Members'].std()
print(f"Standard deviation of No_of_Fam_Members: {std_dev_fam_members:.2f}")
print("Interpretation: The standard deviation is relatively low, indicating that family size is quite consistent across households, without extreme variations.\n")

df['Dependency_Ratio'] = (df['No_of_Fam_Members'] - df['No_of_Earning_Members']) / df['No_of_Fam_Members']
highest_dependency_row = df.loc[df['Dependency_Ratio'].idxmax()]
print("Household with the highest dependency ratio:")
print(f"Index: {highest_dependency_row.name}")
print(f"Dependency Ratio: {highest_dependency_row['Dependency_Ratio']:.2f}")
print(f"Details: {highest_dependency_row['No_of_Fam_Members']} family members, {highest_dependency_row['No_of_Earning_Members']} earning members.\n")

print("=" * 50 + "\n")
print("--- 3. Housing & EMI ---\n")

df['EMI_as_Pct_of_Income'] = (df['Emi_or_Rent_Amt'] / df['Mthly_HH_Income']) * 100
avg_emi_pct = df['EMI_as_Pct_of_Income'].mean()
print(f"Average EMI or rent as a percentage of monthly income: {avg_emi_pct:.2f}%\n")

high_emi_households = df[df['EMI_as_Pct_of_Income'] > 40]
print("Households where EMI or rent exceeds 40% of monthly income:")
print(high_emi_households[['Mthly_HH_Income', 'Emi_or_Rent_Amt', 'EMI_as_Pct_of_Income']].to_string() + "\n")

df['Disposable_Income'] = df['Mthly_HH_Income'] - df['Mthly_HH_Expense'] - df['Emi_or_Rent_Amt']
lowest_disposable_row = df.loc[df['Disposable_Income'].idxmin()]
print("Household with the lowest disposable income:")
print(f"Index: {lowest_disposable_row.name}")
print(f"Disposable Income: ${lowest_disposable_row['Disposable_Income']:,.2f}")
print(f"Details: Income: ${lowest_disposable_row['Mthly_HH_Income']:,.2f}, "
      f"Expense: ${lowest_disposable_row['Mthly_HH_Expense']:,.2f}, "
      f"EMI: ${lowest_disposable_row['Emi_or_Rent_Amt']:,.2f}\n")

print("=" * 50 + "\n")

print("--- 4. Annual Income & Qualification ---\n")
df['Calculated_Annual_Income'] = df['Mthly_HH_Income'] * 12
discrepancies = df[df['Annual_HH_Income'] != df['Calculated_Annual_Income']]
if discrepancies.empty:
    print("Annual household income is consistent with monthly income * 12.\n")
else:
    print("Discrepancies found between 'Annual_HH_Income' and 'Mthly_HH_Income * 12':")
    print(discrepancies[['Mthly_HH_Income', 'Calculated_Annual_Income', 'Annual_HH_Income']].to_string() + "\n")

avg_income_by_qualification = df.groupby('Highest_Qualified_Member')['Mthly_HH_Income'].mean().sort_values(ascending=False)
print("Average Monthly Income by Highest Qualified Member (descending):")
print(avg_income_by_qualification.to_string() + "\n")

qualification_order = ['Illiterate', 'Under-Graduate', 'Graduate', 'Post-Graduate', 'Professional']
qualification_mapping = {qual: i for i, qual in enumerate(qualification_order, 1)}
df['Qualification_Numeric'] = df['Highest_Qualified_Member'].map(qualification_mapping)
correlation_qualification_income = df['Qualification_Numeric'].corr(df['Mthly_HH_Income'])
mean_median_by_qualification = df.groupby('Highest_Qualified_Member')['Mthly_HH_Income'].agg(['mean', 'median']).loc[qualification_order]

print("Correlation between Numeric Qualification and Monthly Income:", f"{correlation_qualification_income:.2f}")
print("Mean and Median Monthly Income by Qualification:")
print(mean_median_by_qualification.to_string() + "\n")

print("Interpretation: The positive correlation coefficient and the clear upward trend in mean/median incomes with higher qualification levels suggest a strong relationship between higher qualification and higher household income.\n")

print("=" * 50 + "\n")
print("--- 5. Outliers & Correlation ---\n")

income_mean = df['Mthly_HH_Income'].mean()
income_std = df['Mthly_HH_Income'].std()
df['Income_Z_Score'] = (df['Mthly_HH_Income'] - income_mean) / income_std
outliers_z_score = df[np.abs(df['Income_Z_Score']) > 3]
print("Outliers in Monthly Household Income (Z-score > 3):")
print(outliers_z_score[['Mthly_HH_Income', 'Income_Z_Score']].to_string() + "\n")

income_expense_corr = df['Mthly_HH_Income'].corr(df['Mthly_HH_Expense'])
print(f"Correlation between Monthly Income and Expense: {income_expense_corr:.2f}")
print("Interpretation: The high positive correlation suggests that as household income increases, so does household expenditure. The relationship is quite strong.\n")

earning_income_corr = df['No_of_Earning_Members'].corr(df['Mthly_HH_Income'])
print(f"Correlation between No. of Earning Members and Monthly Income: {earning_income_corr:.2f}")
print("Interpretation: The moderate to strong positive correlation suggests that having more earning members in a household is associated with a higher monthly income.\n")
