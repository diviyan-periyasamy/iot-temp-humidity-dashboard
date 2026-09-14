#  IoT-Based Temperature & Humidity Monitoring Dashboard

A real-time environmental monitoring dashboard that simulates **IoT temperature and humidity sensor data** and visualizes it through an interactive **Python Dash** application.

The project demonstrates a typical IoT monitoring workflow with **real-time data simulation, interactive visualization, threshold-based alerting, and user-controlled filtering**.

---

##  Overview

This project simulates temperature and humidity sensor readings and displays them on an interactive, real-time dashboard.

The system demonstrates how sensor data can be:

```text
IoT Sensor Simulation
        │
        ▼
Sensor Data Generation
        │
        ▼
Python Data Processing
        │
        ▼
Dash Application
        │
        ├── Temperature Monitoring
        ├── Humidity Monitoring
        ├── Interactive Charts
        ├── Threshold Alerts
        └── Date/Time Filtering
```

The dashboard is designed to represent a simplified **IoT environmental monitoring system**.

---

#  Features

### 📡 Real-Time Sensor Simulation

* Generates simulated temperature readings
* Generates simulated humidity readings
* Continuously updates sensor values
* Mimics a real-world IoT monitoring environment

### 📈 Interactive Visualizations

Interactive Plotly charts display:

* Temperature trends
* Humidity trends
* Historical sensor readings
* Time-based changes

###  Threshold-Based Alerts

The dashboard monitors sensor readings against predefined thresholds.

Alerts can be triggered when:

* Temperature exceeds the configured limit
* Humidity exceeds the configured limit
* Environmental conditions move outside the expected range

### 🎛️ User-Controlled Filtering

Users can interact with the dashboard to:

* Filter sensor data
* Select date ranges
* Select time ranges
* Explore historical temperature readings
* Explore historical humidity readings

---

#  Dashboard Architecture

```text
┌──────────────────────────┐
│   Simulated IoT Sensors  │
│                          │
│ Temperature + Humidity   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   sensor_simulator.py    │
│                          │
│ Sensor Data Generation   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│        Pandas            │
│   Data Processing        │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│       Python Dash        │
│     Web Dashboard        │
└────────────┬─────────────┘
             │
       ┌─────┴─────┐
       ▼           ▼
┌────────────┐ ┌────────────┐
│ Temperature│ │  Humidity  │
│   Chart    │ │   Chart    │
└────────────┘ └────────────┘
             │
             ▼
     ┌────────────────┐
     │ Alert System   │
     └────────────────┘
```

---

# 🛠️ Tech Stack

| Category             | Technology            |
| -------------------- | --------------------- |
| Programming Language | Python                |
| Dashboard Framework  | Dash                  |
| Visualization        | Plotly                |
| Data Processing      | Pandas                |
| Data Source          | Simulated IoT Sensors |

---

#  Project Structure

```text
iot-temp-humidity-dashboard/
│
├── app.py
│   # Main Dash application
│
├── sensor_simulator.py
│   # Simulated IoT sensor data generator
│
├── assets/
│   # Dashboard styling and static assets
│
├── requirements.txt
│   # Python dependencies
│
└── README.md
    # Project documentation
```

---

#  Running Locally

## 1. Clone the Repository

```bash
git clone https://github.com/DhulakshanKannan/iot-temp-humidity-dashboard.git
cd iot-temp-humidity-dashboard
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run the Dashboard

```bash
python app.py
```

The dashboard will be available at:

```text
http://localhost:8050
```

Open the address in your web browser to access the monitoring dashboard.

---

#  Dashboard Capabilities

The dashboard provides real-time monitoring of:

| Metric          | Monitoring                                 |
| --------------- | ------------------------------------------ |
|  Temperature | Real-time trend visualization              |
|  Humidity     | Real-time trend visualization              |
|  Alerts       | Threshold-based abnormal reading detection |
|  Time Range   | User-controlled filtering                  |
|  Date Range   | Historical data filtering                  |

---

#  Project Objectives

The main objectives of this project are to demonstrate:

* Real-time data visualization
* IoT sensor data simulation
* Interactive dashboard development
* Time-series data analysis
* Threshold-based alert systems
* User-controlled data filtering
* Python-based web application development

---

#  Future Improvements

Potential improvements include:

* [ ] Connect to real IoT sensors
* [ ] MQTT-based sensor communication
* [ ] Store sensor data in PostgreSQL
* [ ] Add multiple sensor locations
* [ ] Add historical data analytics
* [ ] Add email/SMS notifications
* [ ] Add anomaly detection using machine learning
* [ ] Add sensor health monitoring
* [ ] Dockerize the application
* [ ] Deploy the dashboard to the cloud
* [ ] Add authentication and user management

---

#  IoT Data Flow

The project can be extended into a production IoT architecture:

```text
Physical IoT Sensors
        │
        ▼
      MQTT
        │
        ▼
Message Broker
        │
        ▼
Data Processing
        │
        ▼
   PostgreSQL
        │
        ▼
   Analytics
        │
        ▼
 Dash Dashboard
        │
        ▼
Alerts & Monitoring
```

---

#  Author

**Diviyan Periyasamy**

BSc (Hons) Data Science, Coventry University | NIBM
---

> Developed as part of academic coursework.

