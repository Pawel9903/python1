import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[10, 4])
axins1 = inset_axes(ax1,
                    width="50%",
                    height="5%",
                    loc=1)

im1 = ax1.imshow([[1, 2], [2, 3]])
plt.colorbar(im1, cax=axins1, orientation="horizontal", ticks=[1, 2, 3])
axins1.xaxis.set_ticks_position("bottom")

axins2 = inset_axes(ax2,
                    width="5%",
                    height="50%",
                    loc=3,
                    bbox_to_anchor=(1.05, 0., 1, 1),
                    bbox_transform=ax2.transAxes,
                    borderpad=0,
                   )

im2 = ax2.imshow([[1, 2], [2, 3]])
plt.colorbar(im2, cax=axins2, ticks=[1, 2, 3])
plt.draw()
plt.show()