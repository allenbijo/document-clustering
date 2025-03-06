from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd


file_path = "./1787_2_2025_1.xlsx"
df = pd.read_excel(file_path)  # Reads the Excel file

emails = df.iloc[:, 0].dropna().tolist()  # Remove NaN values and convert to list

print("Read emails")

model = SentenceTransformer('all-MiniLM-L6-v2')

email_embeddings = model.encode(emails, normalize_embeddings=True)
d = email_embeddings.shape[1]  # Dimension of embeddings

num_clusters = 5  # Adjust as needed
kmeans = faiss.Kmeans(d, num_clusters, niter=100, verbose=True)
kmeans.train(email_embeddings)

_, labels = kmeans.index.search(email_embeddings, 1)  # Get closest cluster for each email
labels = labels.flatten()

df['Cluster'] = labels  # Add cluster labels to DataFrame
output_file = "faiss_clustered_emails.xlsx"
df.to_excel(output_file, index=False)

print(f"Clustered emails saved to {output_file}")

clusters = {}
for email, label in zip(emails, labels):
    if label not in clusters:
        clusters[label] = []
    clusters[label].append(email)

for cluster, grouped_emails in clusters.items():
    print(f"Cluster {cluster} (Length: {len(grouped_emails)}):")
    for email in grouped_emails:
        continue
        # print(f"  - {email}")
    print()