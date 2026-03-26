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
            print(f"Warning: String not found in {filepath}:\n{old_str}")
        content = content.replace(old_str, new_str)
        
    with open(filepath, 'w') as f:
        f.write(content)

base_dir = "/Users/vincentjulijanto/Downloads/NUS/CS2103T/tp/"

patch_file(base_dir + "src/main/java/seedu/address/logic/Messages.java", [
(
"""<<<<<<< HEAD
                .append("; Emergency Contact: ")
                .append(person.getEmergencyContact())
=======
                .append("; Start Date: ")
                .append(person.getStartDate())
>>>>>>> master""",
"""                .append("; Emergency Contact: ")
                .append(person.getEmergencyContact())
                .append("; Start Date: ")
                .append(person.getStartDate())"""
)
])

patch_file(base_dir + "src/main/java/seedu/address/logic/parser/AddCommandParser.java", [
(
"""<<<<<<< HEAD
                ArgumentTokenizer.tokenize(args,
                        PREFIX_NAME, PREFIX_PHONE, PREFIX_EMAIL, PREFIX_ADDRESS, PREFIX_TAG,
                        PREFIX_EMERGENCY_CONTACT);
=======
                ArgumentTokenizer.tokenize(args, PREFIX_NAME, PREFIX_AGE, PREFIX_PHONE,
                        PREFIX_EMAIL, PREFIX_ADDRESS, PREFIX_START_DATE, PREFIX_TAG);
>>>>>>> master""",
"""                ArgumentTokenizer.tokenize(args,
                        PREFIX_NAME, PREFIX_AGE, PREFIX_PHONE, PREFIX_EMAIL, PREFIX_ADDRESS,
                        PREFIX_EMERGENCY_CONTACT, PREFIX_START_DATE, PREFIX_TAG);"""
),
(
"""<<<<<<< HEAD
        if (argMultimap.getValue(PREFIX_EMERGENCY_CONTACT).isPresent()) {
            emergencyContact = new EmergencyContact(argMultimap.getValue(PREFIX_EMERGENCY_CONTACT).get());
        } else {
            emergencyContact = new EmergencyContact("N/A");
        }

        Person person = new Person(name, phone, email, address, emergencyContact, tagList);
=======
        Person person = new Person(name, age, phone, email, address, startDate, tagList);
>>>>>>> master""",
"""        if (argMultimap.getValue(PREFIX_EMERGENCY_CONTACT).isPresent()) {
            emergencyContact = new EmergencyContact(argMultimap.getValue(PREFIX_EMERGENCY_CONTACT).get());
        } else {
            emergencyContact = new EmergencyContact("N/A");
        }

        Person person = new Person(name, age, phone, email, address, emergencyContact, startDate, tagList);"""
)
])

patch_file(base_dir + "src/main/java/seedu/address/logic/parser/CliSyntax.java", [
(
"""<<<<<<< HEAD
    public static final Prefix PREFIX_EMERGENCY_CONTACT = new Prefix("ec/");
=======
    public static final Prefix PREFIX_DISTANCE = new Prefix("dist/");
    public static final Prefix PREFIX_MIN = new Prefix("min/");
    public static final Prefix PREFIX_SEC = new Prefix("sec/");
    public static final Prefix PREFIX_BY = new Prefix("by/");
    public static final Prefix PREFIX_ORDER = new Prefix("order/");
>>>>>>> master""",
"""    public static final Prefix PREFIX_EMERGENCY_CONTACT = new Prefix("ec/");
    public static final Prefix PREFIX_DISTANCE = new Prefix("dist/");
    public static final Prefix PREFIX_MIN = new Prefix("min/");
    public static final Prefix PREFIX_SEC = new Prefix("sec/");
    public static final Prefix PREFIX_BY = new Prefix("by/");
    public static final Prefix PREFIX_ORDER = new Prefix("order/");"""
)
])

