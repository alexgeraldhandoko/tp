import sys

filepath = "/Users/vincentjulijanto/Downloads/NUS/CS2103T/tp/src/main/java/seedu/address/logic/commands/EditCommand.java"
with open(filepath, "r") as f:
    content = f.read()

content = content.replace(
"""        Address updatedAddress = editPersonDescriptor.getAddress().orElse(personToEdit.getAddress());
        EmergencyContact updatedEmergencyContact = editPersonDescriptor.getEmergencyContact().orElse(personToEdit.getEmergencyContact());
        Set<Tag> updatedTags = editPersonDescriptor.getTags().orElse(personToEdit.getTags());

        return new Person(updatedName, updatedPhone, updatedEmail, updatedAddress, updatedEmergencyContact,
                updatedTags);""",
"""        Address updatedAddress = editPersonDescriptor.getAddress().orElse(personToEdit.getAddress());
        Age updatedAge = editPersonDescriptor.getAge().orElse(personToEdit.getAge());
        StartDate updatedStartDate = editPersonDescriptor.getStartDate().orElse(personToEdit.getStartDate());
        EmergencyContact updatedEmergencyContact = editPersonDescriptor.getEmergencyContact().orElse(personToEdit.getEmergencyContact());
        Set<Tag> updatedTags = editPersonDescriptor.getTags().orElse(personToEdit.getTags());

        return new Person(updatedName, updatedAge, updatedPhone, updatedEmail, updatedAddress, updatedEmergencyContact,
                updatedStartDate, updatedTags);""")

content = content.replace(
"""        private Name name;
        private Phone phone;
        private Email email;
        private Address address;
        private EmergencyContact emergencyContact;
        private Set<Tag> tags;""",
"""        private Name name;
        private Age age;
        private Phone phone;
        private Email email;
        private Address address;
        private StartDate startDate;
        private EmergencyContact emergencyContact;
        private Set<Tag> tags;""")

content = content.replace(
"""        public EditPersonDescriptor(EditPersonDescriptor toCopy) {
            setName(toCopy.name);
            setPhone(toCopy.phone);
            setEmail(toCopy.email);
            setAddress(toCopy.address);
            setEmergencyContact(toCopy.emergencyContact);
            setTags(toCopy.tags);
        }""",
"""        public EditPersonDescriptor(EditPersonDescriptor toCopy) {
            setName(toCopy.name);
            setAge(toCopy.age);
            setPhone(toCopy.phone);
            setEmail(toCopy.email);
            setAddress(toCopy.address);
            setStartDate(toCopy.startDate);
            setEmergencyContact(toCopy.emergencyContact);
            setTags(toCopy.tags);
        }""")

content = content.replace(
"""        public boolean isAnyFieldEdited() {
            return CollectionUtil.isAnyNonNull(name, phone, email, address,
                     emergencyContact, tags);
        }""",
"""        public boolean isAnyFieldEdited() {
            return CollectionUtil.isAnyNonNull(name, age, phone, email, address,
                     startDate, emergencyContact, tags);
        }""")

setters_str = """        public void setPhone(Phone phone) {
            this.phone = phone;
        }"""
new_setters = """        public void setAge(Age age) {
            this.age = age;
        }

        public Optional<Age> getAge() {
            return Optional.ofNullable(age);
        }

        public void setStartDate(StartDate startDate) {
            this.startDate = startDate;
        }

        public Optional<StartDate> getStartDate() {
            return Optional.ofNullable(startDate);
        }

        public void setPhone(Phone phone) {
            this.phone = phone;
        }"""
content = content.replace(setters_str, new_setters)

content = content.replace(
"""            return Objects.equals(name, otherEditPersonDescriptor.name)
                    && Objects.equals(phone, otherEditPersonDescriptor.phone)
                    && Objects.equals(email, otherEditPersonDescriptor.email)
                    && Objects.equals(address, otherEditPersonDescriptor.address)
                    && Objects.equals(emergencyContact, otherEditPersonDescriptor.emergencyContact)
                    && Objects.equals(tags, otherEditPersonDescriptor.tags);""",
"""            return Objects.equals(name, otherEditPersonDescriptor.name)
                    && Objects.equals(age, otherEditPersonDescriptor.age)
                    && Objects.equals(phone, otherEditPersonDescriptor.phone)
                    && Objects.equals(email, otherEditPersonDescriptor.email)
                    && Objects.equals(address, otherEditPersonDescriptor.address)
                    && Objects.equals(startDate, otherEditPersonDescriptor.startDate)
                    && Objects.equals(emergencyContact, otherEditPersonDescriptor.emergencyContact)
                    && Objects.equals(tags, otherEditPersonDescriptor.tags);""")

imports_to_replace = "import seedu.address.model.person.Address;"
imports_new = "import seedu.address.model.person.Address;\nimport seedu.address.model.person.Age;\nimport seedu.address.model.person.StartDate;"
content = content.replace(imports_to_replace, imports_new)

with open(filepath, "w") as f:
    f.write(content)

filepath = "/Users/vincentjulijanto/Downloads/NUS/CS2103T/tp/src/main/java/seedu/address/storage/JsonAdaptedPerson.java"
with open(filepath, "r") as f:
    jap = f.read()

jap = jap.replace(
"""        Person person = new Person(modelName, modelAge, modelPhone, modelEmail,
                modelAddress, modelStartDate, modelTags);""",
"""        Person person = new Person(modelName, modelAge, modelPhone, modelEmail,
                modelAddress, modelEmergencyContact, modelStartDate, modelTags);""")

with open(filepath, "w") as f:
    f.write(jap)
