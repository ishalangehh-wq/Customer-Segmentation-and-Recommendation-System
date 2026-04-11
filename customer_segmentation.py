import pandas as pd

# Step 1: Create dataset
data = {
    "CustomerID": [1,2,3,4,5,6,7,8,9,10],
    "Age": [25,34,45,23,40,36,52,28,30,48],
    "AnnualIncome": [30000,50000,70000,20000,65000,60000,80000,35000,40000,75000],
    "SpendingScore": [60,40,80,20,75,65,90,50,55,85]
}

df = pd.DataFrame(data)

# Step 2: Segmentation function
def segment_customer(row):
    if row["AnnualIncome"] > 60000 and row["SpendingScore"] > 70:
        return "High Value"
    elif row["AnnualIncome"] > 40000 and row["SpendingScore"] > 50:
        return "Medium Value"
    else:
        return "Low Value"

# Apply segmentation
df["Segment"] = df.apply(segment_customer, axis=1)

# Step 3: Analysis
print("Segment Count:\n", df["Segment"].value_counts())

# Step 4: Save dataset
df.to_csv("data.csv", index=False)

print("\nFinal Data:\n", df)
