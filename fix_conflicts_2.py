import sys

def patch_file(filepath, replacements):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return
    
    for old_str, new_str in replacements:
        if old_str not in content:
            print(f"Warning: String not found in {filepath}:\n{old_str[:100]}...")
        content = content.replace(old_str, new_str)
        
    with open(filepath, 'w') as f:
        f.write(content)

base_dir = "/Users/vincentjulijanto/Downloads/NUS/CS2103T/tp/"

patch_file(base_dir + "src/test/data/JsonSerializableAddressBookTest/invalidPersonAddressBook.json", [
(
"""<<<<<<< HEAD
    "emergencyContact": "Mom 91234567"
=======
    "startDate": "01/01/2001"
>>>>>>> master""",
"""    "emergencyContact": "Mom 91234567",
    "startDate": "01/01/2001\""""
)
])

patch_file(base_dir + "src/test/java/seedu/address/logic/commands/CommandTestUtil.java", [
(
"""<<<<<<< HEAD
    public static final String INVALID_TAG_DESC = " " + PREFIX_TAG + "hubby*";
    public static final String INVALID_EMERGENCY_CONTACT_DESC = " " + PREFIX_EMERGENCY_CONTACT + " ";// '*' not allowed in tags
=======
    public static final String INVALID_START_DATE_DESC = " " + PREFIX_START_DATE + "30/02/2025"; // must be a real date
    public static final String INVALID_TAG_DESC = " " + PREFIX_TAG + "hubby*"; // '*' not allowed in tags
>>>>>>> master""",
"""    public static final String INVALID_START_DATE_DESC = " " + PREFIX_START_DATE + "30/02/2025"; // must be a real date
    public static final String INVALID_TAG_DESC = " " + PREFIX_TAG + "hubby*"; // '*' not allowed in tags
    public static final String INVALID_EMERGENCY_CONTACT_DESC = " " + PREFIX_EMERGENCY_CONTACT + " ";"""
),
(
"""<<<<<<< HEAD
                .withPhone(VALID_PHONE_AMY).withEmail(VALID_EMAIL_AMY).withAddress(VALID_ADDRESS_AMY)
                .withEmergencyContact(VALID_EMERGENCY_CONTACT_AMY)
                .withTags(VALID_TAG_FRIEND).build();
        DESC_BOB = new EditPersonDescriptorBuilder().withName(VALID_NAME_BOB)
                .withPhone(VALID_PHONE_BOB).withEmail(VALID_EMAIL_BOB).withAddress(VALID_ADDRESS_BOB)
                .withEmergencyContact(VALID_EMERGENCY_CONTACT_BOB)
=======
                .withAge(VALID_AGE_AMY).withPhone(VALID_PHONE_AMY)
                .withEmail(VALID_EMAIL_AMY).withAddress(VALID_ADDRESS_AMY)
                .withStartDate(VALID_START_DATE_AMY).withTags(VALID_TAG_FRIEND).build();
        DESC_BOB = new EditPersonDescriptorBuilder().withName(VALID_NAME_BOB)
                .withAge(VALID_AGE_BOB).withPhone(VALID_PHONE_BOB)
                .withEmail(VALID_EMAIL_BOB).withAddress(VALID_ADDRESS_BOB)
                .withStartDate(VALID_START_DATE_BOB)
>>>>>>> master""",
"""                .withAge(VALID_AGE_AMY).withPhone(VALID_PHONE_AMY)
                .withEmail(VALID_EMAIL_AMY).withAddress(VALID_ADDRESS_AMY)
                .withEmergencyContact(VALID_EMERGENCY_CONTACT_AMY)
                .withStartDate(VALID_START_DATE_AMY).withTags(VALID_TAG_FRIEND).build();
        DESC_BOB = new EditPersonDescriptorBuilder().withName(VALID_NAME_BOB)
                .withAge(VALID_AGE_BOB).withPhone(VALID_PHONE_BOB)
                .withEmail(VALID_EMAIL_BOB).withAddress(VALID_ADDRESS_BOB)
                .withEmergencyContact(VALID_EMERGENCY_CONTACT_BOB)
                .withStartDate(VALID_START_DATE_BOB)"""
)
])

