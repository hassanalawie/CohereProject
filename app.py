import json
from random import randint, uniform
from flask import Flask, jsonify
import json
from flask_cors import CORS
import cohere
from cohere.responses.classify import Example


app = Flask(__name__)
CORS(app, origins='http://localhost:3000', supports_credentials=True)


tickets_json = '''
{
  "support_tickets": [
    {
      "ticket_id": 1,
      "customer_id": "C12345",
      "date": "2024-02-07",
      "category": "Billing",
      "description": "I was charged twice this month for my subscription. Can you please explain why this happened and correct the mistake?"
    },
    {
      "ticket_id": 2,
      "customer_id": "C12346",
      "date": "2024-02-06",
      "category": "Technical Support",
      "description": "The latest update is not compatible with my device. The app crashes every time I try to open it."
    },
    {
      "ticket_id": 3,
      "customer_id": "C12347",
      "date": "2024-02-05",
      "category": "Product Feedback",
      "description": "I love the new features introduced in the latest version! Especially the new dashboard layout is very user-friendly."
    },
    {
      "ticket_id": 4,
      "customer_id": "C12348",
      "date": "2024-02-04",
      "category": "Service Feedback",
      "description": "I had an issue with my order, and the customer service representative was extremely helpful and polite. Thank you for the great service!"
    },
    {
      "ticket_id": 5,
      "customer_id": "C12349",
      "date": "2024-02-03",
      "category": "Feature Request",
      "description": "Could you consider adding a dark mode feature to the app? It would really help reduce eye strain during nighttime use."
    },
    {
      "ticket_id": 6,
      "customer_id": "C12350",
      "date": "2024-02-02",
      "category": "Account Management",
      "description": "I'm having trouble accessing my account even after resetting my password several times. Can someone assist me with this issue?"
    },
    {
      "ticket_id": 7,
      "customer_id": "C12351",
      "date": "2024-02-01",
      "category": "Other",
      "description": "I noticed a small typo in the help documentation under the 'Getting Started' section. Just wanted to let you know!"
    },
    {
      "ticket_id": 8,
      "customer_id": "C22351",
      "date": "2024-02-01",
      "category": "Other",
      "description": "Your product saved us 1000000 dollars. Thank you so much!"
    },
    {
      "ticket_id": 7,
      "customer_id": "C12351",
      "date": "2024-02-01",
      "category": "Other",
      "description": "I was able to increase my reach because of your product"
    }
  ]
}
'''

examples=[
  Example("The order came 5 days early", "positive review"),
  Example("The item exceeded my expectations", "positive review"),
  Example("I ordered more for my friends", "positive review"),
  Example("I would buy this again", "positive review"),
  Example("I would recommend this to others", "positive review"),
  Example("The package was damaged", "negative review"),
  Example("The order is 5 days late", "negative review"),
  Example("The order was incorrect", "negative review"),
  Example("I want to return my item", "negative review"),
  Example("The item's material feels low quality", "negative review"),
  Example("The product was okay", "neutral review"),
  Example("I received five items in total", "neutral review"),
  Example("I bought it from the website", "neutral review"),
  Example("I used the product this morning", "neutral review"),
  Example("The product arrived yesterday", "neutral review")
]
data = json.loads(tickets_json)

# Extract descriptions from each support ticket
inputs = [ticket["description"] for ticket in data["support_tickets"]]


client = cohere.Client(api_key="API_KEY")
tickets_data = json.loads(tickets_json)

@app.route('/sentiment_summary', methods=['GET'])
def sentiment_summary():
    response = client.classify(
    inputs=inputs,
    examples=examples,
    )
    print("RESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSERESPONSE")
    print(response)
    print(len(response))

    neg_count = 0
    pos_count = 0
    for result in response:
        if "negative" in result.prediction and result.confidence >0.6:
            neg_count += 1
        elif "positive" in result.prediction and result.confidence >0.6:
            pos_count += 1
    
    return {
        "positive_tickets":pos_count,
        "negative_tickets":neg_count
    }

def generate_fake_metrics():
    nps_score = randint(-100, 100)  
    csat_score = uniform(0, 100) 
    ces_score = uniform(1, 5)  
    churn_rate = uniform(0, 10)
    retention_rate = uniform(0, 100)  
    average_resolution_time = randint(1, 48)
    first_contact_resolution = uniform(0, 100)

    return {
        "nps_score": nps_score,
        "csat_score": csat_score,
        "ces_score": ces_score,
        "churn_rate": churn_rate,
        "retention_rate": retention_rate,
        "average_resolution_time": average_resolution_time,
        "first_contact_resolution": first_contact_resolution,
        # Add other metrics here...
    }

@app.route('/metrics', methods=['GET'])
def metrics():
    return jsonify(generate_fake_metrics())

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)