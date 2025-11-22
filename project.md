# University of Waterloo Student Thrift Shopping Behavior Study

## Project Overview

### Research Background
This study aims to conduct an in-depth analysis of thrift shopping (secondhand shopping) behavior characteristics among University of Waterloo students, exploring key factors influencing students' thrift shopping decisions and trends over the past five years. With the growing awareness of sustainable consumption and changing economic environments, understanding thrift shopping behavior among student populations is crucial for policy-making, business decisions, and sustainable development education.

### Research Objectives
1. Analyze whether barriers faced by different shopping frequency groups differ
2. Quantify the impact of clothing quality, price, and social perceptions on students' thrift shopping willingness
3. Assess changes in students' thrift shopping tendencies over the past five years
4. Explore other potential influencing factors (income, international student status, political views, etc.)

### Data Source
- **Sample Size**: 119 University of Waterloo students
- **Data Collection**: Online survey questionnaire
- **Survey Period**: 2024-2025 academic year
- **Variables**: 23 core variables

---

## I. Data Description and Sample Characteristics

### 1.1 Sample Overview

**Demographic Characteristics**:
- Age primarily concentrated in the 21-23 age range
- Programs mainly Environment & Business, with others including Systems Engineering, Knowledge Integration, etc.
- International students: 37.8% (45 students)
- Domestic students: 62.2% (74 students)

**Income Distribution**:
- Low income ($0-20,000): 74 students (62.2%)
- Medium-low income ($20,001-40,000): 33 students (27.7%)
- Medium income ($40,001-60,000): 7 students (5.9%)
- High income ($60,001+): 3 students (2.5%)

### 1.2 Thrift Shopping Behavior Overview

**Past Year Shopping Frequency Statistics**:
- Mean frequency: 6.59 times/year
- Median: 6 times/year
- Standard deviation: 6.89 times
- Range: 0-24 times

**Frequency Group Distribution**:
- **Occasional Thrifters** (1-8 times/year): 69 students (58.0%)
- **Frequent Thrifters** (≥9 times/year): 33 students (27.7%)
- **Non-Thrifters** (0 times): 17 students (14.3%)

**Shopping Motivations**:
- Affordability: 96 students (80.7%) - **Primary motivation**
- Sustainability: 75 students (63.0%)
- Enjoyment: 64 students (53.8%)

> 💡 **Key Finding**: Over 80% of students cited affordability as a primary motivation for thrift shopping, indicating that price factors dominate among the student population.

![Thrift Shopping Frequency Distribution](plots/01_thrift_frequency_distribution.png)

![Shopping Motivation Analysis](plots/03_motivations.png)

---

## II. Core Question Analysis

### Question 1: Are Barriers Consistent Across Different Shopping Frequency Groups?

#### Analytical Method
One-way ANOVA was employed to compare three groups (frequent thrifters, occasional thrifters, non-thrifters) across various barrier indicators, including:
- Price impact on purchase decisions
- Clothing condition assessment
- High-quality brand availability
- Style fit
- Social acceptability

#### Research Results

**Barrier Indicator Comparison by Group**:

| Group | Sample Size | Price Impact | Condition | Brand Quality | Style Fit | Social Accept | % Perceive Overpriced |
|-------|------------|-------------|-----------|---------------|-----------|--------------|----------------------|
| Frequent Thrifters | 33 | 4.31 | 3.85 | 3.46 | 4.00 | 4.39 | 45.5% |
| Non-Thrifters | 17 | 4.40 | 3.47 | 3.53 | 3.00 | 3.88 | 23.5% |
| Occasional Thrifters | 69 | 4.26 | 3.61 | 3.36 | 3.49 | 4.33 | 31.9% |

**Statistical Test Results**:

1. **Price Impact on Decisions**: F = 0.349, p = 0.706
   - **Conclusion**: No significant difference among the three groups

2. **Clothing Condition Assessment**: F = 0.750, p = 0.475
   - **Conclusion**: No significant difference among the three groups

3. **Style Fit**: F = 1.484, p = 0.231
   - **Conclusion**: No significant difference among the three groups
   - Note: Although not significant, frequent thrifters' average score (4.00) was notably higher than non-thrifters (3.00)

![Barrier Comparison by Group](plots/04_barriers_by_group.png)

#### Core Findings

