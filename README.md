# Disease Symptom Checker using Bayes' Rule

A simple Python project I built for the BYOP assignment in CSA2001.
It takes symptoms as input and uses Bayes' Rule to guess which disease
you might have.
---

## What it does

You type in symptoms like fever or cough, and the program calculates
the probability of 5 diseases — Flu, Cold, Malaria, Typhoid, and COVID.
It then tells you which one is most likely, along with percentages for all.

I got the idea from the Unit 3 slides where our professor used the
cavity and toothache example to explain Bayes' Rule. I thought —
why not build something similar but for real symptoms?

---

## Why I chose this project

Honestly I wanted something I could actually understand and code myself.
Bayes' Rule was one of the clearest things in Unit 3 for me — the formula
P(Disease | Symptoms) = P(Symptoms | Disease) × P(Disease) / P(Symptoms)
made sense once I saw the meningitis example in the slides. So I built
this project around that same idea.

---

## How this connects to Unit 3

| What I learned in class | How I used it in code |
|---|---|
| Prior Probability P(Disease) | the diseases dictionary |
| Conditional Probability P(Symptom Disease) | the symptoms_prob dictionary |
| Bayes' Rule formula | the main calculation loop |
| Normalisation / P(Symptoms) | dividing by total at the end |
| Posterior Probability | the final percentage output |

---

## How to run it


git clone https://github.com/maahi-y/disease-symptom-checker.git cd disease-symptom-checker python symptom_checker.py

Then just type your symptoms when it asks.

---

## Symptoms you can enter


fever, cough, headache, runny_nose, body_ache, chills, sore_throat, fatigue, nausea, loss_of_taste

Type them separated by commas like:

Enter your symptoms: fever, chills, body_ache

---

## Example outputs

**fever, chills, body_ache → Malaria**

Malaria 43.21% ████████ 
Flu 28.14% █████ 
Typhoid 16.82% ███ 
COVID 8.74% █ 
Cold 3.09%
Most likely: Malaria (43.21%)

**runny_nose, sore_throat, cough → Cold**

Cold 61.25% ████████████ 
Flu 19.84% ███ 
COVID 12.47% ██
Typhoid 4.31%
Malaria 2.13%
Most likely: Cold (61.25%)

**loss_of_taste, fatigue, cough → COVID**

COVID 71.33% ██████████████ 
Flu 16.42% ███ 
Malaria 7.21% █ 
Typhoid 3.58%
Cold 1.46%
Most likely: COVID (71.33%)

---

## Honest limitations

- I set the probability numbers myself based on general knowledge,
  not real medical data
- Only 5 diseases and 10 symptoms — a real system would need way more
- Obviously not actual medical advice, just an academic project

---

## About

Made by: [Maahi Yadav] | [25BCE10998]
student of VIT Bhopal university


