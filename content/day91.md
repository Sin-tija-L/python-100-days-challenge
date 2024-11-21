# Day 91: Funny, Eh? Funny, How? 😂  

The **API** we're using today is the fantastic [JokeAPI](https://jokeapi.dev), which offers jokes in categories like programming, general, and dark humor. With advanced filtering and response customization, it's a great way to learn API integration while adding a touch of humor. 😄  

This tutorial is adjusted for **VSCode**, so make sure you're running it using the command:  
```python
python3 python_files/day91.py
```  

---

### 👉 Get a Random Joke  

Here's how to fetch a random programming joke from the API and display it. The API provides jokes in JSON format, and you can request specific categories or types (single-line or two-part jokes).  

```python
import requests, json

# Fetch a random programming joke
url = "https://v2.jokeapi.dev/joke/Programming"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    joke_data = response.json()
    
    # Print the entire response nicely formatted
    print(json.dumps(joke_data, indent=2))
else:
    print(f"Error: Unable to fetch jokes. Status code {response.status_code}")
```

<img id="image" src="assets/day91_1.png" alt="day91 image" width="450">

---

### 👉 Display Only the Joke 🎭  

If you only want to display the joke, update the code as follows:  

```python
import requests, json

# Fetch a random programming joke
url = "https://v2.jokeapi.dev/joke/Programming"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    joke_data = response.json()

    # Check if it's a single-line or two-part joke
    if joke_data["type"] == "single":
        print(joke_data["joke"])  # Output single-line joke
    else:
        print(f"{joke_data['setup']} - {joke_data['delivery']}")  # Output two-part joke

else:
    print(f"Error: Unable to fetch jokes. Status code {response.status_code}")
```

<img id="image" src="assets/day91_2.png" alt="day91 image" width="720">

---

## Why This API is Great for Learning  

The **JokeAPI** is an excellent tool for learning about API integration because:  

1. **Customizable Categories**: Choose jokes from categories like programming, general, or pun.  
2. **Multiple Formats**: Request jokes as single-line or two-part for variety.  
3. **Advanced Filtering**: Exclude certain categories or flags for tailored results.  
4. **Educational Documentation**: Comprehensive examples make it easy to get started.  