patch_file(base_dir + "src/main/java/seedu/address/logic/parser/EditCommandParser.java", [
(
"""<<<<<<< HEAD
                ArgumentTokenizer.tokenize(args,
                        PREFIX_NAME, PREFIX_PHONE, PREFIX_EMAIL, PREFIX_ADDRESS, PREFIX_TAG,
                        PREFIX_EMERGENCY_CONTACT);
=======
                ArgumentTokenizer.tokenize(args, PREFIX_NAME, PREFIX_AGE, PREFIX_PHONE,
                        PREFIX_EMAIL, PREFIX_ADDRESS, PREFIX_START_DATE, PREFIX_TAG);

>>>>>>> master""",
"""                ArgumentTokenizer.tokenize(args,
                        PREFIX_NAME, PREFIX_AGE, PREFIX_PHONE, PREFIX_EMAIL, PREFIX_ADDRESS, PREFIX_TAG,
                        PREFIX_EMERGENCY_CONTACT, PREFIX_START_DATE);"""
),
(
"""<<<<<<< HEAD
        argMultimap.verifyNoDuplicatePrefixesFor(
                PREFIX_NAME, PREFIX_PHONE, PREFIX_EMAIL, PREFIX_ADDRESS, PREFIX_EMERGENCY_CONTACT);
=======
        argMultimap.verifyNoDuplicatePrefixesFor(PREFIX_NAME, PREFIX_AGE, PREFIX_PHONE,
                PREFIX_EMAIL, PREFIX_ADDRESS, PREFIX_START_DATE);
>>>>>>> master""",
"""        argMultimap.verifyNoDuplicatePrefixesFor(
                PREFIX_NAME, PREFIX_AGE, PREFIX_PHONE, PREFIX_EMAIL, PREFIX_ADDRESS, PREFIX_EMERGENCY_CONTACT, PREFIX_START_DATE);"""
),
(
"""<<<<<<< HEAD
        if (argMultimap.getValue(PREFIX_EMERGENCY_CONTACT).isPresent()) {
            editPersonDescriptor.setEmergencyContact(
                    new EmergencyContact(argMultimap.getValue(PREFIX_EMERGENCY_CONTACT).get()));
=======
        if (argMultimap.getValue(PREFIX_START_DATE).isPresent()) {
            editPersonDescriptor.setStartDate(ParserUtil.parseStartDate(argMultimap.getValue(PREFIX_START_DATE).get()));
>>>>>>> master""",
"""        if (argMultimap.getValue(PREFIX_EMERGENCY_CONTACT).isPresent()) {
            editPersonDescriptor.setEmergencyContact(
                    new EmergencyContact(argMultimap.getValue(PREFIX_EMERGENCY_CONTACT).get()));
        }
        if (argMultimap.getValue(PREFIX_START_DATE).isPresent()) {
            editPersonDescriptor.setStartDate(ParserUtil.parseStartDate(argMultimap.getValue(PREFIX_START_DATE).get()));"""
)
])

patch_file(base_dir + "src/main/java/seedu/address/model/person/Person.java", [
(
"""<<<<<<< HEAD
    private final EmergencyContact emergencyContact;
=======
    private final StartDate startDate;

    /** Tags associated with this person. */
>>>>>>> master""",
"""    private final EmergencyContact emergencyContact;
    private final StartDate startDate;

    /** Tags associated with this person. */"""
),
(
"""<<<<<<< HEAD
    public Person(Name name, Phone phone, Email email, Address address,
                  EmergencyContact emergencyContact, Set<Tag> tags) {
        requireAllNonNull(name, phone, email, address, emergencyContact, tags);
=======
    public Person(Name name, Age age, Phone phone, Email email,
                  Address address, StartDate startDate, Set<Tag> tags) {
        requireAllNonNull(name, age, phone, email, address, startDate, tags);
>>>>>>> master""",
"""    public Person(Name name, Age age, Phone phone, Email email, Address address,
                  EmergencyContact emergencyContact, StartDate startDate, Set<Tag> tags) {
        requireAllNonNull(name, age, phone, email, address, emergencyContact, startDate, tags);"""
),
(
"""<<<<<<< HEAD
        this.emergencyContact = emergencyContact;
=======
        this.startDate = startDate;
>>>>>>> master""",
"""        this.emergencyContact = emergencyContact;
        this.startDate = startDate;"""
),
(
"""<<<<<<< HEAD
                && emergencyContact.equals(otherPerson.emergencyContact)
=======
                && startDate.equals(otherPerson.startDate)
>>>>>>> master""",
"""                && emergencyContact.equals(otherPerson.emergencyContact)
                && startDate.equals(otherPerson.startDate)"""
),
(
"""<<<<<<< HEAD
        // use this method for custom fields hashing instead of implementing your own
        return Objects.hash(name, phone, email, address, emergencyContact, tags);
=======
        return Objects.hash(name, age, phone, email, address, startDate, tags);
>>>>>>> master""",
"""        // use this method for custom fields hashing instead of implementing your own
        return Objects.hash(name, age, phone, email, address, emergencyContact, startDate, tags);"""
),
(
"""<<<<<<< HEAD
                .add("emergencyContact", emergencyContact)
=======
                .add("start date", startDate)
>>>>>>> master""",
"""                .add("emergencyContact", emergencyContact)
                .add("start date", startDate)"""
)
])

