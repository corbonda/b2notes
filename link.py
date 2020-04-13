## Todo BUILD NICE LINKING FUNCTION ##    
def link(note0, note1=None):
  if isinstance(note0, list):
    # print(f'Length: {len(note0)}')
    i = 1
    while i < len(note0):
      print(f'first element: {i-1}')
      print(f'second element: {1}')
      link(note0[i-1], note0[i])
      i += 1
  else:
    #note0.link = note1.ID
    if isinstance(note0.link, list):
     note0.link.append(note1.ID)
    else:
      note0.link = list(note1.ID)
    note1.link = note0.ID
    # note1.link.append(note0.ID)


print(note1.link)
print(note2.link)


link(note1, note2)

link([note1, note2])
 
