package pl.dmcs.nsai

import groovy.transform.ToString
import groovy.transform.EqualsAndHashCode


@EqualsAndHashCode(includes='username')
@ToString(includes='username', includeNames=true, includePackage=true)
class User implements Serializable {
    transient springSecurityService
    static mapping = {
        table('users')
        password(column: 'password')
    }

    static transients = ['passwordConfirm', 'springSecurityService']
    static constraints = {
        username(minSize: 3, blank: false, unique: true)
        password(minSize: 3, blank: false, password: true, validator: {val, obj ->
            def passwordConfirm = obj.passwordConfirm
            def isValid = (passwordConfirm == val || obj.springSecurityService.passwordEncoder.isPasswordValid(val, passwordConfirm, null))
            return (isValid ? true : ['invalid.matchingpasswords'])
        })
    }

    String username
    String password
    String passwordConfirm

    boolean enabled = true
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
