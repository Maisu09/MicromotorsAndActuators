import tkinter as tk
import pyfirmata

def change_rpm():
    next_rpm_value = enter_rpm.get()

# def userWindow():

window = tk.Tk()
window.title("Raport Turatie")
window.resizable(
    width = True,
    height = True
)

frm_entry = tk.Frame(master = window)
enter_rpm = tk.Entry(
    master = frm_entry,
    width = 10
)
lable_rpm = tk.Label(
    master = frm_entry,
    text = "RPM -> 0 - 255: " 
)

enter_rpm.grid(
    row = 0,
    column = 1,
    sticky = "e"
)

lable_rpm.grid(
    row = 0,
    column = 0,
    sticky = "w"
)

button_change_rpm = tk.Button(
    master = window,
    command = change_rpm
)


frm_entry.grid(
    row = 0,
    column = 0,
    padx = 10
)


window.mainloop()
    

# def main():
#     userWindow()


# if __name__ == '__main__':
#     main()