patch_file(base_dir + "src/main/java/seedu/address/model/util/SampleDataUtil.java", [
(
"""<<<<<<< HEAD
                new Person(new Name("Alex Yeoh"), new Phone("87438807"), new Email("alexyeoh@example.com"),
                        new Address("Blk 30 Geylang Street 29, #06-40"),
                        new EmergencyContact("Mom 91234567"),
                        getTagSet("friends")),
                new Person(new Name("Bernice Yu"), new Phone("99272758"), new Email("berniceyu@example.com"),
                        new Address("Blk 30 Lorong 3 Serangoon Gardens, #07-18"),
                        new EmergencyContact("Dad 92345678"),
                        getTagSet("colleagues", "friends")),
                new Person(new Name("Charlotte Oliveiro"), new Phone("93210283"), new Email("charlotte@example.com"),
                        new Address("Blk 11 Ang Mo Kio Street 74, #11-04"),
                        new EmergencyContact("Sister 93456789"),
                        getTagSet("neighbours")),
                new Person(new Name("David Li"), new Phone("91031282"), new Email("lidavid@example.com"),
                        new Address("Blk 436 Serangoon Gardens Street 26, #16-43"),
                        new EmergencyContact("Brother 94567890"),
                        getTagSet("family")),
                new Person(new Name("Irfan Ibrahim"), new Phone("92492021"), new Email("irfan@example.com"),
                        new Address("Blk 47 Tampines Street 20, #17-35"),
                        new EmergencyContact("Uncle 95678901"),
                        getTagSet("classmates")),
                new Person(new Name("Roy Balakrishnan"), new Phone("92624417"), new Email("royb@example.com"),
                        new Address("Blk 45 Aljunied Street 85, #11-31"),
                        new EmergencyContact("Aunt 96789012"),
                        getTagSet("colleagues"))
=======
            new Person(new Name("Alex Yeoh"), new Age("18"), new Phone("87438807"),
                    new Email("alexyeoh@example.com"), new Address("Blk 30 Geylang Street 29, #06-40"),
                    new StartDate("01/01/2001"), getTagSet("friends")),
            new Person(new Name("Bernice Yu"), new Age("25"), new Phone("99272758"),
                    new Email("berniceyu@example.com"), new Address("Blk 30 Lorong 3 Serangoon Gardens, #07-18"),
                    new StartDate("02/02/2002"), getTagSet("colleagues", "friends")),
            new Person(new Name("Charlotte Oliveiro"), new Age("63"), new Phone("93210283"),
                    new Email("charlotte@example.com"), new Address("Blk 11 Ang Mo Kio Street 74, #11-04"),
                    new StartDate("03/03/2003"), getTagSet("neighbours")),
            new Person(new Name("David Li"), new Age("34"), new Phone("91031282"),
                    new Email("lidavid@example.com"), new Address("Blk 436 Serangoon Gardens Street 26, #16-43"),
                    new StartDate("04/04/2004"), getTagSet("family")),
            new Person(new Name("Irfan Ibrahim"), new Age("20"), new Phone("92492021"),
                    new Email("irfan@example.com"), new Address("Blk 47 Tampines Street 20, #17-35"),
                    new StartDate("05/05/2005"), getTagSet("classmates")),
            new Person(new Name("Roy Balakrishnan"), new Age("29"), new Phone("92624417"),
                    new Email("royb@example.com"), new Address("Blk 45 Aljunied Street 85, #11-31"),
                    new StartDate("06/06/2006"), getTagSet("colleagues"))
>>>>>>> master""",
"""            new Person(new Name("Alex Yeoh"), new Age("18"), new Phone("87438807"),
                    new Email("alexyeoh@example.com"), new Address("Blk 30 Geylang Street 29, #06-40"),
                    new EmergencyContact("Mom 91234567"), new StartDate("01/01/2001"), getTagSet("friends")),
            new Person(new Name("Bernice Yu"), new Age("25"), new Phone("99272758"),
                    new Email("berniceyu@example.com"), new Address("Blk 30 Lorong 3 Serangoon Gardens, #07-18"),
                    new EmergencyContact("Dad 92345678"), new StartDate("02/02/2002"), getTagSet("colleagues", "friends")),
            new Person(new Name("Charlotte Oliveiro"), new Age("63"), new Phone("93210283"),
                    new Email("charlotte@example.com"), new Address("Blk 11 Ang Mo Kio Street 74, #11-04"),
                    new EmergencyContact("Sister 93456789"), new StartDate("03/03/2003"), getTagSet("neighbours")),
            new Person(new Name("David Li"), new Age("34"), new Phone("91031282"),
                    new Email("lidavid@example.com"), new Address("Blk 436 Serangoon Gardens Street 26, #16-43"),
                    new EmergencyContact("Brother 94567890"), new StartDate("04/04/2004"), getTagSet("family")),
            new Person(new Name("Irfan Ibrahim"), new Age("20"), new Phone("92492021"),
                    new Email("irfan@example.com"), new Address("Blk 47 Tampines Street 20, #17-35"),
                    new EmergencyContact("Uncle 95678901"), new StartDate("05/05/2005"), getTagSet("classmates")),
            new Person(new Name("Roy Balakrishnan"), new Age("29"), new Phone("92624417"),
                    new Email("royb@example.com"), new Address("Blk 45 Aljunied Street 85, #11-31"),
                    new EmergencyContact("Aunt 96789012"), new StartDate("06/06/2006"), getTagSet("colleagues"))"""
)
])

