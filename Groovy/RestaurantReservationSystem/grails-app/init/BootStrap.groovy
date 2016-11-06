import pl.dmcs.nsai.Role
import pl.dmcs.nsai.User
import pl.dmcs.nsai.UserRole


class BootStrap {
    def init = {
        def adminRole = new Role(authority: 'ROLE_ADMIN').save()
        def userRole = new Role(authority: 'ROLE_USER').save()
        def admin = new User(username: 'admin', password: 'admin', passwordConfirm: 'admin', email: 'admin@admin.pl').save()
        def testUser = new User(username: 'mic4ael', password: 'mic4ael', passwordConfirm: 'mic4ael', email: 'mic4ael@mic4ael.pl').save()

        UserRole.create(admin, adminRole)
        UserRole.create(testUser, userRole)
        UserRole.withSession {
            it.flush()
            it.clear()
        }
    }
}
