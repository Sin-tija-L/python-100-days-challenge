# Day 97 Challenge: Scraping and Filtering Wikipedia Paragraphs 🐾📜

For today’s challenge, you'll scrape a webpage, filter specific content, and present it in a well-formatted way in the console. This challenge combines web scraping, string filtering, and formatting to hone your skills. Let’s dive in! 🚀

---

## 🏁 **Your Mission**

1. Choose a Wikipedia or similar webpage on a topic that interests you. For example, this page on black cats:  
   👉 [10 Fascinating Facts About Black Cats](https://us.feliway.com/blogs/news/10-fascinating-facts-about-black-cats).  

2. Extract the **first three paragraphs** from the page.

3. Filter paragraphs that include one or more **keywords** of your choice.  
   - Example keywords: "kitty" or "cat".  

4. Display the paragraphs in the console, adding this line at the end:  
   _"Ja Tu vēlies uzzināt vairāk, dodies uz šo linku."_  

5. Format the output neatly for a clean and engaging display.

---

## 🔧 **Step-by-Step Instructions**

### 1. Choose Your Page 🌐
Pick a page from Wikipedia or another information-rich website on a topic you’re passionate about. Copy the URL for use in your program.

---

### 2. Set Your Keywords 🔍
Think about the words that interest you in the topic and use them as your filter. For example:
- If you’re researching black cats, you might use "kitty" or "cat".  
- If you’re exploring space, your keywords might be "star" or "galaxy".  

---

### 3. Scrape the Page 🥣
Retrieve the HTML content of your chosen webpage. Parse the content using a library like BeautifulSoup to extract text from the first three paragraphs.

---

### 4. Filter and Format ✨
Filter paragraphs based on your chosen keywords and format the output:
- Include only paragraphs that contain at least one of your keywords.  
- For each matching paragraph:
  - Add a title like **"Paragraph X:"** before the content.  
  - Insert line breaks for readability.  
- At the bottom, append this line:  
  _"Ja Tu vēlies uzzināt vairāk, dodies uz šo linku."_  

---

### 5. Display Results 🖥️
Print the filtered and formatted paragraphs to the console.

---

## 🌟 **Stretch Goals (Optional)**

1. **Make It Dynamic**:  
   Allow the user to input their keywords and the number of paragraphs they want to scrape.

2. **Save to a File**:  
   Write the filtered paragraphs and the reference link to a `.txt` file.

3. **Explore Formatting**:  
   Use color or ASCII art to make the console output more visually appealing.

---

## 💡 **Why This Challenge is Valuable**

- **Real-World Skills**: Scraping, filtering, and presenting data are key in many tech domains.  
- **Personalized Learning**: You get to explore topics you love while practicing coding!  
- **Inspiration Through Creativity**: Sharing your formatted output can inspire others to explore web scraping.

---

Happy scraping! 🐾✨

<img id="image" src="assets/day97_1.png" alt="day97 image" width="720">

---

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
import requests
from bs4 import BeautifulSoup

url = "https://us.feliway.com/blogs/news/10-fascinating-facts-about-black-cats"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

paragraphs = soup.find_all("p")

print("\n🐈‍⬛ Black Cat Facts 🐈‍⬛\n")

displayed_count = 0

for paragraph in paragraphs:
    paragraph_text = paragraph.get_text().strip()
    if 'kitty' in paragraph_text.lower() or 'cat' in paragraph_text.lower():
        displayed_count += 1
        print(f"Paragraph {displayed_count}: {paragraph_text}\n")
        if displayed_count == 3:
            break

print(f"If you want to know more, go here: {url}\n")
print("🐱🐱🐱")
```

</details>