**Finding 1: Consistency in Barrier Perception**
Despite significant differences in shopping frequency among the three groups, their perception ratings of various barriers were relatively consistent, with statistical tests showing no significant differences. This suggests:
- Differences in shopping frequency do not stem from different perceptions of barriers
- Other unobserved factors (such as time, transportation convenience, personal preferences) may be at play

**Finding 2: The Price Perception Paradox**
Interestingly, frequent thrifters had the highest proportion (45.5%) perceiving prices as too high, which seems counterintuitive. Possible explanations include:
- Frequent thrifters are more price-sensitive and better able to detect price increases
- They have more comparison shopping experience, forming clearer price expectations
- Despite perceiving high prices, they continue shopping due to other factors (sustainability, uniqueness)

**Finding 3: High Level of Social Acceptability**
All groups showed high social acceptability scores (3.88-4.39), indicating that thrift shopping is widely accepted among University of Waterloo students, with minimal social stigma.

---

### Question 2: How Do Clothing Quality, Price, and Social Perceptions Affect Students' Thrift Shopping Willingness?

#### Analytical Method
Multiple linear regression model (OLS) was employed, with past year shopping frequency as the dependent variable and key barrier indicators as independent variables:

**Model Specification**:
```
Shopping Frequency = β₀ + β₁(Condition Rating) + β₂(Brand Quality) + β₃(Price Perception) 
                    + β₄(Social Acceptability) + β₅(Affordability Motivation) 
                    + β₆(Sustainability Motivation) + ε
```

#### Regression Results

**Model Fit**:
- R² = 0.128
- Adjusted R² = 0.081
- F-statistic = 2.710 (p = 0.017)
- **Model is overall significant**, but explanatory power is limited

**Regression Coefficient Estimates**:

| Variable | Coefficient | Std Error | t-value | p-value | Significance |
|----------|------------|-----------|---------|---------|--------------|
| Constant | -8.572 | 4.998 | -1.715 | 0.089 | |
| Condition Rating | -0.044 | 0.926 | -0.048 | 0.962 | |
| Brand Quality | 0.698 | 0.812 | 0.859 | 0.392 | |
| Price Perception | 1.908 | 1.159 | 1.646 | 0.103 | |
| Social Acceptability | 1.041 | 0.804 | 1.294 | 0.198 | |
| **Affordability Motivation** | **4.277** | **1.613** | **2.652** | **0.009** | **\*\*** |
| Sustainability Motivation | 1.211 | 1.301 | 0.931 | 0.354 | |

*Note: \*\* indicates significance at the 1% level*

**Multicollinearity Diagnostics (VIF)**:
- Condition Rating: VIF = 30.7 (severe multicollinearity)
- Brand Quality: VIF = 21.7 (severe multicollinearity)
- Social Acceptability: VIF = 20.7 (severe multicollinearity)
- Price Perception: VIF = 14.7 (severe multicollinearity)

> **Methodological Warning**: The model exhibits severe multicollinearity (VIF > 10), meaning independent variables are highly correlated, potentially leading to unstable coefficient estimates. Interpretation requires caution.

![Correlation Heatmap](plots/05_correlation_heatmap.png)

#### In-depth Analysis: Bivariate Relationships

To avoid multicollinearity effects, we examined bivariate relationships between key variables and shopping frequency:

**1. Price Perception vs. Shopping Frequency**

![Price Perception vs Frequency](plots/06_price_vs_frequency.png)

- Correlation coefficient: r = 0.173 (weak positive correlation)
- Students who perceive prices as high actually shop slightly more frequently, possibly reflecting:
  - Reverse causation: More shopping leads to greater awareness of price increases
  - Economic pressure or sustainability concerns drive shopping despite perceived high prices

**2. Clothing Condition vs. Shopping Frequency**

![Clothing Condition vs Frequency](plots/07_condition_vs_frequency.png)

- Correlation coefficient: r = 0.046 (negligible correlation)
- Clothing condition assessment has minimal impact on shopping frequency
- Students rating condition as "always good" (5 points) don't shop significantly more than those with lower ratings

**3. Social Acceptability vs. Shopping Frequency**

![Social Acceptability vs Frequency](plots/08_social_vs_frequency.png)

