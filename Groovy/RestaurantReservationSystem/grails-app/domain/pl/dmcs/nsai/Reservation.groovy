package pl.dmcs.nsai


class Reservation {
    Date createdAt
    Date reservedAt

    String firstName
    String lastName
    String phoneNumber

    static belongsTo = [createdBy: User, reservedTable: Table]
    static mapping = {
        version(false)
        table('reservations')
    }
}
