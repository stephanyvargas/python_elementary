# streamlit_pages/python_first_steps.py

import streamlit as st
import io
import sys

def python_onsite_compiler():
    # Code Compiler Box
    st.write("### Try Your Code Here! 🐍")
    st.write("Type your Python code below and click 'Run' to see it in action!")

    # Code input box
    code = st.text_area("Python Code:", value="print('Hello, World!')", height=150)

    # Run button and output
    if st.button("Run"):
        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()

        try:
            exec(code)  # Execute the code
        except Exception as e:
            st.error(f"Error: {e}")  # Display error if there's an issue in the code
        finally:
            # Reset stdout
            sys.stdout = old_stdout

        # Display output from the executed code
        output = redirected_output.getvalue()
        st.code(output, language="python")

python_onsite_compiler()