- Correlation coefficient: r = 0.146 (weak positive correlation)
- Students perceiving thrift shopping as "very acceptable" shop slightly more frequently
- Overall, social acceptability is generally high in the sample with limited variation

#### Core Findings

**Finding 1: Economic Motivation is the Core Driver**
After controlling for other factors, **students with affordability motivation shop 4.3 times/year more than those without**, the only statistically significant predictor. This confirms descriptive statistics: affordability is the primary motivation for student thrift shopping.

**Finding 2: Limited Impact of Quality and Social Perceptions**
Contrary to expectations, clothing quality, brand availability, and social acceptability did not significantly impact shopping frequency. Possible reasons:
- **Measurement issue**: These variables may reflect shopping experience outcomes rather than causes
- **Range restriction**: Social acceptability is universally high in the sample, lacking sufficient variation
- **Mediation effects**: These factors may indirectly affect behavior through motivations

**Finding 3: Complexity of Price Perception**
Price perception (perceiving prices as too high) shows positive correlation with shopping frequency, but not significantly (p=0.103). This may indicate:
- Students have high price tolerance for secondhand goods
- Price increases haven't reached a threshold that significantly suppresses shopping
- Need for more detailed price elasticity analysis

**Finding 4: Limited Model Explanatory Power**
R² = 0.128 indicates the model explains only 12.8% of shopping frequency variance, with most variation explained by factors outside the model. Future research should consider including:
- Geographic accessibility (distance to thrift stores)
- Time constraints
- Peer influence
- Personal values and lifestyle

---

### Question 3: How Have Students' Thrift Shopping Tendencies Changed Over the Past Five Years?

#### Analytical Method
Paired sample t-test was used to compare shopping frequency for the same individuals "in the past year" versus "five years ago."

**Hypothesis Test**:
- H₀: μ_current = μ_five_years_ago (no change)
- H₁: μ_current ≠ μ_five_years_ago (change exists)

#### Statistical Test Results

**Paired t-test**:
- t-statistic = 0.810
- Degrees of freedom = 118
- **p-value = 0.420**
- **Conclusion**: At 5% significance level, **cannot reject null hypothesis**. No significant difference in average shopping frequency between past year and five years ago.

**Descriptive Statistics**:

| Period | Mean | Median | Std Dev |
|--------|------|--------|---------|
| Five Years Ago | 6.17 times/year | 2 times/year | 7.48 |
| Past Year | 6.59 times/year | 6 times/year | 6.89 |
| **Change** | **+0.42 times/year** | **+4 times/year** | |

![Time Comparison Boxplot](plots/02_time_comparison_boxplot.png)

![Change Distribution Histogram](plots/09_thrift_change_distribution.png)

#### Heterogeneity Analysis of Changes

While overall average change was not significant, individual changes showed diverse patterns:

**Change Direction Distribution**:
- **No Change**: 51 students (42.9%)
- **Significant Increase** (+5 times or more): 21 students (17.6%)
- **Slight Increase** (+1 to +5 times): 18 students (15.1%)
- **Slight Decrease** (-1 to -5 times): 16 students (13.4%)
- **Significant Decrease** (-5 times or below): 13 students (10.9%)

**Change by Current Frequency Group**:

| Current Group | Five Years Ago Avg | Current Avg | Avg Change | % Increased | % Decreased |
|---------------|-------------------|-------------|------------|-------------|-------------|
| Frequent Thrifters | 13.45 | 16.32 | +2.87 | 51.5% | 15.2% |
| Occasional Thrifters | 3.36 | 3.57 | +0.21 | 31.9% | 30.4% |
| Non-Thrifters | 1.06 | 0.00 | -1.06 | 0.0% | 17.6% |

![Individual Change Trajectories](plots/10_paired_change_plot.png)

#### Core Findings

**Finding 1: Overall Stability with Individual Differentiation**
- At the macro level, average shopping frequency remained relatively stable over five years
- At the micro level, approximately 57% of individuals experienced changes (increases or decreases)
- This "stable instability" reflects the dynamic nature of thrift shopping behavior

**Finding 2: Continued Growth Among Frequent Thrifters**
Current frequent thrifters increased by an average of 2.87 times/year over five years, with over half (51.5%) showing growth trends. This may indicate:
- Thrift shopping exhibits "habit formation" effects: once shopping habits are established, they tend to continue increasing
- Frequent thrifters are more adaptable to changes in the secondhand market (quality, prices)

