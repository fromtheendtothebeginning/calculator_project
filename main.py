from levels import MainLevel
from win import Win

if __name__ == '__main__':

    win = Win('计算器','220x320')
    level = MainLevel(win.win)
    level.win_item()

    win.win.mainloop()
    