<!doctype html>
<html>
<head>
    <meta name="layout" content="main"/>
    <title>Rejestracja w systemie restauracji Kaczorek</title>

    <asset:link rel="icon" href="favicon.ico" type="image/x-ico" />
    <asset:stylesheet src="registration.css"/>
</head>
<body>
    <div class="main ui container">
        <g:form class="ui form" name="registration-form">
            <div class="field">
                <label><g:message code="labels.username"/></label>
                <g:textField name="username"/>
            </div>
            <div class="field">
                <label><g:message code="labels.password"/></label>
                <g:passwordField name="password"/>
            </div>
            <div class="field">
                <label><g:message code="labels.passwordRepeat"/></label>
                <g:passwordField name="password-repeat"/>
            </div>
            <recaptcha:ifEnabled>
                <div class="field">
                    <recaptcha:recaptcha theme="light"/>
                </div>
            </recaptcha:ifEnabled>
            <div class="ui two column grid">
                <div class="column">
                    <g:submitButton class="ui button" name="login" value="${message(code: 'buttons.register')}"/>
                </div>
            </div>
        </g:form>
    </div>
</body>
</html>
