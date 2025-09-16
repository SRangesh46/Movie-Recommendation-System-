# 🎬 Movie Recommendation System

The **Movie Recommendation System** is a web-based application that suggests similar movies based on the movie entered by a user.  
It is built with **Flask, Python, and Machine Learning** using **content-based filtering** techniques.  

The system leverages **pre-trained similarity scores** to recommend the top 30 most relevant movies.  
Users can access it through a simple **web interface** or call the **REST API** to integrate recommendations into other apps.

---

## ✨ Features
- 🌐 Flask-based web application  
- 🔍 Accepts movie name as input (handles spelling mistakes & close matches)  
- 🎯 Suggests the top **30 most similar movies**  
- 📦 Pre-trained model stored in a `.pkl` file for fast recommendations  
- 📊 Content-based filtering using similarity scores  
- 🛠 REST API support for integration with external apps or frontends  
- 🖼 Simple web interface using HTML templates  

---

## 📂 Project Structure
Movie-Recommendation-System/
│── app.py # Main Flask application
│── recommendation system.pkl # Pre-trained model (movies_data + similarity matrix)
│── templates/
│ └── index.html # Frontend template (search box + results)
│── requirements.txt # Python dependencies
│── README.md # Project documentation

