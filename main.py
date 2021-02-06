import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


data = pd.read_csv("50_states.csv")

state_names = data["state"].to_list()

score = 0
max_score = len(data)
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{score}/{max_score}State Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in state_names:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")

        break
    if answer_state in state_names:
        tim = turtle.Turtle()
        tim.hideturtle()
        required_state = data[data["state"] == answer_state]
        move_x = int(required_state.x)
        move_y = int(required_state.y)
        tim.penup()
        tim.goto(move_x,move_y)
        tim.write(answer_state)
        score += 1
        guessed_states.append(answer_state)






#Code to get all the x & y coordinates on click

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop() #Replacement of screen.exitonclick(


