
from state_machine import (
    State,
    Event,
    acts_as_state_machine,
    after,
    before,
    InvalidStateTransition
)


@acts_as_state_machine
class Room:
    """The State pattern implemented for multiroom
    computer game in docs/state-diagrams.pdf
    """

    entry = State(initial=True)
    hall = State()
    dining_room = State()
    study = State()
    cellar = State()
    barn = State()
    ferry = State()

    east_to_hall = Event(from_states=entry,
                         to_state=hall)
    south_to_hall = Event(from_states=dining_room,
                          to_state=hall)
    west_to_hall = Event(from_states=study,
                         to_state=hall)
    west_to_dining_room = Event(from_states=hall,
                                to_state=dining_room)
    north_to_dining_room = Event(from_states=hall,
                                 to_state=dining_room)
    down_to_cellar = Event(from_states=(hall, study),
                           to_state=cellar)
    east_to_cellar = Event(from_states=cellar,
                           to_state=cellar)
    east_to_study = Event(from_states=hall,
                          to_state=study)
    west_to_study = Event(from_states=barn,
                          to_state=study)

    east = Event(from_states=entry,
                 to_state=hall)
    east = Event(from_states=hall,
                 to_state=study)
    east = Event(from_states=study,
                 to_state=barn)
    east = Event(from_states=barn,
                 to_state=ferry)
    east = Event(from_states=cellar,
                 to_state=cellar)



def transition(room, event, event_name):
    try:
        event()
    except InvalidStateTransition as err:
        print(f'Error: transition of {room.name} from {room.current_state} to {event_name} failed')


def main():
    EAST = 'east'
    WEST = 'west'
    ...

    p = Room()

    transition(p, p.entry, EAST)
