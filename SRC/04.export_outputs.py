import pandas as pd
import matplotlib.pyplot as plt

monthly = pd.read_csv("outputs/02.tables/kpi_monthly_complaints.csv")
product_summary = pd.read_csv("outputs/02.tables/kpi_product_summary.csv").head(10)
issue_summary = pd.read_csv("outputs/02.tables/kpi_issue_summary.csv").head(10)

plt.figure(figsize=(12, 6))
plt.plot(monthly["year_month"], monthly["complaint_count"])
plt.xticks(rotation=90)
plt.title("Monthly Complaint Volume")
plt.xlabel("Month")
plt.ylabel("Complaint Count")
plt.tight_layout()
plt.savefig("outputs/01.charts/monthly_complaints.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.bar(product_summary["product"], product_summary["complaint_count"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Products by Complaint Volume")
plt.xlabel("Product")
plt.ylabel("Complaint Count")
plt.tight_layout()
plt.savefig("outputs/01.charts/top_products.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.bar(issue_summary["issue"], issue_summary["complaint_count"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Issues by Complaint Volume")
plt.xlabel("Issue")
plt.ylabel("Complaint Count")
plt.tight_layout()
plt.savefig("outputs/01.charts/top_issues.png")
plt.close()

print("Charts exported successfully.")