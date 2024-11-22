# Day 96: Web Scraping 🌐

Some websites don't have lovely APIs for us to interface with. 

If we want data from these pages, we need to use a technique called **web scraping**. This involves downloading the entire webpage and extracting the information we need. 💡

---

### Get Started 🚀

👉 Go to a website [WebScraper](https://webscraper.io/test-sites/e-commerce/scroll). Copy the URL.

<img id="image" src="assets/day96_1.png" alt="day96 image" width="720">

Example URL:  
```python
url = "https://webscraper.io/test-sites/e-commerce/scroll"
 ```

---

### Import Libraries 📚

Import the required libraries:  
- `requests` for downloading web content  
- `BeautifulSoup` for parsing HTML

Run your code once to ensure all necessary libraries are installed. Pro tip: You can use **pip** in your VSCode terminal to install missing libraries! 😎

```python
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/scroll"
```

👉 Install **bs4**

```python
pip3 install beautifulsoup4  
```

---

### Fetch Webpage Content 🌍

👉 Use `requests` to get the webpage as text. This step ensures you're downloading the page's HTML correctly.

```python
response = requests.get(url)
html = response.text
print(html)  # This shows you the raw HTML of the webpage
```

---

### Parse HTML with BeautifulSoup 🥣

👉 Use `BeautifulSoup` to process the HTML and make it more structured.

```python
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/scroll"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
```

#### Pro Tip for Women in Tech 👩‍💻:
Inspect the webpage in your browser **(Right-click → Inspect)** to understand its structure and find the information you need.

---

### Extract Restaurant Links 🔗

Let’s extract the links to items:
 
👉 On [WebScraper](https://webscraper.io/test-sites/e-commerce/scroll), right-click the first item from the grid and select **Inspect**. Look for an `<a>` tag with a unique class (e.g., `title`).

<img id="image" src="assets/day96_2.png" alt="day96 image" width="720">

```python
<a href="/test-sites/e-commerce/scroll/product/17" class="title" title="IdeaTab A3500-H">IdeaTab A3500-...</a>
```

---

### Store results

👉 I've created a new variable to store the result of the beautiful soup search.
- `find_all` takes two arguments. The first is the `a` tag. The second is a dictionary that tells it what class to search for. This effectively says *'find me all the a tags with this class in them.'*
- I've printed the `len` of those results to see how many I get back.

```python
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/scroll"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

myLinks = soup.find_all("a", {"class":"title"})
print(len(myLinks))
```

---

### Loop Through Results 🔄

👉 Use a loop to display the restaurant names and their links. Add a counter to skip unnecessary items.

```python
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/scroll"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

myLinks = soup.find_all("a", {"class":"title"})

for link in myLinks:
    print(link.text)  # Item name
```

👉 I'm also going to include the link to the item in the output by using a dictionary.

```python
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/scroll"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

myLinks = soup.find_all("a", {"class":"title"})

counter = 0
for link in myLinks:
    print(link.text)  # Item name
    print(link["href"])  # Full link
    counter += 1
```

<img id="image" src="assets/day96_3.png" alt="day96 image" width="720">

---

### Add an fstring

👉 The web links are local, they aren't relative to the site I'm using, so I've formatted the `print(link["href"])` as an fString to add the relative address (that I found in the Yelp inspect code).

```python
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/scroll"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

myLinks = soup.find_all("a", {"class":"title"})

counter = 0
for link in myLinks:
    print(link.text)  # Item name
    print(link["href"])  # Full link
    print(f"""https://webscraper.io{link["href"]}""")
    counter += 1
```

---

### Test Your Links 🔗

Try clicking on a link in your output—it should take you to the item's page! 🎉

---

### Additional Tips for Women in Tech 🌟

- **Leverage Your Curiosity:** Inspect HTML elements to explore how websites are built and gain insights into web development!  
- **Build Confidence:** Every step you complete, no matter how small, adds to your growing tech skill set! 💪  
- **Share Your Work:** Post your scraping results and code on platforms like LinkedIn to inspire other women entering the field. 🚀   

---

Happy scraping! 🕸️  
You're one step closer to becoming a data wizard. ✨

---

## Common Errors
 
 First, delete any other code in your `day96` files. Copy each code snippet below into `day96` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

 ### What's Your Tag?

```python
myLinks = soup.find_all({"class":"css-1m051bw"})
```

<details>
<summary>👀 Answer</summary>

The most common problem is not identifying the correct tag. Sometimes the text is in the `<a>` tag. Sometimes it's in an `<h>`. Inspect a few links to see what the common class and tag are.

The tag must be the first argument in the `find_all`.

```python
myLinks = soup.find_all("a", {"class":"css-1m051bw"})
```

</details>

---

## Fix My Code
 
 First, delete any other code in your `day96` files. Copy each code snippet below into `day96` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/scroll"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

myLinks = soup.find_all("h", {"class":"title"})

print(len(myLinks))

counter = 0
for link in myLinks:
    print(link.text)
    print(f"""https://webscraper.io{link["href"]}""")
    counter +=1
```

<details>
<summary>👀 Answer</summary>

```python
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/scroll"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
 
myLinks = soup.find_all("a", {"class":"title"}) # Wrong tag

print(len(myLinks))

counter = 0
for link in myLinks:
    print(link.text)
    print(f"""https://webscraper.io{link["href"]}""")
    counter +=1
```

</details>

---

# Day 96 Challenge: Scrape Hacker News Headlines 📰✨

Today, you’ll take your web scraping skills to the next level by analyzing data from [Hacker News](https://news.ycombinator.com/)! 🎯

---

## 🏁 **Your Mission**

1. Access the Hacker News homepage to scrape headlines.  
2. Search for and display headlines that include the words:  
   - **Python** 🐍  
   - **vscode** 🔄  
3. Use logic to filter and display only relevant results.  

---

## 🔧 **Step-by-Step Instructions**

### 1. Prepare Your Tools 🛠️
Before diving in, ensure you have a Python environment ready with the necessary libraries installed.

---

### 2. Access Hacker News 🌐
Connect to the Hacker News homepage and retrieve its HTML content. This will serve as your raw data source for extracting headlines.

---

### 3. Parse the Data 🔍
Break down the HTML content to isolate the elements that contain headlines. This involves identifying patterns in the page’s structure—think of it as solving a puzzle! 🧩

---

### 4. Search for Keywords 🐍🔄
Go through each headline and check if it contains either of the target keywords:  
- **Python**: Representing programming and problem-solving brilliance.  
- **vscode**: Highlighting innovation in collaborative coding.  

Only keep and display the headlines that match these criteria.

---

### 5. Present Your Findings ✨
Output the filtered headlines in a readable and engaging way. Add some personal flair, like numbering the results or organizing them by relevance.

---

## 🌟 **Stretch Goals (Optional)**

1. **Save Your Results**  
   Store the filtered headlines in a file so you can reference or share them later.

2. **Expand Keyword Search**  
   Allow the program to accept user-input keywords. This makes your scraper dynamic and reusable for other searches.

3. **Analyze Trends**  
   Observe patterns in the headlines. Are there more articles about Python than Replit? What could that mean?

---

## 💡 **Why This Challenge is Amazing**

- **Real-World Skills**: Web scraping is a key tool in data gathering and automation.  
- **Empowerment Through Knowledge**: Practice extracting and analyzing data independently.  
- **Inspire Others**: Show off your results and share how coding helps uncover trends.  

---

Scrape those headlines, uncover hidden insights, and have fun while doing it! 🌐✨

<img id="image" src="assets/day96_4.png" alt="day96 image" width="720">

---

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

headlines = soup.find_all("a", class_=None)  # Filtering for links without additional classes

# Step 6: Filter and display headlines containing "Python" or "Replit"
print("🔍 Filtering headlines containing 'Python' or 'vscode':\n")
for headline in headlines:
    headline_text = headline.get_text()  # Extract the text of the headline
    if 'Python' in headline_text or 'VSCode' in headline_text:  # Check for the keywords
        print(f"📰 {headline_text}")
```

</details>
