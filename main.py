import tkinter as tk
import pyfirmata

def change_rpm():
    next_rpm_value = enter_rpm.get()
    lbl_value_now["text"] = f"{next_rpm_value} \N{DEGREE CELSIUS}"



window = tk.Tk()
window.title("Raport Turatie")
window.resizable(
    width = True,
    height = True,
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
    text = "CHANGE",
    command = change_rpm,
)

lbl_value_now = tk.Label(
    master = window,
    text = "\N{DEGREE CELSIUS}"
)


# TODO:add grid and make the display of the transmission ratio!! 
frm_transmission = tk.Entry(
    master = frm_entry,
    width = 20
)

#Layout program
frm_entry.grid(
    row = 0,
    column = 0,
    padx = 10
)

button_change_rpm.grid(
    row = 0,
    column = 1,
    pady = 10,
)



window.mainloop()
    

# def main():
#     userWindow()


# if __name__ == '__main__':
#     main()