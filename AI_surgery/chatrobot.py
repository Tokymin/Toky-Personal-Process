import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(16, 8))

# Create a timeline
timeline = [1966, 1972, 1992, 1995, 2010, 2014, 2016, 2018, 2019, 2020, 2022, 2023]
labels = [
    "ELIZA (NLP)",
    "PARRY",
    "AI-Chatbot",
    "Alicebot",
    "Apple Siri",
    "Amazon Alexa",
    "OpenAI created",
    "Google Duplex",
    "GPT-2",
    "GPT-3",
    "Google DeepMind",
    "ChatGPT + orthopedic robots"
]

# Y position for the events
y_pos = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6]

# Plot the timeline
ax.plot(timeline, [y + 0.2 for y in y_pos], "k-o", alpha=0.7)

# Add event labels with adjusted positions to avoid overlap
for (x, y, label) in zip(timeline, y_pos, labels):
    offset = 0.5 if y % 2 == 0 else -0.5
    ax.text(x, y + offset, label, ha="center", va="bottom" if y % 2 == 0 else "top", fontsize=10,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white"))

# Draw the major timeline
ax.axhline(y=0.2, color='purple', linestyle='--', linewidth=2)

# Annotate significant events with arrows and labels
annotations = [
    (2010, "Apple Siri"),
    (2014, "Amazon Alexa"),
    (2016, "Google Assistant"),
    (2018, "Google Duplex"),
    (2019, "GPT-2"),
    (2020, "GPT-3"),
    (2022, "InstructGPT"),
    (2023, "AI Chatbot for orthopedics")
]

for (x, label) in annotations:
    ax.annotate(label, xy=(x, 0.2), xytext=(x, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='center', verticalalignment='top', fontsize=10)

# Set labels for x-axis
ax.set_xticks(timeline)
ax.set_xticklabels(timeline)
ax.set_yticks([])

# Set title
plt.title("AI Chatbot and NLP Developments Timeline", fontsize=14)
plt.xlabel("Year")

# Show the plot
plt.show()
