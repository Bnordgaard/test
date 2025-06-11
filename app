import streamlit as st
from calculations.addition import add
from calculations.multiplication import multiply
from visualization.plot_results import plot_results

st.title("Simple X and Y Processor")

# Input fields
x = st.number_input("Enter value for x", value=0.0)
y = st.number_input("Enter value for y", value=0.0)

# Processing
sum_result = add(x, y)
product_result = multiply(x, y)

# Output
st.write(f"**Sum (x + y):** {sum_result}")
st.write(f"**Product (x * y):** {product_result}")

# Plotting
fig = plot_results(x, y, sum_result, product_result)
st.pyplot(fig)
