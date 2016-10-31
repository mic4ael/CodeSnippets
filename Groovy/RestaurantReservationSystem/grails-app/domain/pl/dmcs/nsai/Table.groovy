package pl.dmcs.nsai

class Table {
    Integer numberOfSeats

    static mapping = {
        table('tables')
        numberOfSeats(column: 'number_of_seats')
    }
}
