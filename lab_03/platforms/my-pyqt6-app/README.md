# My PyQt6 Application

This is a simple PyQt6 application that demonstrates the use of a main window designed with Qt Designer.

## Project Structure

```
platforms
├── my-pyqt6-app
│   ├── src
│   │   ├── main.py          # Entry point of the application
│   │   ├── ui
│   │   │   └── main_window.ui # UI layout for the main window
│   │   └── resources
│   │       └── __init__.py  # Package for resources
│   ├── requirements.txt      # Project dependencies
│   └── README.md             # Project documentation
```

## Requirements

To run this application, you need to have the following dependencies installed:

- PyQt6
- requests

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Running the Application

To run the application, execute the following command in your terminal:

```
python src/main.py
```

Make sure you are in the `my-pyqt6-app` directory when running this command. 

## License

This project is licensed under the MIT License.