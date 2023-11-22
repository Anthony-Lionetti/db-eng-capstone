import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# from dashboard.custom.my_component import plotly_events

## Set GLOBAL Config for Ploty Charts ##
CONFIG = {
    'modeBarButtonsToRemove': ['zoom', 'zoomIn', 'zoomOut', 'select', 'lasso', "autoScale2d"],
}


def CustomerTab(df: pd.DataFrame, tab) -> go.Figure:
    cust_sales = df.copy()
    cust_sales = cust_sales.loc[cust_sales["Sales"] >= 70]
    cust_sales = cust_sales.groupby("Customer Name", as_index=False).sum(
        numeric_only=True)[["Customer Name", "Sales"]].sort_values("Sales", ascending=False)

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cust_sales["Customer Name"],
        y=cust_sales["Sales"],
        hovertemplate="""
    <b>Customer:</b> %{x}<br>
    <b>Total Sales:</b> %{y:$,.2f}
    <extra></extra>
    """,
        texttemplate="<b>%{y:$,.2f}</b>"
    ))
    fig.update_xaxes(range=[-1, 10])
    fig.update_yaxes(fixedrange=True)
    fig.update_layout(
        dragmode="pan",
        xaxis_title='Customer',
        yaxis_title='Total Sales ($ USD)',
        height=600,
        margin=dict(l=0, r=0, t=10,)
    )

    with tab:
        st.subheader("🤵 Customer Sales")
        # chart, info = st.columns([2, 1], gap="medium")

        st.plotly_chart(fig, use_container_width=True, config=CONFIG)
        # val = plotly_events(fig)
        # info.write(val)


def ProfitTab(df: pd.DataFrame, tab) -> None:
    profit_df = df.copy()
    profit_df = profit_df.groupby("Order Date", as_index=False).sum(
        numeric_only=True).sort_values("Order Date")
    profit_df = profit_df.loc[profit_df["Order Date"] < "2023-01-01"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=profit_df["Order Date"],
        y=profit_df["Profit"],
        mode="lines",
        hovertemplate="""
    <b>Profit:</b> %{y:$,.2f}<br>
    <b>Date:</b> %{x}
    <extra></extra>
    """
    ))
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector_buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=2, label="2yr", step="year", stepmode="backward"),
            dict(count=3, label="3yr", step="year", stepmode="backward"),
        ]),
    )
    fig.update_layout(
        dragmode="pan",
        xaxis_title='Order Date',
        yaxis_title='Total Profit ($ USD)',
        yaxis_tickformat='$,.2f',
        height=600,
        margin=dict(l=0, r=0, t=10,)
    )
    with tab:
        st.subheader("📈 Profit Chart")
        st.plotly_chart(fig, use_container_width=True, config=CONFIG)


def BubbleTab(df: pd.DataFrame, tab) -> None:
    bubble_df = df.copy()
    bubble_df = bubble_df.groupby(
        "Customer Name", as_index=False).sum(numeric_only=True)

    fig = px.scatter(
        bubble_df,
        x="Profit",
        y="Sales",
        color="Customer Name",
        size="Quantity",
        hover_data={
            "Customer Name": False,
            "Profit": ":$,.2f",
            "Sales": ":$,.2f",
        },
        hover_name="Customer Name"
    )
    fig.update_layout(
        showlegend=False,
        yaxis_title='Total Sales ($ USD)',
        yaxis_tickformat="$,.2f",
        xaxis_title='Total Profit ($ USD)',
        xaxis_tickformat="$,.2f",
        height=600,
        margin=dict(l=0, r=0, t=10,)
    )
    config = {
        'modeBarButtonsToRemove': ['zoomIn', 'zoomOut', 'select', 'lasso', "autoScale2d"],
    }

    with tab:
        st.subheader("🫧 Sales Buble Chart (w/ size=Quantity)")
        st.plotly_chart(fig, use_container_width=True, config=config)


def CuisineTab(df: pd.DataFrame, tab) -> None:
    cuisine_df = df.copy()
    cuisine_df["Year"] = cuisine_df["Order Date"].dt.year
    cuisine_df = cuisine_df.loc[cuisine_df["Year"].between(
        2020, 2022, inclusive="both")]
    cuisine_df = cuisine_df.groupby(["Cuisine Name", "Year"], as_index=False).sum(
        numeric_only=True).sort_values(["Year", "Sales"], ascending=False)
    fig = px.histogram(
        cuisine_df,
        x="Year",
        y="Profit",
        color="Cuisine Name",
        barmode='group',
        hover_data={
            "Cuisine Name": False,
            "Year": True,
            "Profit": ":$,.2f"
        },
        hover_name="Cuisine Name"
    )
    fig.update_traces(texttemplate="%{y:$,.2f}")
    fig.update_layout(
        yaxis_title='Total Profit ($ USD)',
        yaxis_tickformat="$,.2f",
        xaxis_title='Year',
        height=600,
        margin=dict(l=0, r=0, t=10,)
    )
    config = {
        'modeBarButtonsToRemove': ['zoomIn', 'zoomOut', 'select', 'lasso', "autoScale2d"],
    }

    with tab:
        st.subheader("🧑‍🍳 Yearly Profit by Cuisine")
        st.plotly_chart(fig, use_container_width=True, config=config)
