import random as r
import time
import pandas as pd
import matplotlib.pyplot as plt

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    'A': 1,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 8,
    'BONUS': 1
}

symbol_value = {
    'A': 10,
    'B': 7,
    'C': 5,
    'D': 3,
    'E': 2,
    'BONUS': 0
}

class GameHistory:
    def __init__(self):
        self.history = pd.DataFrame(columns=['Spin', 'Bet', 'Lines', 'Win', 'Balance'])
        self.spin_count = 0

    def add_record(self, bet, lines, win, balance):
        self.spin_count += 1
        new_record = pd.DataFrame({
            'Spin': [self.spin_count],
            'Bet': [bet],
            'Lines': [lines],
            'Win': [win],
            'Balance': [balance]
        })
        self.history = pd.concat([self.history, new_record], ignore_index=True)

    def get_summary(self):
        summary = self.history.describe()
        return summary

def get_winning(columns, lines, bet, values):
    winning = 0
    win_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol] * bet
            win_lines.append(line + 1)
    return winning, win_lines

def get_slot_machine_spins(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_cnt in symbols.items():
        for _ in range(symbol_cnt):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        current_cols = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = r.choice(current_symbols)
            current_symbols.remove(value)
            current_cols.append(value)

        columns.append(current_cols)

    return columns

def print_slot_machine(columns):
    print("\n╔═════════════════════╗")
    print("║      SLOT MACHINE   ║")
    print("╠═════════════════════╣")
    for row in range(len(columns[0])):
        print("║", end="")
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(f"  {column[row]}  │", end="")
            else:
                print(f"  {column[row]}  ", end="")
        print("║")
        if row < len(columns[0]) - 1:
            print("║───────┼───────┼───────║")
    print("╚═════════════════════╝")

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0....!")
        else:
            print("Please enter a number.")
    return amount

def get_num_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"lines must be between (1-{MAX_LINES}).....!")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}...!")
        else:
            print("Please enter a number.")
    return bet

def bonus_round(balance, bet):
    free_spins = r.randint(5, 10)
    print(f"\n🌟 BONUS ROUND! You've won {free_spins} free spins! 🌟")
    total_bonus_winnings = 0
    
    for _ in range(free_spins):
        slots = get_slot_machine_spins(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winning, win_lines = get_winning(slots, MAX_LINES, bet, symbol_value)
        total_bonus_winnings += winning
        print(f"Free spin win: ${winning}")
    
    print(f"Total bonus winnings: ${total_bonus_winnings}")
    return total_bonus_winnings

def risk_game(winning):
    print(f"\n🎲 RISK GAME: You've won ${winning}! Double or nothing? 🎲")
    choice = input("Enter 'y' to play or any other key to keep your winnings: ").lower()
    if choice == 'y':
        print("Guess if the next number will be high (7-13) or low (1-6).")
        guess = input("Enter 'h' for high or 'l' for low: ").lower()
        number = r.randint(1, 13)
        print(f"The number is: {number}")
        if (guess == 'h' and number >= 7) or (guess == 'l' and number <= 6):
            print(f"Congratulations! You've doubled your winnings to ${winning * 2}")
            return winning * 2
        else:
            print("Sorry, you've lost this round.")
            return 0
    return winning

def game(balance, game_history):
    lines = get_num_of_lines()
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
        print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        return 0

    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')

    slots = get_slot_machine_spins(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winning, win_lines = get_winning(slots, lines, bet, symbol_value)
    
    if winning > 0:
        print(f"You won ${winning}!")
        print(f"You won on lines:", *win_lines)
        winning = risk_game(winning)
    else:
        print("Sorry, no win this time.")

    if 'BONUS' in [column[1] for column in slots]:
        bonus_winnings = bonus_round(balance, bet)
        winning += bonus_winnings

    balance += winning - total_bet
    game_history.add_record(total_bet, lines, winning, balance)
    
    return balance

def plot_balance_history(game_history):
    plt.figure(figsize=(10, 6))
    plt.plot(game_history.history['Spin'], game_history.history['Balance'], marker='o')
    plt.title('Balance History')
    plt.xlabel('Spin Number')
    plt.ylabel('Balance ($)')
    plt.grid(True)
    plt.show()

def plot_win_distribution(game_history):
    plt.figure(figsize=(10, 6))
    game_history.history['Win'].hist(bins=20)
    plt.title('Distribution of Wins')
    plt.xlabel('Win Amount ($)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def analyze_roi(game_history):
    game_history.history['ROI'] = (game_history.history['Win'] - game_history.history['Bet']) / game_history.history['Bet'] * 100
    
    plt.figure(figsize=(10, 6))
    plt.plot(game_history.history['Spin'], game_history.history['ROI'].cumsum(), marker='o')
    plt.title('Cumulative Return on Investment')
    plt.xlabel('Spin Number')
    plt.ylabel('Cumulative ROI (%)')
    plt.grid(True)
    plt.show()

def main():
    balance = deposit()
    game_history = GameHistory()

    while True:
        print(f"\n💰 Current Balance: ${balance} 💰")
        if balance == 0:
            print("Your balance is zero. You need to deposit more money to continue playing.")
            deposit_more = input("Would you like to deposit more? (yes/no): ").lower()
            if deposit_more == 'yes':
                balance += deposit()
            else:
                break
        
        user = input('Press Enter to play (q to quit): ').lower()
        if user == 'q':
            break
        
        balance = game(balance, game_history)
    
    print(f'\n🎉 Thanks for playing! You left with ${balance} 🎉')
    print("\nGame Summary:")
    print(game_history.get_summary())

    plot_balance_history(game_history)
    plot_win_distribution(game_history)
    analyze_roi(game_history)

if __name__ == "__main__":
    main()
