import sys

filepath = "src/main/java/seedu/address/storage/JsonAdaptedPerson.java"
with open(filepath, "r") as f:
    content = f.read()

# Fix instantiation at the bottom of JsonAdaptedPerson
content = content.replace(
"""        Person person = new Person(modelName, modelAge, modelPhone, modelEmail,
                modelAddress, modelStartDate, modelTags);""",
"""        Person person = new Person(modelName, modelAge, modelPhone, modelEmail,
                modelAddress, modelEmergencyContact, modelStartDate, modelTags);""")

with open(filepath, "w") as f:
    f.write(content)

