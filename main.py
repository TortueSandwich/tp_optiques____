import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    data = {
        "Id": [0,     0.033, 0.066,   0.1,   0.2,   0.3,   0.4,   0.5,   0.6],
        "Ud": [1.447, 1.740, 1.770, 1.793, 1.845, 1.888, 1.925, 1.959, 1.992],
        "P":  [0.55,   8.07, 17.31,  27.2,  54.9,  81.5, 106.6, 129.7, 151.1],
    }

    data["Id"] = np.array(data["Id"]) / 10.0
    # data["P2"] = np.array(data["P2"]) *10**()
    df = pd.DataFrame(data)

    print(df)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 8), sharex=True)

    ax1.plot(df["Id"], df["Ud"], marker="x", color="tab:blue", alpha=0.7)
    ax1.set_title("Tension Ud en fonction de Id")
    ax1.set_ylabel("Ud (V)")
    ax1.grid(True)

    ax2.plot(df["Id"], df["P"], marker="o", color="tab:orange", alpha=0.7)
    ax2.set_title("Puissance P en fonction de Id")
    ax2.set_xlabel("Id (A)")
    ax2.set_ylabel("P (W)")
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
