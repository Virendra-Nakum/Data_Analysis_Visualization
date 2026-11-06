# Data Analysis & Visualization Program

### A Python-Based Project for Data Analysis, Statistical Operations, and Data Visualization

## 📌 Project Overview

The **Data Analysis & Visualization Program** is a Python-based application that uses Pandas, NumPy (where applicable), Matplotlib, and Seaborn to analyze CSV datasets, handle missing values, calculate descriptive statistics, perform DataFrame operations, and generate visualizations.

The project provides a menu-driven interface that allows users to perform different data analysis tasks easily.

## ✨ Features

- Load datasets from CSV files.
- Explore the first and last five rows of a dataset.
- Display column names, data types, and basic information.
- Identify and handle missing values.
- Calculate minimum, maximum, mean, median, and standard deviation.
- Perform DataFrame operations such as total sales and product-wise quantity analysis.
- Identify regions with the highest sales.
- Find the top five products with the highest and lowest sales.
- Generate bar plots, line plots, scatter plots, pie charts, histograms, and area-style plots.
- Allow users to select columns dynamically for visualization.
- Save generated visualizations as PNG images inside the `plot/` folder.

## 🛠️ Technologies Used

- **Python** — Core programming language.
- **Pandas** — Data manipulation and analysis.
- **Matplotlib** — Data visualization and graph generation.
- **Seaborn** — Statistical data visualization.
- **CSV** — Dataset file format.

## ⚙️ Process

1. **Load Dataset:** The user enters the path of a CSV file, which is loaded into a Pandas DataFrame.
2. **Explore Data:** The user examines the first five rows, last five rows, column names, data types, and dataset information.
3. **Perform DataFrame Operations:** The program calculates total sales, identifies high- and low-sales records, analyzes regional sales, and summarizes product quantities.
4. **Handle Missing Data:** The user can display missing values, fill missing numerical values with the mean, replace missing values with a specific value, or remove incomplete rows.
5. **Generate Statistics:** The program provides minimum, maximum, average, median, and standard deviation calculations.
6. **Visualize Data:** The user selects a chart type and enters the required column names to generate a visualization.
7. **Save Visualization:** The generated graph can be saved as a PNG file inside the `plot/` folder.
8. **Exit:** The user exits the program through the main menu.

## 📂 Project Structure

```text
Data-Analysis-Visualization/
│
├── README.md
├── main.py
├── data.csv
│
└── plot/
 
```

**Note:** `main.py` contains the Python program. The `data.csv` file contains the input dataset, and the `plot/` folder stores generated visualizations. Graph images are created when the user saves them.

## ▶️ How to Run Project

### 1. Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

### 2. Install Required Libraries

Open a terminal or command prompt and run:

```bash
pip install pandas matplotlib seaborn
```

### 3. Create the Project Files

Save the Python code in a file named `main.py`.

Create the following folder in the project directory:

```text
plot/
```

Place your CSV dataset inside the project directory or provide its complete path when prompted.

### 4. Run the Program

Open the terminal in the project directory and execute:

```bash
python main.py
```

### 5. Load the Dataset

When prompted, enter the CSV file path:

```text
data.csv
```

Make sure the dataset exists at the specified path.

### 6. Select an Operation

Enter the corresponding menu number to explore the dataset, perform DataFrame operations, handle missing values, calculate statistics, generate charts, or save a visualization.

## 📊 Sample Output

The following is an illustrative example of the program's console output.

### Main Menu

```text
=============== Data Analysis & Visualization Program ===============

1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit

======================================================================

Enter Your Choice: 1

Enter Dataset Path: data.csv

Dataset Loaded Successfully!
```

### Example: Data Visualization

```text
========== DATA VISUALIZATION ==========

Bar Plot
Line Plot
Scatter Plot
Pie Chart
Histogram
Area Plot

Choose Plot: bar

Available Columns:
['Product', 'Sales', 'Quantity', 'Region']

Enter X-axis column: Product
Enter Y-axis column: Sales
```

The program displays the selected chart using Matplotlib and Seaborn.

### Example: Saving a Visualization

```text
Enter File Name: sales

Graph Saved Successfully: plot/sales.png
```

The generated graph is saved inside the `plot/` directory.

## 🎯 Objectives

- Understand practical data analysis using Python.
- Learn how to manipulate CSV datasets with Pandas.
- Identify and handle missing data.
- Calculate useful statistical measures.
- Perform DataFrame operations on real-world datasets.
- Represent data visually using different chart types.
- Develop a menu-driven Python application.

## 🔮 Future Improvements

- Add support for Excel files.
- Add more statistical operations.
- Add advanced data visualization techniques.
- Add interactive dashboards.
- Improve input validation and error handling.
- Export analysis results to CSV or Excel files.
- Automatically create output directories.

## Output

![Program Output](output.png)

## 👨‍💻 Author

**Virendra Nakum**