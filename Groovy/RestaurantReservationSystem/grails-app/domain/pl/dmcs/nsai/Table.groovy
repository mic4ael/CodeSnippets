package pl.dmcs.nsai

class Table {
    String config

    static mapping = {
        table('tables')
        config(type: 'text')
    }
}
