<!doctype html>
<html>
<head>
    <meta name="layout" content="home"/>
    <title>Home</title>
</head>
<body>
    <div class="ui secondary pointing menu">
        <g:link url="[action: 'index', controller: 'Home']" class="ui item ${controllerName == 'home' ? 'active' : ''}">
            <i class="home icon"></i>
            <g:message code="menu.items.home"/>
        </g:link>
        <g:link url="[action: 'index', controller: 'Users']" class="ui item ${controllerName == 'users' ? 'active' : ''}">
            <i class="users icon"></i>
            <g:message code="menu.items.users"/>
        </g:link>
        <a class="item"><g:message code="menu.items.reservations"/></a>
        <div class="right menu">
            <g:link url="[action: '', controller: 'logout']" class="ui item">
                <i class="sign out icon"></i>
                <g:message code="menu.items.logout"/>
            </g:link>
        </div>
    </div>
    <div class="ui segment">
        <canvas id="canvas"></canvas>
        <div class="row">

        </div>
    </div>

    <asset:javascript src="dependencies/fabric.min.js"/>
    <asset:javascript src="home.js"/>
</body>
</html>
