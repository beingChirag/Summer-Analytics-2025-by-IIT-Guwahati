import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from xgboost import XGBClassifier

# Load Data
train = pd.read_csv('Train_Data.csv')
test = pd.read_csv('Test_Data.csv')

# Target
train = train.dropna(subset=['age_group'])
train['age_group'] = train['age_group'].map({'Adult': 0, 'Senior': 1})

# Features
features = [col for col in train.columns if col not in ['SEQN', 'age_group'] and col in test.columns]

# Impute missing
imputer = SimpleImputer(strategy='median')
X_train = imputer.fit_transform(train[features])
y_train = train['age_group']
X_test = imputer.transform(test[features])

# Feature Engineering
train['BMI_cat'] = pd.cut(train['BMXBMI'], bins=[0, 18.5, 25, 30, 100], labels=[0, 1, 2, 3])
test['BMI_cat'] = pd.cut(test['BMXBMI'], bins=[0, 18.5, 25, 30, 100], labels=[0, 1, 2, 3])

train['GLU_IN_ratio'] = train['LBXGLU'] / (train['LBXIN'] + 0.1)
test['GLU_IN_ratio'] = test['LBXGLU'] / (test['LBXIN'] + 0.1)

train['is_diabetic'] = (train['DIQ010'] == 1).astype(int)
test['is_diabetic'] = (test['DIQ010'] == 1).astype(int)

# Final Features
final_features = features + ['BMI_cat', 'GLU_IN_ratio', 'is_diabetic']
X_train_full = imputer.fit_transform(train[final_features])
X_test_full = imputer.transform(test[final_features])

# Models
xgb = XGBClassifier(
    n_estimators=600,
    max_depth=8,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.5,
    reg_lambda=1,
    random_state=42
)

rf = RandomForestClassifier(
    n_estimators=500,
    max_depth=12,
    class_weight='balanced',
    random_state=42
)

# Voting Ensemble
ensemble = VotingClassifier(
    estimators=[('xgb', xgb), ('rf', rf)],
    voting='soft'
)

# Train Model
ensemble.fit(X_train_full, y_train)

# Predict
preds = ensemble.predict(X_test_full)

# Save CSV
submission = pd.DataFrame({'age_group': preds.astype(int)})
submission.to_csv('submissionfinal.csv', index=False)

print("✅ submissionfinal.csv is ready!")
