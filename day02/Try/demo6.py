import streamlit as st

# Initialize the counter in session state if it doesn't exist
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Create two columns for Increment and Reset buttons
col1, col2 = st.columns(2)

with col1:
    # Increment button
    if st.button("Increment"):
        st.session_state.counter += 1

with col2:
    # Reset button
    if st.button("Reset"):
        st.session_state.counter = 0

# Display the current counter value
st.write(f"**Counter Value:** {st.session_state.counter}")