patch_file(base_dir + "src/main/java/seedu/address/storage/JsonAdaptedPerson.java", [
(
"""<<<<<<< HEAD
import seedu.address.model.person.EmergencyContact;
=======
import seedu.address.model.person.RunTiming;
import seedu.address.model.person.StartDate;
>>>>>>> master""",
"""import seedu.address.model.person.EmergencyContact;
import seedu.address.model.person.RunTiming;
import seedu.address.model.person.StartDate;"""
),
(
"""<<<<<<< HEAD
    private final String emergencyContact;
    private final List<JsonAdaptedTag> tags = new ArrayList<>();
=======
    private final String startDate;

    private final List<JsonAdaptedTag> tags = new ArrayList<>();
    private final List<JsonAdaptedRunTiming> timings = new ArrayList<>();
>>>>>>> master""",
"""    private final String emergencyContact;
    private final String startDate;

    private final List<JsonAdaptedTag> tags = new ArrayList<>();
    private final List<JsonAdaptedRunTiming> timings = new ArrayList<>();"""
),
(
"""<<<<<<< HEAD
    public JsonAdaptedPerson(@JsonProperty("name") String name, @JsonProperty("phone") String phone,
                             @JsonProperty("email") String email, @JsonProperty("address") String address,
                             @JsonProperty("emergencyContact") String emergencyContact,
                             @JsonProperty("tags") List<JsonAdaptedTag> tags) {
=======
    public JsonAdaptedPerson(
            @JsonProperty("name") String name,
            @JsonProperty("age") String age,
            @JsonProperty("phone") String phone,
            @JsonProperty("email") String email,
            @JsonProperty("address") String address,
            @JsonProperty("startDate") String startDate,
            @JsonProperty("tags") List<JsonAdaptedTag> tags,
            @JsonProperty("timings") List<JsonAdaptedRunTiming> timings) {

>>>>>>> master""",
"""    public JsonAdaptedPerson(
            @JsonProperty("name") String name,
            @JsonProperty("age") String age,
            @JsonProperty("phone") String phone,
            @JsonProperty("email") String email,
            @JsonProperty("address") String address,
            @JsonProperty("emergencyContact") String emergencyContact,
            @JsonProperty("startDate") String startDate,
            @JsonProperty("tags") List<JsonAdaptedTag> tags,
            @JsonProperty("timings") List<JsonAdaptedRunTiming> timings) {"""
),
(
"""<<<<<<< HEAD
        this.emergencyContact = emergencyContact;
=======
        this.startDate = startDate;

>>>>>>> master""",
"""        this.emergencyContact = emergencyContact;
        this.startDate = startDate;
"""
),
(
"""<<<<<<< HEAD
        emergencyContact = source.getEmergencyContact().value;
=======
        startDate = source.getStartDate().value;

>>>>>>> master""",
"""        emergencyContact = source.getEmergencyContact().value;
        startDate = source.getStartDate().value;
"""
),
(
"""<<<<<<< HEAD
        final Set<Tag> modelTags = new HashSet<>(personTags);
        return new Person(modelName, modelPhone, modelEmail, modelAddress, modelEmergencyContact, modelTags);
    }
=======
        if (startDate == null) {
            throw new IllegalValueException(String.format(MISSING_FIELD_MESSAGE_FORMAT,
                    StartDate.class.getSimpleName()));
        }
        if (!StartDate.isValidStartDate(startDate)) {
            throw new IllegalValueException(StartDate.MESSAGE_CONSTRAINTS);
        }
        final StartDate modelStartDate = new StartDate(startDate);
>>>>>>> master""",
"""        if (startDate == null) {
            throw new IllegalValueException(String.format(MISSING_FIELD_MESSAGE_FORMAT,
                    StartDate.class.getSimpleName()));
        }
        if (!StartDate.isValidStartDate(startDate)) {
            throw new IllegalValueException(StartDate.MESSAGE_CONSTRAINTS);
        }
        final StartDate modelStartDate = new StartDate(startDate);"""
)
])

