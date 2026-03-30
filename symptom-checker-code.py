# ============================================================
# Disease Symptom Checker using Naive Bayes
# CSA2001 - Fundamentals of AI and ML
# ============================================================

import math

# Step 1: Prior probabilities P(Disease)
diseases = {
    "Flu":     0.30,
    "Cold":    0.25,
    "Malaria": 0.20,
    "Typhoid": 0.15,
    "COVID":   0.10
}

# Step 2: P(Symptom | Disease)
symptoms_prob = {
    "Flu": {
        "fever": 0.90, "cough": 0.80, "headache": 0.70,
        "runny_nose": 0.60, "body_ache": 0.85, "chills": 0.70,
        "sore_throat": 0.50, "fatigue": 0.75, "nausea": 0.40,
        "loss_of_taste": 0.05
    },
    "Cold": {
        "fever": 0.30, "cough": 0.60, "headache": 0.40,
        "runny_nose": 0.90, "body_ache": 0.30, "chills": 0.25,
        "sore_throat": 0.85, "fatigue": 0.50, "nausea": 0.20,
        "loss_of_taste": 0.05
    },
    "Malaria": {
        "fever": 0.95, "cough": 0.20, "headache": 0.85,
        "runny_nose": 0.10, "body_ache": 0.80, "chills": 0.95,
        "sore_throat": 0.10, "fatigue": 0.90, "nausea": 0.60,
        "loss_of_taste": 0.05
    },
    "Typhoid": {
        "fever": 0.90, "cough": 0.15, "headache": 0.80,
        "runny_nose": 0.10, "body_ache": 0.70, "chills": 0.60,
        "sore_throat": 0.15, "fatigue": 0.85, "nausea": 0.70,
        "loss_of_taste": 0.05
    },
    "COVID": {
        "fever": 0.85, "cough": 0.85, "headache": 0.70,
        "runny_nose": 0.40, "body_ache": 0.80, "chills": 0.55,
        "sore_throat": 0.60, "fatigue": 0.80, "nausea": 0.45,
        "loss_of_taste": 0.75
    }
}

# All valid symptoms
all_symptoms = list(symptoms_prob["Flu"].keys())

# UI
print("=" * 50)
print("  Disease Symptom Checker - Naive Bayes")
print("=" * 50)

print("\nAvailable symptoms:")
print(", ".join(all_symptoms))

# Input
user_input = input("\nEnter symptoms (comma separated): ").lower()
user_symptoms = [s.strip() for s in user_input.split(",")]

# Filter valid symptoms
valid_symptoms = []
invalid_symptoms = []

for s in user_symptoms:
    if s in all_symptoms:
        valid_symptoms.append(s)
    else:
        invalid_symptoms.append(s)

if invalid_symptoms:
    print("\nIgnored invalid symptoms:", invalid_symptoms)

print("Using symptoms:", valid_symptoms)

# Step 3: Apply Naive Bayes using LOG to avoid underflow
results = {}

for disease in diseases:
    log_prob = math.log(diseases[disease])  # log(P(D))

    for symptom in valid_symptoms:
        prob = symptoms_prob[disease][symptom]
        log_prob += math.log(prob)

    results[disease] = log_prob

# Step 4: Convert back from log space
max_log = max(results.values())

exp_results = {}
for d in results:
    exp_results[d] = math.exp(results[d] - max_log)

# Normalize
total = sum(exp_results.values())

final_results = {}
for d in exp_results:
    final_results[d] = round((exp_results[d] / total) * 100, 2)

# Sort
sorted_results = sorted(final_results.items(), key=lambda x: x[1], reverse=True)

# Output
print("\n" + "-" * 40)
print("Diagnosis (Naive Bayes):")
print("-" * 40)

for disease, prob in sorted_results:
    bar = "█" * int(prob / 5)
    print(f"{disease:<10} {prob:>6}%  {bar}")

print("-" * 40)

best = sorted_results[0]
print(f"\nMost likely: {best[0]} ({best[1]}%)")
print("\nNOTE: Not real medical advice.")
print("=" * 50)
  
  







