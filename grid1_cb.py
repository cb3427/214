import tkinter as tk


root = tk.Tk()
root.wm_geometry("400x400")
root.title("Grid")

frame1 = tk.Frame(root)
frame1.grid(row='0', column='0')
blue = tk.Label(frame1, bg='blue', width="25", height="10")
blue.pack()

frame2 = tk.Frame(root)
frame2.grid(row='0', column='1')
green = tk.Label(frame2, bg='green', width ="10", height="10")
green.pack()

frame3 = tk.Frame(root)
frame3.grid(row='1', column='0')
red = tk.Label(frame3, bg='red', width="25", height="10")
red.pack()

frame4 = tk.Frame(root)
frame4.grid(row='1', column='1')
yellow = tk.Label(frame4, bg='yellow', width="10", height="10")
yellow.pack()

root.mainloop()