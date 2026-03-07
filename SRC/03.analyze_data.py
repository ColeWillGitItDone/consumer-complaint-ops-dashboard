import pandas as pd

df = pd.read_csv("data/02.processed/complaints_cleaned.csv")

monthly = (
    df.groupby("year_month")
      .size()
      .reset_index(name="complaint_count")
      .sort_values("year_month")
)

monthly["previous_month_count"] = monthly["complaint_count"].shift(1)
monthly["month_over_month_pct_change"] = (
    (monthly["complaint_count"] - monthly["previous_month_count"])
    / monthly["previous_month_count"]
) * 100

product_summary = (
    df.groupby("product")
      .size()
      .reset_index(name="complaint_count")
      .sort_values("complaint_count", ascending=False)
)

product_summary["share_of_total_pct"] = (
    product_summary["complaint_count"] / product_summary["complaint_count"].sum()
) * 100

product_summary["rank"] = range(1, len(product_summary) + 1)

issue_summary = (
    df.groupby("issue")
      .size()
      .reset_index(name="complaint_count")
      .sort_values("complaint_count", ascending=False)
)

issue_summary["share_of_total_pct"] = (
    issue_summary["complaint_count"] / issue_summary["complaint_count"].sum()
) * 100

issue_summary["cumulative_share_pct"] = issue_summary["share_of_total_pct"].cumsum()

state_summary = (
    df.groupby("state")
      .size()
      .reset_index(name="complaint_count")
      .sort_values("complaint_count", ascending=False)
)

product_issue = (
    df.groupby(["product", "issue"])
      .size()
      .reset_index(name="complaint_count")
      .sort_values("complaint_count", ascending=False)
)

monthly.to_csv("outputs/02.tables/kpi_monthly_complaints.csv", index=False)
product_summary.to_csv("outputs/02.tables/kpi_product_summary.csv", index=False)
issue_summary.to_csv("outputs/02.tables/kpi_issue_summary.csv", index=False)
state_summary.to_csv("outputs/02.tables/kpi_state_summary.csv", index=False)
product_issue.to_csv("outputs/02.tables/kpi_product_issue_summary.csv", index=False)

print("Analysis complete. KPI tables exported.")