<!doctype html>
<html>
<head>
    <meta name="layout" content="main"/>
    <title>Rejestracja w systemie restauracji Kaczorek</title>

    <asset:link rel="icon" href="favicon.ico" type="image/x-ico" />
    <asset:stylesheet src="registration.css"/>
</head>
<body>
    <div id="registration-form" class="main ui container segment">
        <div class="langs">
            <a href="/register?lang=pl">
                <asset:image src="polish.png"/>
            </a>
            <a href="/register?lang=en">
                <asset:image src="english.png"/>
            </a>
        </div>
        <g:form class="ui form ${hasErrors(bean: user, field: '', 'error')} ${invalidRecaptcha == true ? 'error' : ''}"
                url="['controller': 'register', 'action': '']">
            <div class="field ${hasErrors(bean: user, field: 'username', 'error')}">
                <label><g:message code="labels.username"/></label>
                <g:textField name="username" value="${user != null ? user.username : ''}"/>
            </div>
            <g:hasErrors bean="${user}" field="username">
                <div class="ui message error">
                    <div class="header">
                        <g:message code="User.invalidUsername"/>
                    </div>
                    <g:eachError bean="${user}" field="username">
                        <p><g:message error="${it}"/></p>
                    </g:eachError>
                </div>
            </g:hasErrors>
            <div class="field ${hasErrors(bean: user, field: 'email', 'error')}">
                <label><g:message code="labels.email"/></label>
                <g:textField name="email" value="${user != null ? user.email : ''}"/>
            </div>
            <g:hasErrors bean="${user}" field="email">
                <div class="ui message error">
                    <div class="header">
                        <g:message code="User.invalidEmail"/>
                    </div>
                    <g:eachError bean="${user}" field="email">
                        <p><g:message error="${it}"/></p>
                    </g:eachError>
                </div>
            </g:hasErrors>
            <div class="field ${hasErrors(bean: user, field: 'password', 'error')}">
                <label><g:message code="labels.password"/></label>
                <g:passwordField name="password"/>
            </div>
            <g:hasErrors bean="${user}" field="password">
                <div class="ui message error">
                    <div class="header">
                        <g:message code="User.invalidPassword"/>
                    </div>
                    <g:eachError bean="${user}" field="password">
                        <p><g:message error="${it}"/></p>
                    </g:eachError>
                </div>
            </g:hasErrors>
            <div class="field">
                <label><g:message code="labels.passwordConfirm"/></label>
                <g:passwordField name="passwordConfirm"/>
            </div>
            <recaptcha:ifEnabled>
                <div class="field">
                    <recaptcha:recaptcha theme="light"/>
                </div>
            </recaptcha:ifEnabled>
            <g:if test="${invalidRecaptcha == true}">
                <div class="ui message error">
                    <g:message code="User.invalidRecaptcha"/>
                </div>
            </g:if>
            <div class="ui two column grid">
                <div class="column">
                    <g:submitButton class="ui button" name="login" value="${message(code: 'buttons.register')}"/>
                </div>
                <div class="column">
                    <g:link url="[action: 'auth', controller: 'login']" class="ui primary button right floated">
                        <g:message code="buttons.back"/>
                    </g:link>
                </div>
            </div>
        </g:form>
    </div>
</body>
</html>
