# University of Waterloo Student Thrift Shopping Behavior Study

## Project Overview

This project presents a comprehensive statistical analysis of thrift shopping behavior among 119 University of Waterloo students, examining key factors influencing students' thrift shopping decisions and trends over the past five years.

## Core Research Questions

1. **Barrier Consistency**: Are the barriers for thrifting consistent across people who thrift often and people who don't?
2. **Influencing Factors**: How does the decrease in quality of clothing items, the increase in prices and social perceptions affect students' willingness to thrift?
3. **Temporal Trends**: How have students' tendency to thrift changed over the past five years?

## Key Findings

### ✅ Question 1: Consistency in Barrier Perception
- Different shopping frequency groups showed highly consistent barrier perceptions (ANOVA tests showed no significant differences)
- Differences in shopping frequency stem more from unobserved factors like personal preferences rather than barrier perceptions

### 💰 Question 2: Economic Motivation Dominates
- **Affordability is the strongest driver**: Students with affordability motivation shop 4.3 times/year more (p<0.01)
- 80.7% of students cited affordability as their primary motivation
- Quality and social acceptability did not reach statistical significance

### ⏱️ Question 3: Overall Stability with Individual Variation
- No significant change in average shopping frequency over five years (p=0.420)
- However, 57% of individuals experienced changes (32.8% increased, 24.4% decreased)
- **Frequent thrifters continued to increase** (+2.87 times/year), showing habit formation effects

### 🔍 Additional Insights
- Lower-income students shop more frequently, confirming "inferior good" characteristics
- Conservative students unexpectedly showed the highest shopping frequency
- 34.7% of students perceive prices as too high, yet this hasn't significantly suppressed shopping

## Project Structure

```
thrift_store_analysis/
├── Survey_Data_GRP-04.csv          # Original survey data
├── analysis.py                      # Python analysis script
├── data_cleaned.csv                 # Cleaned data
├── project.md                       # Detailed analysis report (English)
├── project_zh.md                    # Detailed analysis report (Chinese)
├── README.md                        # Project documentation (this file)
├── README_zh.md                     # Project documentation (Chinese)
├── analysis_output.txt              # Analysis output log
├── analysis_results_summary.json   # Results summary
├── results_barriers_by_group.csv   # Barrier analysis results
├── results_change_by_group.csv     # Temporal change results
├── results_income_analysis.csv     # Income analysis results
├── results_international_analysis.csv  # International student analysis
├── results_political_analysis.csv  # Political views analysis
└── plots/                           # Visualization directory
    ├── 01_thrift_frequency_distribution.png
    ├── 02_time_comparison_boxplot.png
    ├── 03_motivations.png
    ├── 04_barriers_by_group.png
    ├── 05_correlation_heatmap.png
    ├── 06_price_vs_frequency.png
    ├── 07_condition_vs_frequency.png
    ├── 08_social_vs_frequency.png
    ├── 09_thrift_change_distribution.png
    ├── 10_paired_change_plot.png
    └── 11_income_vs_frequency.png
```

## How to Run the Analysis

### Using Python (Recommended)

```bash
# Install required packages
pip install pandas numpy matplotlib seaborn scipy statsmodels

# Run analysis
python3 analysis.py
```

## Data Description

- **Sample Size**: 119 University of Waterloo students
- **Survey Period**: 2024-2025 academic year
- **Variables**: 23 core variables
- **Main Variables**:
  - Demographic information (age, program, income, etc.)
  - Shopping behavior (past year frequency, five years ago frequency)
  - Barrier assessment (price, quality, social acceptability, etc.)
  - Motivations (sustainability, affordability, enjoyment)

## Analytical Methods

This study employs multiple statistical methods:

1. **Descriptive Statistics**: Mean, median, standard deviation, frequency distributions
2. **Hypothesis Testing**: 
   - One-way ANOVA
   - Paired sample t-test
   - Independent sample t-test
   - Kruskal-Wallis test (non-parametric)
3. **Regression Analysis**: 
   - Multiple linear regression (OLS)
   - Multicollinearity diagnostics (VIF)
4. **Post-hoc Testing**: Tukey HSD
5. **Correlation Analysis**: Pearson correlation coefficient

## Key Results Files

### 📊 Visualizations (plots/)
11 high-resolution charts covering frequency distributions, temporal comparisons, barrier analysis, and correlations

### 📝 Detailed Reports
- `project.md`: Comprehensive analysis report in English
- `project_zh.md`: Comprehensive analysis report in Chinese
Including:
- Complete research background and objectives
- Detailed statistical analysis results
- In-depth findings interpretation
- Policy recommendations and theoretical contributions
- Research limitations and future directions

### 📈 Data Files
- `data_cleaned.csv`: Cleaned data for further analysis
- `results_*.csv`: Detailed result tables for each analysis
- `analysis_results_summary.json`: Summary of key metrics

## Key Statistical Results

| Metric | Value |
|--------|-------|
| Sample Size | 119 |
| Average Shopping Frequency (Past Year) | 6.59 times/year |
| Average Shopping Frequency (Five Years Ago) | 6.17 times/year |
| Affordability Motivation Rate | 80.7% |
| Sustainability Motivation Rate | 63.0% |
| Perceive Prices as Too High | 34.7% |
| Social Acceptability Mean | 4.3/5 |
| Regression Model R² | 0.128 |

## Policy Recommendations Highlights

### For University Administrators
- Establish regular thrift markets on campus
- Organize "thrift shopping experience days" to promote habit formation
- Provide thrift shopping subsidies for low-income students

### For Thrift Store Merchants
- Review pricing strategies, consider student-exclusive discounts
- Establish quality grading and labeling systems
- Offer membership programs for frequent shoppers

### For Policy Makers
- Provide tax incentives to support the secondhand market
- Incorporate sustainable consumption into general education
- Establish quality standards for secondhand goods

## Technology Stack

- **Programming Languages**: Python 3.x
- **Data Processing**: pandas, numpy
- **Statistical Analysis**: scipy, statsmodels
- **Visualization**: matplotlib, seaborn

## Authors & Version

- **Analysis Date**: November 22, 2025
- **Analysis Tools**: Python 3.x
- **Version**: 1.0

## License & Citation

To cite this research, please use the following format:

```
University of Waterloo Student Thrift Shopping Behavior Study (2024). 
Analysis Based on Survey Data from 119 Students. 
Faculty of Environment and Business, University of Waterloo.
```

## Contact

For questions or additional information, please refer to the detailed reports `project.md` or `project_zh.md`.

---

**Note**: Chart text is in English to conform to international academic standards; reports are available in both English and Chinese for accessibility.
