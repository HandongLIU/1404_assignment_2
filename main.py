"""
Name:handong Liu
Date:28/1/2023
Brief Project Description:ReadingTrackerApp
GitHub URL:
"""
# Create your main program in this file, using the ReadingTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


NEW_COLOUR = (0, 1, 0, 1)
ALTERNATIVE_COLOUR = (0, 0, 1, 1)


class ReadingTrackerApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super(ReadingTrackerApp, self).__init__(**kwargs)
        self.Book = {"In Search of Lost Time": "John Maxwell", "the 360 Degree Leader": "John Maxwell",
                     "The Practice of Computing Using Python": "Punch and Enbody"}

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "ReadingTrackerApp"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        return self.root



    def create_widgets(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        for name in self.Book:
            # create a button for each phonebook entry
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)

            temp_button.background_color = NEW_COLOUR
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """Handle pressing entry buttons."""
        # get name (dictionary key) from the text of Button we clicked on
        name = instance.text
        # change the button's background colour
        # update status text
        self.status_text = f"{name}'s Author is {self.Book[name]}"
        instance.background_color = ALTERNATIVE_COLOUR

    def press_save(self, added_Title, added_Author, added_Pages):

        self.Book[added_Title] = added_Author
        self.Book[added_Author] = added_Pages
        # change the number of columns based on the number of entries (no more than 5 rows of entries)
        self.root.ids.entries_box.cols = len(self.Book) // 5 + 1
        # add button for new entry (same as in create_entry_buttons())
        temp_button = Button(text=added_Title)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entries_box.add_widget(temp_button)



    def press_clear(self):
        for instance in self.root.ids.entries_box.children:
            instance.state = 'normal'
        self.status_text = ""

ReadingTrackerApp().run()