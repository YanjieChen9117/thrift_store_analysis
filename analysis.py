"""
滑铁卢大学学生二手购物行为分析
Thrift Store Shopping Behavior Analysis - University of Waterloo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import ttest_rel, ttest_ind, f_oneway, kruskal, chi2_contingency
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.outliers_influence import variance_inflation_factor
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体和绘图风格
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")
sns.set_palette("Set2")

print("=" * 80)
print("滑铁卢大学学生二手购物行为统计分析")
print("=" * 80)
print()

# ============================================================================
# 1. 数据导入和清洗
# ============================================================================

print("1. 数据导入和清洗...")
print("-" * 80)

# 读取数据
data = pd.read_csv("Survey_Data_GRP-04.csv")

print(f"原始数据维度: {data.shape}")
print(f"样本量: {data.shape[0]}")
print(f"变量数: {data.shape[1]}")
print()

# 获取实际列名并创建映射(处理特殊字符)
actual_columns = data.columns.tolist()
print("实际列名:", actual_columns[:5], "...")  # 打印前5个列名

# 创建清理的列名
new_columns = ['respondentID', 'duration_hours', 'age_group', 'program', 'year_of_study',
               'international_student', 'employed', 'income', 'housing', 'living_arrangement',
               'hometown_size', 'has_pets', 'political_views', 'motivations',
               'thrift_past_year', 'thrift_five_years_ago', 'price_affects_decision',
               'clothes_good_condition', 'find_quality_brands', 'find_style_fit',
               'clothing_durability', 'price_perception', 'social_acceptability']

# 直接设置列名
data.columns = new_columns

# 数据转换函数
def convert_thrift_frequency(value):
    """将购物频率转换为数值"""
    if pd.isna(value):
        return np.nan
    elif "did not thrift" in str(value):
        return 0
    elif "1 to 3" in str(value):
        return 2
    elif "4 to 8" in str(value):
        return 6
    elif "9 to 12" in str(value):
        return 10.5
    elif "13 to 20" in str(value):
        return 16.5
    elif "21 or more" in str(value):
        return 24
    else:
        return np.nan

def extract_rating(value):
    """提取Likert量表数值"""
    if pd.isna(value):
        return np.nan
    try:
        return int(str(value).split('-')[0].strip())
    except:
        return np.nan

def convert_social_acceptability(value):
    """转换社会接受度"""
    if pd.isna(value):
        return np.nan
    elif "1" in str(value) and "Very Unacceptable" in str(value):
        return 1
    elif "2" in str(value) and "Unacceptable" in str(value):
        return 2
    elif "3" in str(value) and "Neutral" in str(value):
        return 3
    elif "4" in str(value) and "Acceptable" in str(value):
        return 4
    elif "5" in str(value) and ("Very acceptable" in str(value) or "Very Acceptable" in str(value)):
        return 5
    else:
        return np.nan

def convert_price_perception(value):
    """转换价格感知"""
    if pd.isna(value):
        return np.nan
    elif "Underpriced" in str(value):
        return 1
    elif "Priced correctly" in str(value):
        return 2
    elif "Overpriced" in str(value):
        return 3
    else:
        return np.nan

# 应用转换
data['thrift_past_year_num'] = data['thrift_past_year'].apply(convert_thrift_frequency)
data['thrift_five_years_ago_num'] = data['thrift_five_years_ago'].apply(convert_thrift_frequency)

data['price_affects_num'] = data['price_affects_decision'].apply(extract_rating)
data['condition_rating'] = data['clothes_good_condition'].apply(extract_rating)
data['quality_brands'] = data['find_quality_brands'].apply(extract_rating)
data['style_fit'] = data['find_style_fit'].apply(extract_rating)

data['social_accept_num'] = data['social_acceptability'].apply(convert_social_acceptability)
data['price_perception_num'] = data['price_perception'].apply(convert_price_perception)

# 创建分组变量
def categorize_thrift_frequency(value):
    if pd.isna(value):
        return np.nan
    elif value >= 9:
        return "Frequent Thrifters"
    elif value > 0:
        return "Occasional Thrifters"
    else:
        return "Non-Thrifters"

data['thrift_frequency_group'] = data['thrift_past_year_num'].apply(categorize_thrift_frequency)

# 计算变化
data['thrift_change'] = data['thrift_past_year_num'] - data['thrift_five_years_ago_num']

# 动机变量
data['motivated_by_sustainability'] = data['motivations'].str.contains('Sustainability', na=False)
data['motivated_by_affordability'] = data['motivations'].str.contains('Affordability', na=False)
data['motivated_by_enjoyment'] = data['motivations'].str.contains('Enjoyment', na=False)

# 收入分组
def categorize_income(value):
    if pd.isna(value):
        return np.nan
    elif "0-20,000" in str(value):
        return "Low"
    elif "20,001-40,000" in str(value):
        return "Medium-Low"
    elif "40,001-60,000" in str(value):
        return "Medium"
    elif "60,001" in str(value) or "80,001" in str(value):
        return "High"
    else:
        return np.nan

data['income_level'] = data['income'].apply(categorize_income)

# 删除关键变量缺失的样本
data_clean = data[data['thrift_past_year_num'].notna()].copy()

print(f"清洗后样本量: {data_clean.shape[0]}")
print()

# 保存清洗后的数据
data_clean.to_csv("data_cleaned.csv", index=False)

# ============================================================================
# 2. 描述性统计分析
# ============================================================================

print("\n2. 描述性统计分析")
print("-" * 80)

print("\n过去一年二手购物频率统计:")
print(data_clean['thrift_past_year_num'].describe())

print("\n五年前二手购物频率统计:")
print(data_clean['thrift_five_years_ago_num'].describe())

print("\n二手购物频率分组:")
print(data_clean['thrift_frequency_group'].value_counts())

print("\n购物动机统计:")
print(f"可持续性: {data_clean['motivated_by_sustainability'].sum()} ({data_clean['motivated_by_sustainability'].mean()*100:.1f}%)")
print(f"经济性: {data_clean['motivated_by_affordability'].sum()} ({data_clean['motivated_by_affordability'].mean()*100:.1f}%)")
print(f"享受: {data_clean['motivated_by_enjoyment'].sum()} ({data_clean['motivated_by_enjoyment'].mean()*100:.1f}%)")

# ============================================================================
# 3. 可视化 - 基础探索
# ============================================================================

print("\n3. 生成可视化图表...")
print("-" * 80)

import os
if not os.path.exists("plots"):
    os.makedirs("plots")

# 图1: 二手购物频率分布
plt.figure(figsize=(10, 6))
plt.hist(data_clean['thrift_past_year_num'], bins=15, color='#3498db', alpha=0.8, edgecolor='white')
plt.xlabel('Number of Times Thrifted', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Distribution of Thrifting Frequency in Past Year', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/01_thrift_frequency_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# 图2: 时间变化比较
comparison_data = pd.DataFrame({
    'Past Year': data_clean['thrift_past_year_num'].dropna(),
    'Five Years Ago': data_clean['thrift_five_years_ago_num'].dropna()
})

plt.figure(figsize=(10, 6))
box_data = [comparison_data['Five Years Ago'].dropna(), comparison_data['Past Year'].dropna()]
bp = plt.boxplot(box_data, labels=['Five Years Ago', 'Past Year'],
                 patch_artist=True, widths=0.6)
bp['boxes'][0].set_facecolor('#e74c3c')
bp['boxes'][1].set_facecolor('#2ecc71')
for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
    plt.setp(bp[element], linewidth=1.5)
plt.ylabel('Frequency (times per year)', fontsize=12)
plt.title('Comparison of Thrifting Frequency: Past Year vs. Five Years Ago', 
          fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/02_time_comparison_boxplot.png', dpi=300, bbox_inches='tight')
plt.close()

# 图3: 动机分析
motivation_counts = {
    'Sustainability': data_clean['motivated_by_sustainability'].sum(),
    'Affordability': data_clean['motivated_by_affordability'].sum(),
    'Enjoyment': data_clean['motivated_by_enjoyment'].sum()
}
motivations_df = pd.DataFrame(list(motivation_counts.items()), 
                              columns=['Motivation', 'Count'])
motivations_df = motivations_df.sort_values('Count')

plt.figure(figsize=(10, 6))
colors = sns.color_palette("Set2", 3)
plt.barh(motivations_df['Motivation'], motivations_df['Count'], color=colors, alpha=0.8)
plt.xlabel('Number of Respondents', fontsize=12)
plt.title('Motivations for Thrift Shopping', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/03_motivations.png', dpi=300, bbox_inches='tight')
plt.close()

print("基础可视化完成!")

# ============================================================================
# 4. 问题1: 不同购物频率群体的障碍是否一致？
# ============================================================================

print("\n" + "=" * 80)
print("问题1: 不同购物频率群体面临的障碍是否一致？")
print("=" * 80)

# 按频率分组比较各项障碍指标
barriers_by_group = data_clean.groupby('thrift_frequency_group').agg({
    'respondentID': 'count',
    'price_affects_num': 'mean',
    'condition_rating': 'mean',
    'quality_brands': 'mean',
    'style_fit': 'mean',
    'social_accept_num': 'mean'
}).round(3)

barriers_by_group.columns = ['n', 'avg_price_barrier', 'avg_condition', 
                              'avg_quality_brands', 'avg_style_fit', 'avg_social_accept']

# 计算认为价格过高的比例
overpriced_pct = data_clean.groupby('thrift_frequency_group')['price_perception_num'].apply(
    lambda x: (x == 3).mean() * 100
).round(1)
barriers_by_group['pct_overpriced'] = overpriced_pct

print("\n不同群体的障碍指标对比:")
print(barriers_by_group)

# ANOVA检验
print("\n\n=== 统计检验: ANOVA分析 ===\n")

# 准备数据（移除NA）
groups_for_anova = data_clean[data_clean['thrift_frequency_group'].notna()]

# 价格影响
groups_price = [group['price_affects_num'].dropna() for name, group in 
                groups_for_anova.groupby('thrift_frequency_group')]
f_stat_price, p_val_price = f_oneway(*groups_price)
print(f"价格对决策的影响 - ANOVA结果:")
print(f"  F统计量 = {f_stat_price:.4f}, p值 = {p_val_price:.4f}")
if p_val_price < 0.05:
    print(f"  结论: 不同群体间存在显著差异 (p < 0.05)")
else:
    print(f"  结论: 不同群体间无显著差异 (p >= 0.05)")

# 衣物状况评价
groups_condition = [group['condition_rating'].dropna() for name, group in 
                    groups_for_anova.groupby('thrift_frequency_group')]
f_stat_cond, p_val_cond = f_oneway(*groups_condition)
print(f"\n衣物状况评价 - ANOVA结果:")
print(f"  F统计量 = {f_stat_cond:.4f}, p值 = {p_val_cond:.4f}")
if p_val_cond < 0.05:
    print(f"  结论: 不同群体间存在显著差异 (p < 0.05)")
else:
    print(f"  结论: 不同群体间无显著差异 (p >= 0.05)")

# 风格匹配
groups_style = [group['style_fit'].dropna() for name, group in 
                groups_for_anova.groupby('thrift_frequency_group')]
f_stat_style, p_val_style = f_oneway(*groups_style)
print(f"\n风格匹配 - ANOVA结果:")
print(f"  F统计量 = {f_stat_style:.4f}, p值 = {p_val_style:.4f}")
if p_val_style < 0.05:
    print(f"  结论: 不同群体间存在显著差异 (p < 0.05)")
else:
    print(f"  结论: 不同群体间无显著差异 (p >= 0.05)")

# Tukey HSD事后检验（针对风格匹配）
if p_val_style < 0.05:
    print("\nTukey HSD事后检验 - 风格匹配:")
    style_data = groups_for_anova[['style_fit', 'thrift_frequency_group']].dropna()
    tukey_result = pairwise_tukeyhsd(style_data['style_fit'], 
                                     style_data['thrift_frequency_group'], 
                                     alpha=0.05)
    print(tukey_result)

# 可视化 - 障碍比较
barriers_plot = barriers_by_group[['avg_price_barrier', 'avg_condition', 
                                     'avg_quality_brands', 'avg_style_fit', 
                                     'avg_social_accept']].T

plt.figure(figsize=(12, 7))
x = np.arange(len(barriers_plot.index))
width = 0.25
colors_bar = ['#e74c3c', '#3498db', '#2ecc71']

for i, col in enumerate(barriers_plot.columns):
    plt.bar(x + i*width, barriers_plot[col], width, label=col, 
            color=colors_bar[i % len(colors_bar)], alpha=0.8)

plt.xlabel('Barrier Type', fontsize=12)
plt.ylabel('Average Rating (1-5 scale)', fontsize=12)
plt.title('Barriers to Thrifting by Shopping Frequency Group', 
          fontsize=14, fontweight='bold')
plt.xticks(x + width, ['Price Impact', 'Condition', 'Quality Brands', 
                        'Style Fit', 'Social Accept'], rotation=45, ha='right')
plt.legend(title='Group')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/04_barriers_by_group.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n障碍分析可视化完成!")

# ============================================================================
# 5. 问题2: 质量、价格和社会认知对购物意愿的影响
# ============================================================================

print("\n" + "=" * 80)
print("问题2: 质量、价格和社会认知对购物意愿的影响")
print("=" * 80)

# 准备回归数据
regression_data = data_clean[[
    'thrift_past_year_num', 'condition_rating', 'quality_brands',
    'price_perception_num', 'social_accept_num', 
    'motivated_by_affordability', 'motivated_by_sustainability'
]].dropna()

# 转换布尔值为数值
regression_data['motivated_by_affordability'] = regression_data['motivated_by_affordability'].astype(int)
regression_data['motivated_by_sustainability'] = regression_data['motivated_by_sustainability'].astype(int)

# 多元线性回归
X = regression_data[['condition_rating', 'quality_brands', 'price_perception_num',
                     'social_accept_num', 'motivated_by_affordability', 
                     'motivated_by_sustainability']]
y = regression_data['thrift_past_year_num']

X = sm.add_constant(X)
model1 = sm.OLS(y, X).fit()

print("\n多元线性回归结果:")
print(model1.summary())

# VIF检验（多重共线性）
print("\n\n=== 多重共线性检验 (VIF) ===")
X_no_const = regression_data[['condition_rating', 'quality_brands', 'price_perception_num',
                               'social_accept_num', 'motivated_by_affordability', 
                               'motivated_by_sustainability']]
vif_data = pd.DataFrame()
vif_data["Variable"] = X_no_const.columns
vif_data["VIF"] = [variance_inflation_factor(X_no_const.values, i) 
                   for i in range(X_no_const.shape[1])]
print(vif_data)
print("\n注: VIF > 10 表示存在严重多重共线性")

# 相关性分析
print("\n\n=== 相关性矩阵 ===")
cor_vars = data_clean[[
    'thrift_past_year_num', 'condition_rating', 'quality_brands',
    'price_perception_num', 'social_accept_num', 'price_affects_num'
]].dropna()

cor_matrix = cor_vars.corr()
print(cor_matrix.round(3))

# 相关性热图
plt.figure(figsize=(10, 8))
sns.heatmap(cor_matrix, annot=True, cmap='RdBu_r', center=0, 
            square=True, linewidths=1, cbar_kws={"shrink": 0.8},
            fmt='.3f', vmin=-1, vmax=1)
plt.title('Correlation Matrix: Thrifting Behavior and Barriers', 
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('plots/05_correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 散点图: 价格感知 vs 购物频率
plt.figure(figsize=(10, 6))
for price_val in [1, 2, 3]:
    subset = data_clean[data_clean['price_perception_num'] == price_val]
    price_labels = {1: 'Underpriced', 2: 'Priced Correctly', 3: 'Overpriced'}
    plt.scatter(subset['price_perception_num'], subset['thrift_past_year_num'],
               alpha=0.5, s=50, label=price_labels[price_val])

# 添加趋势线
price_freq_data = data_clean[['price_perception_num', 'thrift_past_year_num']].dropna()
z = np.polyfit(price_freq_data['price_perception_num'], 
               price_freq_data['thrift_past_year_num'], 1)
p = np.poly1d(z)
x_line = np.linspace(price_freq_data['price_perception_num'].min(), 
                     price_freq_data['price_perception_num'].max(), 100)
plt.plot(x_line, p(x_line), "r--", linewidth=2, label='Trend Line')

plt.xlabel('Price Perception (1=Underpriced, 2=Correct, 3=Overpriced)', fontsize=12)
plt.ylabel('Thrifting Frequency (times/year)', fontsize=12)
plt.title('Price Perception vs. Thrifting Frequency', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('plots/06_price_vs_frequency.png', dpi=300, bbox_inches='tight')
plt.close()

# 箱线图: 衣物状况 vs 购物频率
plt.figure(figsize=(10, 6))
condition_data = data_clean[data_clean['condition_rating'].notna()]
condition_groups = [condition_data[condition_data['condition_rating'] == i]['thrift_past_year_num'].values 
                   for i in sorted(condition_data['condition_rating'].unique())]
bp = plt.boxplot(condition_groups, 
                labels=sorted(condition_data['condition_rating'].unique()),
                patch_artist=True, widths=0.6)
for patch in bp['boxes']:
    patch.set_facecolor('#2ecc71')
    patch.set_alpha(0.7)
plt.xlabel('Condition Rating (1=Never good, 5=Always good)', fontsize=12)
plt.ylabel('Thrifting Frequency (times/year)', fontsize=12)
plt.title('Thrifting Frequency by Perceived Clothing Condition', 
          fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/07_condition_vs_frequency.png', dpi=300, bbox_inches='tight')
plt.close()

# 箱线图: 社会接受度 vs 购物频率
plt.figure(figsize=(10, 6))
social_data = data_clean[data_clean['social_accept_num'].notna()]
social_groups = [social_data[social_data['social_accept_num'] == i]['thrift_past_year_num'].values 
                for i in sorted(social_data['social_accept_num'].unique())]
bp = plt.boxplot(social_groups,
                labels=sorted(social_data['social_accept_num'].unique()),
                patch_artist=True, widths=0.6)
for patch in bp['boxes']:
    patch.set_facecolor('#9b59b6')
    patch.set_alpha(0.7)
plt.xlabel('Social Acceptability (1=Very Unacceptable, 5=Very Acceptable)', fontsize=12)
plt.ylabel('Thrifting Frequency (times/year)', fontsize=12)
plt.title('Thrifting Frequency by Social Acceptability Perception', 
          fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/08_social_vs_frequency.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n质量、价格和社会认知分析可视化完成!")

# ============================================================================
# 6. 问题3: 过去五年购物倾向的变化
# ============================================================================

print("\n" + "=" * 80)
print("问题3: 过去五年购物倾向的变化")
print("=" * 80)

# 配对数据
change_data = data_clean[
    data_clean['thrift_past_year_num'].notna() & 
    data_clean['thrift_five_years_ago_num'].notna()
].copy()

print(f"\n有效配对样本量: {len(change_data)}")

# 配对t检验
t_stat, p_value = ttest_rel(change_data['thrift_past_year_num'], 
                            change_data['thrift_five_years_ago_num'])

print("\n=== 配对样本t检验 ===")
print(f"t统计量 = {t_stat:.4f}")
print(f"p值 = {p_value:.4f}")
if p_value < 0.05:
    print("结论: 过去一年与五年前的购物频率存在显著差异 (p < 0.05)")
else:
    print("结论: 过去一年与五年前的购物频率无显著差异 (p >= 0.05)")

# 变化统计
print("\n=== 变化统计 ===")
print(f"平均变化: {change_data['thrift_change'].mean():.2f} 次/年")
print(f"中位数变化: {change_data['thrift_change'].median():.2f} 次/年")
print(f"标准差: {change_data['thrift_change'].std():.2f}")
print(f"\n增加的人数: {(change_data['thrift_change'] > 0).sum()} ({(change_data['thrift_change'] > 0).mean()*100:.1f}%)")
print(f"减少的人数: {(change_data['thrift_change'] < 0).sum()} ({(change_data['thrift_change'] < 0).mean()*100:.1f}%)")
print(f"不变的人数: {(change_data['thrift_change'] == 0).sum()} ({(change_data['thrift_change'] == 0).mean()*100:.1f}%)")

# 变化方向分类
def categorize_change(value):
    if value > 5:
        return "Significant Increase"
    elif value > 0:
        return "Slight Increase"
    elif value == 0:
        return "No Change"
    elif value >= -5:
        return "Slight Decrease"
    else:
        return "Significant Decrease"

change_data['change_direction'] = change_data['thrift_change'].apply(categorize_change)
print("\n变化方向分布:")
print(change_data['change_direction'].value_counts())

# 可视化: 变化分布直方图
plt.figure(figsize=(10, 6))
plt.hist(change_data['thrift_change'], bins=20, color='#f39c12', 
         alpha=0.8, edgecolor='white')
plt.axvline(x=0, color='red', linestyle='--', linewidth=2, label='No Change')
plt.axvline(x=change_data['thrift_change'].mean(), color='blue', 
            linestyle='--', linewidth=2, label=f'Mean Change ({change_data["thrift_change"].mean():.1f})')
plt.xlabel('Change in Frequency (Past Year - Five Years Ago)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Change in Thrifting Frequency Over 5 Years', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/09_thrift_change_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# 成对比较可视化
sample_size = min(50, len(change_data))
sample_data = change_data.sample(n=sample_size, random_state=42)

plt.figure(figsize=(10, 6))
for idx, row in sample_data.iterrows():
    plt.plot([1, 2], [row['thrift_five_years_ago_num'], row['thrift_past_year_num']], 
             'o-', color='gray', alpha=0.3, markersize=4)

# 平均值线
avg_five_years = change_data['thrift_five_years_ago_num'].mean()
avg_past_year = change_data['thrift_past_year_num'].mean()
plt.plot([1, 2], [avg_five_years, avg_past_year], 
         'o-', color='#e74c3c', linewidth=3, markersize=10, label='Average Trend')

plt.xticks([1, 2], ['Five Years Ago', 'Past Year'])
plt.ylabel('Frequency (times per year)', fontsize=12)
plt.title(f'Individual Changes in Thrifting Frequency (Sample of {sample_size})', 
          fontsize=14, fontweight='bold')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/10_paired_change_plot.png', dpi=300, bbox_inches='tight')
plt.close()

# 按当前频率分组查看变化
print("\n=== 按当前购物频率分组的变化情况 ===")
change_by_group = change_data.groupby('thrift_frequency_group').agg({
    'respondentID': 'count',
    'thrift_past_year_num': 'mean',
    'thrift_five_years_ago_num': 'mean',
    'thrift_change': 'mean'
}).round(2)

change_by_group.columns = ['n', 'avg_past_year', 'avg_five_years_ago', 'avg_change']

# 计算增加和减少的百分比
for group in change_data['thrift_frequency_group'].unique():
    if pd.notna(group):
        group_data = change_data[change_data['thrift_frequency_group'] == group]
        pct_increased = (group_data['thrift_change'] > 0).mean() * 100
        pct_decreased = (group_data['thrift_change'] < 0).mean() * 100
        change_by_group.loc[group, 'pct_increased'] = round(pct_increased, 1)
        change_by_group.loc[group, 'pct_decreased'] = round(pct_decreased, 1)

print(change_by_group)

print("\n时间变化分析可视化完成!")

# ============================================================================
# 7. 其他发现和深入分析
# ============================================================================

print("\n" + "=" * 80)
print("其他发现和深入分析")
print("=" * 80)

# 7.1 收入水平的影响
print("\n=== 收入水平对购物频率的影响 ===")
income_analysis = data_clean.groupby('income_level').agg({
    'respondentID': 'count',
    'thrift_past_year_num': 'mean',
    'motivated_by_affordability': lambda x: x.mean() * 100
}).round(2)

income_analysis.columns = ['n', 'avg_frequency', 'pct_motivated_by_affordability']

# 按收入排序
income_order = ['Low', 'Medium-Low', 'Medium', 'High']
income_analysis = income_analysis.reindex([i for i in income_order if i in income_analysis.index])
print(income_analysis)

# 可视化
plt.figure(figsize=(10, 6))
income_data = data_clean[data_clean['income_level'].notna()]
income_data['income_level'] = pd.Categorical(income_data['income_level'], 
                                             categories=income_order, ordered=True)
income_groups = [income_data[income_data['income_level'] == level]['thrift_past_year_num'].values 
                for level in income_order if level in income_data['income_level'].values]

bp = plt.boxplot(income_groups, labels=[l for l in income_order if l in income_data['income_level'].values],
                patch_artist=True, widths=0.6)
colors_income = ['#e74c3c', '#f39c12', '#f1c40f', '#2ecc71']
for patch, color in zip(bp['boxes'], colors_income):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

plt.xlabel('Income Level', fontsize=12)
plt.ylabel('Frequency (times per year)', fontsize=12)
plt.title('Thrifting Frequency by Income Level', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('plots/11_income_vs_frequency.png', dpi=300, bbox_inches='tight')
plt.close()

# 7.2 国际学生 vs 本地学生
print("\n=== 国际学生 vs 本地学生 ===")
intl_analysis = data_clean.groupby('international_student').agg({
    'respondentID': 'count',
    'thrift_past_year_num': 'mean',
    'social_accept_num': 'mean',
    'motivated_by_affordability': lambda x: x.mean() * 100
}).round(2)

intl_analysis.columns = ['n', 'avg_frequency', 'avg_social_accept', 'pct_motivated_by_affordability']
print(intl_analysis)

# t检验
intl_yes = data_clean[data_clean['international_student'] == 'Yes']['thrift_past_year_num'].dropna()
intl_no = data_clean[data_clean['international_student'] == 'No ']['thrift_past_year_num'].dropna()
t_stat_intl, p_val_intl = ttest_ind(intl_yes, intl_no)
print(f"\nt检验结果: t = {t_stat_intl:.4f}, p = {p_val_intl:.4f}")
if p_val_intl < 0.05:
    print("结论: 国际学生与本地学生的购物频率存在显著差异")
else:
    print("结论: 国际学生与本地学生的购物频率无显著差异")

# 7.3 政治观点的影响
print("\n=== 政治观点对购物行为的影响 ===")
political_data = data_clean[data_clean['political_views'].notna() & (data_clean['political_views'] != '')]
political_analysis = political_data.groupby('political_views').agg({
    'respondentID': 'count',
    'thrift_past_year_num': 'mean',
    'motivated_by_sustainability': lambda x: x.mean() * 100
}).round(2)

political_analysis.columns = ['n', 'avg_frequency', 'pct_motivated_by_sustainability']
political_analysis = political_analysis.sort_index()
print(political_analysis)

# 7.4 价格感知统计
print("\n=== 价格感知详细分析 ===")
price_perception_counts = data_clean['price_perception'].value_counts()
print("\n价格感知分布:")
print(price_perception_counts)
print("\n比例:")
print((price_perception_counts / price_perception_counts.sum() * 100).round(1))

# Kruskal-Wallis检验（非参数）
price_groups = [data_clean[data_clean['price_perception_num'] == i]['thrift_past_year_num'].dropna().values
               for i in [1, 2, 3] if i in data_clean['price_perception_num'].values]
h_stat, p_val_kw = kruskal(*price_groups)
print(f"\nKruskal-Wallis检验: H = {h_stat:.4f}, p = {p_val_kw:.4f}")
if p_val_kw < 0.05:
    print("结论: 价格感知对购物频率有显著影响")
else:
    print("结论: 价格感知对购物频率无显著影响")

print("\n所有可视化图表生成完成!")

# ============================================================================
# 8. 保存结果摘要
# ============================================================================

print("\n" + "=" * 80)
print("保存分析结果")
print("=" * 80)

results_summary = {
    'sample_size': len(data_clean),
    'avg_thrift_past_year': data_clean['thrift_past_year_num'].mean(),
    'avg_thrift_five_years': data_clean['thrift_five_years_ago_num'].mean(),
    'avg_change': change_data['thrift_change'].mean(),
    't_test_p_value': p_value,
    'pct_increased': (change_data['thrift_change'] > 0).mean() * 100,
    'pct_decreased': (change_data['thrift_change'] < 0).mean() * 100,
    'model_r_squared': model1.rsquared,
    'model_adj_r_squared': model1.rsquared_adj
}

# 保存为JSON
import json
with open('analysis_results_summary.json', 'w', encoding='utf-8') as f:
    json.dump(results_summary, f, indent=2, ensure_ascii=False)

# 保存详细结果
barriers_by_group.to_csv('results_barriers_by_group.csv')
change_by_group.to_csv('results_change_by_group.csv')
income_analysis.to_csv('results_income_analysis.csv')
intl_analysis.to_csv('results_international_analysis.csv')
political_analysis.to_csv('results_political_analysis.csv')

print("\n分析完成！")
print("- 图表保存在: plots/")
print("- 清洗后数据: data_cleaned.csv")
print("- 结果摘要: analysis_results_summary.json")
print("- 详细结果表格: results_*.csv")
print("\n" + "=" * 80)

