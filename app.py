from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_grouped_pokemon():
    number_dict = {}

    with open("data_final_evos.txt") as file:
        for line in file:
            if line[-3:] == ": \n": #if the line is a number
                number = int(line[:-3])
                number_dict[number] = []
                for i in range(11):
                    number_dict[number].append({})
                j = 0

            elif line != '\n': #if the line is a pokemon
                line_filtered = line.split(" | ")
                number_dict[number][j]["name"] = line_filtered[0] #within a number's list, configures every pokemon to a name
                number_dict[number][j]["sprite"] = line_filtered[1][:-1] #within a number's list, configures every pokemon to a sprite

                j += 1

    return number_dict

@app.route("/")
def index():
    grouped_pokemon = get_grouped_pokemon()
    return render_template("index.html", groups=grouped_pokemon)

if __name__ == "__main__":
    app.run(debug=True)