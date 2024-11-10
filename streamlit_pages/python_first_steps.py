# streamlit_pages/python_first_steps.py

import streamlit as st

def python_first_steps():
    st.write("### Python First Steps Quiz 🐍")
    st.write("Answer these questions to see how much you know about Python! You can reveal the answer after each question.")

    # Multiple-choice questions with revealable answers, emojis, and examples
    q1 = st.radio("1. 📢 How do you make Python show something on the screen?",
                  ("A. shout()", "B. print()", "C. display()"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: B. `print()` 🖨️")
        st.write("Example: `print('Hello, world!')`")

    q2 = st.radio("2. 📝 Which character is used for comments in Python?",
                  ("A. //", "B. ##", "C. #"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: C. `#` 💬")
        st.write("Example: `# This is a comment`")

    q3 = st.radio("3. 🖊️ Which one of these is used to store words or sentences?",
                  ("A. int", "B. str", "C. list"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: B. `str` 📄")
        st.write("Example: `name = 'Alice'`")

    q4 = st.radio("4. ➕ What symbol do you use to add two numbers together?",
                  ("A. +", "B. -", "C. *"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. `+` ➕")
        st.write("Example: `5 + 3` gives `8`")

    q5 = st.radio("5. 📏 What function gives you the number of items in a list?",
                  ("A. len()", "B. count()", "C. size()"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. `len()` 📏")
        st.write("Example: `len([1, 2, 3])` gives `3`")

    q6 = st.radio("6. 📦 What is a variable?",
                  ("A. A container for data", "B. A type of loop", "C. A math symbol"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. A container for data 📦")
        st.write("Example: `age = 12` creates a variable called `age`")

    q7 = st.radio("7. 🖥️ How do you assign the number 10 to a variable called x?",
                  ("A. x = 10", "B. let x = 10", "C. x : 10"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. `x = 10` ✅")
        st.write("Example: `x = 10`")

    q8 = st.radio("8. ⚙️ What does `def` do in Python?",
                  ("A. Starts a function", "B. Ends a function", "C. Loops a function"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. Starts a function 🔄")
        st.write("Example: `def greet():` starts a function called `greet`")

    q9 = st.radio("9. 🔁 Why do we use loops?",
                  ("A. To repeat actions", "B. To end the program", "C. To make a comment"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. To repeat actions 🔄")
        st.write("Example: `for i in range(3): print('Hello')` prints 'Hello' 3 times")

    q10 = st.radio("10. 🔄 Which one of these is a loop?",
                   ("A. while", "B. when", "C. what"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. `while` 🔄")
        st.write("Example: `while x < 5: print(x)` repeats while `x` is less than 5")

    # Fun coding scenarios with revealable answers
    q11 = st.selectbox("11. 👋 How would you greet someone 5 times?",
                       ("A. print('Hello' 5 times)", "B. Use a loop to print 'Hello'", "C. shout('Hello')"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: B. Use a loop to print 'Hello' 👋")
        st.write("Example: `for i in range(5): print('Hello')`")

    q12 = st.selectbox("12. ➕ Which code creates a function to add two numbers?",
                       ("A. def add(a, b): return a + b", "B. function add(a, b)", "C. add a + b"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. `def add(a, b): return a + b` 📝")
        st.write("Example: `def add(a, b): return a + b`")

    q13 = st.radio("13. 🔢 How would you print numbers 1 to 5?",
                   ("A. Use a loop", "B. print(1,2,3,4,5)", "C. print('1-5')"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. Use a loop 🔢")
        st.write("Example: `for i in range(1, 6): print(i)`")

    q14 = st.radio("14. 🔁 Which statement keeps running until x equals 3?",
                   ("A. while x != 3", "B. while x == 3", "C. repeat until x is 3"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. `while x != 3` ⏳")
        st.write("Example: `while x != 3: x += 1`")

    q15 = st.radio("15. 🔍 How do you check if a number is even?",
                   ("A. if number % 2 == 0", "B. if number == even", "C. if number / 2"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. `if number % 2 == 0` ⚖️")
        st.write("Example: `if number % 2 == 0: print('Even')`")

    # More questions with revealable answers
    q16 = st.radio("16. 📜 What is a list?",
                   ("A. A way to organize items", "B. A math operation", "C. A function"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. A way to organize items 📋")
        st.write("Example: `my_list = [1, 2, 3]` creates a list")

    q17 = st.radio("17. 📖 What is a dictionary?",
                   ("A. A book of words", "B. A place to store data as key-value pairs", "C. A list of items"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: B. A place to store data as key-value pairs 📖")
        st.write("Example: `my_dict = {'name': 'Alice', 'age': 10}`")

    q18 = st.radio("18. 🛠️ How do you get the first item in `my_list`?",
                   ("A. my_list[0]", "B. my_list[1]", "C. my_list[first]"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. `my_list[0]` 🔢")
        st.write("Example: `my_list[0]` gives the first item")

    q19 = st.radio("19. 📌 What is a parameter in a function?",
                   ("A. Data passed to the function", "B. The function name", "C. The result of a function"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. Data passed to the function 📥")
        st.write("Example: `def greet(name): print('Hello,', name)`")

    q20 = st.radio("20. 🔙 What does `return` do?",
                   ("A. Gives a result back", "B. Stops the function", "C. Adds two numbers"))
    with st.expander("🔍 Reveal Answer"):
        st.write("Answer: A. Gives a result back 🔙")
        st.write("Example: `return a + b` gives back the result of `a + b`")

python_first_steps()
