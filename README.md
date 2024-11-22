# AutoCalc Notepad

AutoCalc Notepad is a simple, interactive notepad application built with Python and Tkinter. It allows you to perform real-time calculations (Add, Subtract, Multiply, Divide) on numbers entered into the text area. Perfect for quick calculations or practicing arithmetic!

## Features

- **Dynamic Operations**: Automatically calculates numbers in the text area based on the selected mode.
- **Modes**:
  - **Add**: Adds all numbers.
  - **Subtract**: Subtracts numbers sequentially.
  - **Multiply**: Multiplies all numbers.
  - **Divide**: Divides numbers sequentially with error handling for division by zero.
- **Real-Time Updates**: Results update as you type or change the mode.
- **User-Friendly Interface**: Clean, minimal interface with buttons to select operation modes.

## Screenshots
(Include screenshots or gifs here of the app in use for better visual representation.)

## Requirements

- Python 3.x
- Tkinter (pre-installed with most Python distributions)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/AutoCalc-Notepad.git
   ```
2. Navigate to the project folder:
   ```bash
   cd AutoCalc-Notepad
   ```
3. Run the application:
   ```bash
   python autocac_notepad.py
   ```

## Usage

1. Enter numbers and text freely in the text area.
2. Click on the operation mode buttons (`Sum`, `Subtract`, `Multiply`, `Divide`) to switch between calculations.
3. The result will automatically update in real-time, displayed at the bottom of the app.

### Example
- Input: `10 20 30`
  - **Add**: `60`
  - **Subtract**: `-40`
  - **Multiply**: `6000`
  - **Divide**: `0.01667`

## Error Handling

- **Division by Zero**: Displays `Error (Division by Zero)` if division by zero occurs.

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

Thanks to the Python and Tkinter community for making GUI development accessible and enjoyable!
