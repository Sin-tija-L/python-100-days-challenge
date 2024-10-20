# 👉 Day 64: OOP


<a href="https://youtu.be/g6JBGwm1p3c" target="_blank">📹 David video</a>


Object Oriented Programming (OOP) is a **programming paradigm** (a way of thinking about how to solve a problem) that is based on classes and objects, which store all of their data and behaviors inside them.

You can think of a class like a cookie cutter, or template. It has pre-defined characteristics (shape, size etc).

Objects are like the cookies created using the cutter. They all get the same size and shape, but then we can personalize each one (sprinkles, icing, etc).

Some programming languages, like Java, are entirely based on OOP. So all you Java coders will be used to this way of thinking.

If you're a Python programmer, then this may take some getting used to, but stay with it.

This approach lets us create a template for something like an enemy in a video game, and then use that template to create, say, 20 enemies. Instead of having to code each one individually.

It's very powerful for large scale projects, but we're going to start small.


## Classes

👉 Let's create a template, known as a **class**. Our theme is animals. Our class will contain all the characteristics (think variables) that animals have in common.

Remember that this is just a template. All the characteristics are set to 'None' in the template and we will customize these values when we use the template to create (*instantiate*) each animal. The values will be passed as arguments into the `__init__` subroutine inside each animal object.

We also want to create a subroutine called *init* (short for initialization) which tells the class what to do when it is used to create each instance of an animal.

<img id="image" src="assets/day64_1.png" alt="day64 image" width="960">

```python
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound
  # 'self' means 'this object'
  # This code sets the name, species and sound of each object to the arguments passed in when it is created (instantiated).
```


## Instantiation

Instantiation means 'use the template to create an object'. Like pressing the cutter into the dough to make a cookie.

👉 Let's instantiate a dog object.

```python
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

##### THE NEW BIT #######

dog = animal("Brian", "Canine", "Woof") # Use the animal class to create a new object called 'dog' with the following parameters.
```

👉 Now let's output the dog's name.

```python
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

dog = animal("Brian", "Canine", "Woof")

##### THE NEW BIT ################
print(dog.name)
```

👉 I can use the `animal()` class to create as many different animals as I want.

```python
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

dog = animal("Brian", "Canine", "Woof")
print(dog.name)

##### THE NEW BIT ################
cow = animal("Ermintrude", "Bo Taurus", "Moo")
print(cow.sound)
```

### Try it out!


## More Methods

Functions inside an object are called methods.

👉 Let's create a `talk` method inside the `animal` class. This can then be used by both our `dog` and `cow` objects.

```python
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

  def talk(self):
    print((f"{self.name} says {self.sound}"))
```

👉 Now I can use the `talk()` method for each object.

```python
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

  def talk(self):
    print((f"{self.name} says {self.sound}")) 
  # 'self' means 'use the identifier given to the object that is accessing this method'. So If I use it with dog it will become 'dog.talk()' etc.

dog = animal("Brian", "Canine", "Woof")
dog.talk()

cow = animal("Ermintrude", "Bo Taurus", "Moo")
cow.talk()
```

### Try it out!


## Inheritance

Inheritance means that we can take the template from `animal` and break it down into sub-classes that use all the attributes and methods from that class, but also add their own attributes.

This is useful when we're thinking about animals as we can start breaking the animal kingdom apart by species.

When I create the sub-class, I use the name of its parent class as a parameter. This means 'get all the features of animal and use them here too'.

Here, I'm creating a sub-class of `bird`, which inherits from `animal`.

👉 I can then create the 'bird specific' features inside the bird sub-class.

```python
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

##### The New Bit ##########

class bird(animal):

  def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"

    # This automatically sets the information for each bird when it is created.


polly = bird() # Instantiates a new bird which gets it's details from the sub-class.

polly.talk() # polly uses the `talk()` method from the animal class
```

👉 Let's add a specific color to the bird class.

```python
class bird(animal):

  def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color # Only applies to the bird sub class


polly = bird("Green") # Sets polly's colour to 'Green'
polly.talk()
print(polly.color) # Prints polly's color
```

**We can use inheritance to create a generic class (like 'character') and then sub-divide it into different types (player, enemy, boss etc.)**


## Common Errors
 
 First, delete any other code in your `day64.py` file. Copy each code snippet below into `day64.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


 ### A Cow Of Many Colors?

 👉 What's wrong here?

 ```python
class animal:
  species = None
  name = None
  sound = None
 
  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

class bird(animal):

 def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color 


cow = animal("Ermintrude", "Bo Taurus", "Moo")
print(cow.sound)
print(cow.color)

