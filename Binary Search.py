import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm


#setup parameters

BAR_COUNT = 60
THEME = "dark"     # Change to "light"
SPEED = 1000        # Higher = slower (binary search has fewer steps)

#theme 

if THEME == "dark":
    BG = "#0f0f0f"
    BAR = "#4cc9f0"
    ACTIVE = "#ff595e"   # middle
    RANGE = "#ffd166"    # current search range
    TARGET = "#80ed99"   # found target
else:
    BG = "#ffffff"
    BAR = "#4361ee"
    ACTIVE = "#ef233c"
    RANGE = "#ffbe0b"
    TARGET = "#2ec4b6"

#random generated data

data = sorted([random.randint(10, 400) for _ in range(BAR_COUNT)])

# Pick random target from list
target_value = random.choice(data)

#binary search algorithm 

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        yield arr, low, high, mid, False

        if arr[mid] == target:
            yield arr, low, high, mid, True
            return

        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    yield arr, low, high, -1, False


#visualization setup through matplotlib

fig, ax = plt.subplots()
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

bars = ax.bar(range(len(data)), data, color=BAR, width=0.85)

# Remove axes
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xlim(0, BAR_COUNT)
ax.set_ylim(0, max(data) * 1.1)

title = ax.text(
    0.5, 1.02,
    f"Target: {target_value}",
    transform=ax.transAxes,
    ha="center",
    color="white" if THEME == "dark" else "black",
    fontsize=14
)

#update animation 

def update(frame):
    arr, low, high, mid, found = frame

    for i, (bar, val) in enumerate(zip(bars, arr)):
        bar.set_height(val)
         
        #rainbow color for value not yet found
        if not found and val == target_value:
            norm = val / max(arr)
            bar.set_color(cm.rainbow(norm))

        #when target found
        elif found and i == mid:
            bar.set_color(TARGET)

        elif i == mid:
            bar.set_color(ACTIVE)

        elif low <= i <= high:
            bar.set_color(RANGE)

        else:
            bar.set_color(BAR)

    return bars






#run the animation

ani = animation.FuncAnimation(
    fig,
    update,
    frames=binary_search(data, target_value),
    interval=SPEED,
    repeat=False
)

plt.tight_layout()
plt.show()
