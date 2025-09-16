import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configure Google API key from an environment variable for security
# NOTE: In a real project, you would use a secure method like Google Cloud Secrets
# For this hackathon, you can place your key directly here if needed:
# genai.configure(api_key="YOUR_API_KEY_HERE")

# Updated placeholder function to simulate AI-powered itinerary generation
def generate_itinerary(destination, duration, archetype):
    # This is a simple dynamic placeholder. In a real project, this would call the Gemini API.
    
    # We'll customize the itinerary based on the archetype.
    if "foodie" in archetype.lower():
        theme_activity = "indulge in a local street food tour"
    elif "history" in archetype.lower():
        theme_activity = "visit a historic monument or museum"
    elif "adventurer" in archetype.lower():
        theme_activity = "explore a local hiking trail or adventure park"
    else:
        theme_activity = "explore the city's highlights"

    # Now, we use f-strings to create a dynamic itinerary using the user's inputs.
    itinerary = f"""
    **Your {duration}-day trip to {destination} ({archetype} Theme)**

    **Day 1: Arrival & Local Exploration**
    * Morning: Arrive at {destination} and check into your accommodation.
    * Afternoon: Settle in and {theme_activity}.
    * Evening: Enjoy a welcome dinner at a highly-rated local restaurant.

    **Day 2: City Highlights**
    * Morning: Go for a sightseeing tour of the city's famous landmarks.
    * Afternoon: Discover some local hidden gems.
    * Evening: Experience the city's nightlife or a cultural show.
    
    **Day {duration}: Farewell**
    * Morning: Do some last-minute souvenir shopping.
    * Afternoon: Head to the airport for your departure.
    """
    return itinerary

# Placeholder function for real-time adaptation (no changes needed here)
def adapt_itinerary(itinerary, condition):
    if "rain" in condition.lower():
        # Simple string replacement for demo purposes
        return itinerary.replace("a local hiking trail or adventure park", "an indoor activity like a bowling alley or gaming cafe.")
    return itinerary

# Define the routes for our web pages
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plan', methods=['POST'])
def plan():
    destination = request.form['destination']
    duration = request.form['duration']
    archetype = request.form['archetype']
    
    # The new function is called here, passing the dynamic inputs
    itinerary = generate_itinerary(destination, duration, archetype)
    
    return render_template('itinerary.html', itinerary=itinerary)

@app.route('/adapt', methods=['POST'])
def adapt():
    current_itinerary = request.form['itinerary']
    condition = "rain" # This would be a real-time API call in a full project
    
    adapted_itinerary = adapt_itinerary(current_itinerary, condition)
    
    return render_template('adapted_itinerary.html', adapted_itinerary=adapted_itinerary)

if __name__ == '__main__':
    app.run(debug=True)