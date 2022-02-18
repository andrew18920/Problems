from dataclasses import dataclass

booking_length = 1.5


@dataclass
class Booking:
    name: str
    time: int
    people: int

    def __iter__(self):
        return iter((self.name, self.time, self.people))


bookings = [
    Booking("Rebecca A", 13, 6),
    Booking("Rebecca B", 13, 2),
    Booking("Stiller", 20, 5),
    Booking("Lauren", 18, 2),
    Booking("Gabi", 18, 7),
    Booking("Gavin", 18, 2),
    Booking("Monia", 19, 4),
    Booking("Kevin", 18, 4),
    Booking("Steven", 19, 2),
    Booking("Amy", 14, 2),
]

tables = {
    "T1": 2,
    "T2": 2,
    "T3": 6,
    "T4": 4,
    "T5": 3,
    "T6": 2,
    "T7": 3,
    "T8": 2,
    "T9": 4,
    "T10a": 3,
    "T10b": 2,
    "T11": 2,
    "T12": 2,
    "OT1": 2,
    "OT2": 2,
}

taken_tables = {}


def find_tables(people):
    return sorted(
        [tb for tb, p in tables.items() if p >= people], key=lambda x: tables[x]
    )


def available(tb):
    return tb not in taken_tables.keys()


bookings.sort(key=lambda x: x.time)

successful_bookings = {tb: [] for tb in tables.keys()}
unsuccessful_bookings = []

for (name, time, people) in bookings:
    taken_tables = {
        tb: finish_time
        for tb, finish_time in taken_tables.items()
        if time < finish_time
    }

    if poss := [tb for tb in find_tables(people) if available(tb)]:
        successful_bookings[poss[0]].append(Booking(name, time, people))
        taken_tables[poss[0]] = time + booking_length
    else:
        poss_if_avail = list(find_tables(people))
        unsuccessful_bookings.append((name, time, people))
        print(
            f"{name}, {time}:00, {people}pp.\n\
At this time, tables {', '.join(poss_if_avail)} are taken.\n\
The restaurant is unable to accommodate this reservation; \
please choose a different time."
        )

bookings_by_time = {}
for table, li in successful_bookings.items():
    for booking in li:
        if booking.time in bookings_by_time:
            bookings_by_time[booking.time].append((table, booking.name, booking.people))
        else:
            bookings_by_time[booking.time] = [(table, booking.name, booking.people)]

for time, tbs in bookings_by_time.items():
    tbs = [f"{(tb[2])}pp ({tb[0]})" for tb in tbs]
    print(f"{time}:00: {', '.join(tbs)}")
