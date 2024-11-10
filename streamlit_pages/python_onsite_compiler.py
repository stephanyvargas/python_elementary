# streamlit_pages/python_onsite_compiler.py

import streamlit as st
import io
import sys

def python_onsite_compiler():
    st.sidebar.write("## Python Code Compiler 🐍")
    st.sidebar.write("Type your Python code below and click 'Run' to see it in action!")

    # Code input in the sidebar
    code = st.sidebar.text_area("Python Code:", value="print('Hello, World!')", height=150)

    # Run button in the sidebar
    if st.sidebar.button("Run"):
        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()

        try:
            exec(code)  # Execute the code
        except Exception as e:
            st.sidebar.error(f"Error: {e}")  # Display error in the sidebar
        finally:
            # Reset stdout
            sys.stdout = old_stdout

        # Display output from the executed code in the sidebar
        output = redirected_output.getvalue()
        if output:
            st.sidebar.write("### Output")
            st.sidebar.code(output, language="python")
        else:
            st.sidebar.write("### Output")
            st.sidebar.write("No output produced.")
