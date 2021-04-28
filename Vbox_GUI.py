from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import array as arr
from tkinter import messagebox

r = tk.Tk()
r.minsize(500, 300)
Lb = Listbox(r)

vm1 = 0
vm2 = 0
vm3 = 0
vm4 = 0
new_clone_n = 2


def show_vms(size):
    vm_list.pack_forget()
    for i in range(size):
        Lb.insert(i, 'vm' + str(i + 1))
    Lb.bind('<Double-1>', go)
    Lb.pack()


def go(event):
    cs = Lb.curselection()
    for li in cs:
        if li == 0:
            print(vm1)
            if vm1 == 0:
                messagebox.showinfo("vm1", "First vm in the list is off")
            else:
                messagebox.showinfo("vm1", "First vm in the list is on")
            on_button.configure(command=lambda: turn_on(0))
            off_button.configure(command=lambda: turn_off(0))
            delete_button.configure(command=lambda: delete_vm(0))
        elif li == 1:
            if vm2 == 0:
                messagebox.showinfo("vm2", "Second vm in the list is off")
            else:
                messagebox.showinfo("vm2", "Second vm in the list is on")
            on_button.configure(command=lambda: turn_on(1))
            off_button.configure(command=lambda: turn_on(1))
            delete_button.configure(command=lambda: delete_vm(1))
        elif li == 2:
            if vm3 == 0:
                messagebox.showinfo("vm2", "Third vm in the list is off")
            else:
                messagebox.showinfo("vm2", "Third vm in the list is on")
            on_button.configure(command=lambda: turn_on(2))
            off_button.configure(command=lambda: turn_on(2))
            delete_button.configure(command=lambda: delete_vm(2))


def delete_vm(index):
    if index == 0:
        Lb.delete(0)
        Lb.insert(0, 'deleted')
    elif index == 1:
        Lb.delete(1)
        Lb.insert(1, 'deleted')
    elif index == 2:
        Lb.delete(2)
        Lb.insert(2, 'deleted')
    elif index == 3:
        Lb.delete(3)
        Lb.insert(3, 'deleted')


def turn_on(index):
    if index == 0:
        global vm1
        vm1 = 1
    elif index == 1:
        global vm2
        vm2 = 1
    elif index == 2:
        global vm3
        vm3 = 1
    elif index == 3:
        global vm4
        vm4 = 1


def turn_off(index):
    if index == 0:
        global vm1
        vm1 = 0
    elif index == 1:
        global vm2
        vm2 = 0
    elif index == 2:
        global vm3
        vm3 = 0
    elif index == 3:
        global vm4
        vm4 = 0


def new_clone():
    global new_clone_n
    Lb.delete(new_clone_n)
    Lb.insert(new_clone_n, 'vm' + str(new_clone_n + 1))
    new_clone_n -= 1
    if new_clone_n < 0:
        new_clone_n = 2


r.title('Vm Interface')
vm_list = tk.Button(r, text='List', bg="black", fg="white", command=lambda: show_vms(3))

vm_list.pack()
vm_list.place(relx=0.5,
              rely=0.75,
              anchor='center', height=35, width=90)

on_button = tk.Button(r, text='On', bg="green", fg='white')
on_button.pack()
on_button.place(relx=0.53, rely=0.59, anchor='center')
off_button = tk.Button(r, text='Off', bg="red", fg='white')
off_button.pack()
off_button.place(relx=0.47, rely=0.59, anchor='center')
delete_button = tk.Button(r, text='Delete', bg="gray", fg='red')
delete_button.pack()
delete_button.place(relx=0.46, rely=0.9, anchor='center')
clone_button = tk.Button(r, text='Clone', bg="gray", fg='green', command=lambda: new_clone())
clone_button.pack()
clone_button.place(relx=0.54, rely=0.9, anchor='center')
r.mainloop()
