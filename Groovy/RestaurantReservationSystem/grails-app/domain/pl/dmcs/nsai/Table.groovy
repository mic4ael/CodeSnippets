package pl.dmcs.nsai

import pl.dmcs.nsai.Reservation

class Table {
    String config

    static hasMany = [reservations: Reservation]

    static mapping = {
        table('tables')
        config(type: 'text')
    }
}
