import tkinter as tk
import getpass
import oracledb

pw = getpass.getpass("root")

connection = oracledb.connect(
    user="system",
    password=pw,
    dsn="localhost/xe")

print("Successfully connected to Oracle Database")

root = tk.Tk()
root.title("Transaction bancaire")




root.mainloop()



