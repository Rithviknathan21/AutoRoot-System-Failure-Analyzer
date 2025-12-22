# AutoRoot – System Failure Analyzer

AutoRoot is an AI-powered system failure analysis tool designed to simulate how SRE and DevOps teams detect anomalies and identify root causes in production environments.

## What it does
- Generates system telemetry (CPU, memory, latency, error rate)
- Detects anomalies using an ML model (Isolation Forest)
- Correlates metrics to infer probable root causes
- Exposes inference through a backend API
- Provides an interactive web dashboard for analysis

## Tech Stack
- Python, Pandas, NumPy
- Scikit-learn (Isolation Forest)
- FastAPI (backend API)
- Streamlit (dashboard)
- Google Colab + Ngrok (deployment)

## Use Case
Designed as a simulation of real-world AI-based observability and incident analysis systems used in SRE workflows.

## Author
Rithviknathan M
