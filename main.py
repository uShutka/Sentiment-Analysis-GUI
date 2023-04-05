import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob

# This function is called when the user clicks the "Analyze" button
def analyze_text():
    # Get the text entered by the user from the text box
    input_text = input_text_box.get("1.0", "end-1c")

    # Use TextBlob to analyze the sentiment of the input text
    sentiment = TextBlob(input_text).sentiment.polarity

    # Display a message box with the sentiment score
    messagebox.showinfo("Sentiment Analysis Result", f"The sentiment score is: {sentiment}")

# Create a new tkinter window
window = tk.Tk()

# Set the title of the window
window.title("Sentiment Analysis")

# Create a label for the input text box
input_text_label = tk.Label(text="Enter text to analyze:")

# Create a text box for the user to enter text
input_text_box = tk.Text(height=10)

# Create a button to trigger the analysis
analyze_button = tk.Button(text="Analyze", command=analyze_text)

# Add the label, text box, and button to the window using a grid layout
input_text_label.grid(row=0, column=0, padx=10, pady=10)
input_text_box.grid(row=1, column=0, padx=10, pady=10)
analyze_button.grid(row=2, column=0, padx=10, pady=10)

# Start the tkinter event loop
window.mainloop()