patch_file(base_dir + "src/test/java/seedu/address/logic/commands/EditPersonDescriptorTest.java", [
(
"""<<<<<<< HEAD
                + editPersonDescriptor.getAddress().orElse(null) + ", emergencyContact="
                + editPersonDescriptor.getEmergencyContact().orElse(null) + ", tags="
=======
                + editPersonDescriptor.getAddress().orElse(null) + ", startDate="
                + editPersonDescriptor.getStartDate().orElse(null) + ", tags="
>>>>>>> master""",
"""                + editPersonDescriptor.getAddress().orElse(null) + ", emergencyContact="
                + editPersonDescriptor.getEmergencyContact().orElse(null) + ", startDate="
                + editPersonDescriptor.getStartDate().orElse(null) + ", tags="""
)
])

patch_file(base_dir + "src/test/java/seedu/address/model/person/PersonTest.java", [
(
"""<<<<<<< HEAD
        String expected = Person.class.getCanonicalName() + "{name=" + ALICE.getName() + ", phone=" + ALICE.getPhone()
                + ", email=" + ALICE.getEmail() + ", address=" + ALICE.getAddress() + ", emergencyContact="
                + ALICE.getEmergencyContact() + ", tags=" + ALICE.getTags() + "}";
=======
        String expected = Person.class.getCanonicalName() + "{name=" + ALICE.getName()
                + ", age=" + ALICE.getAge() + ", phone=" + ALICE.getPhone()
                + ", email=" + ALICE.getEmail() + ", address=" + ALICE.getAddress()
                + ", start date=" + ALICE.getStartDate()
                + ", tags=" + ALICE.getTags() + "}";
>>>>>>> master""",
"""        String expected = Person.class.getCanonicalName() + "{name=" + ALICE.getName()
                + ", age=" + ALICE.getAge() + ", phone=" + ALICE.getPhone()
                + ", email=" + ALICE.getEmail() + ", address=" + ALICE.getAddress()
                + ", emergencyContact=" + ALICE.getEmergencyContact()
                + ", start date=" + ALICE.getStartDate()
                + ", tags=" + ALICE.getTags() + "}";"""
)
])

patch_file(base_dir + "src/test/java/seedu/address/storage/JsonAdaptedPersonTest.java", [
(
"""<<<<<<< HEAD
import seedu.address.model.person.EmergencyContact;
=======
import seedu.address.model.person.StartDate;
>>>>>>> master""",
"""import seedu.address.model.person.EmergencyContact;
import seedu.address.model.person.StartDate;"""
),
(
"""<<<<<<< HEAD
    private static final String VALID_EMERGENCY_CONTACT = BENSON.getEmergencyContact().toString();
=======
    private static final String VALID_START_DATE = BENSON.getStartDate().toString();
>>>>>>> master""",
"""    private static final String VALID_EMERGENCY_CONTACT = BENSON.getEmergencyContact().toString();
    private static final String VALID_START_DATE = BENSON.getStartDate().toString();"""
),
(
"""<<<<<<< HEAD
                new JsonAdaptedPerson(INVALID_NAME, VALID_PHONE, VALID_EMAIL, VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_TAGS);
=======
                new JsonAdaptedPerson(INVALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                        VALID_ADDRESS, VALID_START_DATE, VALID_TAGS, null);
>>>>>>> master""",
"""                new JsonAdaptedPerson(INVALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                        VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_START_DATE, VALID_TAGS, null);"""
),
(
"""<<<<<<< HEAD
        JsonAdaptedPerson person = new JsonAdaptedPerson(null, VALID_PHONE, VALID_EMAIL, VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_TAGS);
=======
        JsonAdaptedPerson person = new JsonAdaptedPerson(null, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                VALID_ADDRESS, VALID_START_DATE, VALID_TAGS, null);
>>>>>>> master""",
"""        JsonAdaptedPerson person = new JsonAdaptedPerson(null, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_START_DATE, VALID_TAGS, null);"""
),
(
"""<<<<<<< HEAD
                new JsonAdaptedPerson(VALID_NAME, INVALID_PHONE, VALID_EMAIL, VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_TAGS);
=======
                new JsonAdaptedPerson(VALID_NAME, VALID_AGE, INVALID_PHONE, VALID_EMAIL,
                        VALID_ADDRESS, VALID_START_DATE, VALID_TAGS, null);
>>>>>>> master""",
"""                new JsonAdaptedPerson(VALID_NAME, VALID_AGE, INVALID_PHONE, VALID_EMAIL,
                        VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_START_DATE, VALID_TAGS, null);"""
),
(
"""<<<<<<< HEAD
        JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, null, VALID_EMAIL, VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_TAGS);
=======
        JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, VALID_AGE, null, VALID_EMAIL,
                VALID_ADDRESS, VALID_START_DATE, VALID_TAGS, null);
>>>>>>> master""",
"""        JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, VALID_AGE, null, VALID_EMAIL,
                VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_START_DATE, VALID_TAGS, null);"""
),
(
"""<<<<<<< HEAD
                new JsonAdaptedPerson(VALID_NAME, VALID_PHONE, INVALID_EMAIL, VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_TAGS);
=======
                new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, INVALID_EMAIL,
                        VALID_ADDRESS, VALID_START_DATE, VALID_TAGS, null);
>>>>>>> master""",
"""                new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, INVALID_EMAIL,
                        VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_START_DATE, VALID_TAGS, null);"""
),
(
"""<<<<<<< HEAD
        JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, VALID_PHONE, null, VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_TAGS);
=======
        JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, null,
                VALID_ADDRESS, VALID_START_DATE, VALID_TAGS, null);
>>>>>>> master""",
"""        JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, null,
                VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_START_DATE, VALID_TAGS, null);"""
),
(
"""<<<<<<< HEAD
                new JsonAdaptedPerson(VALID_NAME, VALID_PHONE, VALID_EMAIL, INVALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_TAGS);
=======
                new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                        INVALID_ADDRESS, VALID_START_DATE, VALID_TAGS, null);
>>>>>>> master""",
"""                new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                        INVALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_START_DATE, VALID_TAGS, null);"""
),
(
"""<<<<<<< HEAD
        JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, VALID_PHONE, VALID_EMAIL, null, VALID_EMERGENCY_CONTACT, VALID_TAGS);
=======
        JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                null, VALID_START_DATE, VALID_TAGS, null);
>>>>>>> master""",
"""        JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                null, VALID_EMERGENCY_CONTACT, VALID_START_DATE, VALID_TAGS, null);"""
),
(
"""<<<<<<< HEAD
                new JsonAdaptedPerson(VALID_NAME, VALID_PHONE, VALID_EMAIL, VALID_ADDRESS,
                            VALID_EMERGENCY_CONTACT, invalidTags);
=======
                new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                        VALID_ADDRESS, VALID_START_DATE, invalidTags, null);
>>>>>>> master""",
"""                new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                        VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_START_DATE, invalidTags, null);"""
)
])

