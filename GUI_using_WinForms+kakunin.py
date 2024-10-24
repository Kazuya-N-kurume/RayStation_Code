from connect import *
import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import Application, Form, Label, ComboBox, Button
from System.Drawing import Point, Size

class SelectPRESCRIPTIONForm(Form):

    def __init__(self, examination):
        # Set the size of the form
        self.Size = Size(300, 200)
        # Set title of the form
        self.Text = 'Select D50 or D95'
        # Add a label
        label = Label()
        label.Text = 'Please select Prescription percentage'
        label.Location = Point(15, 15)
        label.AutoSize = True
        self.Controls.Add(label)

        # Add a ComboBox that will display the PRESCRIPTION:s to select
        # Define the items to show up in the combobox,
        prescription = ['D50', 'D95']
        self.combobox = ComboBox()
        self.combobox.DataSource = prescription
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
        # Initialize prescription_name attribute
        self.prescription_name = None

    def ok_button_clicked(self, sender, event):
        # Method invoked when the button is clicked
        self.prescription_name = self.combobox.SelectedItem
        # Close the form
        self.Close()

# Access current examination and show the form
examination = get_current('Examination')
# Create an instance of the form and run it
form = SelectPRESCRIPTIONForm(examination)
Application.Run(form)

# Check the selected prescription and assign the value
if form.prescription_name == 'D50':
    prescription1 = 50
else:
    prescription1 = 95

# Create the second form
from System.Windows.Forms import Application, Form, Label, ComboBox, Button
from System.Drawing import Point, Size

class SelectKAKUNINForm(Form):

    def __init__(self, prescription1):
        # Set the size of the form
        self.Size = Size(300, 200)
        # Set title of the form
        self.Text = 'Check your select!'
        # Add a label with the confirmation message
        label = Label()
        label.Text = 'Did you choose D{}?'.format(prescription1)
        label.Location = Point(15, 15)
        label.AutoSize = True
        self.Controls.Add(label)

        # Add a ComboBox that will display the confirmation options
        kakunin = ['Yes', 'NO!']
        self.combobox = ComboBox()
        self.combobox.DataSource = kakunin
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

        # Initialize kakunin_name attribute
        self.kakunin_name = None

    def ok_button_clicked(self, sender, event):
        # Method invoked when the button is clicked
        # Save the selected confirmation option
        self.kakunin_name = self.combobox.SelectedItem
        # Close the form
        self.Close()


# フォーム1の選択をフォーム2に渡して初期化
form2 = SelectKAKUNINForm(prescription1)  # prescription1を渡す
while True:
    Application.Run(form2)

    if form2.kakunin_name == 'NO!':
        form = SelectPRESCRIPTIONForm(examination)
        Application.Run(form)
        if form.prescription_name == 'D50':
            prescription1 = 50
        else:
            prescription1 = 95
        # フォーム1の選択をフォーム2に再度渡して初期化
        form2 = SelectKAKUNINForm(prescription1)
    else:
        # 'Yes' が選択された場合、ループを終了
        break


await_user_input('{}'.format(prescription1))
