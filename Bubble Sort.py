import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#setup parameters
BAR_COUNT = 50
THEME = "dark"   # Change to "light"
SPEED = 40       # Lower = faster

#theme colors

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

#generate random data
data = [random.randint(10, 400) for _ in range(BAR_COUNT)]

#sorting algorithm

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            yield arr, j, j + 1, n - i

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr, j, j + 1, n - i

    yield arr, -1, -1, 0


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

#update aniation through matplotlib

def update(frame):
    arr, current1, current2, sorted_start = frame

    for i, (bar, val) in enumerate(zip(bars, arr)):
        bar.set_height(val)

        if i == current1 or i == current2:
            bar.set_color(ACTIVE)

        elif i >= sorted_start:
            bar.set_color(SORTED)

        else:
            bar.set_color(BAR)

    return bars

#run the animation

ani = animation.FuncAnimation(
    fig,
    update,
    frames=bubble_sort(data),
    interval=SPEED,
    repeat=False
)

plt.tight_layout()
plt.show()
