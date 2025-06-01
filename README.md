# Imdb-movies-analysis
Imdb movies data analysis project in python
🎬 IMDb Movies Data Analysis Project
This project performs exploratory data analysis (EDA) on a dataset of movies, leveraging Python libraries like pandas, matplotlib, and plotly. It uncovers insights into trends in genres, popularity, revenue, ratings, and profitability.

📁 Dataset
- Source: movies.csv
- Size: ~10,000+ records (depending on your version)
- Columns include:
  - Title, Budget, Revenue, Popularity
  - Genres, Director, Release Date
  - Vote Count, Vote Average, etc.

📊 Key Analyses Performed
🧹 Data Cleaning
- Dropped irrelevant columns: id, homepage, tagline, etc.
- Handled missing values
- Converted release_date to datetime

📈 Feature Engineering
- Added profit and ROI (Return on Investment)
- Extracted release month from release date

📉 Visual Explorations
- Distributions: Popularity, revenue, vote count, etc.
- Trends Over Time:
  - Popularity by release year
  - Ratings over years
  - Revenue and popularity by release month
- Genre Popularity: Using bar charts and treemaps
- Top 5 profitable movies: Pie chart
- Correlation: Popularity vs rating (scatter plot)

📎 Technologies Used
- Python 3.x
- pandas
- numpy
- matplotlib
- plotly (express)

📁 How to Run the Project
1. Clone this repo or download the .py/.ipynb file
2. Place the movies.csv file in the same directory
3. Run the code in a Jupyter notebook or any Python IDE

pip install pandas matplotlib plotly numpy
📌 Project Highlights
- Insightful ROI trends across years
- Genre-based popularity analysis
- Monthly patterns in movie success
- Clean and professional visualizations

📬 Author
Sanjana Singh
sanjanaa.singh.work@gmail.com

📝 License
This project is for educational purposes only.
Feel free to contribute or suggest improvements!