polly = bird("Green") 
polly.talk()
print(polly.color)
```

<details>
<summary>👀 Answer</summary>

- cow was created using the `animal` class. The `colo` attribute only belongs to bird objects. Inheritance only works one way.
- `talk` was not defined so `polly.talk()` should be removed.

</details>


### A strong Sense Of Self

👉 What is the problem here?

```python
class animal:
  species = None
  name = None
  sound = None
 
  def __init__(name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

class bird(animal):

 def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color # Only applies to the bird sub class


cow = animal("Ermintrude", "Bo Taurus", "Moo")
print(cow.sound)
```

<details>
<summary>👀 Answer</summary>

A mistake like this will throw an error like: 'takes 3 positional arguments but 4 were given'.

It will look weird because there are only 3 parameters in the brackets of the animal class's `init` method.

However, instantiating an object also creates an invisible extra argument, called 'self', so you have to include that as the first argument in the parameters of the `init`.

```python
class animal:
  species = None
  name = None
  sound = None
 
  def __init__(self, name, species, sound, color): # Include the 'self' in the 'init'
    self.name = name
    self.species = species
    self.sound = sound
    self.color = color

class bird(animal):

 def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = "green"


cow = animal("Ermintrude", "Bo Taurus", "Moo", "black")
print(cow.sound)
```

</details>


## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day64.py` file. Copy each code snippet below into `day64.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
class animal:
  species = None
  name = None
  sound = None
 
  def __init__(name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

class bird():

 def __init__():
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"


cow = animal("Ermintrude", "Bo Taurus", "Moo")
print(cow.sound)
print(cow.color)

polly = bird("Green") 
polly.talk()
print(polly.color)
```

<details>
<summary>👀 Answer</summary>

```python
class animal:
  species = None
  name = None
  sound = None
 
  def __init__(self, name, species, sound): # missed the 'self'
    self.name = name
    self.species = species
    self.sound = sound

class bird(animal): # missed the inheritance from animal

 def __init__(self): # missed the 'self'
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color


cow = animal("Ermintrude", "Bo Taurus", "Moo")
print(cow.sound)
print(cow.color) # no such property in the animal class.

polly = bird("Green") 
polly.talk()
print(polly.color)
```

</details>


## 👉 Day 64 Challenge

In today's project, create classes to represent jobs.

Your program should:
1. Create a generic 'job' class.
2. The init method will store the details for name, salary and hours worked.
3. 'job' will have another method that prints those details nicely.
4. Create two sub-classes from job: 'doctor' and 'teacher'
5. The 'doctor' subclass should also include 'speciality' and 'years of experience'.
6. The 'teacher' subclass should also include 'subject' and 'position'.
7. The print functions for each sub-class should print this extra data.
8. Instantiate a lawyer, a computer science teacher, and a pediatric doctor (this is a doctor for children) with 7 years of experience.
9. Output the information for each job.

**Example:**

<img id="image" src="assets/day64_2.png" alt="day64 image" width="960">

<details>
<summary>💡 Hints</summary>

- Copy the `print` *method* to each of your sub-classes and customize it for each one.
- Don't worry about keeping the same method name. The one in the sub-class will override the one in the 'job' main class.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/IBiCbb0Mugg" target="_blank">📹 David solution video</a>

<details>
<summary>👀 Answer</summary>

```python
class job:
  type = None
  salary = None
  hoursWorked = None
 
  def __init__(self,salary, type, hoursWorked):
    self.salary = salary
    self.type = type
    self.hoursWorked = hoursWorked

class teacher(job):
  subject = None
  position = None
  
  def __init__(self, subject, position):
    self.type = "Teacher"
    self.salary = "$ Nowhere near enough"
    self.hoursWorked = "All of them"
    self.subject = subject
    self.position = position

class doctor(job):
  speciality = None
  experience = None

  def __init__(self, speciality, experience):
    self.type = "Doctor"
    self.salary = "$ Doing very nicely thank you"
    self.hoursWorked = "50"
    self.speciality = speciality
    self.experience = experience

lawyer = job("$ Squillions", "Lawyer", "60")
teacher = teacher("Computer Science", "Classroom Teacher")
doctor = doctor("Neurosurgery", "7")

list = [lawyer, teacher, doctor]

print("🌟Jobs Jobs Jobs!🌟")
print()
for type in list:
  print(f"Job type: {type.type}")
  print(f"Salary: {type.salary}")
  print(f"Hours worked: {type.hoursWorked}")
  if type.type == "Teacher":
    print(f"Subject: {type.subject}")
    print(f"Position: {type.position}")
  elif type.type == "Doctor":
    print(f"Speciality: {type.speciality}")
    print(f"Experience: {type.experience}")
  print("")
```

</details>