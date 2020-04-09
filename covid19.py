from covid19parse.parser import Covid19Parser
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import pickle

c19 = Covid19Parser.parse()
#pickle.dump( c19, open( 'c19.p', 'wb' ) )
#c19 = pickle.load( open( 'c19.p', 'rb' ) )
country = 'United States'
state = None
place = None
confirmed = c19.get_confirmed(country=country, state=state, place=place)
deaths = c19.get_deaths(country=country, state=state, place=place)
recovered = c19.get_recovered(country=country, state=state, place=place)

root = tkinter.Tk()
root.wm_title('COVID19 %s' % country)

fig = Figure(figsize=(5,4), dpi=100)

t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(list(range(len(confirmed))), confirmed)
fig.add_subplot(111).plot(list(range(len(deaths))), deaths)
fig.add_subplot(111).plot(list(range(len(recovered))), recovered)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.