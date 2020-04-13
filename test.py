import uuid
## NOTE CLASS ##
class note:
  def __init__(self, text, link=None):
    self.text = text
    self.ID = uuid.uuid4().hex
    self.link = link
  # def append(obj):
  #   if isinstance(self, list):
  #    obj = .append(note1.ID)
  #   else:
  #     note0.link = list(note1.ID)
  #   note1.link = note0.ID 


    
# del note1
note1 = note(text="onzin")
note2 = note('mooie dingen')


print(note1.text)
print(note1.ID)
print(note1.link)


print(note2.text)
print(note2.ID)
print(note2.link)




