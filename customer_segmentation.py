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
import matplotlib.pyplot as plt

# Segment count plot
df["Segment"].value_counts().plot(kind="bar")
plt.title("Customer Segmentation")
plt.xlabel("Segment")
plt.ylabel("Count")
plt.savefig("segment_chart.png")
df.groupby("Segment")["AnnualIncome"].mean().plot(kind="bar")
plt.title("Average Income by Segment")
plt.savefig("income_segment.png")
def recommend_action(segment):
    if segment == "High Value":
        return "Give premium offers and loyalty rewards"
    elif segment == "Medium Value":
        return "Give discounts and bundle offers"
    else:
        return "Target with ads and basic offers"

df["Recommendation"] = df["Segment"].apply(recommend_action)

print(df[["CustomerID", "Segment", "Recommendation"]])
