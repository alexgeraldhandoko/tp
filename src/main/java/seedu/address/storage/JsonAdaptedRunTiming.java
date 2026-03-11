package seedu.address.storage;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import seedu.address.model.person.RunTiming;

class JsonAdaptedRunTiming {

    private final double distance;
    private final int minutes;
    private final double seconds;

    @JsonCreator
    public JsonAdaptedRunTiming(
            @JsonProperty("distance") double distance,
            @JsonProperty("minutes") int minutes,
            @JsonProperty("seconds") double seconds) {

        this.distance = distance;
        this.minutes = minutes;
        this.seconds = seconds;
    }

    public JsonAdaptedRunTiming(RunTiming source) {
        distance = source.getDistance();
        minutes = source.getMinutes();
        seconds = source.getSeconds();
    }

    public RunTiming toModelType() {
        return new RunTiming(distance, minutes, seconds);
    }
}
