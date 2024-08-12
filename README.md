# slot-machine-using-python

## Description
This project implements a text-based slot machine game with data tracking and visualization features. Players can bet on multiple lines, experience bonus rounds, and participate in risk games. The game tracks player performance and provides visual analytics at the end of the session.

## Features
- Customizable slot machine with different symbols and values
- Multi-line betting system
- Bonus round with free spins
- Double-or-nothing risk game
- Game history tracking
- Visual analytics of game performance

## Requirements
- Python 3.7+
- pandas
- matplotlib

## Installation
1. Clone this repository:
   ```
   https://github.com/Athrudev/slot-machine-using-python.git
   ```
2. Navigate to the project directory:
   ```
   cd slot-machine-using-python
   ```
3. Install required packages:
   ```
   pip install pandas matplotlib
   ```

## Usage
Run the game by executing:
```
python main.py
```

## Live Preview

For a live preview of this project, you can use Google Colab. Click on the link below to open the notebook:

[Open in Google Colab](https://colab.research.google.com/drive/1BDvpgEwmT6XnGz4KWSHR5KTBXJV5-Qn6?usp=sharing)

https://colab.research.google.com/drive/1BDvpgEwmT6XnGz4KWSHR5KTBXJV5-Qn6?usp=sharing


Follow the on-screen prompts to play:
1. Make an initial deposit
2. Choose the number of lines to bet on
3. Set your bet amount per line
4. Press Enter to spin or 'q' to quit

## Game Rules
- Win by matching symbols across the lines you bet on
- 'BONUS' symbol on the middle row triggers a bonus round
- After each win, you can choose to play a double-or-nothing risk game

## Data Analytics
At the end of your gaming session, the program will display:
- A summary of your game statistics
- A plot of your balance history
- A histogram of your win distribution
- A graph of your cumulative Return on Investment (ROI)

## Customization
You can customize the game by modifying:
- `symbol_count` and `symbol_value` dictionaries to change symbol frequencies and values
- `MAX_LINES`, `MAX_BET`, and `MIN_BET` constants to adjust betting limits

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/Athrudev/slot-machine-using-python/issues) if you want to contribute.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
[Your Name]

## Acknowledgements
- This project was created as a learning exercise in Python programming, data management with pandas, and data visualization with matplotlib.
