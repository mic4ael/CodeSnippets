package pl.dmcs.nsai


class Reservation {
    Date createdAt
    Datetime reservedAt

    static belongsTo = [createdBy: User, reservedTable: Table]
    static mapping = {
        table('reservations')
        createdAt(column: 'created_at', defaultValue: 'NOW()')
        reservedAt(column: 'reserved_at')
    }
}
