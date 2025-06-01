# Data Interpreter & Analyzer

## Description

Analyzes datasets, interprets statistical findings, and provides actionable insights from data. Creates comprehensive data analysis reports with visualizations, trends, and business recommendations.

## Usage

Provide your dataset, analysis goals, and any specific questions you want answered. Include context about the business problem and decision criteria. Works with various data formats and analysis types.

## Prompt

```markdown
Analyze the following dataset and provide comprehensive insights:

**Analysis Objective:**
[What specific questions or problems are you trying to solve with this data?]

**Dataset Information:**
- **Data Source:** [Where the data comes from and collection methodology]

- **Time Period:** [Date range and frequency of data collection]

- **Sample Size:** [Number of records/observations]
- **Key Variables:** [Main columns/metrics in the dataset]



**Data to Analyze:**
```

[PASTE YOUR DATA HERE - CSV format, table, or summary statistics]

```

**Analysis Requirements:**
- **Analysis Type:** [Descriptive / Diagnostic / Predictive / Prescriptive]
- **Key Questions:** [Specific questions you want the data to answer]
- **Target Audience:** [Who will use these insights - executives, managers, technical team]
- **Decision Context:** [What decisions will be made based on this analysis]

**Specific Analysis Requests:**
1. **Descriptive Statistics**
   - Summary statistics for key variables
   - Distribution analysis and outlier detection
   - Missing data assessment

2. **Trend Analysis**
   - Time-based patterns and seasonality
   - Growth rates and change over time
   - Correlation between variables

3. **Segmentation Analysis**
   - Customer/product/geographic segments
   - Performance differences between groups
   - Behavioral patterns within segments

4. **Predictive Insights**
   - Forecasting based on historical patterns
   - Risk factors and warning indicators
   - Scenario modeling and what-if analysis

**Output Requirements:**
- **Format:** [Executive summary / Detailed report / Dashboard format]
- **Visualizations:** [Charts, graphs, and visual representations needed]
- **Recommendations:** [Strategic recommendations and next steps]
- **Confidence Levels:** [Statistical confidence and reliability assessment]

**Business Context:**
[Industry, company background, competitive landscape, and strategic goals]


Please provide:
1. **Executive Summary** with key findings and recommendations
2. **Detailed Analysis** with statistical insights and interpretations
3. **Visual Representation** suggestions for key findings
4. **Action Items** with prioritized recommendations

5. **Risk Assessment** and limitations of the analysis
6. **Next Steps** for further investigation or data collection
```

## Example Input

```markdown
**Analysis Objective:**
Understand customer churn patterns and identify factors that predict customer retention for our SaaS subscription service.

**Dataset Information:**
- **Data Source:** Customer database and usage analytics from past 12 months
- **Time Period:** January 2024 - December 2024
- **Sample Size:** 10,000 customers
- **Key Variables:** Subscription tier, usage frequency, support tickets, payment history, churn status

**Data to Analyze:**
| Customer_ID | Subscription_Tier | Monthly_Usage_Hours | Support_Tickets | Payment_Delays | Tenure_Months | Churned |
|-------------|------------------|-------------------|-----------------|----------------|---------------|---------|
| 1001        | Premium          | 45                | 2               | 0              | 18            | No      |
| 1002        | Basic            | 8                 | 5               | 2              | 6             | Yes     |
| 1003        | Pro              | 32                | 1               | 0              | 24            | No      |
| 1004        | Basic            | 15                | 3               | 1              | 12            | No      |

| 1005        | Premium          | 52                | 0               | 0              | 30            | No      |
| 1006        | Basic            | 3                 | 8               | 3              | 3             | Yes     |
...

**Key Questions:**
- What factors most strongly predict customer churn?

- Which customer segments have the highest retention rates?
- What usage patterns indicate at-risk customers?
- How does subscription tier affect churn probability?
```

## Example Output

