import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Sample dataset (you can expand this)
data = [
    {"title": "Fix critical bug", "description": "Urgent production issue", "priority": "high"},
    {"title": "Write documentation", "description": "Add usage guide", "priority": "low"},
    {"title": "Update UI", "description": "Improve user interface layout", "priority": "medium"},
    {"title": "Deploy to production", "description": "Final deployment", "priority": "high"},
    {"title": "Clean up code", "description": "Refactor and organize files", "priority": "medium"},
    {"title": "Schedule meeting", "description": "Discuss features", "priority": "low"},
]

df = pd.DataFrame(data)
df['text'] = df['title'] + " " + df['description']

# Create pipeline
model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

# Train
model.fit(df['text'], df['priority'])

# Save model
joblib.dump(model, 'priority_model.joblib')
print("✅ Model trained and saved as priority_model.joblib")