**Finding 3: Significant Median Growth Despite Non-significant Mean**
- Median increased from 2 to 6 times (+300%)
- Mean only increased from 6.17 to 6.59 (+6.8%)
- This difference may be driven by extreme values: a few high-frequency shoppers inflated the mean

**Finding 4: Exit Pathways for Non-Thrifters**
Among current non-thrifters, 17.6% had shopping experience five years ago but have since stopped. Possible reasons:
- Negative shopping experiences (quality, price, time costs)
- Income increase leading to shift toward new goods consumption
- Life stage changes (e.g., moving off campus, losing convenience)

#### Possible Drivers of Temporal Changes

While overall change was not significant, the following factors may have influenced individual trajectories:

1. **Pandemic Impact** (2020-2022):
   - Physical store closures may have led some students to reduce shopping
   - Rise of online secondhand platforms may have encouraged other students to increase shopping

2. **Price Changes**:
   - 34.7% of respondents perceive current prices as too high
   - Price increases may have suppressed some potential growth

3. **Social Norm Evolution**:
   - High social acceptability of thrift shopping (average 4.3/5) may have encouraged new participants
   - Promotion of sustainable consumption movements may have changed some students' attitudes

---

## III. Other Important Findings

### 3.1 Income Level Impact

![Income vs Shopping Frequency](plots/11_income_vs_frequency.png)

**Key Findings**:
- Low-income groups (6.72 times/year) and medium-low income groups (7.36 times/year) shop more frequently than medium-high income groups (3.79-4.67 times/year)
- 77% of low-income groups are motivated by affordability, with this proportion reaching 100% in medium-income groups
- **Negative income elasticity**: Lower income correlates with higher thrift shopping frequency, confirming secondhand goods as "inferior goods" in economic terms

**Policy Implications**:
The secondhand market provides an important consumption channel for low-income students. Maintaining affordability of secondhand goods is crucial for social equity.

---

### 3.2 International vs. Domestic Students

| Group | Sample Size | Avg Shopping Freq | Social Accept | Affordability Motivation % |
|-------|-------------|-------------------|---------------|---------------------------|
| International Students | 45 | 6.51 times/year | 4.27 | 68.9% |
| Domestic Students | 74 | 6.64 times/year | 4.31 | 87.8% |

**Statistical Test**: t-test showed no significant difference (insufficient data to calculate valid p-value)

**Observations**:
1. Shopping frequency is similar between international and domestic students
2. However, **domestic students have a significantly higher affordability motivation rate (87.8%) than international students (68.9%)**
3. International students may shop more for cultural exploration, social, or sustainability motivations
4. Domestic students are more price-sensitive

**Possible Explanations**:
- International students may have more adequate family financial support
- Domestic students are more familiar with the secondhand market and can utilize its economic benefits more effectively
- Cultural differences: Some countries/regions have more developed secondhand shopping cultures

---

### 3.3 Political Views Impact

| Political Views | Sample Size | Avg Shopping Freq | Sustainability Motivation % |
|----------------|-------------|-------------------|---------------------------|
| 1 - Very Liberal | 14 | 9.54 times/year | 64.3% |
| 2 - Liberal | 39 | 6.28 times/year | 71.8% |
| 3 - Moderate | 54 | 5.59 times/year | 64.8% |
| 4 - Conservative | 9 | 10.89 times/year | 22.2% |

**Unexpected Finding**:
- **Conservative students show the highest shopping frequency (10.89 times/year)**, even exceeding very liberal students (9.54 times/year)
- However, conservatives have the lowest proportion motivated by sustainability (22.2%)

**Explanation**:
- Conservative students may shop more for economic reasons rather than environmental ideology
- Liberal students may view thrift shopping as an expression of political stance (environmentalism, anti-consumerism)
- Conservative students may focus more on practicality and thrift values
- This challenges the stereotype that "thrift shopping = progressive values"

---

### 3.4 In-depth Price Perception Analysis

**Price Perception Distribution**:
- Perceive prices as fair: 73 students (61.9%)
- Perceive prices as too high: 41 students (34.7%)
- Perceive prices as low: 4 students (3.4%)

