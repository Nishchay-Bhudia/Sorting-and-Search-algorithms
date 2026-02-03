# Sorting and Searching Visualiser

This project demonstrates how popular sorting and searching algorithms work using animated visualisations built with **Matplotlib**. It helps users understand how algorithms process data step-by-step in a visual and interactive way.

## Features

- Binary Search visualisation  
- Bubble Sort visualisation  
- Insertion Sort visualisation  
- Customisable themes (dark / light mode)  
- Adjustable animation speed  
- Randomly generated datasets  

## Algorithms Included

### 🔍 Searching
- Binary Search

### 📊 Sorting
- Bubble Sort
- Insertion Sort

## How It Works

Each algorithm is implemented using Python generators. These generators produce frames that are animated using **Matplotlib Animation**. The bars represent data values and change colour to show comparisons, active elements, and sorted sections.

## Requirements

Make sure you have Python installed, then install the required libraries:

```bash
pip install matplotlib
```

Each file runs a different algorithm visualisation.

## Customisation

You can change settings inside each script:

- `BAR_COUNT` → Number of data bars  
- `SPEED` → Animation speed  
- `THEME` → `"dark"` or `"light"` mode  

## Purpose

This project is designed to help students and beginners learn algorithm behaviour visually rather than only through theory or code.

## Preview

Bars represent numbers. Colours highlight:
- Active comparisons  
- Search ranges  
- Sorted sections  
- Target values  

## License

This project is open source and free to use for educational purposes.
MIT LICENSE
