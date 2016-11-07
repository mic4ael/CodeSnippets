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
        def response = [success: false]

        if (!user) {
            response.message = 'User with id ${params.id} does not exist'
            return render(response as JSON)
        }

        def data = request.JSON
        if (data) {
            user.toggleState(data.enabled)
            user.save(flush: true, validate: false)
            response.success = true
            response.message = 'User has been updated'
        }

        return render(response as JSON)
    }

    def delete() {
        def user = User.get(params.id)
        def response = [success: false]

        if (!user) {
            response.message = 'User with id ${params.id} does not exist'
        } else {
            UserRole.removeAll(user)
            user.delete()
            response.success = true
            response.message = 'User has been removed'
        }

        return render(response as JSON)
    }
}
