<!doctype html>
<html>
<head>
    <meta name="layout" content="home"/>
    <title>Home</title>
</head>
<body>
    <div class="ui container home">
        <div class="ui secondary pointing menu">
            <g:link url="[action: 'index', controller: 'Home']" class="ui item">
                <g:message code="menu.items.home"/>
            </g:link>
            <g:link url="[action: 'index', controller: 'User']" class="ui item active">
                <g:message code="menu.items.users"/>
            </g:link>
            <a class="item"><g:message code="menu.items.reservations"/></a>
            <div class="right menu">
                <g:link url="[action: '', controller: 'logout']" class="ui item">
                    <g:message code="menu.items.logout"/>
                </g:link>
            </div>
        </div>
        <div class="ui">
            <table class="ui very padded table">
                <thead>
                    <tr>
                        <th>Adres email</th>
                        <th>Nazwa użytkownika</th>
                        <th>Enabled</th>
                    </tr>
                </thead>
                <tbody>
                    <g:each var="user" in="${users}">
                        <tr>
                            <td>${user.email}</td>
                            <td>${user.username}</td>
                            <td>${user.enabled}</td>
                        </tr>
                    </g:each>
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