```markdown
# Customer Churn Analysis Report

## Executive Summary

### Key Findings
Our analysis of 10,000 customers reveals **critical churn predictors** that can help reduce customer loss by up to 35% through targeted interventions.

**Primary Insights:**
- **Churn Rate:** Overall churn rate is 23% annually, highest in Basic tier (31%)
- **Key Predictor:** Monthly usage below 10 hours predicts 78% churn probability
- **Critical Period:** 85% of churn occurs within first 6 months of subscription

- **Support Impact:** Customers with 4+ support tickets have 65% higher churn risk


**Strategic Recommendations:**
1. **Immediate Action:** Implement usage-based early warning system for sub-10 hour users
2. **Tier Strategy:** Enhance Basic tier value proposition or sunset the offering
3. **Onboarding Focus:** Intensive support during first 6 months to drive engagement

4. **Support Optimization:** Proactive outreach for customers with multiple tickets



---


## Detailed Statistical Analysis


### 1. Churn Rate by Subscription Tier

```

Tier Analysis:

- Basic: 31% churn (3,100/10,000 customers)
- Pro: 18% churn (1,800/10,000 customers)  

- Premium: 12% churn (1,200/10,000 customers)

Statistical Significance: p < 0.001 (highly significant)

```

**Interpretation:** Clear inverse relationship between subscription tier and churn. Premium customers are 2.6x more likely to stay than Basic customers.



### 2. Usage Pattern Analysis
```

Usage Hour Segments:

- 0-5 hours/month: 67% churn rate (High Risk)

- 6-15 hours/month: 34% churn rate (Medium Risk)
- 16-30 hours/month: 15% churn rate (Low Risk)
- 31+ hours/month: 8% churn rate (Very Low Risk)

Correlation: r = -0.73 (strong negative correlation)

```

**Interpretation:** Usage is the strongest predictor of retention. Customers using less than 10 hours monthly should be flagged for intervention.



### 3. Tenure and Churn Relationship
```

Churn by Tenure:

- 0-3 months: 45% churn rate
- 4-6 months: 28% churn rate
- 7-12 months: 15% churn rate
- 13+ months: 7% churn rate

Critical Period: 85% of all churn happens in first 6 months

```

**Interpretation:** Onboarding and early engagement are crucial. Customers who survive 6 months have high long-term retention probability.




### 4. Support Ticket Impact

```

Support Interaction Analysis:

- 0 tickets: 18% churn rate
- 1-2 tickets: 22% churn rate
- 3-4 tickets: 35% churn rate
- 5+ tickets: 52% churn rate

Pattern: Each additional ticket increases churn risk by 8-12%

```




**Interpretation:** While some support is normal, multiple tickets indicate frustration. Proactive outreach needed for high-ticket customers.

### 5. Payment Behavior Correlation

```

Payment Delay Analysis:

- No delays: 19% churn rate

- 1 delay: 28% churn rate  
- 2+ delays: 46% churn rate

Financial stress strongly correlates with churn risk

```

---

## Predictive Model Results

### Churn Risk Score Formula
```

Risk Score = (10 - Monthly_Usage_Hours) × 0.4 +
             (Support_Tickets × 2.5) +
             (Payment_Delays × 3.2) +
             (Tier_Risk_Multiplier)

Where:

- Basic Tier Multiplier: +5

- Pro Tier Multiplier: +2  

- Premium Tier Multiplier: 0

```


### Risk Categories
- **High Risk (Score 15+):** 70% churn probability - Immediate intervention needed
- **Medium Risk (Score 8-14):** 35% churn probability - Monitor and engage
- **Low Risk (Score 0-7):** 12% churn probability - Standard retention efforts

---

## Visualization Recommendations

### 1. Executive Dashboard
```

Suggested Charts:

- Churn Rate by Tier (Bar Chart)
- Usage vs. Retention (Scatter Plot)  
- Monthly Churn Trend (Line Chart)
- Risk Score Distribution (Histogram)