**Kruskal-Wallis Test**: H = 4.38, p = 0.112
- Price perception's impact on shopping frequency is not significant

**Key Insights**:
1. Despite over 1/3 of students perceiving prices as too high, this hasn't significantly reduced shopping frequency
2. This may be because:
   - Student price expectations for secondhand goods have adjusted
   - Even with price increases, costs remain lower than new goods
   - Economic pressure forces continued shopping despite perceived high prices
   - Non-price values (uniqueness, sustainability) compensate for price increases

---

## IV. Research Limitations and Future Directions

### 4.1 Research Limitations

**1. Sample Representativeness**
- Sample primarily from Environment & Business program, possibly having special interest in sustainability topics
- Lacks representation from engineering, science, and other programs
- Relatively limited sample size (n=119), restricting statistical power of subgroup analyses

**2. Causal Inference Issues**
- Cross-sectional data makes causal relationship establishment difficult
- Retrospective questions (five years ago shopping frequency) may have recall bias
- Cannot control for time trend confounding factors (pandemic, economic cycles)

**3. Measurement Issues**
- Some variables (clothing quality, social acceptability) may reflect shopping experience outcomes rather than causes
- Likert scale subjectivity may introduce measurement error
- Lacks objective price measurements (actual price data)

**4. Model Limitations**
- Linear regression model has limited explanatory power (R²=0.128)
- Severe multicollinearity weakens coefficient estimate reliability
- Important control variables not included (geographic location, time constraints, peer influence)

### 4.2 Future Research Directions

**1. Longitudinal Study Design**
- Track shopping behavior changes for the same cohort of students
- Establish dynamic panel data models
- Identify lifecycle effects vs. period effects

**2. Experimental or Quasi-experimental Design**
- Utilize exogenous price variation shocks to assess price elasticity
- Intervention experiments: Test impact of information provision (quality certification, price comparison) on shopping decisions

**3. Qualitative Research Supplement**
- In-depth interviews: Understand psychological mechanisms of shopping decisions
- Participant observation: Learn about actual barriers in shopping processes
- Focus groups: Explore social norm evolution

**4. Extended Research Scope**
- Cross-school comparisons: Impact of different campus cultures on shopping behavior
- Cross-national comparisons: Role of cultural differences in secondhand consumption
- Cross-category research: Secondhand books, electronics, furniture, etc.

**5. Policy Evaluation**
- Assess impact of secondhand market tax policies
- Analyze effectiveness of campus secondhand market/exchange programs
- Study long-term effects of sustainable consumption education

---

## V. Conclusions and Policy Recommendations

### 5.1 Core Conclusions

Through systematic analysis of survey data from 119 University of Waterloo students, this study draws the following core conclusions:

**1. Regarding Barrier Consistency (Question 1)**
- Different shopping frequency groups show highly consistent perceptions of thrift shopping barriers, with statistical tests showing no significant differences
- Shopping frequency differences stem more from personal preferences, time constraints, and other unobserved factors rather than different views on quality, price, and social acceptability
- This means reducing barriers may have similar incentive effects for all students

**2. Regarding Influencing Factors (Question 2)**
- **Affordability motivation is the strongest driver**, with motivated students shopping 4.3 times/year more (p<0.01)
- Clothing quality, brand availability, and social acceptability did not reach statistical significance
- Price perception shows complexity: students perceiving high prices actually shop more frequently, possibly reflecting reverse causation or high price tolerance
- Model has limited explanatory power (R²=12.8%), indicating many unincluded influencing factors

**3. Regarding Temporal Trends (Question 3)**
- **Overall stability**: No significant change in average shopping frequency over five years (p=0.420)
- **Individual differentiation**: 57% of students experienced changes (increases or decreases), reflecting behavioral dynamism
- **Habit formation**: Frequent thrifters continued increasing (+2.87 times/year), indicating thrift shopping has inertia
- **Median growth**: From 2 to 6 times, possibly reflecting widespread increase in participation

**4. Other Key Findings**
- Lower-income students shop more frequently, confirming "inferior good" characteristics of secondhand goods
- International and domestic students have similar frequencies but different motivation structures
- Conservative political views unexpectedly correlate with high shopping frequency, challenging stereotypes
- Over 1/3 of students perceive prices as too high, but this hasn't significantly suppressed shopping

