package pl.dmcs.nsai

import grails.plugin.springsecurity.annotation.Secured

@Secured(['ROLE_ANONYMOUS'])
class RegistrationController {
    def index() {

    }
}
