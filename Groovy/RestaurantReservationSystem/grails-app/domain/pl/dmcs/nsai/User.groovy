package pl.dmcs.nsai

import groovy.transform.ToString
import groovy.transform.EqualsAndHashCode

@EqualsAndHashCode(includes='username')
@ToString(includes='username', includeNames=true, includePackage=true)
class User implements Serializable {
    transient springSecurityService

    static transients = ['springSecurityService']

    static mapping = {
        password(column: '`password`')
    }

    static constraints = {
        password(blank: false, password: true)
        username(blank: false, unique: true)
    }

    String username
    String password

    boolean enabled
    boolean accountExpired
    boolean accountLocked
    boolean passwordExpired

    Set<Role> getAuthorities() {
        UserRole.findAllByUser(this)*.role
    }

    def beforeInsert() {
        encodePassword()
    }

    def beforeUpdate() {
        if (isDirty('password')) {
            encodePassword()
        }
    }

    protected void encodePassword() {
        if (springSecurityService?.passwordEncoder) {
            password = springSecurityService.encodePassword(password)
        } else {
            password = password
        }
    }
}