patch_file(base_dir + "src/main/java/seedu/address/ui/PersonCard.java", [
(
"""<<<<<<< HEAD
    private Label emergencyContact;
=======
    private Label startDate;
>>>>>>> master""",
"""    private Label emergencyContact;
    @FXML
    private Label startDate;"""
),
(
"""<<<<<<< HEAD
        emergencyContact.setText(person.getEmergencyContact().value);
=======
        startDate.setText(person.getStartDate().value);
>>>>>>> master""",
"""        emergencyContact.setText(person.getEmergencyContact().value);
        startDate.setText(person.getStartDate().value);"""
)
])

patch_file(base_dir + "src/main/resources/view/PersonListCard.fxml", [
(
"""<<<<<<< HEAD
      <Label fx:id="phone" styleClass="cell_small_label" text="$phone" />
      <Label fx:id="address" styleClass="cell_small_label" text="$address" />
      <Label fx:id="email" styleClass="cell_small_label" text="$email" />
      <Label fx:id="emergencyContact" styleClass="cell_small_label" text="$emergencyContact" />
=======
      <Label fx:id="age" styleClass="cell_small_label" text="\\$age" />
      <Label fx:id="phone" styleClass="cell_small_label" text="\\$phone" />
      <Label fx:id="address" styleClass="cell_small_label" text="\\$address" />
      <Label fx:id="email" styleClass="cell_small_label" text="\\$email" />
      <Label fx:id="startDate" styleClass="cell_small_label" text="\\$startDate" />
>>>>>>> master""",
"""      <Label fx:id="age" styleClass="cell_small_label" text="\\$age" />
      <Label fx:id="phone" styleClass="cell_small_label" text="\\$phone" />
      <Label fx:id="address" styleClass="cell_small_label" text="\\$address" />
      <Label fx:id="email" styleClass="cell_small_label" text="\\$email" />
      <Label fx:id="emergencyContact" styleClass="cell_small_label" text="\\$emergencyContact" />
      <Label fx:id="startDate" styleClass="cell_small_label" text="\\$startDate" />"""
)
])

# Also doing tests since they are in get_changed_files

print("All main sources patched!")
