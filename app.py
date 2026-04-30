import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def load_superstore_data(path: str = "data/Sample - Superstore.csv") -> pd.DataFrame:
    """Load and prepare the Superstore dataset."""
    df = pd.read_csv(path)

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

    df["Profit Margin"] = df["Profit"] / df["Sales"]

    return df


def filter_data(
    dataframe: pd.DataFrame,
    years: list[int],
    regions: list[str],
    categories: list[str],
    segments: list[str]
) -> pd.DataFrame:
    """Filter the dataframe based on sidebar selections."""
    filtered_dataframe = dataframe[
        dataframe["Year"].isin(years)
        & dataframe["Region"].isin(regions)
        & dataframe["Category"].isin(categories)
        & dataframe["Segment"].isin(segments)
    ].copy()

    return filtered_dataframe


def main():
    """Run the Streamlit dashboard."""
    st.set_page_config(
        page_title="Superstore Sales Dashboard",
        layout="wide"
    )

    st.title("Superstore Sales Dashboard")
    st.write(
        "Interactive dashboard to explore sales, profit, discounts and customer segments."
    )

    df = load_superstore_data()

    st.sidebar.header("Filters")

    years = sorted(df["Year"].unique())
    regions = sorted(df["Region"].unique())
    categories = sorted(df["Category"].unique())
    segments = sorted(df["Segment"].unique())

    selected_years = st.sidebar.multiselect(
        "Year",
        options=years,
        default=years
    )

    selected_regions = st.sidebar.multiselect(
        "Region",
        options=regions,
        default=regions
    )

    selected_categories = st.sidebar.multiselect(
        "Category",
        options=categories,
        default=categories
    )

    selected_segments = st.sidebar.multiselect(
        "Segment",
        options=segments,
        default=segments
    )

    filtered_df = filter_data(
        df,
        selected_years,
        selected_regions,
        selected_categories,
        selected_segments
    )

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        return

    total_sales = filtered_df["Sales"].sum()
    total_profit = filtered_df["Profit"].sum()
    average_discount = filtered_df["Discount"].mean()
    profit_margin = total_profit / total_sales if total_sales != 0 else 0

    st.subheader("Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Sales", f"${total_sales:,.0f}")
    col2.metric("Total Profit", f"${total_profit:,.0f}")
    col3.metric("Average Discount", f"{average_discount:.2%}")
    col4.metric("Profit Margin", f"{profit_margin:.2%}")

    st.subheader("Filtered Data Preview")

    with st.expander("Show data"):
        st.dataframe(filtered_df.head(50))

    category_summary = (
        filtered_df
        .groupby("Category", as_index=False)
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum")
        )
    )

    region_summary = (
        filtered_df
        .groupby("Region", as_index=False)
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum")
        )
    )

    monthly_sales = (
        filtered_df
        .groupby("Month", as_index=False)["Sales"]
        .sum()
        .sort_values("Month")
    )

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader("Sales by Category")

        fig1, ax1 = plt.subplots(figsize=(7, 4))
        sns.barplot(
            data=category_summary.sort_values("Total_Sales", ascending=False),
            x="Category",
            y="Total_Sales",
            ax=ax1,
            color="#4C72B0"
        )

        ax1.set_xlabel("Category")
        ax1.set_ylabel("Total Sales")
        ax1.set_title("Total Sales by Category")

        plt.tight_layout()
        st.pyplot(fig1)

    with col_chart2:
        st.subheader("Profit by Region")

        fig2, ax2 = plt.subplots(figsize=(7, 4))
        sns.barplot(
            data=region_summary.sort_values("Total_Profit", ascending=False),
            x="Region",
            y="Total_Profit",
            ax=ax2,
            color="#55A868"
        )

        ax2.set_xlabel("Region")
        ax2.set_ylabel("Total Profit")
        ax2.set_title("Total Profit by Region")

        plt.tight_layout()
        st.pyplot(fig2)

    st.subheader("Monthly Sales Trend")

    fig3, ax3 = plt.subplots(figsize=(10, 4))
    sns.lineplot(
        data=monthly_sales,
        x="Month",
        y="Sales",
        marker="o",
        ax=ax3,
        color="#8172B2"
    )

    ax3.set_xlabel("Month")
    ax3.set_ylabel("Total Sales")
    ax3.set_title("Monthly Sales Trend")
    plt.xticks(rotation=45)

    plt.tight_layout()
    st.pyplot(fig3)


if __name__ == "__main__":
    main()