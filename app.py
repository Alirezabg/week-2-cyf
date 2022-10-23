from flask import Flask, render_template
from random import randint
from time import time

from helpers.numbers_api import get_fact_for_number
from helpers.first_api import get_lucky_number
from helpers.second_api import get_worst_food

app = Flask(__name__)

WEEK2_FIRST_API = "http://10.182.0.4/"
WEEK2_SECOND_API = "http://10.182.0.5/"


@app.route("/")
def homepage():
    current_epoch = time()
    random_number = randint(0, 10000)
    lucky = get_lucky_number(WEEK2_FIRST_API, "luckynumber")
    worst = get_worst_food(WEEK2_FIRST_API, "worstfoodfrom1",
                           "Something went wrong, fix and try again.")
    worstsource = get_worst_food(
        WEEK2_SECOND_API, "worstfoodfrom2", "Unavailable, Great Job!")
    YOUR_NAME = "Alireza"
    return render_template("homepage.html", number=random_number, time=current_epoch, lucky=lucky, worst=worst, worstsource=worstsource, YOUR_NAME=YOUR_NAME)


@app.route("/number-fact")
def number_fact():
    random_number = randint(0, 100)
    fact = get_fact_for_number(random_number)

    return render_template("number-fact.html", number=random_number, fact=fact)
