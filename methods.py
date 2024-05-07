def clean_axes(ax):
    """
    Alternative to ax.axis("off") that allows to include
    xlabel and ylabel
    """
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])
    ax.axes.spines.left.set_visible(False)
    ax.axes.spines.right.set_visible(False)
    ax.axes.spines.top.set_visible(False)
    ax.axes.spines.bottom.set_visible(False)
