import streamlit as st
from logic_engine import clear_all_tasks, auto_schedule

# --- CUSTOM CSS FOR JARVIS VIBE ---
st.markdown("""
    <style>
    .main { background-color: #0D1117; }
    .stButton>button { border-radius: 20px; border: 1px solid #00FF41; color: #00FF41; background-color: transparent; }
    .stButton>button:hover { background-color: #00FF41; color: black; }
    div[data-testid="stMetricValue"] { color: #00FF41; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
col_logo, col_text = st.columns([1, 4])
with col_text:
    st.title("🧬 AETHER-FLOW // JARVIS v3.1")
    st.caption("NEURAL SCHEDULER ACTIVE | CHENNAI NODE")

# --- ACTION RADIUS ---
st.divider()
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("☢️ NUCLEAR RESET"):
        clear_all_tasks()
        st.toast("Notion Database Purged.", icon="🗑️")

with c2:
    if st.button("🛰️ SYNC SYLLABUS"):
        # Your AI Analysis call here
        st.toast("Analyzing Timetable...", icon="🧠")

with c3:
    if st.button("🔄 AUTO-SHUFFLE"):
        auto_schedule()
        st.success("Timeline Optimized.")

# --- THE "JARVIS" HUD ---
st.subheader("📊 Tactical Overview")
m1, m2, m3 = st.columns(3)
m1.metric("Exam Countdown", "8 Days", "May 21")
m2.metric("Knowledge Score", "68%", "+12%")
m3.metric("Focus Mode", "ACTIVE", "S23 Ultra Locked")

# --- TASK HUD ---
st.write("---")
st.subheader("⚡ Next Objective")
# Use st.container for a 'card' look
with st.container(border=True):
    st.markdown("### 🧬 Genetic Engineering: rDNA Vectors")
    st.progress(0.4)
    st.write("⏱️ *Estimated completion: 14:30 IST*")
