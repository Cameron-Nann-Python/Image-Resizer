from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk

class CustomImageResizerGUI():
    def __init__(self, root):
        # style the GUI
        ctk.set_appearance_mode("dark") # modes: System, light, dark
        ctk.set_default_color_theme("dark-blue") # themes: blue, dark-blue, green
        root.option_add('*tearOff', False)
        root.title('Image Resizer')
        root.resizable(True, True)

        # build the menubar
        self.menubar = Menu(root, bg = 'black', fg = 'white', activebackground = "black", activeforeground = 'white')
        root.config(menu = self.menubar)


        # set up file menu
        self.file = Menu(self.menubar, bg = 'black', fg = 'white', activebackground = 'black', activeforeground = 'white')
        self.menubar.add_cascade(menu = self.file, label = 'File')
        self.edit = Menu(self.menubar)
        self.menubar.add_cascade(menu = self.edit, label = 'Edit')
        self.options = Menu(self.menubar)
        self.menubar.add_cascade(menu = self.options, label = 'Options')
        self.help_ = Menu(self.menubar)
        self.menubar.add_cascade(menu = self.help_, label = 'Help') 

        # set up submenus
        self.file.add_command(label = 'New', command = lambda: print('New File'))
        self.file.add_separator() 

        # build the header frame
        self.header = ctk.CTkFrame(root)
        self.header.grid()
        self.header.configure(height = 150, width = 400)

        # set up instructions for the user
        self.user_instructions = ctk.CTkLabel(self.header, text = ('Select an image to be resized:' 
                                                                ' Enter the new dimensions of the image, and then'
                                                                ' select "Create Image."'), wraplength = 320)
        self.user_instructions.grid(row = 0, column = 0, rowspan = 2)

        # build the content frame
        self.content = ctk.CTkFrame(root)
        self.content.grid(ipadx = 10)
        self.content.configure(height = 250, width = 400)
         
        # set up user field to display file path
        self.user_field = ctk.CTkEntry(self.content)
        self.user_field.grid(row = 2, column = 1, columnspan = 2, sticky = 'ew')

        """set up the image resizing method"""
        self.pixels = [' ','100', '200', '300', '400', '500', '600']
        # fields to resize x-dim pixels
        self.x_label = ctk.CTkLabel(self.content, text = 'X Dimension (pixels)')
        self.x_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.x_field = ctk.CTkComboBox(self.content, values = self.pixels, width = 60)
        self.x_field.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        # fields to resize y-dim pixels
        self.y_label = ctk.CTkLabel(self.content, text = 'Y Dimension (pixels)')
        self.y_label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.y_field = ctk.CTkComboBox(self.content, values = self.pixels, width = 60)
        self.y_field.grid(row = 1, column = 2, padx = 10, pady = 10)

        """set up buttons and event handling"""

        # create a button to let users choose image path from computer
        self.choose_file = ctk.CTkButton(self.content, text = 'Select File', 
                                                   font = ('Arial', 12),
                                                   width = 40,
                                                   corner_radius = 50, 
                                                   command = self.choose_file)
        self.choose_file.grid(row = 2, column = 0, padx = 5, pady = 5)

        # create a button to generate a new image
        self.create_image = ctk.CTkButton(self.content, text = 'Create Image', 
                                                    font = ('Arial', 12),
                                                    corner_radius = 50,
                                                    command = self.create_image)
        self.create_image.grid(row = 3, column = 0, padx = 30, pady = 10, sticky = 'ew', columnspan = 3)

    def choose_file(self):
        self.filename = filedialog.askopenfile()
        self.user_field.insert(0, self.filename.name)
        return self.filename.name
        
    def create_image(self):
        self.new_height = self.y_field.get()
        self.new_width = self.x_field.get()
        self.image_path = self.user_field.get()
        print(self.new_height, self.new_width, self.image_path)
        #messagebox.askyesno(title = 'confirmation check', message = 'Are you sure about your new image?')
        try:
            messagebox.showinfo(title = 'confirmation message', message = 'Image resized successfully!')
        
            with Image.open(self.image_path, 'r') as img:
                img = img.resize((int(self.new_width), int(self.new_height)))
                img.save(self.image_path)
            self.user_field.delete(0, END)
            img.show(self.image_path)
        except Exception as e:
            print(e)

def main():
    root = ctk.CTk()
    root.geometry('350x300')
    root.grid_columnconfigure((0,2), weight = 1) 
    root.grid_rowconfigure((0,3), weight = 1)
    app = CustomImageResizerGUI(root)
    root.mainloop()  

if __name__ == '__main__':

    main()