Explore more possibilities in the [JokeAPI documentation](https://jokeapi.dev/documentation). Have fun coding with humor! 🎉

---

## Common Errors
 
 First, delete any other code in your `day91` files. Copy each code snippet below into `day91` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

👉 What's the problem here?

 ```python
import requests, json

url = "https://v2.jokeapi.dev/joke/Programming"
response = requests.get(url)

if response.status_code == 200:
    joke_data = response.json()

    if joke_data["type"] = "single": 
        print(joke_data["joke"])
    else:
        print(f"{joke_data['setup']} + {joke_data['delivery']}")

else:
    print(f"Error: Unable to fetch jokes. Status code {response.status_code}")
```

<details>
<summary>👀 Answer</summary>

```python
import requests, json

url = "https://v2.jokeapi.dev/joke/Programming"
response = requests.get(url)

if response.status_code == 200:
    joke_data = response.json()

    if joke_data["type"] == "single": # Mistake 1: Using '=' instead of '==' for comparison
        print(joke_data["joke"]) 
    else:
        print(f"{joke_data['setup']} - {joke_data['delivery']}") # Mistake 2: Using '+' instead of '-' for formatting

else:
    print(f"Error: Unable to fetch jokes. Status code {response.status_code}")
```

</details>

---

## Fix My Code
 
 First, delete any other code in your `day91` files. Copy each code snippet below into `day91` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

  ```python
import requests, json

url = "https://v2.jokeapi.dev/joke/Programming"
response = requests.get(url)

if response.status_code == 200:
    joke_data = response.json()
    
    print(json.dumps(joke_data, indent=two))
    print(joke_data['random'])
else:
    print("Error Unable to fetch jokes. Status code {response.status_code}") 

```

<details>
<summary>👀 Answer</summary>

```python
import requests, json

url = "https://v2.jokeapi.dev/joke/Programming"
response = requests.get(url)

if response.status_code == 200:
    joke_data = response.json()
    
    print(json.dumps(joke_data, indent=2))   # Mistake 1: Using "two" instead of 2 for the indent value
      # Mistake 2: Attempting to access a non-existent key 'random' in the joke_data dictionary
else:
    print(f"Error: Unable to fetch jokes. Status code {response.status_code}")  # Mistake 3: Missing 'f' before the string for string interpolation
```

</details>

---

# Day 91 Challenge: Your Personalized Joke Vault! 🎭🤣  

Today’s challenge takes humor to the next level by building a **personalized joke-saving program**! This program will let you:  

1. **Fetch a Random Joke**: Get a fresh dose of humor on-demand.  
2. **Save Your Favorites**: Decide which jokes are worth keeping for later laughs.  
3. **View Your Saved Jokes**: Build and display your personal joke collection.  

Let’s turn laughter into a fun and interactive coding experience! 🚀  

---

## 📝 **Challenge Requirements**  

Here’s what your program should do step-by-step:  

1. **Fetch a Random Joke**:  
   - Use the [JokeAPI](https://jokeapi.dev) to get a random joke.  
   - Display the joke to the user.  

2. **Save Jokes by Choice**:  
   - Ask the user if they want to save the joke.  
   - If they say yes, store the joke's **ID number** and content in a local Python dictionary.  

3. **View Saved Jokes**:  
   - Ask the user if they’d like to see their saved jokes.  
   - If yes, display all the jokes saved in the dictionary, formatted nicely.  

---

## 🚀 **Stretch Goals (Optional)**  

1. **Filter by Joke Category**:  
   Allow users to specify the category of jokes they want (e.g., programming, pun, etc.).  

2. **Add a Search Feature**:  
   Let users search for saved jokes by keywords in the setup or delivery.  

3. **Save Data Persistently**:  
   Store the saved jokes in a file (e.g., `saved_jokes.json`) so they persist across program runs.  

4. **Remove Jokes**:  
   Add functionality to delete jokes from the saved list.  

---

## 💡 **Implementation Hints**  

1. **Fetching the Joke**:  
   Use the API endpoint to get a random joke:  
   ```python
   https://v2.jokeapi.dev/joke/Any
   ```

2. **Dynamic User Input**:  
   Use `input()` to interact with the user for saving jokes and displaying saved ones.  

3. **Saving Jokes**:  
   Use a Python dictionary to store jokes with their IDs as keys:  
   ```python
   saved_jokes = {}
   ```

4. **Viewing Saved Jokes**:  
   Loop through the dictionary and print each joke in a user-friendly format:  
   ```python
   for joke_id, joke_content in saved_jokes.items():
       print(f"ID: {joke_id}, Joke: {joke_content}")
   ```

---

## 🎉 **What You’ll Learn**  

By completing this challenge, you’ll strengthen your understanding of:  

- **APIs**: Fetching and working with data from APIs.  
- **Data Storage**: Using Python dictionaries to manage and display saved data.  
- **User Interaction**: Building an interactive command-line program.  
- **Error Handling**: Managing invalid user inputs gracefully.  

---

Take on the challenge, bring humor to your code, and build your personalized joke vault! 😄🎭 Good luck! 🚀

<img id="image" src="assets/day91_3.png" alt="day91 image" width="720">

<img id="image" src="assets/day91_4.png" alt="day91 image" width="720">

---

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

```python
import requests
import json
import os

# Global variables
JOKES_DIR = "python_files/jokes"
SAVED_JOKES_FILE = os.path.join(JOKES_DIR, "saved_jokes.json")
AVAILABLE_CATEGORIES = ["Programming", "Misc", "Dark", "Pun", "Spooky", "Christmas"]


def ensure_directory():
    os.makedirs(JOKES_DIR, exist_ok=True)


def load_saved_jokes():
    if os.path.exists(SAVED_JOKES_FILE):
        with open(SAVED_JOKES_FILE, "r") as file:
            return json.load(file)
    return {}


def save_jokes_to_file(saved_jokes):
    with open(SAVED_JOKES_FILE, "w") as file:
        json.dump(saved_jokes, file, indent=2)
    print(f"Saved jokes have been written to '{SAVED_JOKES_FILE}'.")


def display_categories():
    print("\nAvailable joke categories:")
    for category in AVAILABLE_CATEGORIES:
        print(f"- {category}")


def get_category():
    chosen_category = input("\nChoose a category for your joke (leave blank for 'Any'): ").strip().capitalize()
    if chosen_category not in AVAILABLE_CATEGORIES and chosen_category != "":
        print(f"Invalid category '{chosen_category}'. Defaulting to 'Any'.")
        chosen_category = "Any"
    return chosen_category


def fetch_joke(category):
    url = f"https://v2.jokeapi.dev/joke/{category if category else 'Any'}"
    response = requests.get(url, headers={"Accept": "application/json"})
    if response.status_code != 200:
        print("Error fetching joke. Please try again.")
        return None
    return response.json()


def display_joke(joke):
    if joke["type"] == "single":
        print(f"\nJoke: {joke['joke']}")
        return joke["joke"]
    else:
        print(f"\nJoke: {joke['setup']} - {joke['delivery']}")
        return f"{joke['setup']} - {joke['delivery']}"


def save_joke(joke_id, joke_text, saved_jokes):
    saved_jokes[joke_id] = joke_text
    print("Joke saved!")


def view_saved_jokes(saved_jokes):
    if saved_jokes:
        print("\nSaved Jokes:")
        for joke_id, joke_text in saved_jokes.items():
            print(f"- ID: {joke_id}, Joke: {joke_text}")
    else:
        print("No jokes saved.")


def main():
    """Main program loop."""
    ensure_directory()
    saved_jokes = load_saved_jokes()

    while True:
        display_categories()
        chosen_category = get_category()

        joke = fetch_joke(chosen_category)
        if not joke:
            continue

        joke_text = display_joke(joke)

        save_joke_option = input("\nDo you want to save this joke? (yes/no): ").strip().lower()
        if save_joke_option == "yes":
            save_joke(joke["id"], joke_text, saved_jokes)
            save_jokes_to_file(saved_jokes)

        view_saved_jokes_option = input("\nDo you want to see your saved jokes? (yes/no): ").strip().lower()
        if view_saved_jokes_option == "yes":
            view_saved_jokes(saved_jokes)

        continue_program = input("\nDo you want to continue? (yes to continue, no to exit): ").strip().lower()
        if continue_program == "no":
            print("Goodbye! Hope you enjoyed the jokes! 🎭")
            break


if __name__ == "__main__":
    main()
```

</details>