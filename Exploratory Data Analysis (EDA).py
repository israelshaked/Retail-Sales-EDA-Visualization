import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. יצירת דאטה-סט של מכירות
data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Laptop', 'Monitor', 'Mouse', 'Laptop', 'Keyboard', 'Monitor'],
    'Sales_Amount': [1200, 50, 300, 80, 1250, 310, 55, 1180, 85, 290],
    'Day_of_Week': ['Mon', 'Mon', 'Tue', 'Tue', 'Wed', 'Wed', 'Thu', 'Thu', 'Fri', 'Fri'],
    'Discount_Applied': [True, False, False, True, True, False, False, False, True, False]
}

df = pd.DataFrame(data)

# 2. ניתוח בסיסי - ממוצע מכירות לפי מוצר
product_sales = df.groupby('Product')['Sales_Amount'].sum().reset_index()

# 3. ויזואליזציה 1: גרף עמודות של סך מכירות לפי מוצר
plt.figure(figsize=(10, 6))
# הוספנו hue='Product' ו-legend=False כדי להשתיק את האזהרה
sns.barplot(x='Product', y='Sales_Amount', data=product_sales, hue='Product', palette='viridis', legend=False)
plt.title('Total Sales by Product')
plt.xlabel('Product Name')
plt.ylabel('Total Revenue ($)')
plt.show()

# 4. ויזואליזציה 2: הקשר בין הנחה למחיר המכירה (Boxplot)
plt.figure(figsize=(8, 5))
sns.boxplot(x='Discount_Applied', y='Sales_Amount', data=df)
plt.title('Impact of Discounts on Sales Amount')
plt.show()

print("EDA Analysis complete. Graphs generated.")