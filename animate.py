import pandas as pd
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
from IPython import display

style.use('fivethirtyeight')
fig = plt.figure(figsize=(15, 6), dpi=200)
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)


def animate(i):
    df = pd.read_csv('real_time_stock_price.csv')
    y = df.iloc[:i, 2].values
    x = list(range(1, len(y) + 1))
    ax1.clear()
    ax1.plot(x, y)
    ax1.set_title('BTC-GBP', fontsize=8)

    y = df.iloc[:i, 3].values
    ax2.clear()
    ax2.plot(x, y)
    ax2.set_title('ETH-GBP', fontsize=8)

    y = df.iloc[:i, 4].values
    ax3.clear()
    ax3.plot(x, y)
    ax3.set_title('LTC-GBP', fontsize=8)

    y = df.iloc[:i, 5].values
    ax4.clear()
    ax4.plot(x, y)
    ax4.set_title('LINK-GBP', fontsize=8)


# ani = animation.FuncAnimation(fig, animate, interval=10000)
ani = animation.FuncAnimation(fig, animate, interval=5000, frames=100, repeat=False)
#video = ani.to_html5_video()
#html = display.HTML(video)
#display.display(html)
#plt.close()
writervideo = animation.FFMpegWriter(fps=30)
ani.save('animation.gif', writer=writervideo)
plt.close()
#plt.tight_layout()
#plt.show()
