import turtle
import pandas
guessed = []
missing_states=[]
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
    global missing_states
    answer_state = screen.textinput(f"Guess a state, guessed: {len(guessed)}", "What is the name of the state you think is the capital of the U.S.?")
    #print(answer_state)
    df = pandas.read_csv('50_states.csv')
    all_states = df.state.tolist()
    if answer_state.lower() == "exit":
            #missing_states.append(answer_state)
            for state in all_states:
                #print(state)
                if state not in guessed:
                    #print(f"state guessed: {guessed}")
                    #print(f"state not guessed: {state}")
                    missing_states.append(state)
            saved_df = pandas.DataFrame({'state': missing_states,'guessed': False})
        #saved_df = pandas.DataFrame(missing_states)
            saved_df.to_csv('missing_states.csv')
            exit()

    if answer_state.capitalize() not in guessed:
        if not(df.state[df.state.str.lower() == answer_state.lower()].empty):
            guessed.append(answer_state.capitalize())
            #print(guessed)
            state = df.state[df.state.str.lower() == answer_state.lower()].item()
            x = float(df.x[df.state.str.lower() == answer_state.lower()])
            y = float(df.y[df.state.str.lower() == answer_state.lower()])
            turtle.goto(x,y)
            turtle.write(state, font=("Arial", 8, "bold"))
            #guessed += 1


    #print(y)

while has_states:
    guess_name()

screen.exitonclick()