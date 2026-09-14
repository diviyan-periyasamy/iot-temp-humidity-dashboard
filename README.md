# IoT-Based Temperature & Humidity Monitoring Dashboard

A real-time environmental monitoring dashboard simulating IoT sensor data, built with Python Dash for interactive live visualization.

## Overview

This project simulates temperature and humidity sensor readings and displays them on an interactive, real-time dashboard — with alerting and user-controlled filtering — demonstrating a typical IoT monitoring use case using Python's Dash framework.

## Features

- Real-time simulated sensor data updates
- Interactive line charts for temperature and humidity trends
- Threshold-based alerts for abnormal readings
- User-controlled filtering and date/time range selection

## Tech Stack

Python · Dash · Plotly · Pandas

## Project Structure

```
iot-temp-humidity-dashboard/
├── app.py                # Main Dash application
├── sensor_simulator.py   # Simulated IoT data generator
├── assets/                # Dashboard styling
├── requirements.txt
└── README.md
```

## Running Locally

```bash
git clone https://github.com/DhulakshanKannan/iot-temp-humidity-dashboard.git
cd iot-temp-humidity-dashboard
pip install -r requirements.txt
python app.py
```

Dashboard available at `http://localhost:8050`.

## Author

**Dhulakshan Kannan**
BSc (Hons) Data Science, Coventry University | NIBM
[LinkedIn](https://www.linkedin.com/in/dhulakshan-kannan-a9b874224) · [GitHub](https://github.com/DhulakshanKannan)

> Developed as part of academic coursework.
