# Credit Card Anomaly Detection App

This web-based application uses **machine learning** to detect fraudulent or unusual credit card transactions. Built with **Streamlit**, it provides an intuitive interface for users to upload transaction datasets and perform anomaly detection efficiently.

---

## 🚀 Features

- **User-Friendly Interface**: Simple and interactive layout for uploading and analyzing datasets.
- **Anomaly Detection**: Employs advanced techniques like **Isolation Forest** to flag suspicious transactions.
- **Customizable Parameters**:
  - Select specific features for analysis.
  - Adjust contamination levels to control the anomaly threshold.
- **Interactive Visualizations**:
  - View data distribution and anomalies through interactive plots.
  - Highlight anomalies in real-time.
- **Streamlined Process**: Supports credit card datasets and is adaptable for other datasets.

---

## 🌐 Live Demo

Check out the app here: [Credit Card Anomaly Detection](https://creditcardanomalydetection.streamlit.app/)

---

## 🗉 Prerequisites (For Local Setup)

To run the app locally, you'll need:

- Python 3.9 or higher
- `pip` package manager

---

## 🛠 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/souadELmaazouzi/deployProjetPYTHON.git
   cd deployProjetPYTHON
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to `http://localhost:8501`.

---

## 🐂 Project Structure

```
deployProjetPYTHON/
│
├── app.py                 # Main Streamlit application
├── anomaly_detection.py   # Core logic for detecting anomalies
├── requirements.txt       # Python dependencies
├── data/                  # Example datasets
├── README.md              # Project documentation
└── __pycache__/           # Cached Python files
```

---

## 🕰 Screenshots

### Homepage
![Homepage Screenshot](https://via.placeholder.com/800x400.png?text=Homepage)

### Upload Dataset
![Upload Screenshot](https://via.placeholder.com/800x400.png?text=Upload+Dataset)

### Results Visualization
![Results Screenshot](https://via.placeholder.com/800x400.png?text=Anomaly+Detection+Results)

---

## 🔍 Technologies Used

- **Streamlit**: For building the web interface
- **Scikit-learn**: For implementing Isolation Forest
- **Pandas**: For data manipulation
- **Matplotlib/Seaborn**: For plotting and visualization

---

## 🧬 Example Workflow

1. **Step 1**: Upload a credit card dataset (CSV format).
2. **Step 2**: Configure detection parameters (columns, contamination rate).
3. **Step 3**: Run the detection algorithm.
4. **Step 4**: View anomalies and insights.

---

## 🤝 Contributions

Contributions are welcome! Please fork this repository and submit a pull request with your enhancements or bug fixes.

---

## ⚡️ Future Plans

- Expand to support additional anomaly detection algorithms.
- Add more visualization options (e.g., interactive graphs).
- Extend the app for real-time streaming data.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👩‍💻 Author

Developed by **[Souad El Maazouzi](https://github.com/souadELmaazouzi)**.  

Feel free to connect for questions or collaboration opportunities!

