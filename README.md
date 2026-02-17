# AI Smart Parking System
Intelligent Smart City Parking Command Center with Dynamic Pricing and Interactive Booking

## Overview
AI Smart Parking System is an intelligent parking management platform designed to simulate a smart city parking infrastructure. The system provides real-time parking slot visualization, interactive slot booking, automatic slot release, dynamic pricing based on occupancy rate, and persistent storage using SQLite.

This project demonstrates how AI-driven infrastructure systems can optimize parking allocation, reduce congestion, and simulate intelligent urban mobility management.

## Core Objectives
- Provide real-time parking slot monitoring
- Enable interactive booking and release
- Implement demand-based dynamic pricing
- Simulate time-based auto-release system
- Maintain persistent parking data storage
- Design scalable smart infrastructure architecture

## Key Features
- Real-time parking grid visualization
- Color-coded slots:
  - Green → Free
  - Red → Occupied
  - Blue → Booked
- Zone-based parking organization (A, B, C)
- Interactive booking system
- Automatic slot release simulation
- Dynamic pricing engine based on occupancy
- Occupancy rate progress visualization
- SQLite-based persistent storage
- Modular and scalable architecture

## How the System Works
1. The system initializes parking slots across multiple zones.
2. Each slot is assigned a status (Free or Occupied).
3. Users can book any available slot.
4. Booked slots change to blue and store booking time.
5. After a defined time period, booked slots automatically return to Free (simulation).
6. Occupancy rate is calculated in real time.
7. Parking price dynamically adjusts based on current demand.

## Dynamic Pricing Model
The system calculates price using occupancy percentage.

Example logic:
Base Price + (Occupancy Rate × Dynamic Factor)

This simulates demand-based pricing models used in real smart city systems.

## Parking Layout Visualization
Slots are displayed in a grid layout using colored UI blocks.
Each slot shows:
- Slot ID
- Zone
- Current status
- Booking action button (if applicable)

This simulates a real parking control dashboard.

## Database
SQLite database file is automatically created:
database/parking.db

Stored data includes:
- Slot ID
- Zone
- Status
- Booking timestamp

No manual database setup is required.

## Project Structure
AI-Smart-Parking-System  
│  
├── app.py  
├── database/  
│   └── parking.db (auto-created)  
├── requirements.txt  
├── README.md  

## Installation

Step 1: Clone the repository
git clone https://github.com/YOUR_USERNAME/AI-Smart-Parking-System.git
cd AI-Smart-Parking-System

Step 2: Create virtual environment
python -m venv venv
venv\Scripts\activate

Step 3: Install dependencies
pip install streamlit

## Run Application
streamlit run app.py

The application will run at:
http://localhost:8501

## Real-World Applications
- Smart city infrastructure
- Airport parking systems
- Shopping mall parking
- Corporate campus parking
- Traffic congestion reduction systems
- Intelligent urban mobility platforms

## Scalability Design
The system architecture allows future upgrades including:
- Multi-floor parking support
- REST API backend integration
- Cloud database deployment
- IoT sensor integration
- CCTV-based vehicle detection using computer vision
- Machine learning demand forecasting
- Revenue analytics dashboard
- Vehicle number-based billing system
- Peak-hour congestion prediction

## Innovation Highlights
This project demonstrates:
- Intelligent infrastructure simulation
- Demand-aware dynamic pricing
- Interactive real-time slot booking
- Automated state transition logic
- Persistent storage system
- Scalable modular architecture
- Smart city–ready system design

## Technical Stack
- Python
- Streamlit
- SQLite
- Basic HTML/CSS styling via Streamlit components

## Author
Mohamed Mustak M  
Machine Learning and AI Enthusiast  
GitHub: https://github.com/MOHAMEDMUSTAK
