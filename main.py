import tkinter
import ball
import hole
import sim

anBall = ball.Ball('white', 5, 0)
anHole = hole.Hole(250, 0, 300, 0)


window = tkinter.Tk()
window.geometry('800x600')
window.title('GolfPy')

canvas = tkinter.Canvas(window, bg = 'cyan', width=800, height=600)
canvas.pack()
canvas.create_rectangle(0, 450, 800, 600, fill = 'green')

anSim = sim.Sim(ball, hole, 45, 30, 0, canvas)
anSim.startSim()



window.mainloop()