import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from pandas.errors import EmptyDataError

REPORT_FILE = "reports/attack_report.csv"

st.title("🚨 SSH Threat Monitoring Dashboard")

try:
    df = pd.read_csv(REPORT_FILE)

    if df.empty:
        st.warning("Attack report is empty.")
    else:
        st.subheader("Attack Report")
        st.dataframe(df)

        st.subheader("Top Attacker IPs")

        attack_counts = df.groupby("IP Address")["Failed Attempts"].sum()

        fig, ax = plt.subplots()

        attack_counts.plot(kind="bar", ax=ax)

        ax.set_xlabel("IP Address")
        ax.set_ylabel("Failed Attempts")
        ax.set_title("SSH Failed Login Attempts")

        st.pyplot(fig)

except FileNotFoundError:
    st.error("No attack report found. Run main.py first.")

except EmptyDataError:
    st.error("CSV file is empty.")
