<!doctype html>
<html>
<head>
    <meta name="layout" content="main"/>
    <title>Rezerwacja stolików w restauracji Kaczorek</title>

    <asset:link rel="icon" href="favicon.ico" type="image/x-ico" />
    <asset:stylesheet src="home.css"/>
</head>
<body>
    <div class="main ui container">
        <g:form class="ui form" id="login-form" name="" url="">
            <div class="field">
                <label><g:message code="labels.username"/></label>
                <g:textField name="username"/>
            </div>
            <div class="field">
                <label><g:message code="labels.password"/></label>
                <g:passwordField name="password"/>
            </div>

            <g:submitButton class="ui button" name="login-button" value="${message(code: 'buttons.login')}"/>
        </g:form>
    </div>

</body>
</html>
