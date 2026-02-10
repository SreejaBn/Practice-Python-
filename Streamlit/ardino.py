import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Arduino Simulator", layout="wide")
st.title("Arduino Circuit Simulator")

# ---------- PIN CONFIG ----------
led_pin = st.selectbox("LED Pin", list(range(2, 14)), index=8)

button_pin = st.selectbox(
    "Button Pin",
    [p for p in range(2, 14) if p != led_pin],
    index=0,
)

st.subheader("Generated Arduino Code")

code = f"""
int led = {led_pin};
int button = {button_pin};

void setup() {{
  pinMode(led, OUTPUT);
  pinMode(button, INPUT);
}}

void loop() {{
  digitalWrite(led, digitalRead(button));
}}
"""

st.code(code, language="cpp")

# ---------- WOKWI SIMULATOR ----------
st.divider()
st.subheader("Simulation")

WOKWI_PROJECT = "https://wokwi.com/projects/new/arduino-uno"

components.iframe(WOKWI_PROJECT, height=650, scrolling=True)
