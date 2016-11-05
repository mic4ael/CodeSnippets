package pl.dmcs.nsai


class Reservation {
    Date createdAt
    Date reservedAt

    static belongsTo = [createdBy: User, reservedTable: Table]
    static mapping = {
        table('reservations')
        createdAt(column: 'created_at', defaultValue: 'NOW()')
        reservedAt(column: 'reserved_at')
    }
}
