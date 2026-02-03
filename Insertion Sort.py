import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# settings
BAR_COUNT = 20  #Number of bars to sort
THEME = "dark"   # Change to "light" if you want white background
SPEED = 1   # Lower = faster



if THEME == "dark":
    BG = "#0f0f0f"
    BAR = "#4cc9f0"
    ACTIVE = "#ff595e"
    SORTED = "#80ed99"
else:
    BG = "#ffffff"
    BAR = "#4361ee"
    ACTIVE = "#ef233c"
    SORTED = "#2ec4b6"

#random data

data = [random.randint(10, 400) for _ in range(BAR_COUNT)]

#sorting algorithm 

def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr, j + 1, i

        arr[j + 1] = key
        yield arr, j + 1, i

    yield arr, -1, len(arr)

#visualization setup through matplotlib

fig, ax = plt.subplots()
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

bars = ax.bar(range(len(data)), data, color=BAR, width=0.85)

#remove axes for cleaner look
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xlim(0, BAR_COUNT)
ax.set_ylim(0, max(data) * 1.1)

#update animation function

def update(frame):
    arr, current, sorted_index = frame

    for i, (bar, val) in enumerate(zip(bars, arr)):
        bar.set_height(val)

        if i == current:
            bar.set_color(ACTIVE)
        elif i <= sorted_index:
            bar.set_color(SORTED)
        else:
            bar.set_color(BAR)

    return bars

#run the animation

ani = animation.FuncAnimation(
    fig,
    update,
    frames=insertion_sort(data),
    interval=SPEED,
    repeat=False
)

plt.tight_layout()
plt.show()
