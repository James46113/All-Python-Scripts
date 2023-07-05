from tkinter import Tk

tk = Tk()
tk.attributes('-alpha', 0.1)
tk.attributes('-topmost', True)
tk.attributes('-fullscreen', True)
tk.config(cursor="watch")
tk.focus_set()
tk.mainloop()
