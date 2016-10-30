package pl.dmcs.nsai

import grails.converters.JSON

import pl.dmcs.nsai.Role
import pl.dmcs.nsai.User
import pl.dmcs.nsai.UserRole


class UsersController {
    def index() {
        def users = UserRole.findAllByRole(Role.findByAuthority("ROLE_USER"))*.user
        return [users: users]
    }

    def update() {
        def user = User.get(params.id)
        def response = [success: true]

        if (!user) {
            response.success = false
            return render(response as JSON)
        }

        def data = request.JSON
        if (data) {
            user.toggleState(data.enabled)
            user.save(flush: true, validate: false)
        }

        return render(response as JSON)
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
