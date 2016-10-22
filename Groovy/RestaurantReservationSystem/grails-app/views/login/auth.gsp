<!doctype html>
<html>
<head>
    <meta name="layout" content="main"/>
    <title>Rezerwacja stolików w restauracji Kaczorek</title>

    <asset:link rel="icon" href="favicon.ico" type="image/x-ico" />
    <asset:stylesheet src="auth.css"/>
</head>
<body>
    <div class="main ui container">
        <g:form class="ui form" id="login-form" url="${request.contextPath}/auth/login">
            <div class="field">
                <label><g:message code="labels.username"/></label>
                <g:textField name="username"/>
            </div>
            <div class="field">
                <label><g:message code="labels.password"/></label>
                <g:passwordField name="password"/>
            </div>
            <div class="ui two column grid">
                <div class="column">
                    <g:submitButton class="ui button" name="login" value="${message(code: 'buttons.login')}"/>
                </div>
                <div class="column">
                    <a class="ui primary button right floated" href="${request.contextPath}/register">
                        <g:message code="buttons.register"/>
                    </a>
                </div>
            </div>
        </g:form>
    </div>
</body>
</html>
