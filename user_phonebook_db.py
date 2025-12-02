import sqlite3 
import tkinter as tk

#Class using phonebook
class phonebook:
    def __init__(self):
        #Creating window
        self.main_window = tk.Tk()
        self.main_window.geometry("500x300")
        self.main_window.config(bg = "light blue")
        self.main_window.title("Phonebook")

        #Frames
        self.top_frame = tk.Frame(self.main_window, bg = "light blue")
        self.middle_frame = tk.Frame(self.main_window, bg = "light blue")
        self.bottom_frame = tk.Frame(self.main_window, bg = "light blue")

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        #button 1 to read the phonebook
        self.button1 = tk.Button(self.top_frame, text = "Read Phonebook", relief = "raised", command = self.read_phonebook, bg = "grey", fg = "white")
        self.button1.pack(side = "left")

        #button 2 to add names and numbers
        self.button2 = tk.Button(self.top_frame, text = "Add Info", relief = "raised", command = self.add_info, bg = "grey", fg = "white")
        self.button2.pack(side = "left")

        #button 3 to delete names and numbers
        self.button3 = tk.Button(self.top_frame, text = "Delete Info", relief = "raised", command = self.delete_info, bg = "grey", fg = "white")
        self.button3.pack(side = "left")

        #button to quit program
        self.button4 = tk.Button(self.bottom_frame, text = "QUIT", relief = "raised", command = self.main_window.destroy, bg = "yellow", fg = "black")
        self.button4.pack()
    #Function to read phonebook
    def read_phonebook(self):
        conn = sqlite3.connect("phonebook.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM entries")
        rows = cursor.fetchall()
        conn.close()

        #Clearing previous content
        for widget in self.middle_frame.winfo_children():
            widget.destroy()

        #Displaying all the infomration in a label
        for row in rows: 
            info = f"Name: {row[0]}, Number: {row[1]}"
            label = tk.Label(self.middle_frame, text = info, bg = "light blue")
            label.pack()

    #Function to add names and numbers to the db
    def add_info(self):
        #Clearing previous content
        for widget in self.middle_frame.winfo_children():
            widget.destroy()

        #Labels and entries for name and number
        name_label = tk.Label(self.middle_frame, text = "Name: ", bg = "light blue")
        name_label.pack()
        name_entry = tk.Entry(self.middle_frame)
        name_entry.pack()

        number_label = tk.Label(self.middle_frame, text = "Number: ", bg = "light blue")
        number_label.pack()
        number_entry = tk.Entry(self.middle_frame)
        number_entry.pack()

        #Function to save entries into database
        def save_entry():
            name = name_entry.get()
            number = number_entry.get()

            if name and number: 
                conn = sqlite3.connect("phonebook.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO entries (persons_name, persons_number) VALUES (?,?)", (name, number))
                conn.commit()
                conn.close()

                #Clear entries after saving
                name_entry.delete(0, tk.END)
                number_entry.delete(0, tk.END)

                #Showing confirmation
                tk.Label(self.middle_frame, text = "Entry added succesfully!", fg = "green").pack()
            else:
                tk.Label(self.middle_frame, text = "Please enter both name and number", fg = "red").pack()

        #Save Button
        save_button = tk.Button(self.middle_frame, text = "SAVE", command = save_entry, bg = "green", fg = "white")
        save_button.pack()

    #Function to delete name and number
    def delete_info(self):
        # Clear middle_frame
        for widget in self.middle_frame.winfo_children():
            widget.destroy()

        # Labels and entries for name and number
        name_label = tk.Label(self.middle_frame, text="Name: ", bg = "light blue")
        name_label.pack()
        name_entry = tk.Entry(self.middle_frame)
        name_entry.pack()

        number_label = tk.Label(self.middle_frame, text="Number: ", bg = "light blue")
        number_label.pack()
        number_entry = tk.Entry(self.middle_frame)
        number_entry.pack()

        # Function to delete the entry from database
        def delete_entry():
            name = name_entry.get()
            number = number_entry.get()

            if name and number:
                conn = sqlite3.connect("phonebook.db")
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM entries WHERE persons_name = ? AND persons_number = ?",
                    (name, number)
                )
                conn.commit()
                conn.close()

                # Clear entries after deletion
                name_entry.delete(0, tk.END)
                number_entry.delete(0, tk.END)

                # Show confirmation
                tk.Label(self.middle_frame, text="Entry deleted successfully!", fg="green").pack()
            else:
                tk.Label(self.middle_frame, text="Please enter both name and number", fg="red").pack()

        # Delete button
        delete_button = tk.Button(self.middle_frame, text="Delete", command=delete_entry, bg = "red", )
        delete_button.pack()


        

numbers = phonebook()
tk.mainloop()


