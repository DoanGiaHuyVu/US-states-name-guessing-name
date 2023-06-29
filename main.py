import turtle
import pandas

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # states to learn.csv
        # missing_state = []
        # for state in states_list:
        #     if state not in guessed_states:
        #         missing_state.append(state)

        missing_state = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data = states_data[states_data.state == answer_state]
        t.goto(int(data.x), int(data.y))
        t.write(answer_state)



# Finding coordinates on the screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor())
# turtle.mainloop()

# screen.exitonclick()
