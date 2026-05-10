from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")

# Database
db = client["charityDB"]

# Collection
campaigns = db["campaigns"]


# HOME PAGE (READ)
@app.route('/')
def home():

    # Get all campaigns
    all_campaigns = list(campaigns.find())

    # GRAPH DATA
    names = []
    amounts = []

    for campaign in all_campaigns:
        names.append(campaign['title'])
        amounts.append(campaign['raised'])

    # CREATE GRAPH
    plt.figure(figsize=(7, 5))

    plt.bar(names, amounts)

    plt.xlabel("Campaign Name")
    plt.ylabel("Amount Raised")
    plt.title("Fundraiser Donations")

    # Save graph
    graph_path = "static/graph.png"

    plt.savefig(graph_path)

    plt.close()

    return render_template(
        'index.html',
        campaigns=all_campaigns,
        graph=graph_path
    )


# CREATE CAMPAIGN
@app.route('/add', methods=['GET', 'POST'])
def add_campaign():

    if request.method == 'POST':

        title = request.form['title']
        description = request.form['description']
        goal = int(request.form['goal'])

        campaigns.insert_one({
            "title": title,
            "description": description,
            "goal": goal,
            "raised": 0
        })

        return redirect('/')

    return render_template('add_campaign.html')


# UPDATE CAMPAIGN
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_campaign(id):

    # Find campaign using ObjectId
    campaign = campaigns.find_one({
        "_id": ObjectId(id)
    })

    # If form submitted
    if request.method == 'POST':

        updated_data = {
            "title": request.form['title'],
            "description": request.form['description'],
            "goal": int(request.form['goal'])
        }

        # Update MongoDB
        campaigns.update_one(
            {"_id": ObjectId(id)},
            {"$set": updated_data}
        )

        return redirect('/')

    return render_template(
        'edit_campaign.html',
        campaign=campaign
    )


# DELETE CAMPAIGN
@app.route('/delete/<id>')
def delete_campaign(id):

    campaigns.delete_one({
        "_id": ObjectId(id)
    })

    return redirect('/')


# DONATE
@app.route('/donate/<id>', methods=['POST'])
def donate(id):

    amount = int(request.form['amount'])

    # Find campaign
    campaign = campaigns.find_one({
        "_id": ObjectId(id)
    })

    # Calculate new amount
    new_amount = campaign['raised'] + amount

    # Update raised amount
    campaigns.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "raised": new_amount
            }
        }
    )

    return redirect('/')


# RUN APPLICATION
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)