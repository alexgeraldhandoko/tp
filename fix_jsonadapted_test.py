import sys

filepath = "src/test/java/seedu/address/storage/JsonAdaptedPersonTest.java"
with open(filepath, "r") as f:
    text = f.read()

text = text.replace(
"""JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, null, VALID_PHONE, VALID_EMAIL,
                VALID_ADDRESS, VALID_START_DATE, VALID_TAGS, null);""",
"""JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, null, VALID_PHONE, VALID_EMAIL,
                VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_START_DATE, VALID_TAGS, null);""")

text = text.replace(
"""JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, INVALID_AGE, VALID_PHONE, VALID_EMAIL,
                VALID_ADDRESS, VALID_START_DATE, VALID_TAGS, null);""",
"""JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, INVALID_AGE, VALID_PHONE, VALID_EMAIL,
                VALID_ADDRESS, VALID_EMERGENCY_CONTACT, VALID_START_DATE, VALID_TAGS, null);""")

text = text.replace(
"""JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                VALID_ADDRESS, null, VALID_TAGS, null);""",
"""JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                VALID_ADDRESS, VALID_EMERGENCY_CONTACT, null, VALID_TAGS, null);""")

text = text.replace(
"""JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                VALID_ADDRESS, INVALID_START_DATE, VALID_TAGS, null);""",
"""JsonAdaptedPerson person = new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL,
                VALID_ADDRESS, VALID_EMERGENCY_CONTACT, INVALID_START_DATE, VALID_TAGS, null);""")

text = text.replace(
"""JsonAdaptedPerson person =
                new JsonAdaptedPerson(VALID_NAME, VALID_PHONE, VALID_EMAIL, VALID_ADDRESS,
                        INVALID_EMERGENCY_CONTACT, VALID_TAGS);""",
"""JsonAdaptedPerson person =
                new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL, VALID_ADDRESS,
                        INVALID_EMERGENCY_CONTACT, VALID_START_DATE, VALID_TAGS, null);""")

text = text.replace(
"""JsonAdaptedPerson person =
                new JsonAdaptedPerson(VALID_NAME, VALID_PHONE, VALID_EMAIL, VALID_ADDRESS,
                        null, VALID_TAGS);""",
"""JsonAdaptedPerson person =
                new JsonAdaptedPerson(VALID_NAME, VALID_AGE, VALID_PHONE, VALID_EMAIL, VALID_ADDRESS,
                        null, VALID_START_DATE, VALID_TAGS, null);""")


with open(filepath, "w") as f:
    f.write(text)

