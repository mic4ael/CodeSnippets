package pl.dmcs.nsai

import grails.converters.JSON

import pl.dmcs.nsai.User
import pl.dmcs.nsai.UserRole


class UsersController {
    def index() {
        return [users: User.list()]
    }

    def update() {
        def user = User.get(params.id)
    }

    def delete() {
        def user = User.get(params.id)
        def response = [success: true]

        if (!user) {
            response.success = false
        } else {
            UserRole.removeAll(user)
            user.delete()
        }

        return render(response as JSON)
    }
}
