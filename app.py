import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from datetime import date, timedelta

app = Flask(__name__)

# Configure Google API key from an environment variable for security
# NOTE: In a real project, you would use a secure method like Google Cloud Secrets
# For this hackathon, you can place your key directly here if needed:
# genai.configure(api_key="YOUR_API_KEY_HERE")

# Updated placeholder function to handle dynamic day counts
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

    try:
        num_days = int(duration)
    except ValueError:
        return "Please enter a valid number for trip duration."

    itinerary_content = ""

    # Generate the itinerary for each day dynamically
    for day in range(1, num_days + 1):
        if day == 1:
            itinerary_content += f"""
        **Day {day}: Arrival & Local Exploration**
        * Morning: Arrive at {destination} and check into your accommodation.
        * Afternoon: Settle in and {theme_activity}.
        * Evening: Enjoy a welcome dinner at a highly-rated local restaurant.
            """
        elif day == num_days:
            itinerary_content += f"""
        **Day {day}: Departure**
        * Morning: Do some last-minute souvenir shopping.
        * Afternoon: Head to the airport for your departure.
            """
        else:
            itinerary_content += f"""
        **Day {day}: City Exploration**
        * Morning: Visit a local landmark or attraction.
        * Afternoon: Discover some local hidden gems.
        * Evening: Experience the city's nightlife or a cultural show.
            """
            
    return itinerary_content

def adapt_itinerary(itinerary, event_type, day_to_adapt):
    # This is a hardcoded placeholder to simulate a dynamic adaptation.
    
    # Define a dictionary of adapted itineraries for each scenario
    adapted_plans = {
        "rain": """
        * Morning: Find a local cafe to enjoy a hot beverage and local pastries.
        * Afternoon: Visit an indoor attraction like the Calico Museum of Textiles or a local art gallery.
        * Evening: Catch a movie at a cinema or attend an indoor cultural show.
        """,
        "train_delay": """
        * Morning: The train is delayed. Use this time to explore the area around the station or grab a quick lunch.
        * Afternoon: Head to a nearby bookstore or mall to relax while you wait.
        * Evening: On arrival, check into your accommodation and have a quiet dinner.
        """,
        "luggage_lost": """
        * Morning: File a report with the airline for your lost luggage.
        * Afternoon: Visit a nearby shopping center to buy essential items.
        * Evening: Treat yourself to a comforting meal at a casual restaurant.
        """,
        "sick": """
        * Morning: Rest at your accommodation. Hydrate and eat a light, comforting breakfast.
        * Afternoon: Take a slow, leisurely walk to a nearby park if you feel up to it.
        * Evening: Order room service or a simple takeaway dinner and rest for the night.
        """,
        "spontaneous": """
        * Morning: Follow your curiosity and explore a new neighborhood you discovered.
        * Afternoon: Found a local festival or event! Enjoy the unexpected fun.
        * Evening: Try that hidden gem restaurant you stumbled upon earlier.
        """,
        "other": """
        * Morning: A new plan has emerged! Go with the flow.
        * Afternoon: Take some time to explore this unexpected change.
        * Evening: See where this new path takes you.
        """
    }
    
    # Get the new content based on the selected event type
    new_day_content = adapted_plans.get(event_type, "")

    # Split the original itinerary into a list of lines
    lines = itinerary.strip().split('\n')
    
    # Find the day to replace
    start_index = -1
    for i, line in enumerate(lines):
        if line.strip().startswith(f"**Day {day_to_adapt}:"):
            start_index = i
            break
            
    if start_index != -1:
        # Find the end of the day's itinerary block
        end_index = start_index + 1
        while end_index < len(lines) and lines[end_index].strip():
            end_index += 1

        # Build the adapted day section
        title = event_type.replace('_', ' ').title()
        new_day_section = f"        **Day {day_to_adapt}: City Exploration (Updated due to {title})**\n{new_day_content}"
        
        # Replace the original day's content with the new content
        new_lines = lines[:start_index] + [new_day_section] + lines[end_index:]
        
        return "\n".join(new_lines)
        
    return "Error: Could not adapt itinerary for the selected day."


# Define the routes for our web pages
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plan', methods=['POST'])
def plan():
    destination = request.form['destination']
    duration = request.form['duration']
    archetype = request.form['archetype']
    
    itinerary = generate_itinerary(destination, duration, archetype)
    
    # Pass the duration to the template
    return render_template('itinerary.html', itinerary=itinerary, duration=duration)

@app.route('/adapt', methods=['POST'])
def adapt():
    current_itinerary = request.form['itinerary']
    event_type = request.form['event_type']
    day_to_adapt = request.form['day_to_adapt']
    
    adapted_itinerary = adapt_itinerary(current_itinerary, event_type, day_to_adapt)
    
    # Pass the event_type to the template
    return render_template('adapted_itinerary.html', adapted_itinerary=adapted_itinerary, event_type=event_type)

if __name__ == '__main__':
    app.run(debug=True)