# NetZero House Energy Efficiency Project

Welcome to the NetZero House Energy Efficiency Project! This software, sponsored by the National Institute of Standards and Technology (NIST), utilizes the power of Matplotlib and Pandas to analyze and visualize data from a house equipped with advanced sensors and a dehumidifier. The project was initiated by Aryan Jain on August 1, 2023, with the goal of harnessing valuable insights to enhance the energy efficiency of a house with net-zero emissions.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Data Sources](#data-sources)
- [Analysis](#analysis)
  - [Weather Data](#weather-data)
  - [Dehumidifier Electricity Data](#dehumidifier-electricity-data)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The NetZero House Energy Efficiency Project, sponsored by NIST and initiated by Aryan Jain, focuses on leveraging data to optimize energy usage within a house while maintaining net-zero emissions. This software specifically zooms in on the analysis of the dehumidifier's performance and its impact on energy consumption and efficiency.

## Getting Started

### Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/netzero-energy-project.git
   ```

2. Navigate to the project directory.

   ```bash
   cd netzero-energy-project
   ```

3. Create a virtual environment (recommended).

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment.

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Launch the Jupyter Notebook to start analyzing and visualizing the data.

   ```bash
   jupyter notebook
   ```

2. Open the `NetZero_House_Analysis.ipynb` notebook.

3. Follow the instructions in the notebook to interact with the data and generate insightful visualizations.

## Data Sources

The software utilizes the following data sources:

- Weather data: Historical weather data (temperature, humidity, etc.) relevant to the location of the NetZero house.
- Dehumidifier electricity data: Information about the energy consumption of the dehumidifier, including kWh usage and efficiency (measured in L/kWh).

## Analysis

### Weather Data

The weather data analysis focuses on understanding how external conditions affect the energy efficiency of the house. This includes exploring trends between temperature, humidity, and energy usage.

### Dehumidifier Electricity Data

The dehumidifier electricity data analysis delves into the energy consumption patterns of the dehumidifier. It includes visualizations of kWh usage over time, as well as the efficiency of the dehumidifier in removing moisture from the air.

## Results

The results of the analysis provide valuable insights into the relationship between weather conditions, dehumidifier performance, and energy consumption. By understanding these dynamics, recommendations can be made to optimize the house's energy efficiency and contribute to its net-zero emissions goal.

## Contributing

Contributions to this project are welcome! If you have suggestions, bug reports, or would like to add new features, please feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

By contributing to this project, you're contributing to a greener and more energy-efficient future. Thank you for your interest and support!
