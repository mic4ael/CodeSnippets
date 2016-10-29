package pl.dmcs.nsai

import pl.dmcs.nsai.User


class UsersController {
    def index() {
        return [users: User.list()]
    }
}
