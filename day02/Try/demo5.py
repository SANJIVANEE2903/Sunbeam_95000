import streamlit as st
import pandas as pd
import time

# 1. st.write(): General output (auto-detects type)
st.write("Hello, Streamlit!")
st.write(123, {"key": "value"})

# 2. st.markdown(): Rich text with Markdown formatting
st.markdown("**Bold text**, *italic text*, and [a link](https://streamlit.io)")

# 3. st.dataframe(): Display interactive tables
df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
st.dataframe(df)

# 4. st.json(): Display JSON data
st.json({"name": "Alice", "age": 25, "skills": ["Python", "ML"]})

# 5. st.toast(): Temporary alert message
st.toast("Data loaded successfully!", icon="✅")

# 6. st.title(): Page title
st.title("My Streamlit App")

# 7. st.header(): Section header
st.header("Section 1: Overview")

# 8. st.subheader(): Sub-heading
st.subheader("Details")

# 9. st.write_stream(): Stream output from a generator
def slow_text():
    for word in ["Loading", "data", "..."]:
        yield word + " "
        time.sleep(0.5)

st.write_stream(slow_text)

# 10. st.columns(): Divide screen into columns
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")
