import pandas as pd
import numpy as np

np.random.seed(42)

# 365 days
dates = pd.date_range(start="2026-01-01", periods=365)

# -----------------------------
# 1. BASIC DAILY HABITS
# -----------------------------

sleep = np.random.normal(7, 1, 365).clip(4, 10)
screen = np.random.normal(4.5, 1.5, 365).clip(1, 10)
study = np.random.normal(3.5, 1.5, 365).clip(0, 8)
exercise = np.random.randint(0, 91, 365)
water = np.random.normal(2.5, 0.6, 365).clip(1, 4)
steps = np.random.randint(2000, 15001, 365)
spending = np.random.randint(100, 1501, 365)

# -----------------------------
# 2. MOOD
# Exercise and sleep improve mood
# Too much screen time lowers mood
# -----------------------------

mood = (
    5
    + (sleep - 6) * 0.8
    + exercise * 0.025
    - (screen - 4) * 0.4
    + np.random.normal(0, 1, 365)
)

mood = np.clip(mood, 1, 10)

# -----------------------------
# 3. PRODUCTIVITY
# Sleep, study and exercise
# improve productivity
# Screen time reduces productivity
# Mood also affects productivity
# -----------------------------

productivity = (
    5
    + (sleep - 6) * 0.8
    + study * 0.45
    + exercise * 0.015
    - (screen - 4) * 0.45
    + (mood - 5) * 0.35
    + np.random.normal(0, 1, 365)
)

productivity = np.clip(productivity, 1, 10)

# -----------------------------
# 4. CREATE DATAFRAME
# -----------------------------

df = pd.DataFrame({
    "Date": dates,
    "Sleep_Hours": np.round(sleep, 1),
    "Screen_Time": np.round(screen, 1),
    "Study_Hours": np.round(study, 1),
    "Exercise_Minutes": exercise,
    "Mood_Score": np.round(mood, 1),
    "Productivity_Score": np.round(productivity, 1),
    "Water_Liters": np.round(water, 1),
    "Steps": steps,
    "Spending": spending
})

# -----------------------------
# 5. WAKE-UP & SLEEP TIME
# -----------------------------

wake_times = pd.date_range(
    "2026-01-01 06:00",
    "2026-01-01 09:00",
    freq="15min"
)

sleep_times = pd.date_range(
    "2026-01-01 22:00",
    "2026-01-02 01:00",
    freq="15min"
)

df["Wake_Up_Time"] = np.random.choice(
    wake_times.strftime("%H:%M"),
    365
)

df["Sleep_Time"] = np.random.choice(
    sleep_times.strftime("%H:%M"),
    365
)

# -----------------------------
# 6. SAVE DATASET
# -----------------------------

df.to_csv("life_pattern_data.csv", index=False)

print("Dataset created successfully!")

# -----------------------------
# 7. BASIC ANALYSIS
# -----------------------------

print("\n--- LIFE PATTERN SUMMARY ---")

print("Average Sleep:",
      round(df["Sleep_Hours"].mean(), 2), "hours")

print("Average Screen Time:",
      round(df["Screen_Time"].mean(), 2), "hours")

print("Average Study Time:",
      round(df["Study_Hours"].mean(), 2), "hours")

print("Average Exercise:",
      round(df["Exercise_Minutes"].mean(), 2), "minutes")

print("Average Mood:",
      round(df["Mood_Score"].mean(), 2))

print("Average Productivity:",
      round(df["Productivity_Score"].mean(), 2))

print("Average Daily Spending: ₹",
      round(df["Spending"].mean(), 2))

# -----------------------------
# 8. CORRELATION ANALYSIS
# -----------------------------

print("\n--- CORRELATION WITH PRODUCTIVITY ---")

correlations = df[
    [
        "Sleep_Hours",
        "Screen_Time",
        "Study_Hours",
        "Exercise_Minutes",
        "Mood_Score",
        "Water_Liters",
        "Steps",
        "Spending",
        "Productivity_Score"
    ]
].corr()["Productivity_Score"].sort_values(
    ascending=False
)

print(correlations)
import matplotlib.pyplot as plt
import numpy as np

# Data
x = df["Exercise_Minutes"]
y = df["Mood_Score"]

# Scatter plot
plt.scatter(x, y)

# Trendline
trend = np.polyfit(x, y, 1)
line = np.poly1d(trend)

plt.plot(x, line(x))

# Labels
plt.xlabel("Exercise Minutes")
plt.ylabel("Mood Score")
plt.title("Exercise vs Mood")

plt.show()
# -----------------------------
# 9. AUTOMATIC INSIGHTS
# -----------------------------

print("\n--- AUTOMATIC LIFE PATTERN INSIGHTS ---")

sleep_corr = df["Sleep_Hours"].corr(df["Productivity_Score"])
screen_corr = df["Screen_Time"].corr(df["Productivity_Score"])
exercise_mood_corr = df["Exercise_Minutes"].corr(df["Mood_Score"])

if sleep_corr > 0:
    print("Sleep Insight: More sleep is associated with higher productivity.")
else:
    print("Sleep Insight: More sleep is associated with lower productivity.")

if screen_corr < 0:
    print("Screen Insight: More screen time is associated with lower productivity.")
else:
    print("Screen Insight: More screen time is associated with higher productivity.")

if exercise_mood_corr > 0:
    print("Exercise Insight: More exercise is associated with better mood.")
else:
    print("Exercise Insight: More exercise is associated with lower mood.")

print("\nCorrelation Values:")
print("Sleep → Productivity:", round(sleep_corr, 3))
print("Screen Time → Productivity:", round(screen_corr, 3))
print("Exercise → Mood:", round(exercise_mood_corr, 3))