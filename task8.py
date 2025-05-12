import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 1: Load Dataset
df = pd.read_csv("Mall_Customers.csv")
print("📥 Dataset loaded successfully!")

# Step 2: Select features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Step 3: Elbow Method to find optimal K
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8,5))
plt.plot(K, inertia, 'bo-')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.grid()
plt.show()

# Step 4: Apply KMeans with k=5
kmeans = KMeans(n_clusters=5, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)

# Step 5: Visualize clusters
plt.figure(figsize=(8,5))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', 
                hue='Cluster', data=df, palette='Set1')
plt.title('Customer Segments')
plt.grid()
plt.show()

# Step 6: Silhouette Score
score = silhouette_score(X, df['Cluster'])
print(f"✅ Silhouette Score: {score:.2f}")
