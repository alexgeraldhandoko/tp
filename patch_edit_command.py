import sys

filepath = "src/main/java/seedu/address/logic/commands/EditCommand.java"
with open(filepath, "r") as f:
    content = f.read()

# Add imports for Age and StartDate
imports_to_replace = "import seedu.address.model.person.Address;"
imports_new = "import seedu.address.model.person.Address;\nimport seedu.address.model.person.Age;\nimport seedu.address.model.person.StartDate;"
content = content.replace(imports_to_replace, imports_new)

# Modify createEditedPerson
content = content.replace(
"""        Name updatedName = editPersonDescriptor.getName().orElse(personToEdit.getName());
        Phone updatedPhone = editPersonDescriptor.getPhone().orElse(personToEdit.getPhone());
        Email updatedEmail = editPersonDescriptor.getEmail().orElse(personToEdit.getEmail());
        Address updatedAddress = editPersonDescriptor.getAddress().orElse(personToEdit.getAddress());
        EmergencyContact updatedEmergencyContact =
                editPersonDescriptor.getEmergencyCimport sys

filepath = "src/main/javge
filepatht()with open(filepath, "r") as f:
    content = f.read()

# Add imports fo(p    content = f.read()

# Add  
# Add imports for Agpdaimports_to_replace = "import seedul,imports_new = "import seedu.address.model.person.Address;\nimpordTcontent = content.replace(imports_to_replace, imports_new)

# Modify createEditedPerson
content = content.replace(
"""        Name updatedName ip
# Modify createEditedPerson
content = content.replace(
" upcontent = content.replace(cr"""        Name updatedNaer        Phone updatedPhone = editPersonDescriptor.getPhone().orElse(personToEdit.getPhone()pe        Email updatedEmail = editPersonDescriptor.getEmail().orElse(personToEdit.getEmail())rE        Address updatedAddress = editPersonDescriptor.getAddress().orElse(personToEdit.getAd          EmergencyContact updatedEmergencyContact =
                editPersonDescriptor.getEmergencySt                editPersonDescriptor.getEmergencyet
filepate().orElse(personToEdit.getStartDate());
        Set<Tfilepatht()with open(fileso    content = f.read()

# Add imports fot.
# Add imports fo(p  ret
# Add  
# Add imports for Agpdaimports up# Add ho
# Modify createEditedPerson
content = content.replace(
"""        Name updatedName ip
# Modify createEditedPerson
content = content.replace(
" upcontent = content.replace(cr"""     datcontent = content.replace(e,"""        Name updatedNa  # Modify createEditedPerson
camcontent = content.replace(e," upcontent = content.repre                editPersonDescriptor.getEmergencySt                editPersonDescriptor.getEmergencyet
filepate().orElse(personToEdit.getStartDate());
        Set<Tfilepatht()with open(fileso    content = f.read()

# Add imports fot.
# Add imports fo(p  ret
# Add  
# Add imports for Agpdaimports up# Add ho
# Modify createEditedPerson
content = content.replace(
"""        Name updatedNamonfilepate().orElse(personToEdit.getStartDate());
        Set<Tfilepatht()with open(fileso    content =rg        Set<Tfilepatht()with open(fileso    cote
# Add imports fot.
# Add imports fo(p  ret
# Add  
# Add impent# Add imports fo(e(# Add  
# Add imports tP# Add es# Modify createEditedPerson
content = co  conte    setName(toCopy.name"""        Name updatedNaoC# Modify createEditedPerson
caicontent = content.replace(  " upcontent = content.reps)camcontent = content.replace(e," upcontent = content.repre                editPersonDescriptor.getEmergencySt               c filepate().orElse(personToEdit.getStartDate());
        Set<Tfilepatht()with open(fileso    content = f.read()

# Add imports fot.
# Add imports fo(p  ret
# Ad          Set<Tfilepatht()with open(fileso    codr
# Add imports fot.
# Add imports fo(p  ret
# Add  
# Add impmer# Add imports fo(  # Add  
# Add imports oC# Add ar# Modify createEditedPerson
content = co;
content = content.replace(on"""        Name updatedNapu        Set<Tfilepatht()with open(fileso    content =rg        Set<Tfilepaon# Add imports fot.
# Add imports fo(p  ret
# Add  
# Add impent# Add imports fo(e(# Add  
# Add import  # Add imports fo(sA# Add  
# Add impent#   # Add re# AddCollectionUtil.isAnyNonNull(name, content = co  conte    setName(toCopy.name"""     mecaicontent = content.replace(  " upcontent = content.reps)camcontent = content.replace(e," upcoid        Set<Tfilepatht()with open(fileso    content = f.read()

# Add imports fot.
# Add imports fo(p  ret
# Ad          Set<Tfilepatht()with open(fileso    codr
# Add imports fot.
# Add imports fo(p  ret
# Add  
# Add impmer# Addag
# Add imports fot.
# Add imports fo(p  ret
# Ad          SetrtD# Add imports fo(  # Ad          Set<TfilDa# Add imports fot.
# Add imports fo(p  ret
# Add  
# St# Add imports fo(  # Add  
# Add impmer# fN# Add e(# Add imports oC# Add ar# Modify crea vcontent = co;
content = content.replace(on"""      =content = co  # Add imports fo(p  ret
# Add  
# Add impent# Add imports fo(e(# Add  
# Add import  # Add imports fo(sA# Add  
# Add impent#   # Add re# AddCollect(p# Add  
# Add impent# es# Add r.# Add import  # Add imports fo(sA# Ad.e# Add impent#   # Add re# AddCollectionem
# Add imports fot.
# Add imports fo(p  ret
# Ad          Set<Tfilepatht()with open(fileso    codr
# Add imports fot.
# Add imports fo(p  ret
# Add  
# Add impmer# Addag
# Add imports fot.
# Add imports fo(p  ret
# Ad          SetrtD# Add imports fo(  # Ad          Set<Tfi   # Add imports fo(ec# Ad          Set<Tfildi# Add imports fot.
# Add imports fo(p  ret
# Add  
# s.# Add imports fo(Ed# Add  
# Add impmer# )
# Add   # Add imports fot.ec# Add imports fo(ot# Ad          SetrtD# r.# Add imports fo(p  ret
# Add  
# St# Add imports fo(  # Add  
# Add impmer# fN#ai# Add  
# St# Add impo &# St# ct# Add impmer# fN# Add e(# Addrscontent = content.replace(on"""      =content = co  # Add imports fo(p  rett,# Add  
# Add impent# Add imports fo(e(# Add  
# Add import  # Add importss.# Add (s# Add import  # Add imports fo(sA# Adta# Add impent#   # Add re# AddCollect(p#eq# Add impent# es# Add r.# Add import  # Add ""# Add imports fot.
# Add im as f:
    f.write(content)
