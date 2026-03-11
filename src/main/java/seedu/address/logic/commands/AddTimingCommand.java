package seedu.address.logic.commands;

import static java.util.Objects.requireNonNull;

import java.util.List;

import seedu.address.commons.core.index.Index;
import seedu.address.logic.commands.exceptions.CommandException;
import seedu.address.model.Model;
import seedu.address.model.person.Person;
import seedu.address.model.person.RunTiming;

public class AddTimingCommand extends Command {

    public static final String COMMAND_WORD = "addtiming";

    private final Index index;
    private final RunTiming timing;

    public AddTimingCommand(Index index, RunTiming timing) {
        this.index = index;
        this.timing = timing;
    }

    @Override
    public CommandResult execute(Model model) throws CommandException {

        requireNonNull(model);

        List<Person> athletes = model.getFilteredPersonList();

        if (index.getZeroBased() >= athletes.size()) {
            throw new CommandException("Invalid index: athlete does not exist");
        }

        Person athlete = athletes.get(index.getZeroBased());

        athlete.addRunTiming(timing);

        return new CommandResult(
                "Added timing for "
                        + athlete.getName()
                        + ": "
                        + timing.toString()
        );
    }
}
