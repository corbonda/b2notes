import wx
import uuid

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()


brainlist = ["sasd","lkjlk"]


class note:
  def __init__(self, text, link=None):
    self.text = text
    self.ID = uuid.uuid4().hex
    self.link = link

def link(note0, note2):
    note0.link = note1.ID
    note1.link = note0.ID


def link(note0, note1=None):
    print(len(note0))
    if len(note0) > 1:
        i = 0
        while i < len(note0):
            print(i)
            i += 1
    else:
        note0.link = note1.ID
        note1.link = note0.ID

    
note1 = note(text="onzin")
note2 = note('mooie dingen')

link(note1, note2)
 
print(note1.text)
print(note1.link)


print(note2.text)
print(note2.link)


