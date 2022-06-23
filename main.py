import turtle
import pandas
guessed = 0
guessed_states=[]
has_states = True
screen = turtle.Screen()
screen.title("U.S. States Guesser")
screen.setup(width=800, height=600)
#screen.screensize(800, 600)
image="./blank_states_img.gif"
screen.bgpic('blank_states_img.gif')
screen.update()
#screen.addshape(image)
turtle.hideturtle()
turtle.penup()
#turtle.shape(image)
#turtle.goto(-297,13)
#turtle.write("Califoggia", font=("Arial", 10, "bold"))
def guess_name():
    global guessed
    global guessed_states
    answer_state = screen.textinput(f"Guess a state, guessed: {guessed}", "What is the name of the state you think is the capital of the U.S.?")
    #print(answer_state)
    df = pandas.read_csv('50_states.csv')
    if answer_state.lower() not in guessed_states:
        if not(df.state[df.state.str.lower() == answer_state.lower()].empty):
            state = df.state[df.state.str.lower() == answer_state.lower()].item()
            x = float(df.x[df.state.str.lower() == answer_state.lower()])
            y = float(df.y[df.state.str.lower() == answer_state.lower()])
            turtle.goto(x,y)
            turtle.write(state, font=("Arial", 8, "bold"))
            guessed += 1
            guessed_states.append(answer_state.lower())
    #print(y)

while has_states:
    guess_name()

screen.exitonclick()