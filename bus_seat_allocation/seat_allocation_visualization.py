import matplotlib.pyplot as plt
import numpy as np

def generate_seat_matrix_image(seats):
    rows = len(seats)
    cols = len(seats[0])
    color_matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            color_matrix[i, j] = 1 if seats[i][j] == 'X' else 0

    fig, ax = plt.subplots(figsize=(cols, rows))
    cmap = plt.cm.get_cmap('RdYlGn_r', 2)
    ax.matshow(color_matrix, cmap=cmap)

    for i in range(rows):
        for j in range(cols):
            text = 'X' if color_matrix[i, j] == 1 else 'O'
            ax.text(j, i, text, va='center', ha='center', color='black', fontsize=12)

    ax.set_xticks(np.arange(cols))
    ax.set_yticks(np.arange(rows))
    ax.set_xticklabels([f"{c+1}" for c in range(cols)])
    ax.set_yticklabels([f"R{r+1}" for r in range(rows)])
    ax.set_xlabel("Seat Number")
    ax.set_ylabel("Row")
    plt.title("Bus Seat Matrix (O = Available, X = Booked)")
    plt.tight_layout()
    plt.grid(False)
    plt.show()

# Example usage
generate_seat_matrix_image(bus.seats)
