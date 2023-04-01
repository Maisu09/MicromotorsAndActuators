import tkinter as tk
import pyfirmata


def userWindow():
    window = tk.Tk()
    greeting = tk.Label(text="Hello, Tkinter")
    greeting.pack()

    window.mainloop()
    

def main():
    userWindow()

if __name__ == '__main__':
    main()