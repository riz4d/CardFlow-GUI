from flask import Flask, redirect, render_template, request, jsonify, json
import random
from datetime import datetime, timedelta
import requests
from core.isvalid import is_valid_credit_card
from core.expirydate import generate_date
from core.cvv import generatecvv
from core.validcc import generate_valid_cc
from configs.values import csv_file
import csv
from faker import Faker
fake = Faker()
i=0


app = Flask(__name__, template_folder="public", static_url_path='/static/')


fake = Faker()

def cardholdname(min_length=3, max_length=5):
    while True:
        first_name = fake.first_name()
        last_name = fake.last_name()
        if min_length <= len(first_name) <= max_length and min_length <= len(last_name) <= max_length:
            return f"{first_name} {last_name}"


def bin_generate_bycnt(csv_file, brand, country_name):
    bins = []
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Brand'] == brand and row['CountryName'] == country_name:
                bins.append(row['BIN'])
    
    if bins:
        return random.choice(bins)
    return None

def cc_gen(howmany,bin_num):
    
    i=1
    print(howmany)
    if howmany == "":
        loop_value = 1
    else:
        loop_value = int(howmany)
    card_number_list = []
    while i<=loop_value:
        is_valid_card = generate_valid_cc(bin_number=int(bin_num))
        if is_valid_card != False:
            valid_card = is_valid_card
            cvv = generatecvv()
            random_date = generate_date()
            valid_cardstr = ' '.join(valid_card[i:i+4] for i in range(0, len(valid_card), 4))
            card_holder = cardholdname()
            card_number_list.append([f"{valid_cardstr}",f"{random_date.strftime('%m')}/{random_date.strftime('%Y')}",f"{cvv}",f"{card_holder}"])
            i+=1
    return card_number_list
@app.route("/",methods=['POST','GET'])
def main():
    if request.method == 'POST':
        brand = request.form.get("inputBrand")
        month = request.form.get("inputExpmonth")
        year = request.form.get("expyr")
        country = request.form.get("country")
        quantity = request.form.get("quantity")
        print(brand,month,year,country)
        random_bin = bin_generate_bycnt(csv_file, brand, country)
        credit_cards = cc_gen(howmany=quantity,bin_num=random_bin)
        return render_template('index.html', data=credit_cards)
    return render_template("index.html")
    
if __name__ == '__main__':
    app.debug = False
    app.run(host="0.0.0.0", port=80, use_reloader=True, threaded=True)