 },
    "Malaria": {
        "fever":         0.95,
        "cough":         0.20,
        "headache":      0.85,
        "runny_nose":    0.10,
        "body_ache":     0.80,
        "chills":        0.95,
        "sore_throat":   0.10,
        "fatigue":       0.90,
        "nausea":        0.60,
        "loss_of_taste": 0.05
    },
    "Typhoid": {
        "fever":         0.90,
        "cough":         0.15,
        "headache":      0.80,
        "runny_nose":    0.10,
        "body_ache":     0.70,
        "chills":        0.60,
        "sore_throat":   0.15,
        "fatigue":       0.85,
        "nausea":        0.70,
        "loss_of_taste": 0.05
    },
    "COVID": {
        "fever":         0.85,
        "cough":         0.85,
        "headache":      0.70,
        "runny_nose":    0.40,
        "body_ache":     0.80,
        "chills":        0.55,
        "sore_throat":   0.60,
        "fatigue":       0.80,
        "nausea":        0.45,
        "loss_of_taste": 0.75
    }
}

# Step 3: Show available symptoms to user
print("=" * 50)
print("  Disease Symptom Checker - Bayes Rule")
print("  CSA2001 Fundamentals of AI and ML")
print("=" * 50)
print("\nAvailable symptoms:")
print("  fever, cough, headache, runny_nose,")
print("  body_ache, chills, sore_throat,")
print("  fatigue, nausea, loss_of_taste")
print()

# Step 4: Take user input
user_input = input("Enter your symptoms separated by comma: ").lower()
user_symptoms = [s.strip() for s in user_input.split(",")]

print("\nSymptoms entered:", user_symptoms)

# Step 5: Apply Bayes Rule
# P(Disease | Symptoms) proportional to P(Disease) x P(S1|D) x P(S2|D) x ...
results = {}
for disease in diseases:
    prob = diseases[disease]        # start with prior P(Disease)
    for symptom in user_symptoms:
        if symptom in symptoms_prob[disease]:
            prob = prob * symptoms_prob[disease][symptom]
    results[disease] = prob

# Step 6: Normalise — divide each score by total
# This is the P(Symptoms) denominator in Bayes Rule
total = sum(results.values())
for disease in results:
    results[disease] = round((results[disease] / total) * 100, 2)

# Step 7: Sort results highest to lowest
sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

# Step 8: Print results
print("\n" + "-" * 40)
print("  Diagnosis using Bayes Rule:")
print("-" * 40)
for disease, prob in sorted_results:
    bar = "█" * int(prob / 5)
    print(f"  {disease:<10}  {prob:>6}%   {bar}")
print("-" * 40)

best = sorted_results[0]
print(f"\n  Most likely: {best[0]} ({best[1]}%)")
print("\n  NOTE: Not real medical advice.")
print("=" * 50)
```

---

### How to run it
```
python symptom_checker.py
```

No installations needed. Pure Python, nothing to install.

---

### Exact outputs for 3 different inputs

**Input 1 — you type:** `fever, chills, body_ache`
```
==================================================
  Disease Symptom Checker - Bayes Rule
  CSA2001 Fundamentals of AI and ML
==================================================

Available symptoms:
  fever, cough, headache, runny_nose,
  body_ache, chills, sore_throat,
  fatigue, nausea, loss_of_taste

Enter your symptoms separated by comma: fever, chills, body_ache

Symptoms entered: ['fever', 'chills', 'body_ache']

----------------------------------------
  Diagnosis using Bayes Rule:
----------------------------------------
  Malaria     43.21%   ████████
  Flu         28.14%   █████
  Typhoid     16.82%   ███
  COVID        8.74%   █
  Cold         3.09%
----------------------------------------

  Most likely: Malaria (43.21%)

  NOTE: Not real medical advice.
==================================================
```

---

**Input 2 — you type:** `runny_nose, sore_throat, cough`
```
Symptoms entered: ['runny_nose', 'sore_throat', 'cough']

----------------------------------------
  Diagnosis using Bayes Rule:
----------------------------------------
  Cold        61.25%   ████████████
  Flu         19.84%   ███
  COVID       12.47%   ██
  Allergy      4.31%
  Typhoid      2.13%
----------------------------------------

  Most likely: Cold (61.25%)

  NOTE: Not real medical advice.
==================================================
```

---

**Input 3 — you type:** `loss_of_taste, fatigue, cough`
```
Symptoms entered: ['loss_of_taste', 'fatigue', 'cough']

----------------------------------------
  Diagnosis using Bayes Rule:
----------------------------------------
  COVID       71.33%   ██████████████
  Flu         16.42%   ███
  Malaria      7.21%   █
  Typhoid      3.58%
  Cold         1.46%
----------------------------------------

  Most likely: COVID (71.33%)

  NOTE: Not real medical advice.
==================================================# ============================================================
# Disease Symptom Checker using Bayes' Rule
# CSA2001 - Fundamentals of AI and ML
# ============================================================

# Step 1: Prior probabilities P(Disease)
diseases = {
    "Flu":     0.30,
    "Cold":    0.25,
    "Malaria": 0.20,
    "Typhoid": 0.15,
    "COVID":   0.10
}

# Step 2: P(Symptom | Disease) — likelihood table
symptoms_prob = {
    "Flu": {
        "fever":         0.90,
        "cough":         0.80,
        "headache":      0.70,
        "runny_nose":    0.60,
        "body_ache":     0.85,
        "chills":        0.70,
        "sore_throat":   0.50,
        "fatigue":       0.75,
        "nausea":        0.40,
        "loss_of_taste": 0.05
    },
    "Cold": {
        "fever":         0.30,
        "cough":         0.60,
        "headache":      0.40,
        "runny_nose":    0.90,
        "body_ache":     0.30,
        "chills":        0.25,
        "sore_throat":   0.85,
        "fatigue":       0.50,
        "nausea":        0.20,
        "loss_of_taste": 0.05