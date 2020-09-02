from time import sleep
import bar

def rerender(context, arr):
    sleep(0.05)
    for item in context.items[:]:
        item.undraw()
    context.update()
    bar.renderBars(context, arr)