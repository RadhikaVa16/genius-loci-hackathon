
# Genius Loci: Your AI Trip Co-pilot 

### From Static Itineraries to Dynamic, Real-Time Guidance.

### Introduction

**Genius Loci** is an AI-powered travel co-pilot that transforms static, one-time itineraries into dynamic, adaptable guides. Built on the power of Google's Generative AI, our application anticipates unexpected travel disruptions and instantly re-plans your trip, ensuring a stress-free and authentic travel experience.

### The Problem

Traditional travel planning is a tedious process that creates rigid, easily-broken itineraries. The reality of travel is unpredictable:

  * Unexpected rain or bad weather.
  * Train or bus delays.
  * Sudden sickness or fatigue.

Current solutions offer no way to adapt to these real-world scenarios, leaving travelers frustrated and forced to re-plan on the fly.

### The Solution

Genius Loci is an intelligent, full-stack web application that serves as a **"living" itinerary**.

  * **Initial Planning:** A user provides a destination, duration, and their "Traveler Archetype" (e.g., Foodie, Adventurer). Our system generates a detailed, personalized itinerary.
  * **Real-Time Adaptation:** When an unexpected event occurs, the user can instantly trigger an itinerary change. Our system intelligently re-routes the plan for that specific day, providing a seamless transition to new activities.

### **Key Features**

  * **AI-Powered Itinerary Generation:** Generates comprehensive, day-by-day plans from minimal user input.
  * **Contextual Adaptation Engine:** The core innovation. Itinerary is re-planned in response to disruptions like bad weather, transit delays, or sickness.
  * **Dynamic UI:** The "On which day?" dropdown dynamically updates based on the trip's duration.
  * **User-Friendly Interface:** A simple, clean web interface built with Flask and HTML.



### How to Run the Project (Local Setup)

Follow these steps to set up and run the Genius Loci application on your local machine.

1.  **Clone the Repository:**

    ```bash
    git clone [Your Repository URL]
    cd [Your Project Folder]
    ```

2.  **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**

      * **Windows:** `venv\Scripts\activate`
      * **macOS/Linux:** `source venv/bin/activate`

4.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Flask Application:**

    ```bash
    python app.py
    ```

    Your application will now be running on `http://127.0.0.1:5000`.



### Technology Stack

  * **Backend:** Python, Flask
  * **Frontend:** HTML, CSS, Jinja2
  * **Gen AI:** Google Gemini Pro (via placeholder functions)

### Future Enhancements

  * Integration with live APIs (e.g., Google Maps, Weather APIs) for real-time, automatic adaptation.
  * Natural Language Processing (NLP) to understand complex user prompts for even more flexible changes.
  * Development of a mobile application with push notifications.

### 

  * Radhika Varahagiri
  * Srinath Avantsa
  