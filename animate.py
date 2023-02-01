import pandas as pd
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

#style.use('fivethirtyeight')
style.use('dark_background')
fig = plt.figure(figsize=(15, 6), dpi=200)
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)


def animate(i):
    df = pd.read_csv('real_time_stock_price.csv')
    y = df.iloc[:i, 2].values
    x = list(range(1, len(y) + 1))
    ax1.clear()
    ax1.plot(x, y, color='green')
    ax1.tick_params(axis='x', labelsize=6)
    ax1.tick_params(axis='y', labelsize=6)
    ax1.set_title('BTC-GBP', fontsize=8)

    y = df.iloc[:i, 3].values
    ax2.clear()
    ax2.plot(x, y, color='red')
    ax2.tick_params(axis='x', labelsize=6)
    ax2.tick_params(axis='y', labelsize=6)
    ax2.set_title('ETH-GBP', fontsize=8)

    y = df.iloc[:i, 4].values
    ax3.clear()
    ax3.plot(x, y, color='blue')
    ax3.tick_params(axis='x', labelsize=6)
    ax3.tick_params(axis='y', labelsize=6)
    ax3.set_title('LTC-GBP', fontsize=8)

    y = df.iloc[:i, 5].values
    ax4.clear()
    ax4.plot(x, y, color='magenta')
    ax4.tick_params(axis='x', labelsize=6)
    ax4.tick_params(axis='y', labelsize=6)
    ax4.set_title('LINK-GBP', fontsize=8)


ani = animation.FuncAnimation(fig, animate, interval=2000, frames=100, repeat=False)

writervideo = animation.FFMpegWriter(fps=60)
ani.save('animation.gif', writer=writervideo)
plt.close()
#plt.tight_layout()
#plt.show()
