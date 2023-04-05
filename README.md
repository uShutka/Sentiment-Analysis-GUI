# Sentiment-Analysis-GUI

The Sentiment Analysis GUI is a Python application that allows users to input text and analyze its sentiment using TextBlob, a Python library for natural language processing. The application has a graphical user interface (GUI) created using the tkinter library.

## Requirements

* Python 3.6 or higher
* tkinter
* textblob

## Installation

1. Clone the repository: `git clone https://github.com/your-username/Sentiment-Analysis-GUI.git`
2. Navigate to the project directory: `cd Sentiment-Analysis-GUI`
3. Install the required libraries: `pip install -r requirements.txt`

## Usage

To run the application, navigate to the project directory and run the following command:

```
python main.py
```

When the application starts, you will see a window with a text box and an "Analyze" button. Enter the text you want to analyze in the text box and click the "Analyze" button. The application will use TextBlob to analyze the sentiment of the input text and display the sentiment score in a message box.

The sentiment score ranges from -1 (most negative) to 1 (most positive), with 0 indicating a neutral sentiment. You can use the sentiment score to gauge the overall tone of the text and make informed decisions based on that analysis.

## Contributing

If you find a bug or have a feature request, please open an issue or submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