patch_file(base_dir + "src/test/java/seedu/address/testutil/EditPersonDescriptorBuilder.java", [
(
"""<<<<<<< HEAD
import seedu.address.model.person.EmergencyContact;
=======
import seedu.address.model.person.StartDate;
>>>>>>> master""",
"""import seedu.address.model.person.EmergencyContact;
import seedu.address.model.person.StartDate;"""
),
(
"""<<<<<<< HEAD
        descriptor.setEmergencyContact(person.getEmergencyContact());
=======
        descriptor.setStartDate(person.getStartDate());
>>>>>>> master""",
"""        descriptor.setEmergencyContact(person.getEmergencyContact());
        descriptor.setStartDate(person.getStartDate());"""
),
(
"""<<<<<<< HEAD
     * Sets the {@code EmergencyContact} of the {@code EditPersonDescriptor} that we are building.
     */
    public EditPersonDescriptorBuilder withEmergencyContact(String emergencyContact) {
        descriptor.setEmergencyContact(new EmergencyContact(emergencyContact));
=======
     * Sets the {@code Start Date} of the {@code EditPersonDescriptor} that we are building.
     */
    public EditPersonDescriptorBuilder withStartDate(String startDate) {
        descriptor.setStartDate(new StartDate(startDate));
>>>>>>> master""",
"""     * Sets the {@code EmergencyContact} of the {@code EditPersonDescriptor} that we are building.
     */
    public EditPersonDescriptorBuilder withEmergencyContact(String emergencyContact) {
        descriptor.setEmergencyContact(new EmergencyContact(emergencyContact));
        return this;
    }

    /**
     * Sets the {@code Start Date} of the {@code EditPersonDescriptor} that we are building.
     */
    public EditPersonDescriptorBuilder withStartDate(String startDate) {
        descriptor.setStartDate(new StartDate(startDate));"""
)
])

