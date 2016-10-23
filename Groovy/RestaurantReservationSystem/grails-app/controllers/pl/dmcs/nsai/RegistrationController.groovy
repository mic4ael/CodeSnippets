package pl.dmcs.nsai

import com.megatome.grails.RecaptchaService
import org.slf4j.Logger
import org.slf4j.LoggerFactory

import pl.dmcs.nsai.User

class RegistrationController {
    RecaptchaService recaptchaService
    Logger log = LoggerFactory.getLogger(RegistrationController.class)

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
            return redirect(controller: 'Home')
        } else {
            return render(view: 'index', model: [user: user, invalidRecaptcha: invalidRecaptcha])
        }
    }
}
