from connect import *
import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import Application, Form, Label, ComboBox, Button
from System.Drawing import Point, Size

class SelectMETHODForm(Form):

    def __init__(self, examination):
        # Set the size of the form
        self.Size = Size(300, 200)
        # Set title of the form
        self.Text = 'Check your select !!'
        # Add a label
        label = Label()
        label.Text = 'Do you select [] ?'
        label.Location = Point(15, 15)
        label.AutoSize = True
        self.Controls.Add(label)

        # Add a ComboBox that will display the METHOD:s to select
        # Define the items to show up in the combobox,
        method = ['YES', 'NO']
        self.combobox = ComboBox()
        self.combobox.DataSource = method
        self.combobox.Location = Point(15, 60)
        self.combobox.AutoSize = True
        self.Controls.Add(self.combobox)
        # Add button to press OK and close the form
        button = Button()
        button.Text = 'Go Next'
        button.AutoSize = True
        button.Location = Point(15, 100)
        button.Click += self.ok_button_clicked
        self.Controls.Add(button)
        # Initialize method_name attribute
        self.method_name = None

    def ok_button_clicked(self, sender, event):
        # Method invoked when the button is clicked
        self.method_name = self.combobox.SelectedItem
        # Close the form
        self.Close()

# Access current examination and show the form
examination = get_current('Examination')
# Create an instance of the form and run it
form = SelectMETHODForm(examination)
Application.Run(form)

# Check the selected method and assign the value
if form.method_name == 'NO':
    import sys
    await_user_input('This operation is Stopping./nPlease reselect Script')
    sys.exit()




await_user_input('next')

