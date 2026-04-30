# 🛡️ ML Project – Network Security (Phishing URL Detection)

An end-to-end **Machine Learning system** designed to detect phishing URLs using a trained classification model. The project follows a **production-style pipeline**, is served using **FastAPI**, and fully **containerized with Docker** for consistent and portable execution.

---

## 📌 What this Project Does

This project simulates a real-world **network security system** that:

* Collects data from **MongoDB**
* Processes and validates the data
* Trains a machine learning model
* Provides predictions through an API
* Runs inside a **Docker container**

It demonstrates how to build and structure a complete **ML pipeline from scratch to deployment-ready stage**.

---

## 🔄 End-to-End Workflow

```
MongoDB → Data Ingestion → Data Validation → Data Transformation → Model Training → Prediction API
```

Each stage is modular and designed for scalability and maintainability.

---

## ⚙️ Tech Stack

* **Python** – Core development
* **FastAPI** – API layer
* **Scikit-learn** – Machine Learning
* **Pandas / NumPy** – Data processing
* **MongoDB** – Data source
* **Docker** – Containerization
* **MLflow** – Experiment tracking

---

## 🗂️ Project Structure

```
NETWORKSECURITY/
├── networksecurity/        # Core ML pipeline (components, pipeline, utils, etc.)
├── templates/              # HTML templates for results
├── final_model/            # Trained model & preprocessor
├── prediction_output/      # Output predictions
├── data_schema/            # Schema definitions
├── network_data/           # Dataset
├── notebooks/              # EDA & experiments
├── app.py                  # FastAPI app
├── main.py                 # Pipeline execution
├── Dockerfile              # Docker configuration
├── requirements.txt
├── setup.py
├── .env                    # Environment variables (not committed)
└── other supporting files
```

---

## 🐳 Docker (Run Anywhere)

This project is fully Dockerized and available on Docker Hub.

### 🔹 Pull Image

```
docker pull rakhikumari1/ml-project:latest
```

### 🔹 Run Container

```
docker run -p 8000:8000 rakhikumari1/ml-project:latest
```

### 🔹 Access Application

```
http://localhost:8000/docs
```

---

## 🔌 API Endpoints

* **GET /** → Redirects to API docs
* **GET /train** → Runs full training pipeline
* **POST /predict** → Upload CSV and get predictions

---

## 🔗 Links

* 🔹 **GitHub Repository:** https://github.com/rakhi-kumari-ai/network-security
* 🔹 **Docker Hub Image:** https://hub.docker.com/repository/docker/rakhikumari1/ml-project/general

You can directly pull and run the image from Docker Hub.

---

## 👩‍💻 Author

**Rakhi kumari**
https://github.com/rakhi-kumari-ai


---

## 📄 License
This project is for educational purposes.