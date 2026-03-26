import sys

def patch_file(filepath, replacements):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return
    
    for old_str, new_str in replacements:
        if old_str not in content:
            pass # ignore silently
        content = content.replace(old_str, new_str)
        
    with open(filepath, 'w') as f:
        f.write(content)

base_dir = "/Users/vincentjulijanto/Downloads/NUS/CS2103T/tp/"

patch_file(base_dir + "src/test/data/JsonSerializableAddressBookTest/typicalPersonsAddressBook.json", [
(
"""<<<<<<< HEAD
    "emergencyContact" : "John 91234567",
=======
    "startDate": "01/01/2001",
>>>>>>> master""",
"""    "emergencyContact" : "John 91234567",
    "startDate": "01/01/2001","""
),
(
"""<<<<<<< HEAD
    "emergencyContact" : "Mom 98765432",
=======
    "startDate": "02/02/2002",
>>>>>>> master""",
"""    "emergencyContact" : "Mom 98765432",
    "startDate": "02/02/2002","""
),
(
"""<<<<<<< HEAD
    "emergencyContact" : "N/A",
=======
    "startDate": "03/03/2003",
>>>>>>> master""",
"""    "emergencyContact" : "N/A",
    "startDate": "03/03/2003","""
),
(
"""<<<<<<< HEAD
    "emergencyContact" : "N/A",
=======
    "startDate": "04/04/2004",
>>>>>>> master""",
"""    "emergencyContact" : "N/A",
    "startDate": "04/04/2004","""
),
(
"""<<<<<<< HEAD
    "emergencyContact" : "N/A",
=======
    "startDate": "05/05/2005",
>>>>>>> master""",
"""    "emergencyContact" : "N/A",
    "startDate": "05/05/2005","""
),
(
"""<<<<<<< HEAD
    "emergencyContact" : "N/A",
=======
    "startDate": "06/06/2006",
>>>>>>> master""",
"""    "emergencyContact" : "N/A",
    "startDate": "06/06/2006","""
),
(
"""<<<<<<< HEAD
    "emergencyContact" : "N/A",
=======
    "startDate": "07/07/2007",
>>>>>>> master""",
"""    "emergencyContact" : "N/A",
    "startDate": "07/07/2007","""
)
])

patch_file(base_dir + "src/test/data/JsonSerializableAddressBookTest/duplicatePersonAddressBook.json", [
(
"""<<<<<<< HEAD
  "persons": [
    {
      "name": "Alice Pauline",
      "phone": "94351253",
      "email": "alice@example.com",
      "address": "123, Jurong West Ave 6, #08-111",
      "emergencyContact": "John 91234567",
      "tags": [ "friends" ]
    },
    {
      "name": "Alice Pauline",
      "phone": "94351253",
      "email": "alice@example.com",
      "address": "123, Jurong West Ave 6, #08-111",
      "emergencyContact": "John 91234567",
      "tags": [ "friends" ]
    }
  ]
=======
  "persons": [ {
    "name": "Alice Pauline",
    "age": "19",
    "phone": "94351253",
    "email": "alice@example.com",
    "address": "123, Jurong West Ave 6, #08-111",
    "startDate": "01/01/2001",
    "tags": [ "friends" ]
  }, {
    "name": "Alice Pauline",
    "age": "19",
    "phone": "94351253",
    "email": "pauline@example.com",
    "address": "4th street",
    "startDate": "01/01/2001"
  } ]
>>>>>>> master""",
"""  "persons": [ {
    "name": "Alice Pauline",
    "age": "19",
    "phone": "94351253",
    "email": "alice@example.com",
    "address": "123, Jurong West Ave 6, #08-111",
    "emergencyContact": "John 91234567",
    "startDate": "01/01/2001",
    "tags": [ "friends" ]
  }, {
    "name": "Alice Pauline",
    "age": "19",
    "phone": "94351253",
    "email": "pauline@example.com",
    "address": "4th street",
    "emergencyContact": "John 91234567",
    "startDate": "01/01/2001"
  } ]"""
)
])

