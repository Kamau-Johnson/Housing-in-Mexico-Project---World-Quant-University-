*Import libraries*

```python
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
```
*Import the CSV file*

```python
df = pd.read_csv("data/mexico-real-estate.csv")
```
*Inspect the DataFrame*

```python
df.info()
df.head()
```
*Drop all rows with NaN values*

```python
df = df.dropna()
```
*Create separate columns "lat" and "lon" from "lat-lon"*

```python
df[['lat', 'lon']] = df['lat-lon'].str.split(',', expand=True).astype(float)
```
*Extract "state" from "place_with_parent_names"*

```python
df['state'] = df['place_with_parent_names'].str.split('|México|').str[1].str.strip()
```
*Transform "price_usd" to float*

```python
df['price_usd'] = df['price_usd'].str.replace('$','').str.replace(',','').astype(float)
```
*Drop "lat-lon" and "place_with_parent_names" columns*

```python
df = df.drop(columns=['lat-lon','place_with_parent_names'])
```
*Create summary statistics for "area_m2" and "price_usd"*

```python
summary_stats = df[['area_m2','price_usd']].describe()
summary_stats
```
*Create histogram of "price_usd"*

```python
plt.hist(df['price_usd'][:20000])
plt.xlabel("Price [USD]")
plt.ylabel("Frequency")
plt.title("Distribution of Home Prices")
plt.show()
```
*Create horizontal boxplot of "area_m2"*

```python
plt.boxplot(df['area_m2'], vert=False)
plt.xlabel("Area [sq meters]")
plt.title("Distribution of Home Sizes")
plt.show()
```
*Mean home price by region*

```python
mean_price_by_region = df.groupby("region")['price_usd'].mean().sort_values()
mean_price_by_region
```
*Bar chart of mean home price by region*

```python
mean_price_by_region.plot(kind='bar')
plt.xlabel("Region")
plt.ylabel("Mean Price [USD]")
plt.title("Mean Home Price by Region")
plt.show()
```
*Create DataFrame for southern region*

```python
df_south = df[df['region'] == 'South']
```
*Number of homes by state in southern region*

```python
homes_by_state = df_south['state'].value_counts()
homes_by_state
```


```python
*Scatter plot for the state with most properties*
```


```python
largest_state = homes_by_state.idxmax()
df_south_state = df_south[df_south['state'] == largest_state]
plt.scatter(df_south_state['area_m2'], df_south_state['price_usd'])
plt.xlabel("Area [sq meters]")
plt.ylabel("Price [USD]")
plt.title(f"{largest_state}: Price vs. Area")
plt.show()
```


```python
*Correlation between area and price for southern states*
```


```python
south_states_corr = {state: df_south[df_south['state']==state]['area_m2'].corr(
    df_south[df_south['state']==state]['price_usd']) for state in df_south['state'].unique()}
south_states_corr
```
