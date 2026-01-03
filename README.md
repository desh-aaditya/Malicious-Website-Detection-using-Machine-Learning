<h1 align="center">Malicious Website Detection using Machine Learning</h1>

<h2 align="center">Phishing and Malicious URL Classification System</h2>

<p align="center">
A machine learning–based security system that detects phishing and malicious websites using engineered URL features
and a structured ML pipeline, supporting both real-time URL analysis and high-accuracy batch prediction.
</p>

<hr/>

<h2>About the Project</h2>

<ul>
  <li>This project focuses on detecting malicious and phishing websites using machine learning.</li>
  <li>The system analyzes URL-level and domain-based features to classify websites as benign or harmful.</li>
  <li>It supports both real-time detection and offline batch analysis.</li>
  <li>The project emphasizes correct ML system design rather than only model training.</li>
</ul>

<hr/>

<h2>Key Features</h2>

<h3>Dual Detection Modes</h3>
<ul>
  <li>Real-time URL-based detection for quick phishing analysis.</li>
  <li>CSV-based batch detection using pre-engineered features for higher accuracy.</li>
</ul>

<h3>End-to-End Machine Learning Pipeline</h3>
<ul>
  <li>Data ingestion and validation.</li>
  <li>Feature transformation and preprocessing.</li>
  <li>Model training, evaluation, and inference.</li>
</ul>

<h3>Feature-Based Classification</h3>
<ul>
  <li>Uses URL structure, domain information, and statistical security features.</li>
  <li>Ensures feature consistency between training and inference.</li>
</ul>

<h3>ML-First Decision Logic</h3>
<ul>
  <li>Machine learning model acts as the primary classifier.</li>
  <li>Rule-based indicators highlight suspicious patterns without overriding ML predictions.</li>
</ul>

<h3>Professional Web Interface</h3>
<ul>
  <li>Clean and cyber-themed UI built using FastAPI and Jinja2 templates.</li>
  <li>Supports URL input and CSV upload workflows.</li>
</ul>

<h3>Production-Style Project Structure</h3>
<ul>
  <li>Modular and scalable codebase.</li>
  <li>Separation of training, inference, and UI layers.</li>
  <li>Industry-aligned folder structure.</li>
</ul>

<hr/>

<h2>What This Project Demonstrates</h2>

<ul>
  <li>Designing a complete ETL and ML pipeline for a security use case.</li>
  <li>Understanding how real-world ML projects are structured.</li>
  <li>Separation of data ingestion, transformation, model logic, and UI.</li>
  <li>Handling feature mismatch issues between training and inference.</li>
  <li>Balancing ML predictions with heuristic indicators.</li>
  <li>Building ML systems that support both batch and real-time inference.</li>
</ul>

<hr/>

<h2>Project Architecture</h2>

<pre>
Network_Security/
│
├── networksecurity/
│   ├── pipeline/            # Training and prediction pipelines
│   ├── utils/               # Feature extraction and ML utilities
│   ├── constant/            # Configuration and constants
│   ├── exception/           # Custom exception handling
│   └── logging/             # Centralized logging
│
├── final_models/            # Trained model and preprocessor
├── templates/               # UI templates (HTML)
├── static/                  # CSS and UI assets
├── prediction_output/       # Generated predictions
└── app.py                   # FastAPI application entry
</pre>

<hr/>

<h2>Technology Stack</h2>

<ul>
  <li><b>Programming Language:</b> Python</li>
  <li><b>Machine Learning:</b> Scikit-learn</li>
  <li><b>Backend Framework:</b> FastAPI</li>
  <li><b>Frontend:</b> HTML, CSS (Jinja2 templates)</li>
  <li><b>Database:</b> MongoDB</li>
  <li><b>Model Serialization:</b> Pickle</li>
  <li><b>Environment Management:</b> dotenv</li>
</ul>

<hr/>

<h2>Workflow Overview</h2>

<h3>Training Pipeline</h3>
<ul>
  <li>Ingests datasets containing engineered phishing-related features.</li>
  <li>Performs preprocessing and feature transformation.</li>
  <li>Trains and evaluates the machine learning model.</li>
  <li>Stores the trained model and preprocessor for inference.</li>
</ul>

<h3>URL-Based Detection (Real-Time)</h3>
<ul>
  <li>User submits a URL via the web interface.</li>
  <li>System extracts URL-based features in real time.</li>
  <li>ML model predicts phishing or malicious risk.</li>
  <li>Rule indicators highlight suspicious patterns.</li>
</ul>

<h3>CSV-Based Detection (High Accuracy)</h3>
<ul>
  <li>User uploads a CSV file containing the full feature set.</li>
  <li>Model performs batch inference.</li>
  <li>Predictions are displayed in a structured tabular format.</li>
</ul>

<hr/>

<h2>Why Two Detection Modes?</h2>

<ul>
  <li>URL-based detection provides fast and lightweight threat screening.</li>
  <li>CSV-based detection uses a complete feature set matching training data.</li>
  <li>This mirrors real-world security systems where quick checks and deep analysis coexist.</li>
</ul>

<hr/>

<h2>Learning Outcomes</h2>

<ul>
  <li>Learned how production ML pipelines differ from simple scripts.</li>
  <li>Understood the importance of feature consistency.</li>
  <li>Gained experience debugging real ML deployment issues.</li>
  <li>Learned to present ML predictions responsibly.</li>
  <li>Built confidence in structuring industry-grade ML systems.</li>
</ul>

<hr/>

<h2>Future Enhancements</h2>

<ul>
  <li>WHOIS-based domain age analysis.</li>
  <li>DNS and reputation-based features.</li>
  <li>Model confidence visualization.</li>
  <li>Dockerization and cloud deployment.</li>
  <li>Feature importance and explainability.</li>
</ul>

<hr/>

<h2>Conclusion</h2>

<p>
This project goes beyond basic phishing detection by focusing on proper ML system design,
ETL pipelines, and realistic deployment constraints. It demonstrates not only model building,
but also how machine learning systems are engineered and deployed in practice.
</p>
