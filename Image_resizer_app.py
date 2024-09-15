from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog 
from tkhtmlview import HTMLLabel
from PIL import Image, ImageTk

class ImageResizerGUI():
    
    def __init__(self, root):
        # style the GUI
        root.option_add('*tearOff', False)
        root.title('Image Resizer')# build the header frame
        self.header = ttk.Frame(root)
        self.header.grid(padx = 5, pady = 5)
        self.header.config(height = 75, width = 250)

        # set up instructions for the user
        self.user_instructions = ttk.Label(self.header, text = ('Select an image to be resized:' 
                                                                ' Enter the new dimensions of the image and then'
                                                                ' select "Create Image."'), wrap = 300)
        self.user_instructions.grid(row = 0, column = 0, columnspan = 2)
        root.resizable(False, False)
        root.configure(background = '#008080')
        self.style = ttk.Style()
        self.style.theme_names()
        self.style.theme_use('xpnative')
        self.style.configure('TFrame', background = '#008080')
        self.style.configure('TLabel', background = '#008080', font = ('Arial', 12))
        self.style.configure('TButton', foreground = 'black', background = 'light grey')
        
        #customize menubar
        def configure_menu_style(menu):
            menu.config(background = 'brown')
            menu.config(foreground = 'black')

        # build the menu
        self.menubar = Menu(root)
        configure_menu_style(self.menubar)
        root.config(menu = self.menubar)
        self.file = Menu(self.menubar)
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

        # build the content frame
        self.content = ttk.Frame(root)
        self.content.grid()
        self.content.config(height = 400, width = 250)

        # set up user field to display file path
        self.user_field = ttk.Entry(self.content, width = 40)
        self.user_field.grid(row = 2, column = 1)

        # set up the image resizing method
        self.x_label = ttk.Label(self.content, text = 'x dimensions (pixels)')
        self.x_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.x_field = ttk.Entry(self.content, width = 10)
        self.x_field.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        self.y_label = ttk.Label(self.content, text = 'y dimensions (pixels)')
        self.y_label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.y_field = ttk.Entry(self.content, width = 10)
        self.y_field.grid(row = 1, column = 2, padx = 10, pady = 10)
  
        # set up buttons and event handling
        # let users choose image path from computer
        self.choose_file = ttk.Button(self.content, text = 'Select File', command = self.choose_file)
        self.choose_file.grid(row = 2, column = 0, padx = 10, pady = 10)

        # create a button to generate a new image
        self.create_image = ttk.Button(self.content, text = 'Create Image', command = self.create_image)
        self.create_image.grid(row = 3, column = 1, padx = 10, pady = 10)

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
        except Exception as e:
            print(e)


def main():
    root = Tk()
    app = ImageResizerGUI(root)
    root.mainloop()   

if __name__ == '__main__':
    main()

#Turn into application with pyinstaller -w -F Image_resizer_app.py