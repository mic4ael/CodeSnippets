package pl.dmcs.nsai

import com.megatome.grails.RecaptchaService
import grails.plugins.mail.MailService

import pl.dmcs.nsai.Role
import pl.dmcs.nsai.User
import pl.dmcs.nsai.UserRole


class RegistrationController {
    MailService mailService
    RecaptchaService recaptchaService

    def index() {
        return render(view: 'index')
    }

    def create() {
        def user = new User(params)
        def invalidRecaptcha = true

        if (recaptchaService.verifyAnswer(session, request.getRemoteAddr(), params)) {
            invalidRecaptcha = false
        }

        if (!user.hasErrors() && !invalidRecaptcha && user.save()) {
            recaptchaService.cleanUp(session)
            mailService.sendMail {
                async(true)
                to(user.email)
                subject("Hello ${user.username}")
                text(g.message(code: 'messages.registration'))
            }
            return redirect(controller: 'Home')
        } else {
            return render(view: 'index', model: [user: user, invalidRecaptcha: invalidRecaptcha])
        }
    }
}
