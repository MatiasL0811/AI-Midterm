from sklearn.linear_model import LogisticRegression

# Dataset: [FIN301, FIN305]
# 1 = Yes (completed), 0 = No (not completed)
X = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0],
    [1, 1],
    [1, 0],
    [0, 0],
    [1, 1]
]

# Labels: 1 = Can take FIN 405, 0 = Cannot
y = [1, 0, 0, 0, 1, 0, 0, 1]

# Train the model
model = LogisticRegression()
model.fit(X, y)

# Ask user questions
fin301 = input("Did you complete FIN 301? (yes/no): ").strip().lower()
fin305 = input("Did you complete FIN 305? (yes/no): ").strip().lower()

# Convert answers to numbers
if fin301 == "yes":
    f301 = 1
else:
    f301 = 0

if fin305 == "yes":
    f305 = 1
else:
    f305 = 0

# Make prediction
student = [[f301, f305]]
prediction = model.predict(student)

# Final decision
print("\nResult:")
if prediction[0] == 1:
    print("OK, you CAN take FIN 405.")
else:
    print("Sorry, you CANNOT take FIN 405. You must complete the prerequisites.")