### 5.2 Theoretical Contributions

**1. Consumer Behavior Theory**
- Confirms economic rationality's dominant position among student populations
- Reveals non-linear relationship between social norms (high acceptability) and actual behavior
- Demonstrates path dependence and habit formation mechanisms in consumption behavior

**2. Sustainable Consumption Research**
- Quantifies relative importance of economic motivation (80.7%) vs. environmental motivation (63.0%)
- Suggests pure reliance on environmental appeals is insufficient for large-scale promotion of secondhand consumption
- Emphasizes realistic foundation of "economic-environmental win-win" framework

**3. Market Segmentation Theory**
- Identifies three distinct market segments (frequent/occasional/non-thrifters)
- Finds these market formations are not based on barrier perception differences
- Suggests need for new segmentation dimensions (time preference, exploration tendency)

### 5.3 Policy Recommendations

Based on research findings, we propose the following recommendations for university administrators, thrift merchants, and policy makers:

#### For University Administrators

**1. Strengthen Economic Affordability**
- Establish regular thrift markets on campus to reduce transaction costs
- Partner with local thrift stores to provide discount cards or coupons for students
- Build online secondhand trading platforms to improve market efficiency

**2. Promote Habit Formation**
- Introduce secondhand shopping resources during freshman orientation (orientation handbook, campus tours)
- Organize "thrift shopping experience days" to lower psychological barriers for first attempts
- Establish student thrift shopping communities to reinforce habits through social interaction

**3. Differentiated Support Strategies**
- For low-income students: Provide thrift shopping subsidies or vouchers
- For international students: Emphasize cultural exploration and social functions
- For different political leanings: Diversify promotional angles (thrift vs. environmental)

**4. Infrastructure Improvement**
- Set up secondhand exchange corners in dormitory buildings
- Provide free shuttle buses to thrift stores (especially on weekends)
- Establish end-of-semester item storage and secondhand trading services

#### For Thrift Store Merchants

**1. Price Strategy Optimization**
- Considering 34.7% of students perceive prices as too high, review pricing strategies
- Launch student-exclusive discount days
- Implement tiered pricing: Clearly define pricing grades based on clothing condition to improve price transparency

**2. Quality Assurance Mechanisms**
- Establish quality grading and labeling systems
- Provide cleaning and simple repair services
- Implement short-term return/exchange policies to reduce quality risk

**3. Shopping Experience Enhancement**
- Improve store environment and merchandise display
- Provide online preview and reservation services
- Organize themed events (vintage fashion shows) to enhance enjoyment

**4. Market Segmentation**
- Offer membership programs and reward points for frequent shoppers
- Provide guidance services and styling advice for newcomers
- Create quick shopping zones for time-constrained students

#### For Policy Makers

**1. Support Secondhand Market Development**
- Tax incentives: Reduce or eliminate sales tax on secondhand goods transactions
- Venue support: Provide public spaces for community secondhand markets
- Financial support: Establish secondhand market development funds

**2. Promote Sustainable Consumption Education**
- Incorporate sustainable consumption into university general education
- Conduct publicity campaigns on environmental benefits of thrift shopping
- Recognize and incentivize sustainable consumption behaviors (e.g., award "green consumer" certificates)

**3. Improve Market Regulation**
- Establish quality standards and testing mechanisms for secondhand goods
- Combat counterfeit goods flowing into the secondhand market
- Protect consumer rights, establish complaint and dispute resolution mechanisms

**4. Data-Driven Policy Making**
- Conduct regular secondhand consumption behavior surveys
- Establish secondhand market price indices to monitor market dynamics
- Evaluate actual effects of various policies and adjust timely

### 5.4 Social Significance

This study's findings have important social implications:

**1. Social Equity Perspective**
The secondhand market provides an important consumption channel for low-income students, helping to alleviate economic inequality. Maintaining affordability and accessibility of the secondhand market is a concrete action to promote social equity.

**2. Environmental Sustainability**
Despite economic motivation dominating, 63% of students recognize sustainability values. This suggests potential to guide environmental behavior through economic incentives, achieving "economic-environmental win-win."

**3. Generational Change**
Young generation's high social acceptability of thrift shopping (average 4.3/5) portends generational shift toward sustainable consumption patterns, laying cultural foundation for circular economy development.

