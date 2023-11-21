import streamlit as st
import pandas as pd

# Import Tabs #
from tabs import CustomerTab, ProfitTab, BubbleTab, CuisineTab

st.set_page_config(layout="wide", page_title="🏠 Home")

# Cache Dataset to prevent unneeded reruns #


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_excel("./data/lemon_dat.xlsx")
    df.rename(columns={" Cost": "Cost"}, inplace=True)
    df[["First Name", "Last Name"]] = df["Customer Name"].str.split(
        " ", expand=True, n=1)
    df["Profit"] = df["Sales"] - df["Cost"]
    return df


## Load Data ##
df = load_data()


left, main, right = st.columns([1, 7, 1])

with main:
    st.header("🍋 Little Lemon Dashboard")
    # use markdown to add a spacer
    st.markdown("# ")
    customer, profit, bubble, cuisine = st.tabs(
        ["🤵 Customer", "📈 Profit", "🫧 Bubble Chart", "🧑‍🍳 Cuisine"])

    ##################
    ## Customer Tab ##
    ##################
    CustomerTab(df, customer)

    ###############
    ## Proft Tab ##
    ###############
    ProfitTab(df, profit)

    ################
    ## Bubble Tab ##
    ################
    BubbleTab(df, bubble)

    #################
    ## Cuisine Tab ##
    #################
    CuisineTab(df, cuisine)
