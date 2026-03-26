import sys

filepath = "src/main/java/seedu/address/logic/commands/EditCommand.java"
with open(filepath, "r") as f:
    text = f.read()

import re

text = re.sub(r'import seedu\.address\.model\.person\.Address;', 'import seedu.address.model.person.Address;\nimport seedu.address.model.person.Age;\nimport seedu.address.model.person.StartDate;', text)

text = re.sub(r'private Name name;\n\s*private Phone phone;\n\s*private Email email;\n\s*private Address address;\n\s*private EmergencyContact emergencyContact;\n\s*private Set<Tag> tags;',
              'private Name name;\n        private Age age;\n        private Phone phone;\n        private Email email;\n        private Address address;\n        private StartDate startDate;\n        private EmergencyContact emergencyContact;\n        private Set<Tag> tags;', text)

text = re.sub(r'public EditPersonDescriptor\(EditPersonDescriptor toCopy\) \{\n\s*setName\(toCopy\.name\);\n\s*setPhone\(toCopy\.phone\);\n\s*setEmail\(toCopy\.email\);\n\s*setAddress\(toCopy\.address\);\n\s*setEmergencyContact\(toCopy\.emergencyContact\);\n\s*setTags\(toCopy\.tags\);\n\s*\}',
              'public EditPersonDescriptor(EditPersonDescriptor toCopy) {\n            setName(toCopy.name);\n            setAge(toCopy.age);\n            setPhone(toCopy.phone);\n            setEmail(toCopy.email);\n            setAddress(toCopy.address);\n            setStartDate(toCopy.startDate);\n            setEmergencyContact(toCopy.emergencyContact);\n            setTags(toCopy.tags);\n        }', text)

text = re.sub(r'return CollectionUtil\.isAnyNonNull\(name, phone, email, address,\n\s*emergencyContact, tags\);',
              'return CollectionUtil.isAnyNonNull(name, age, phone, email, address, startDate, emergencyContact, tags);', text)

text = re.sub(r'public void setPhone\(Phone phone\) \{\n\s*this\.phone = phone;\n\s*\}',
              'public void setAge(Age age) {\n            this.age = age;\n        }\n\n        public Optional<Age> getAge() {\n            return Optional.ofNullable(age);\n        }\n\n        public void setStartDate(StartDate startDate) {\n            this.startDate = startDate;\n        }\n\n        public Optional<StartDate> getStartDate() {\n            return Optional.ofNullable(startDate);\n        }\n\n        public void setPhone(Phone phone) {\n            this.phone = phone;\n        }', text)

text = re.sub(r'return Objects\.equals\(name, otherEditPersonDescriptor\.name\)\n(\s*)&& Objects\.equals\(phone, otherEditPersonDescriptor\.phone\)',
              'return Objects.equals(name, otherEditPersonDescriptor.name)\n\\1&& Objects.equals(age, otherEditPersonDescriptor.age)\n\\1&& Objects.equals(phone, otherEditPersonDescriptor.phone)', text)

text = re.sub(r'&& Objects\.equals\(address, otherEditPersonDescriptor\.address\)\n(\s*)&& Objects\.equals\(emergencyContact, otherEditPersonDescriptor\.emergencyContact\)',
              '&& Objects.equals(address, otherEditPersonDescriptor.address)\n\\1&& Objects.equals(startDate, otherEditPersonDescriptor.startDate)\n\\1&& Objects.equals(emergencyContact, otherEditPersonDescriptor.emergencyContact)', text)

text = re.sub(r'Address updatedAddress = editPersonDescriptor\.getAddress\(\)\.orElse\(personToEdit\.getAddress\(\)\);\n\s*EmergencyContact updatedEmergencyContact =\n\s*editPersonDescriptor\.getEmergencyContact\(\)\.orElse\(personToEdit\.getEmergencyContact\(\)\);\n\s*Set<Tag> updatedTags = editPersonDescriptor\.getTags\(\)\.orElse\(personToEdit\.getTags\(\)\);\n\n\s*return new Person\(updatedName, updatedPhone, updatedEmail, updatedAddress, updatedEmergencyContact,\n\s*updatedTags\);',
              'Address updatedAddress = editPersonDescriptor.getAddress().orElse(personToEdit.getAddress());\n        Age updatedAge = editPersonDescriptor.getAge().orElse(personToEdit.getAge());\n        StartDate updatedStartDate = editPersonDescriptor.getStartDate().orElse(personToEdit.getStartDate());\n        EmergencyContact updatedEmergencyContact =\n                editPersonDescriptor.getEmergencyContact().orElse(personToEdit.getEmergencyContact());\n        Set<Tag> updatedTags = editPersonDescriptor.getTags().orElse(personToEdit.getTags());\n\n        return new Person(updatedName, updatedAge, updatedPhone, updatedEmail, updatedAddress, updatedEmergencyContact,\n                updatedStartDate, updatedTags);', text)

with open(filepath, "w") as f:
    f.write(text)