**4. Policy Tools**
Research suggests that compared to changing attitudes (e.g., improving quality perceptions), reducing actual barriers (price, convenience) may be more effective policy tools.

---

## VI. Appendices

### Appendix A: Data Processing Description

**Data Cleaning Steps**:
1. Process special characters in column names (non-breaking spaces, etc.)
2. Convert categorical frequencies to numerical values (e.g., "1 to 3 times" → 2)
3. Extract Likert scale ratings (e.g., "5 - Always" → 5)
4. Create derived variables (groups, change amounts, etc.)
5. Remove samples with missing key variables (no deletions in this study; all 119 samples valid)

**Data Transformation Rules**:
- Shopping frequency: "I did not thrift"=0, "1 to 3 times"=2, "4 to 8 times"=6, "9 to 12 times"=10.5, "13 to 20 times"=16.5, "21 or more times"=24
- Price perception: "Underpriced"=1, "Priced correctly"=2, "Overpriced"=3
- Social acceptability: 1 (Very Unacceptable) to 5 (Very Acceptable)
- Other Likert scales: 1-5 increasing, 6 indicates "Not applicable" (treated as missing in analysis)

### Appendix B: Statistical Methods Description

**1. Descriptive Statistics**
- Mean, median, standard deviation for continuous variables
- Frequency, percentage for categorical variables
- Box plots display distribution characteristics and outliers

**2. Hypothesis Testing**
- **ANOVA**: Compare mean differences among three or more groups, assumes variance homogeneity
- **t-test**: Compare means between two groups (independent or paired)
- **Kruskal-Wallis**: Non-parametric alternative to ANOVA, doesn't assume normal distribution
- **Significance level**: α = 0.05

**3. Regression Analysis**
- **OLS Regression**: Ordinary least squares estimation of linear relationships
- **VIF Diagnostics**: Detect multicollinearity (VIF>10 indicates severity)
- **Model Fit**: R², Adjusted R², F-statistic

**4. Post-hoc Testing**
- **Tukey HSD**: Pairwise comparisons after significant ANOVA, controls family-wise error rate

### Appendix C: Visualization Chart Index

1. **Chart 1**: Thrift shopping frequency distribution - Shows overall distribution pattern
2. **Chart 2**: Time comparison boxplot - Compares current vs. five years ago distributions
3. **Chart 3**: Shopping motivation analysis - Relative importance of three motivations
4. **Chart 4**: Barrier comparison by group - Barrier scores for frequent/occasional/non-thrifters
5. **Chart 5**: Correlation heatmap - Correlation coefficient matrix among key variables
6. **Chart 6**: Price perception vs. shopping frequency - Scatter plot with trend line
7. **Chart 7**: Clothing condition vs. shopping frequency - Frequency distribution by rating groups
8. **Chart 8**: Social acceptability vs. shopping frequency - Frequency distribution by rating groups
9. **Chart 9**: Shopping frequency change distribution - Histogram of five-year changes
10. **Chart 10**: Individual change trajectories - Paired changes for 50 random samples
11. **Chart 11**: Income level vs. shopping frequency - Frequency distribution by income groups

### Appendix D: Original Data Access

Cleaned data file: `data_cleaned.csv`  
Original survey data: `Survey_Data_GRP-04.csv`  
Analysis results summary: `analysis_results_summary.json`  
Detailed result tables: `results_*.csv`

### Appendix E: Code and Reproducibility

Complete analysis code: `analysis.py`  
Analysis output log: `analysis_output.txt`  

All analyses use Python 3.x, main dependency packages:
- pandas (data processing)
- numpy (numerical computation)
- matplotlib, seaborn (visualization)
- scipy (statistical testing)
- statsmodels (regression analysis)

---

## VII. References and Acknowledgments

### Academic References
This research benefits from theories and methods in the following fields:
- Consumer behavior theory
- Sustainable consumption research
- Circular economy research
- Applied statistics and econometrics

### Acknowledgments
Thanks to all University of Waterloo students who participated in the survey.  
Thanks to the open-source community for data analysis tools.

---

**Report Completion Date**: November 22, 2025  
**Analysis Tools**: Python 3.x (pandas, statsmodels, scipy, matplotlib)  
**Sample Size**: 119  
**Data Collection Period**: 2024-2025 academic year

---
