from flask import Flask, render_template
from random import randint
from time import time

from helpers.numbers_api import get_fact_for_number
from helpers.first_api import get_lucky_number
from helpers.second_api import get_worst_food

app = Flask(__name__)

WEEK2_FIRST_API = "https://cyf-first-api-rspelx6baq-vp.a.run.app/"
WEEK2_SECOND_API = "https://cyf-second-api-rspelx6baq-vp.a.run.app/"

@app.route("/")
def homepage():
    current_epoch = time()
    random_number = randint(0, 10000)
    lucky = get_lucky_number(WEEK2_FIRST_API, "luckynumber")
    worst = get_worst_food(WEEK2_FIRST_API,"worstfoodfrom1", "Something went wrong, fix and try again.")
    worstsource = get_worst_food(WEEK2_SECOND_API,"worstfoodfrom2", "Unavailable, Great Job!")
    YOUR_NAME = "Alireza"
    return render_template("homepage.html", number=random_number, time=current_epoch, lucky=lucky, worst=worst, worstsource=worstsource, YOUR_NAME=YOUR_NAME)


@app.route("/number-fact")
def number_fact():
    random_number = randint(0, 100)
    fact = get_fact_for_number(random_number)

    return render_template("number-fact.html", number=random_number, fact=fact)
