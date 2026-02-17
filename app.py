import streamlit as st
import sqlite3
import random
import time
import os

st.set_page_config(page_title="Smart Parking Command Center", layout="wide")
st.title("🚗 AI Smart Parking Command Center")

TOTAL_SLOTS = 30
ZONES = ["A", "B", "C"]

# Ensure database folder exists
if not os.path.exists("database"):
    os.makedirs("database")

conn = sqlite3.connect("database/parking.db", check_same_thread=False)
c = conn.cursor()

# Drop old table (for development safety)
c.execute("DROP TABLE IF EXISTS slots")

# Create fresh table
c.execute("""
CREATE TABLE IF NOT EXISTS slots (
    slot_id INTEGER PRIMARY KEY,
    zone TEXT,
    status TEXT,
    booked_time REAL
)
""")
conn.commit()

# Initialize slots
c.execute("SELECT COUNT(*) FROM slots")
if c.fetchone()[0] == 0:
    for i in range(1, TOTAL_SLOTS + 1):
        zone = random.choice(ZONES)
        status = random.choice(["Free", "Occupied"])
        c.execute(
            "INSERT INTO slots (slot_id, zone, status, booked_time) VALUES (?, ?, ?, ?)",
            (i, zone, status, None)
        )
    conn.commit()

# Fetch slots
c.execute("SELECT * FROM slots")
slots = c.fetchall()

# Auto-release booked slots after 60 seconds (simulation)
AUTO_RELEASE_TIME = 60
for slot in slots:
    slot_id, zone, status, booked_time = slot
    if status == "Booked" and booked_time:
        if time.time() - booked_time > AUTO_RELEASE_TIME:
            c.execute(
                "UPDATE slots SET status='Free', booked_time=NULL WHERE slot_id=?",
                (slot_id,)
            )
conn.commit()

# Re-fetch updated slots
c.execute("SELECT * FROM slots")
slots = c.fetchall()

# Stats
statuses = [slot[2] for slot in slots]
free = statuses.count("Free")
occupied = statuses.count("Occupied")
booked = statuses.count("Booked")

occupancy_rate = (occupied + booked) / TOTAL_SLOTS * 100
dynamic_price = 20 + (occupancy_rate / 100 * 30)

# Dashboard Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Slots", TOTAL_SLOTS)
col2.metric("Free", free)
col3.metric("Occupied", occupied)
col4.metric("Booked", booked)

st.progress(int(occupancy_rate))
st.write(f"Current Occupancy Rate: {round(occupancy_rate,2)}%")
st.write(f"Dynamic Parking Price: ₹{round(dynamic_price,2)}")

st.divider()
st.subheader("Parking Layout")

# Grid layout
columns = st.columns(6)

for index, slot in enumerate(slots):
    slot_id, zone, status, booked_time = slot
    col = columns[index % 6]

    if status == "Free":
        color = "#2ecc71"  # Green
    elif status == "Occupied":
        color = "#e74c3c"  # Red
    else:
        color = "#3498db"  # Blue

    with col:
        st.markdown(
            f"""
            <div style='
                background-color:{color};
                padding:20px;
                border-radius:12px;
                text-align:center;
                color:white;
                font-weight:bold;
                margin-bottom:10px;
            '>
            Slot {slot_id}<br>
            Zone {zone}<br>
            {status}
            </div>
            """,
            unsafe_allow_html=True
        )

        if status == "Free":
            if st.button(f"Book {slot_id}", key=f"book{slot_id}"):
                c.execute(
                    "UPDATE slots SET status='Booked', booked_time=? WHERE slot_id=?",
                    (time.time(), slot_id)
                )
                conn.commit()
                st.rerun()

        elif status == "Booked":
            if st.button(f"Release {slot_id}", key=f"release{slot_id}"):
                c.execute(
                    "UPDATE slots SET status='Free', booked_time=NULL WHERE slot_id=?",
                    (slot_id,)
                )
                conn.commit()
                st.rerun()

st.divider()
st.caption("🔵 Booked slots auto-release after 60 seconds (simulation mode).")
