
It includes test cases for logging in, adding/removing products from the cart.

---

## 📌 Setup Instructions

### **1️⃣ Prerequisites**
Before setting up the framework, ensure you have the following installed:
- **Python 3.8+**
- **Google Chrome** (latest version)
- **ChromeDriver** (matching your Chrome version)
- **pip** (Python package manager)

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

### **3️⃣ Create and Activate a Virtual Environment**
```sh
python -m venv .venv
# Activate the virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### **4️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 🚀 Running Tests

### **1️⃣ Run All Tests**
```sh
pytest -s --log-cli-level=INFO
```

### **2️⃣ Run a Specific Test File**
```sh
pytest tests/test_login.py
```

### **3️⃣ Run Tests and Generate an HTML Report**
```sh
pytest --html=reports/test_report.html --self-contained-html
```

### **4️⃣ Run Tests with Custom Logging**
By default, logs are written to `logs/test_log.log`.  
To see logs in real-time:
```sh
pytest -s --log-cli-level=INFO
```

---

## 🔧 Project Structure
```
📂 your-repo-name
 ├── 📂 pages               # Page Object Model (POM) classes
 │    ├── base_page.py
 │    ├── cart_page.py
 │    ├── login_page.py
 │    ├── product_page.py
 │
 ├── 📂 tests               # Test scripts
 │    ├── test_cart.py
 │    ├── test_login.py
 │
 ├── 📂 utils               # Utilities (configs, logging, helpers)
 │    ├── config.py
 │    ├── logger.py
 │
 ├── 📂 logs                # Test execution logs
 ├── 📂 reports             # Test reports (HTML)
 ├── requirements.txt       # Dependencies
 ├── pytest.ini             # Pytest configurations (logging, test discovery)
 ├── README.md              # Documentation (this file)
```

---

## 🔧 Configuration
You can modify **`config.py`** to update:
- **BASE_URL** (Website under test)
- **Test credentials** (`USERNAME`, `PASSWORD`)
- **Locators** (stored in `LOCATORS` dictionary)

---

## 📄 Generating Test Reports
### **Generate an HTML Test Report**
```sh
pytest --html=reports/test_report.html --self-contained-html
```
This generates a file `reports/test_report.html` with detailed test execution results.

---

## ❓ Troubleshooting

### **1️⃣ ChromeDriver Not Found**
- Download the correct **ChromeDriver** from [here](https://chromedriver.chromium.org/downloads)
- Place it in the `PATH` or specify its location in the WebDriver setup.

### **2️⃣ Logs Not Showing in Console**
- Use `pytest -s --log-cli-level=INFO`
- Modify `pytest.ini`:
  ```ini
  [pytest]
  log_cli = true
  log_cli_level = INFO
  ```

---

## 📢 Contributing
If you'd like to contribute, feel free to submit a pull request! 🚀