patch_file(base_dir + "src/test/java/seedu/address/testutil/PersonBuilder.java", [
(
"""<<<<<<< HEAD
     * Sets the {@code EmergencyContact} of the {@code Person} that we are building.
     */
    public PersonBuilder withEmergencyContact(String emergencyContact) {
        this.emergencyContact = new EmergencyContact(emergencyContact);
=======
     * Sets the {@code StartDate} of the {@code Person} that we are building.
     */
    public PersonBuilder withStartDate(String startDate) {
        this.startDate = new StartDate(startDate);
>>>>>>> master""",
"""     * Sets the {@code EmergencyContact} of the {@code Person} that we are building.
     */
    public PersonBuilder withEmergencyContact(String emergencyContact) {
        this.emergencyContact = new EmergencyContact(emergencyContact);
        return this;
    }

    /**
     * Sets the {@code StartDate} of the {@code Person} that we are building.
     */
    public PersonBuilder withStartDate(String startDate) {
        this.startDate = new StartDate(startDate);"""
),
(
"""<<<<<<< HEAD
        return new Person(name, phone, email, address, emergencyContact,tags);
=======
        return new Person(name, age, phone, email, address, startDate, tags);
>>>>>>> master""",
"""        return new Person(name, age, phone, email, address, emergencyContact, startDate, tags);"""
)
])

patch_file(base_dir + "src/test/java/seedu/address/testutil/PersonUtil.java", [
(
"""<<<<<<< HEAD
        sb.append(PREFIX_NAME).append(person.getName().fullName).append(" ");
        sb.append(PREFIX_PHONE).append(person.getPhone().value).append(" ");
        sb.append(PREFIX_EMAIL).append(person.getEmail().value).append(" ");
        sb.append(PREFIX_ADDRESS).append(person.getAddress().value).append(" ");
        sb.append(PREFIX_EMERGENCY_CONTACT).append(person.getEmergencyContact().value).append(" ");
        person.getTags().forEach(s -> sb.append(PREFIX_TAG).append(s.tagName).append(" "));
=======
        sb.append(PREFIX_NAME + person.getName().fullName + " ");
        sb.append(PREFIX_AGE + person.getAge().value + " ");
        sb.append(PREFIX_PHONE + person.getPhone().value + " ");
        sb.append(PREFIX_EMAIL + person.getEmail().value + " ");
        sb.append(PREFIX_ADDRESS + person.getAddress().value + " ");
        sb.append(PREFIX_START_DATE + person.getStartDate().value + " ");
        person.getTags().stream().forEach(
            s -> sb.append(PREFIX_TAG + s.tagName + " ")
        );
>>>>>>> master""",
"""        sb.append(PREFIX_NAME).append(person.getName().fullName).append(" ");
        sb.append(PREFIX_AGE).append(person.getAge().value).append(" ");
        sb.append(PREFIX_PHONE).append(person.getPhone().value).append(" ");
        sb.append(PREFIX_EMAIL).append(person.getEmail().value).append(" ");
        sb.append(PREFIX_ADDRESS).append(person.getAddress().value).append(" ");
        sb.append(PREFIX_EMERGENCY_CONTACT).append(person.getEmergencyContact().value).append(" ");
        sb.append(PREFIX_START_DATE).append(person.getStartDate().value).append(" ");
        person.getTags().forEach(s -> sb.append(PREFIX_TAG).append(s.tagName).append(" "));"""
),
(
"""<<<<<<< HEAD
        descriptor.getEmergencyContact().ifPresent(emergencyContact ->
                sb.append(PREFIX_EMERGENCY_CONTACT).append(emergencyContact.value).append(" "));
=======
        descriptor.getStartDate().ifPresent(startDate ->
                sb.append(PREFIX_START_DATE).append(startDate.value).append(" "));
>>>>>>> master""",
"""        descriptor.getEmergencyContact().ifPresent(emergencyContact ->
                sb.append(PREFIX_EMERGENCY_CONTACT).append(emergencyContact.value).append(" "));
        descriptor.getStartDate().ifPresent(startDate ->
                sb.append(PREFIX_START_DATE).append(startDate.value).append(" "));"""
)
])

patch_file(base_dir + "src/test/java/seedu/address/testutil/TypicalPersons.java", [
(
"""<<<<<<< HEAD
            .withPhone("94351253")
            .withEmergencyContact("John 91234567")
=======
            .withPhone("94351253").withStartDate("01/01/2001")
>>>>>>> master""",
"""            .withPhone("94351253")
            .withEmergencyContact("John 91234567")
            .withStartDate("01/01/2001")"""
),
(
"""<<<<<<< HEAD
            .withEmergencyContact("Mom 98765432")
=======
            .withStartDate("02/02/2002")
>>>>>>> master""",
"""            .withEmergencyContact("Mom 98765432")
            .withStartDate("02/02/2002")"""
)
])

print("Finished second batch!")