```

### 2. Operational Dashboards
```

Real-time Monitoring:

- At-Risk Customer List (Table with risk scores)
- Usage Heatmap by Customer Segment
- Support Ticket Impact Tracker
- Early Warning Alerts Dashboard

```

---

## Strategic Recommendations

### Priority 1: Early Warning System (Implement in 30 days)
**Action:** Create automated alerts for customers with:
- Usage below 10 hours for 2 consecutive months
- 3+ support tickets in 30 days
- Any payment delays

**Expected Impact:** 25% reduction in preventable churn
**Investment:** $15K in system development

### Priority 2: Enhanced Onboarding (60 days)
**Action:** Intensive 90-day onboarding program including:
- Weekly check-ins for first month
- Usage goal setting and tracking

- Personalized feature recommendations

**Expected Impact:** 40% improvement in 6-month retention
**Investment:** 2 FTE customer success roles

### Priority 3: Basic Tier Strategy Review (90 days)

**Action:** Either enhance Basic tier value or migrate users to Pro tier
- Add features that drive engagement
- Implement usage-based pricing
- Create clear upgrade path incentives

**Expected Impact:** 15% overall churn reduction
**Investment:** Product development and pricing strategy work


---

## Risk Assessment & Limitations

### Data Quality Considerations

- **Sample Bias:** Analysis based on existing customers only
- **Temporal Factors:** Seasonal effects not fully captured in 12-month view
- **External Variables:** Economic factors and competition not included

### Model Limitations
- **Predictive Accuracy:** 78% accuracy in test set
- **False Positives:** 15% of "high risk" customers won't actually churn
- **Causation vs. Correlation:** Usage patterns may be effect, not cause of satisfaction

### Confidence Levels
- **High Confidence:** Usage and tier relationships (>95% confidence)
- **Medium Confidence:** Support ticket correlations (85% confidence)

- **Lower Confidence:** Payment delay causation (70% confidence)

---

## Next Steps & Further Analysis


### Immediate Actions (Week 1)
1. Implement risk scoring system for existing customers
2. Create high-risk customer list for customer success team
3. Set up automated usage monitoring alerts

### Short-term Analysis (Month 1)
1. **Cohort Analysis:** Track retention by acquisition channel and time period
2. **Feature Usage:** Analyze which specific features correlate with retention

3. **Competitive Analysis:** Survey churned customers about alternatives chosen

### Long-term Research (Quarter 1)
1. **A/B Testing:** Test intervention strategies on at-risk segments
2. **Predictive Modeling:** Develop machine learning models for churn prediction

3. **Customer Journey Mapping:** Detailed analysis of pre-churn behavior patterns

### Success Metrics to Track
- Monthly churn rate reduction
- Early warning system accuracy
- Customer lifetime value improvement
- Support ticket resolution impact on retention

This analysis provides a solid foundation for data-driven customer retention strategies. The key is implementing the early warning system quickly while building longer-term engagement programs.
```

## Variations

- **Financial Analysis**: Focus on revenue, profitability, and financial metrics
- **Market Research**: Analyze survey data, market trends, and competitive intelligence
- **Performance Analytics**: Website, app, or business performance data analysis
- **Scientific Data**: Research data analysis with statistical testing and hypothesis validation

## Tips

- Always start with clear questions you want the data to answer
- Provide context about how decisions will be made based on the analysis
- Include information about data collection methods and potential biases
- Ask for confidence levels and limitations along with insights
- Request specific visualizations that would be most helpful for your audience
- Consider asking for both statistical significance and practical significance

## Related Prompts

- `meeting-summary.md` - For documenting data review meetings and decisions
- `proposal-writer.md` - For creating proposals based on analytical findings
- `technical-documentation.md` - For documenting analytical methods and procedures

## Tags

`data-analysis` `statistics` `insights` `reporting` `decision-support` `analytics`
