import pandas as pd
import dill
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("Loading data...")
data = pd.read_csv('../data/data_processed.csv')
print("Data info:")
data.info()

data = data.dropna()
X = data['comment_text']
targets = data.drop('comment_text', axis=1)

print("Vectorizing data...")
vectorizer = TfidfVectorizer(max_features=4096, stop_words='english')
tfidf_data = vectorizer.fit_transform(X)

print("Saving vectorizer...")
with open('../models/tf-idf_vectorizer.pkl', 'wb') as f:
    dill.dump(vectorizer, f)

models = {}

for target in targets.columns:
    model = LogisticRegression(class_weight='balanced', max_iter=500, C=1.6)
    print(f'\nTraining model for: {target}')
    y = data[target]
    model.fit(tfidf_data, y)
    models[target] = model  
    y_pred = model.predict(tfidf_data)
    print(f'Training Accuracy: {accuracy_score(y, y_pred)}')

print("\nSaving classifier models...")
with open('../models/classifier.pkl', 'wb') as f:
    dill.dump(models, f)

print("Done!")
