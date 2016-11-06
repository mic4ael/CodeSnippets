package pl.dmcs.nsai

import grails.plugin.springsecurity.SpringSecurityUtils


class HomeController {
    def index() {
        if (SpringSecurityUtils.ifAllGranted('ROLE_ADMIN')) {
            return render(view: 'admin_home')
        } else {
            return render(view: 'user_home')
        }
    }
}