patch_file(base_dir + "src/test/java/seedu/address/testutil/TypicalPersons.java", [
(
"""<<<<<<< HEAD
    public static final Person CARL = new PersonBuilder().withName("Carl Kurz").withPhone("95352563")
            .withEmail("heinz@example.com").withAddress("wall street").build();
    public static final Person DANIEL = new PersonBuilder().withName("Daniel Meier").withPhone("87652533")
            .withEmail("cornelia@example.com").withAddress("10th street").withTags("friends").build();
    public static final Person ELLE = new PersonBuilder().withName("Elle Meyer").withPhone("9482224")
            .withEmail("werner@example.com").withAddress("michegan ave").build();
    public static final Person FIONA = new PersonBuilder().withName("Fiona Kunz").withPhone("9482427")
            .withEmail("lydia@example.com").withAddress("little tokyo").build();
    public static final Person GEORGE = new PersonBuilder().withName("George Best").withPhone("9482442")
            .withEmail("anna@example.com").withAddress("4th street").build();

    // Manually added
    public static final Person HOON = new PersonBuilder().withName("Hoon Meier").withPhone("8482424")
            .withEmail("stefan@example.com").withAddress("little india").build();
    public static final Person IDA = new PersonBuilder().withName("Ida Mueller").withPhone("8482131")
            .withEmail("hans@example.com").withAddress("chicago ave").build();

    // Manually added - Person's details found in {@code CommandTestUtil}
    public static final Person AMY = new PersonBuilder().withName(VALID_NAME_AMY).withPhone(VALID_PHONE_AMY)
            .withEmail(VALID_EMAIL_AMY).withAddress(VALID_ADDRESS_AMY).withTags(VALID_TAG_FRIEND).build();
    public static final Person BOB = new PersonBuilder().withName(VALID_NAME_BOB).withPhone(VALID_PHONE_BOB)
            .withEmail(VALID_EMAIL_BOB).withAddress(VALID_ADDRESS_BOB).withTags(VALID_TAG_HUSBAND, VALID_TAG_FRIEND)
=======
    public static final Person CARL = new PersonBuilder().withName("Carl Kurz").withPhone("95352563")
            .withAge("45").withEmail("heinz@example.com").withAddress("wall street")
            .withStartDate("03/03/2003").build();
    public static final Person DANIEL = new PersonBuilder().withName("Daniel Meier").withPhone("87652533")
            .withAge("35").withEmail("cornelia@example.com").withAddress("10th street")
            .withStartDate("04/04/2004").withTags("friends").build();
    public static final Person ELLE = new PersonBuilder().withName("Elle Meyer").withPhone("94828224")
            .withAge("23").withEmail("werner@example.com")
            .withStartDate("05/05/2005").withAddress("michegan ave").build();
    public static final Person FIONA = new PersonBuilder().withName("Fiona Kunz").withPhone("94825427")
            .withAge("56").withEmail("lydia@example.com")
            .withStartDate("06/06/2006").withAddress("little tokyo").build();
    public static final Person GEORGE = new PersonBuilder().withName("George Best").withPhone("94842442")
            .withAge("18").withEmail("anna@example.com")
            .withStartDate("07/07/2007").withAddress("4th street").build();

    // Manually added
    public static final Person HOON = new PersonBuilder().withName("Hoon Meier").withPhone("84862424")
            .withAge("43").withEmail("stefan@example.com")
            .withStartDate("08/08/2008").withAddress("little india").build();
    public static final Person IDA = new PersonBuilder().withName("Ida Mueller").withPhone("84842131")
            .withAge("67").withEmail("hans@example.com")
            .withStartDate("09/09/2009").withAddress("chicago ave").build();

    // Manually added - Person's details found in {@code CommandTestUtil}
    public static final Person AMY = new PersonBuilder().withName(VALID_NAME_AMY).withAge(VALID_AGE_AMY)
            .withPhone(VALID_PHONE_AMY).withEmail(VALID_EMAIL_AMY).withStartDate(VALID_START_DATE_AMY)
            .withAddress(VALID_ADDRESS_AMY).withTags(VALID_TAG_FRIEND).build();
    public static final Person BOB = new PersonBuilder().withName(VALID_NAME_BOB).withAge(VALID_AGE_BOB)
            .withPhone(VALID_PHONE_BOB).withEmail(VALID_EMAIL_BOB).withStartDate(VALID_START_DATE_BOB)
            .withAddress(VALID_ADDRESS_BOB).withTags(VALID_TAG_HUSBAND, VALID_TAG_FRIEND)
>>>>>>> master""",
"""    public static final Person CARL = new PersonBuilder().withName("Carl Kurz").withPhone("95352563")
            .withAge("45").withEmail("heinz@example.com").withAddress("wall street")
            .withEmergencyContact("N/A").withStartDate("03/03/2003").build();
    public static final Person DANIEL = new PersonBuilder().withName("Daniel Meier").withPhone("87652533")
            .withAge("35").withEmail("cornelia@example.com").withAddress("10th street")
            .withEmergencyContact("N/A").withStartDate("04/04/2004").withTags("friends").build();
    public static final Person ELLE = new PersonBuilder().withName("Elle Meyer").withPhone("94828224")
            .withAge("23").withEmail("werner@example.com")
            .withEmergencyContact("N/A").withStartDate("05/05/2005").withAddress("michegan ave").build();
    public static final Person FIONA = new PersonBuilder().withName("Fiona Kunz").withPhone("94825427")
            .withAge("56").withEmail("lydia@example.com")
            .withEmergencyContact("N/A").withStartDate("06/06/2006").withAddress("little tokyo").build();
    public static final Person GEORGE = new PersonBuilder().withName("George Best").withPhone("94842442")
            .withAge("18").withEmail("anna@example.com")
            .withEmergencyContact("N/A").withStartDate("07/07/2007").withAddress("4th street").build();

    // Manually added
    public static final Person HOON = new PersonBuilder().withName("Hoon Meier").withPhone("84862424")
            .withAge("43").withEmail("stefan@example.com")
            .withEmergencyContact("N/A").withStartDate("08/08/2008").withAddress("little india").build();
    public static final Person IDA = new PersonBuilder().withName("Ida Mueller").withPhone("84842131")
            .withAge("67").withEmail("hans@example.com")
            .withEmergencyContact("N/A").withStartDate("09/09/2009").withAddress("chicago ave").build();

    // Manually added - Person's details found in {@code CommandTestUtil}
    public static final Person AMY = new PersonBuilder().withName(VALID_NAME_AMY).withAge(VALID_AGE_AMY)
            .withPhone(VALID_PHONE_AMY).withEmail(VALID_EMAIL_AMY).withStartDate(VALID_START_DATE_AMY)
            .withEmergencyContact(VALID_EMERGENCY_CONTACT_AMY).withAddress(VALID_ADDRESS_AMY).withTags(VALID_TAG_FRIEND).build();
    public static final Person BOB = new PersonBuilder().withName(VALID_NAME_BOB).withAge(VALID_AGE_BOB)
            .withPhone(VALID_PHONE_BOB).withEmail(VALID_EMAIL_BOB).withStartDate(VALID_START_DATE_BOB)
            .withEmergencyContact(VALID_EMERGENCY_CONTACT_BOB).withAddress(VALID_ADDRESS_BOB).withTags(VALID_TAG_HUSBAND, VALID_TAG_FRIEND)"""
)
])
