# 🚀 ScrapeForce

**ScrapeForce** is a real-time web scraping and data pipeline project that automates the extraction of headlines from [Hacker News](https://news.ycombinator.com), transforms and stores the data in a PostgreSQL database, and visualizes it using Metabase. The pipeline is orchestrated using Apache Airflow and fully containerized using Docker Compose.

---

## ✨ Features

- 🔁 Automated daily web scraping from Hacker News
- 🧼 Data cleaning and transformation
- 🗃️ Storage in PostgreSQL database
- 📊 Interactive dashboards built with Metabase
- 📧 Email notifications on DAG success and failure
- 🐳 Fully containerized using Docker Compose
- 🔄 Re-runnable and modular ETL design

---

## 🧰 Tech Stack

| Technology       | Purpose                          |
|------------------|----------------------------------|
| **Python**       | Scripting and ETL logic          |
| **Apache Airflow** | DAG scheduling and orchestration |
| **PostgreSQL**   | Relational data storage          |
| **Metabase**     | Data visualization dashboards    |
| **Docker Compose** | Container orchestration         |
| **BeautifulSoup**| HTML parsing for scraping        |
| **Pandas**       | Data transformation and analysis |

---

## 📁 Project Structure
```
ScrapeForce/
│
├── dags/
│ ├── scraping_dag.py # Airflow DAG for pipeline
│ └── scripts/
│ ├── scrape.py # Scraping logic
│ ├── transform.py # Data cleaning
│ └── load.py # Load to PostgreSQL
│
├── data/ # Optional: Output data (CSV)
│
├── Dockerfile.airflow # Custom Airflow image
├── docker-compose.yaml # Container orchestration
├── requirements.txt # Python dependencies
├── .env # SMTP credentials for alerts
└── README.md # Project documentation
```
---

## ⚙️ How to Get Started

### 1. 🔁 Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/ScrapeForce.git
cd ScrapeForce
```
### 2. 🛠️ Configure Environment
```
Create a .env file in the root:
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
SMTP_MAIL_FROM=your_email@gmail.com
```
### 3. 🐳 Build & Run the Containers
```
docker compose up --build
```
Once running:

Airflow UI: http://localhost:8080

Metabase UI: http://localhost:3000
### 4. 🕹️ Trigger the DAG
```
Open Airflow UI

Enable and trigger the scrapeforce_web_scraping DAG

Scraped headlines will be saved to the PostgreSQL table scraped_data

```
--- 
### 📊 Sample Dashboard
Using Metabase:

Connect to the airflow database

Explore the scraped_data table

Create visualizations like:

Number of headlines scraped over time

Latest headlines

Trends per day

Save the visualizations to a dashboard

### 🌱 Future Enhancements
✅ Retry logic and error handling in scrapers

✅ Multi-site scraping support

✅ Support for parameterized scraping (topics, keywords)

✅ Unit tests for ETL scripts using pytest

✅ Deployment to AWS/GCP using ECS or Cloud Composer

✅ Add Grafana/Prometheus for monitoring

### 👨‍💻 Author
Yash Pandey
📧 pandeyash1706@gmail.com
