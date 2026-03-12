package seedu.address.storage;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import seedu.address.commons.exceptions.IllegalValueException;
import seedu.address.model.person.Address;
import seedu.address.model.person.Age;
import seedu.address.model.person.Email;
import seedu.address.model.person.Name;
import seedu.address.model.person.Person;
import seedu.address.model.person.Phone;
import seedu.address.model.person.RunTiming;
import seedu.address.model.person.StartDate;
import seedu.address.model.tag.Tag;

/**
 * Jackson-friendly version of {@link Person}.
 */
class JsonAdaptedPerson {

    public static final String MISSING_FIELD_MESSAGE_FORMAT = "Person's %s field is missing!";

    private final String name;
    private final String age;
    private final String phone;
    private final String email;
    private final String address;
    private final String startDate;

    private final List<JsonAdaptedTag> tags = new ArrayList<>();
    private final List<JsonAdaptedRunTiming> timings = new ArrayList<>();

    @JsonCreator
    public JsonAdaptedPerson(
            @JsonProperty("name") String name,
            @JsonProperty("age") String age,
            @JsonProperty("phone") String phone,
            @JsonProperty("email") String email,
            @JsonProperty("address") String address,
            @JsonProperty("startDate") String startDate,
            @JsonProperty("tags") List<JsonAdaptedTag> tags) {

        this.name = name;
        this.age = age;
        this.phone = phone;
        this.email = email;
        this.address = address;
        this.startDate = startDate;

        if (tags != null) {
            this.tags.addAll(tags);
        }

        if (timings != null) {
            this.timings.addAll(timings);
        }
    }

    /**
     * Converts a given {@code Person} into this class for Jackson use.
     */
    public JsonAdaptedPerson(Person source) {
        name = source.getName().fullName;
        age = source.getAge().value;
        phone = source.getPhone().value;
        email = source.getEmail().value;
        address = source.getAddress().value;
        startDate = source.getStartDate().value;

        tags.addAll(source.getTags().stream()
                .map(JsonAdaptedTag::new)
                .collect(Collectors.toList()));

        timings.addAll(source.getRunTimings().stream()
                .map(JsonAdaptedRunTiming::new)
                .collect(Collectors.toList()));
    }

    /**
     * Converts this Jackson-friendly adapted person object into the model's {@code Person} object.
     */
    public Person toModelType() throws IllegalValueException {

        final List<Tag> personTags = new ArrayList<>();
        for (JsonAdaptedTag tag : tags) {
            personTags.add(tag.toModelType());
        }

        final List<RunTiming> runTimings = new ArrayList<>();
        for (JsonAdaptedRunTiming timing : timings) {
            runTimings.add(timing.toModelType());
        }

        if (name == null) {
            throw new IllegalValueException(String.format(MISSING_FIELD_MESSAGE_FORMAT, Name.class.getSimpleName()));
        }

        final Name modelName = new Name(name);
        final Age modelAge = new Age(age);
        final Phone modelPhone = new Phone(phone);
        final Email modelEmail = new Email(email);
        final Address modelAddress = new Address(address);
        final StartDate modelStartDate = new StartDate(startDate);

        final Set<Tag> modelTags = new HashSet<>(personTags);

        Person person = new Person(modelName, modelAge, modelPhone, modelEmail,
                modelAddress, modelStartDate, modelTags);

        for (RunTiming timing : runTimings) {
            person.addRunTiming(timing);
        }

        return person;
    }
}
