# import tkinter as tk
# from pyfirmata import Arduino, util
#
#
# def change_rpm():
#     next_rpm_value = enter_rpm.get()
#     lbl_value_now["text"] = next_rpm_value
#
#
# window = tk.Tk()
# window.title("Raport Turatie")
# window.resizable(
#     width=True,
#     height=True,
# )
#
# frm_entry = tk.Frame(master=window)
# enter_rpm = tk.Entry(
#     master=frm_entry,
#     width=10
# )
#
# lable_rpm = tk.Label(
#     master=frm_entry,
#     text="RPM -> 0 - 255: "
# )
#
# enter_rpm.grid(
#     row=0,
#     column=1,
#     sticky="e"
# )
#
# lable_rpm.grid(
#     row=0,
#     column=0,
#     sticky="w"
# )
#
# button_change_rpm = tk.Button(
#     master=window,
#     text="CHANGE",
#     command=change_rpm,
# )
#
# lbl_value_now = tk.Label(
#     master=window,
# )
#
# print(lbl_value_now)
# # TODO:add grid and make the display of the transmission ratio!!
# frm_transmission = tk.Entry(
#     master=frm_entry,
#     width=20
# )
#
# # Layout program
# frm_entry.grid(
#     row=0,
#     column=0,
#     padx=10
# )
#
# button_change_rpm.grid(
#     row=0,
#     column=1,
#     pady=10,
# )
#
# window.mainloop()
#
# # def main():
# #     userWindow()
#
#
# # if __name__ == '__main__':
# #     main()


import tkinter as tk
from pyfirmata import Arduino, util

root = tk.Tk()

user_input = tk.StringVar(root)
answer = 3
board = Arduino("COM10")

# def verify():
#     # print(int(user_input.get()))  # calling get() here!
#     # x = int(user_input.get())


entry = tk.Entry(root, textvariable=user_input)
entry.pack()

check = tk.Button(root, text='check 3')
check.pack()
print(user_input.get())

root.mainloop()
