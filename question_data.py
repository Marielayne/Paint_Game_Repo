""" Questions and answers and responses for the Quiz """

# -- Questions --
questions = (
    "What is PVC?",
    "What do dispersants do in paint?",
    "What is the typical volume solids (%) range for a waterborne interior wall paint",
    "What is 'Opacity' the measure of?",
    "What is 'Gloss' the measure of?",
    "What is 'Scrubs' the measure of?",
    "A paint has a mass of 540g and occupies a 400mL vessel, What is the density (g/mL)",
    "A paint batch costs £1,820 to manufacture and yields 780L of paint. What is the cost per litre (£/L)",
)
 
# -- Multiple Choice Answer Options -- 
options = (
    ("Pigment Volume Concentration", "Polymer Volume Content", "Percentage of Volatile Components", "Percentage of viscosity"),
    ("Thicken the paint", "Increase the density of the paint", "Stabilise pigments and prevent settling", "Bind to pigment particles so they don't move",),
    ("15 - 25", "26 - 34", "35 - 45", "45 - 55",),
    ("How quickly the paint dries", "how well the paint covers the underlying coat", "How well the paint flows and levels", "Indicates gloss retention over time",),
    ("How rough the surface is", "The level of UV protection", "how quickly the paint dries", "The level of sheen and reflectivity of a paint",),
    ("How smooth the finish of the paint is", "How durable the paint is to wear and tear", "The amount of brush marks left behind after painting", "Technical name for the foam that forms when rolling paint",),  
    (1.35, 1.62, 1.43, 1.92,),
    (3.50, 1.20, 2.33, 1.97,),
)

# -- Answers -- 
answers = ("1", "3", "3", "2", "4", "2", "1", "3",)

# -- message box response --
G_messages = [
    "Correct, well done!",
    "Correct, amazing!",
    "Correct, excellent work!",
    "Correct, great job!",
    "Correct, nice one!",
]

B_messages = [
    "Incorrect, better luck next time.",
    "Incorrect, nice try though.",
    "Incorrect, try again later.",
]