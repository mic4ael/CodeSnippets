<!doctype html>
<html lang="en" class="no-js">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <title>
        <g:layoutTitle default="Grails"/>
    </title>

    <meta name="viewport" content="width=device-width, initial-scale=1"/>

    <asset:stylesheet src="application.css"/>
    <asset:stylesheet src="semantic.css"/>
    <asset:stylesheet src="styles.css"/>

    <asset:javascript src="jquery-2.2.0.min.js"/>
    <asset:javascript src="semantic.js"/>

    <g:layoutHead/>
</head>
<body>
    <div class="ui container home">
        <div class="ui secondary pointing menu">
            <g:link url="[action: 'index', controller: 'Home']" class="ui item ${controllerName == 'home' ? 'active' : ''}">
                <i class="home icon"></i>
                <g:message code="menu.items.home"/>
            </g:link>
            <sec:ifAllGranted roles="ROLE_ADMIN">
                <g:link url="[action: 'index', controller: 'Users']" class="ui item ${controllerName == 'users' ? 'active' : ''}">
                    <i class="users icon"></i>
                    <g:message code="menu.items.users"/>
                </g:link>
            </sec:ifAllGranted>
            <a class="item"><g:message code="menu.items.reservations"/></a>
            <div class="right menu">
                <g:link url="[action: '', controller: 'logout']" class="ui item">
                    <i class="sign out icon"></i>
                    <g:message code="menu.items.logout"/>
                </g:link>
            </div>
        </div>
        <g:layoutBody/>
    </div>
</body>
</html>
