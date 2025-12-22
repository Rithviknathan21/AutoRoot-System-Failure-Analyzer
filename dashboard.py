import streamlit as st
import requests

API_BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="AutoRoot", layout="centered")

st.title("🛠️ AutoRoot – System Failure Analyzer")
st.caption("AI-driven anomaly detection and root cause analysis")

st.subheader("System Metrics Input")

cpu = st.slider("CPU Usage (%)", 0, 100, 45)
memory = st.slider("Memory Usage (%)", 0, 100, 60)
latency = st.slider("Latency (ms)", 0, 1000, 120)
error_rate = st.slider("Error Rate", 0.0, 5.0, 0.5)
log_severity = st.selectbox("Log Severity", ["INFO", "WARN", "ERROR", "CRITICAL"])

if st.button("Analyze System State"):
    payload = {
        "cpu": cpu,
        "memory": memory,
        "latency": latency,
        "error_rate": error_rate,
        "log_severity": log_severity
    }

    try:
        response = requests.post(
            f"{API_BASE_URL}/analyze",
            json=payload,
            timeout=10
        )

        if response.status_code == 200:
            result = response.json()

            st.divider()
            st.subheader("Analysis Result")

            if result["anomaly"] == 1:
                st.error("🚨 Anomaly Detected")
            else:
                st.success("✅ System Operating Normally")

            st.markdown(f"**Root Cause:** `{result['root_cause']}`")

            st.divider()
            st.subheader("Explainability")
            st.caption("Top contributing signals (conceptual)")

            st.markdown("""
            - CPU usage trend
            - Latency deviation
            - Error rate spikes
            """)

        else:
            st.warning("API responded but returned an error.")

    except Exception as e:
        st.error(f"Failed to connect to API: {e}")
