// Select navigation and content elements
const navigation = document.getElementById("navigation");
const content = document.getElementById("content");

let pyodide = null;  // Variable to hold the Pyodide instance
let currentPythonCode = "";  // Variable to store the current Python code to execute
let runPythonButton = null;  // Reference to the Run button

// Function to initialize Pyodide
async function initializePyodide() {
  if (!pyodide) {
    try {
      pyodide = await loadPyodide();  // Load Pyodide asynchronously
      console.log("Loaded successfully");
      runPythonButton.disabled = false;  // Enable the button if Pyodide loads successfully
    } catch (error) {
      console.error("Failed to load Pyodide:", error);
      runPythonButton.disabled = true;  // Disable the button if Pyodide fails to load
    }
  }
}

// Event listener for DOMContentLoaded to ensure all DOM elements are ready
document.addEventListener('DOMContentLoaded', async () => {
  // console.log('DOM fully loaded and parsed');
  
  runPythonButton = document.getElementById('run-python');  // Get the button element
  // console.log('Run button element:', runPythonButton);

  // Set up the button click handler
  runPythonButton.addEventListener('click', async () => {
    // console.log("Run button clicked!");

    if (!pyodide) {
      console.log("Pyodide is not loaded yet. Attempting to load...");
      await initializePyodide();  // Attempt to initialize Pyodide if not already loaded
    }

    if (!pyodide) {
      console.error("Failed to load Pyodide. Cannot run Python code.");
      return;
    }

    try {
      // Load any required Python packages from the current Python code
      await pyodide.loadPackagesFromImports(currentPythonCode);

      // Set up custom input and logging functions
      pyodide.globals.set("js_custom_input", customInput);
      pyodide.globals.set("js_custom_log", customLog);

      // Run the Python code asynchronously
      await pyodide.runPythonAsync(`
def custom_print(*args, sep=' ', end='\\n'):
    result = sep.join(str(arg) for arg in args)
    js_custom_log(result + end)

def custom_input(prompt):
    return js_custom_input(prompt)

__builtins__.print = custom_print
__builtins__.input = custom_input

${currentPythonCode}
      `);
    } catch (error) {
      console.error("Python execution error:", error);
    }
  });

  // Attempt to initialize Pyodide immediately
  await initializePyodide();

  // Initialize navigation menu
  for (let i = 1; i <= 35; i++) {
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = `#day${i}`;
    a.textContent = `Day ${i}`;
    a.onclick = (e) => {
      e.preventDefault();
      loadContent(i);
    };
    li.appendChild(a);
    navigation.appendChild(li);
  }

  // Load the first day's content by default
  loadContent(1);
});

// Function to load content based on the day selected
async function loadContent(day) {
  try {
    // Fetch and display markdown content
    const mdResponse = await fetch(
      `content/day${day.toString().padStart(2, "0")}.md?cacheBust=${new Date().getTime()}`
    );
    if (!mdResponse.ok) throw new Error("Content not found");
    const markdown = await mdResponse.text();
    content.innerHTML = marked(markdown);

    // Fetch Python code to execute with cache-busting parameter
    const pyResponse = await fetch(
      `python_files/day${day.toString().padStart(2, "0")}.py?cacheBust=${new Date().getTime()}`
    );
    if (!pyResponse.ok) throw new Error("Python file not found");
    currentPythonCode = await pyResponse.text();
  } catch (error) {
    console.error("Error loading content:", error);
    content.innerHTML = `<h2>Day ${day}</h2><p>Content not available yet. Error: ${error.message}</p>`;
    currentPythonCode = "";
  }
}

// Function to handle custom input in Python
function customInput(prompt) {
  return window.prompt(prompt);
}

// Function to handle custom logging in Python
function customLog(message) {
  console.log(message);
}

