import gradio as gr
from catppuccin import PALETTE

# ------------------------------------------------------------------------------
# THEME
# ------------------------------------------------------------------------------

mocha = PALETTE.mocha.colors

catppuccin_theme = gr.themes.Default(
    primary_hue=gr.themes.utils.colors.Color(
        name="mauve",
        c50=mocha.lavender.hex,
        c100=mocha.lavender.hex,
        c200=mocha.lavender.hex,
        c300=mocha.mauve.hex,
        c400=mocha.mauve.hex,
        c500=mocha.mauve.hex,
        c600=mocha.mauve.hex,
        c700=mocha.mauve.hex,
        c800=mocha.mauve.hex,
        c900=mocha.mauve.hex,
        c950=mocha.mauve.hex,
    ),
    neutral_hue=gr.themes.utils.colors.Color(
        name="mocha",
        c50=mocha.text.hex,
        c100=mocha.subtext1.hex,
        c200=mocha.subtext0.hex,
        c300=mocha.overlay2.hex,
        c400=mocha.overlay1.hex,
        c500=mocha.overlay0.hex,
        c600=mocha.surface2.hex,
        c700=mocha.surface1.hex,
        c800=mocha.surface0.hex,
        c900=mocha.base.hex,
        c950=mocha.crust.hex,
    ),
).set(
    body_background_fill=mocha.base.hex,
    block_background_fill=mocha.mantle.hex,
    block_border_color=mocha.surface0.hex,
)

demo = gr.Interface(
    title="Title", description="Description", theme=catppuccin_theme
)

demo.launch()
