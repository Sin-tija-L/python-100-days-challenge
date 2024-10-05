# 👉 Day 47 Challenge: Feel The Power Of My, erm, Stats!

<a href="https://youtu.be/8XHcmA7spX0?si=eI3yV-hsyQaKs2vS" target="_blank">📹 Dāvida video</a>


Today brings another challenge to help you practice the skills you've learned over the past few days.

In this challenge, we'll be recreating [Top Trumps](https://en.wikipedia.org/wiki/Top_Trumps), the game with the name that's been making British schoolboys snicker since 1978 (Ok, not really, but can you blame me for more British jokes?).

This is a card based stat battling game where you can compare stats for items in a category - TV show characters, trucks, cars, planes, cheese (mmmmm).

For details of the challenge, scoot on over to - yep, you guessed it - the challenge page.


## 👉 Day 47 Challenge

Alright Top Trumpers. Your program should work like this.

1. Pick a category. Something popular. You know like 'most handsome computer science teachers'. 😆
2. Store the information of **two** different objects in a **2D dictionary**.
3. The key field should be **name**.
4. The data in the sub-dictionary should be some stats about the object. For example:
   - **Intelligence**
   - **Handsomeness**
   - **L33t c0ding skillz**
   - **Baldness level**
5. Use an infinite loop to get the user to pick one of the two cards, then pick a stat from that card.
6. Display the chosen stat for both cards and output which has won.

🎉 **Extra points for:**
- Making the dictionary dynamic so you can add your own cards.
- Using a loop to play the game in a 2 player format, keeping track of points scored.

**Example:**

<img id="image" src="assets/day47_1.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>💡 Hints</summary>

- If you're adding your own cards dynamically, try using the `random.choice()` function to 'draw' two cards from the deck.

</details>

## Solution (No Peeking!)

<a href="https://youtu.be/s-sJhLRLYPE?si=o-N6HDTDEYoColoE" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import random

# Function to get valid input from the user
def get_valid_input(prompt, valid_choices):
    choice = input(prompt)
    while choice not in valid_choices:
        print("Invalid choice. Please try again.")
        choice = input(prompt)
    return choice

# Create a dictionary for each card with name and stats
cards = [
    {
        "name": "Mr. Morgan",
        "Intelligence": 90,
        "Handsomeness": 85,
        "L33t c0ding skillz": 95,
        "Baldness level": 99,
    },
    {
        "name": "Mr. Colley",
        "Intelligence": 88,
        "Handsomeness": 92,
        "L33t c0ding skillz": 90,
        "Baldness level": -68,
    },
]

# Initialize player scores
player1_score = 0
player2_score = 0

# Function to print card options
def print_card_options(cards):
    print("Choose your card:")
    for i, card in enumerate(cards, 1):
        print(f"{i} - {card['name']}")

# Function to print stat options
def print_stat_options(stat_choices):
    print("\nChoose your stat:")
    for i, stat in enumerate(stat_choices, 1):
        print(f"{i}. {stat}")

# Function to compare chosen stats between two cards
def compare_stats(cards, stat_choices, player_stat_choice):
    player1_stat = cards[0][stat_choices[player_stat_choice]]
    player2_stat = cards[1][stat_choices[player_stat_choice]]

    print(f"\n{cards[0]['name']} has a {stat_choices[player_stat_choice]} stat of {player1_stat}")
    print(f"{cards[1]['name']} has a {stat_choices[player_stat_choice]} stat of {player2_stat}")

    return player1_stat, player2_stat

# Function to determine the winner and update scores
def determine_winner(player1_stat, player2_stat, player1_score, player2_score):
    if player1_stat > player2_stat:
        print(f"************* {cards[0]['name']} wins! ********")
        player1_score += 1
    elif player2_stat > player1_stat:
        print(f"************* {cards[1]['name']} wins! ********")
        player2_score += 1
    else:
        print("************* It's a tie! ********")
    
    return player1_score, player2_score

# Function to play a single round
def play_round(cards, player1_score, player2_score):
    print("\n🌟 Top Trumps 🌟")
    print("Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator")

    # Let the player choose a card
    print_card_options(cards)
    player_choice = get_valid_input("> ", ["1", "2"])
    player_choice = int(player_choice) - 1  # Adjust for 0-based index

    # Choose a stat
    stat_choices = list(cards[0].keys())[1:]  # Exclude "name" from stat choices
    print_stat_options(stat_choices)
    
    player_stat_choice = get_valid_input("> ", map(str, range(1, len(stat_choices) + 1)))
    player_stat_choice = int(player_stat_choice) - 1  # Adjust for 0-based index

    # Compare the chosen stat and determine the winner
    player1_stat, player2_stat = compare_stats(cards, stat_choices, player_stat_choice)
    player1_score, player2_score = determine_winner(player1_stat, player2_stat, player1_score, player2_score)

    # Display the current score
    print(f"\nPlayer 1 Score: {player1_score}, Player 2 Score: {player2_score}")

    return player1_score, player2_score

# Main game loop
def main_game():
    player1_score = 0
    player2_score = 0
    
    while True:
        player1_score, player2_score = play_round(cards, player1_score, player2_score)

        # Ask if the players want to continue
        play_again = get_valid_input("Again? (y/n) > ", ["y", "n"]).lower()
        if play_again != "y":
            print("Thanks for playing! Final scores:")
            print(f"Player 1: {player1_score}, Player 2: {player2_score}")
            break

# Run the game
main_game()
```

</details>