import os
import re

files_to_resolve = [
    "src/main/java/seedu/address/logic/Messages.java",
    "src/main/java/seedu/address/logic/parser/AddCommandParser.java",
    "src/main/java/seedu/address/logic/parser/CliSyntax.java",
    "src/main/java/seedu/address/logic/parser/EditCommandParser.java",
    "src/main/java/seedu/address/model/person/Person.java",
    "src/main/java/seedu/address/model/util/SampleDataUtil.java",
    "src/main/java/seedu/address/storage/JsonAdaptedPerson.java",
    "src/main/java/seedu/address/ui/PersonCard.java",
    "src/main/resources/view/PersonListCard.fxml"
]

def resolve(path):
    with open(path, 'r') as f:
        content = f.read()

    # Manual replacements for each file since the logic depends on context
    if path.endswith('Messages.java'):
        content = re.sub(r'<<<<<<< HEAD\n(.*?)\n=======\n(.*?)\n>>>>>>> master', r'\1\n\2', content, flags=re.DOTALL)
    
    with open(path, 'w') as f:
        f.write(content)

# We'll just run git status to check.
