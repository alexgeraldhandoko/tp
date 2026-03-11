package seedu.address.model.person;

import static java.util.Objects.requireNonNull;

/**
 * Represents a timing record for a run distance.
 */
public class RunTiming {

    private final double distance;
    private final int minutes;
    private final double seconds;

    public RunTiming(double distance, int minutes, double seconds) {
        requireNonNull(distance);
        requireNonNull(minutes);
        requireNonNull(seconds);

        this.distance = distance;
        this.minutes = minutes;
        this.seconds = seconds;
    }

    public double getDistance() {
        return distance;
    }

    public int getMinutes() {
        return minutes;
    }

    public double getSeconds() {
        return seconds;
    }

    public double getTotalSeconds() {
        return minutes * 60 + seconds;
    }

    @Override
    public String toString() {
        return distance + "km in " + minutes + "min " + seconds + "s";
    }
}
