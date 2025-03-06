# 📌 Email Clustering using SBERT and FAISS

This project provides an efficient way to cluster similar emails using **SBERT (Sentence-BERT)** for text embeddings and **FAISS (Facebook AI Similarity Search)** for fast and scalable clustering.

---

## 🚀 Features
- 📂 Reads emails from an **Excel file**.
- 🤖 Uses **SBERT** (`all-MiniLM-L6-v2`) to convert emails into numerical embeddings.
- 📊 Clusters emails using **FAISS K-Means**.
- 💾 Saves clustered results in a new **Excel file**.
- ⚡ Fast and scalable for large datasets.

---

## 🛠 Requirements
Install dependencies using:
```bash
pip install pandas openpyxl sentence-transformers faiss-cpu
```

---

## 📌 Usage
1. Place your emails in an **Excel file** (e.g., `emails.xlsx`).
2. Run the notebook to:
   - 📖 Read the emails
   - 🔢 Convert them into embeddings
   - 📌 Cluster using FAISS
   - 💾 Save results to `faiss_clustered_emails.xlsx`
3. Check the output file for cluster assignments.

---

## ⚙️ Configuration
- Modify `num_clusters` to adjust the number of clusters.
- Change **FAISS parameters** (`eps`, `min_samples`) for different clustering behavior.
- Use **`all-mpnet-base-v2`** instead of `all-MiniLM-L6-v2` for better accuracy.

---

## 📄 Output
The output file (`faiss_clustered_emails.xlsx`) contains emails with their assigned cluster labels.

### 🔹 Example Clustering Output
```
Cluster 0:
  - "Meeting scheduled for tomorrow at 10 AM."
  - "Let's have a call regarding the new project."

Cluster 1:
  - "Your invoice for the last order is attached."
  - "Your payment has been processed successfully."
```
