from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home_page():
    return ("<h1 style='color:blue'>Guess a number between 0 and 9</h1>"
            "<img src= 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY20yZWpqNnlnZWxiZ2pscDAwOWU3dWZ5NjQ0emZocXRyMzNvMmVneCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wIo1jZH4iHf6xRwJu4/giphy.gif'>"
            )

def random_number():
    return random.randint(0,9)

@app.route("/<int:guess>")
def guess_number(guess):
    num = random_number()
    if guess == num:
        return (f"<h1 style='color:pink'>You got it! {guess} is correct</h1>"
                f"<img src= 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExejZrZWh0enM1d"
                f"mIwam0wdjA5YmhtemxycDJmdG4xMnBlOWdvN3V4MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQ"
                f"mY3Q9Zw/S9caVuOS5csQvlMscF/giphy.gif'>")
    elif guess > num:
        return ("<h1 style='color:red'>Too high!</h1>"
                "<img src= 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTh6b3Q5d"
                "WVrYzR3YXAycTFqNGJnY3ZoenJ3d3dscG12b2JiczN5MCZlcD12MV9pbnRlcm5hbF9naWZfYnl"
                "faWQmY3Q9Zw/3s298sv3aevOC4fktQ/giphy.gif'>")
    elif guess < num:
        return ("<h1 style='color:orange'>Too low!</h1>"
                "<img src= 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa25zcWhsazFic2Zx"
                "ZGRwZHFsc2NndXA3YmZ3d3IxaHN0bTdsZWVxbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9"
                "Zw/PR3585ZZSvcHO9pa76/giphy.gif'>")






if __name__ == '__main__':
    app.run(debug=True)
