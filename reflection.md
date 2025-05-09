# Reflection

Student Name:  Kobe Sukhatme
Student Email:  kmsukhat@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

## What I Learned
- **API Integration & Caching**  
  Learned to call a live REST API (USGS GeoJSON), parse nested JSON, and cache both raw & processed data to avoid redundant network calls.
- **Modular ETL Pipeline**  
  Broke the workflow into `extract.py`, `transform.py`, and `load.py`, each with its own responsibilities and unit tests.
- **Testing with pytest & monkeypatch**  
  Used `pytest` fixtures and `monkeypatch` to stub out HTTP requests and simulate different cache locations, ensuring robust, offline-friendly tests.
- **Interactive Dashboards with Streamlit**  
  Built a Streamlit UI with sidebar controls, Plotly Express visualizations, and Folium maps, making the data exploration intuitive and dynamic.
- **Geospatial Visualization**  
  Integrated Folium into Streamlit using `streamlit-folium`, learned to validate coordinates and handle missing values to avoid plotting errors.

## Challenges
- **Import Paths & Packaging**  
  Initially struggled with Python not finding modules in `code/`. Solved by adding an empty `__init__.py` and adjusting test imports to `from code.xxx import …`.
- **Testing External Calls**  
  Mocking `requests.get` inside `code.extract` was tricky; building a custom `DummyResponse` class helped keep tests straightforward.
- **Map Centering & NaN Handling**  
  Folium will error if given `NaN` coordinates. I filtered out any missing lat/lon before map rendering to prevent “Location values cannot contain NaNs.”
- **Environment & Commands**  
  On macOS, had to consistently use `python3`/`pip3`. Learning to run Streamlit from the terminal (not the VS Code play button) ensured the app picked up all dependencies correctly.

## Future Work
- **Date-Range Filtering**  
  Add a date picker so users can zoom in on specific weeks or days.
- **Greater Timespan**  
  Increase the timeframe to years (could be cool to see where famous earthquakes historically fall).
- **Additional Visualizations**  
  Include a time-series line chart of daily quake counts or a heatmap of quake density using GeoPandas.
- **Cache Expiry Logic**  
  Automatically re-fetch if raw cache is older than 1 hour, otherwise use the existing file.
- **Deployment**  
  Package and deploy the app on Streamlit Cloud or Heroku for live access without local setup.
- **Advanced Geospatial Analysis**  
  Cluster quakes by region or depth, and incorporate depth-based coloring or 3D scatter plots.

Working through this project solidified my understanding of ETL workflows, testing strategies, and interactive geospatial dashboards—skills I’ll carry forward into future data projects.  