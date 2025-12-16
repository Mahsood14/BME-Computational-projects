# Education vs Alzheimer's percentages
education_levels = [
    "High School",
    "Trade/Tech",
    "Bachelors",
    "Graduate",
    "Professional"
]
dataset = [27.8, 33.3, 18.2, 24.0, 75.0]   # Dataset values
us_avg = [11.0, 9.0, 6.5, 5.5, 5.0]        # U.S. averages

# Function to make bar from percentage
def make_bar(value, scale=2):
    length = int(value / scale)
    return "█" * length

print("\nAlzheimer’s Prevalence by Education Level")
print("-" * 60)
print(f"{'Education':<15} {'Dataset %':<12} {'Bar':<30} {'US Avg %':<10}")
print("-" * 60)

for edu, d_val, u_val in zip(education_levels, dataset, us_avg):
    print(f"{edu:<15} {d_val:<12} {make_bar(d_val):<30} {u_val:<10}")


