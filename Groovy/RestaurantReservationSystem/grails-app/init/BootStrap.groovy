import pl.dmcs.nsai.Role
import pl.dmcs.nsai.User
import pl.dmcs.nsai.UserRole


class BootStrap {
    def init = {
        def adminRole = new Role(authority: 'ROLE_ADMIN').save()
        def userRole = new Role(authority: 'ROLE_USER').save()
        def testUser = new User(username: 'admin', password: 'admin', passwordConfirm: 'admin', email: 'admin@admin.pl').save()

        UserRole.create(testUser, adminRole)
        UserRole.withSession {
            it.flush()
            it.clear()
        }
    }
}
