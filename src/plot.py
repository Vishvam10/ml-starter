import catppuccin
import matplotlib as mpl
from catppuccin.extras.matplotlib import get_colormap_from_list

# ------------------------------------------------------------------------------
# THEME
# ------------------------------------------------------------------------------
mpl.style.use(catppuccin.PALETTE.macchiato.identifier)

cmap = get_colormap_from_list(
    catppuccin.PALETTE.macchiato.identifier, ["blue", "mauve", "green"]
)