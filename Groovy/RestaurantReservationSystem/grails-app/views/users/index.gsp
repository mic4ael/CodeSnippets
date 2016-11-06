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
        <g:link url="[action: 'get', controller: 'Reservations']" class="ui item ${controllerName == 'reservations' ? 'active' : ''}">
            <g:message code="menu.items.reservations"/>
        </g:link>
        <div class="right menu">
            <g:link url="[action: '', controller: 'logout']" class="ui item">
                <i class="sign out icon"></i>
                <g:message code="menu.items.logout"/>
            </g:link>
        </div>
    </div>
    <div id="users-list" class="ui">
        <table class="ui padded table">
            <thead>
                <tr>
                    <th><g:message code="labels.email"/></th>
                    <th><g:message code="labels.username"/></th>
                    <th><g:message code="labels.enabled"/></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <g:each var="user" in="${users}">
                    <tr data-user-id="${user.id}">
                        <td>${user.email}</td>
                        <td>${user.username}</td>
                        <td>
                            <div class="ui toggle checkbox">
                                <input class="toggle-user-state" type="checkbox" ${user.enabled ? 'checked' : ''}
                                       data-href="${createLink(mapping: 'userManagement', params: [id: user.id])}">
                                <label></label>
                            </div>
                        </td>
                        <td>
                            <i class="remove user large link icon remove-user"
                               data-href="${createLink(mapping: 'userManagement', params: [id: user.id])}"></i>
                        </td>
                    </tr>
                </g:each>
            </tbody>
        </table>
    </div>
    <asset:javascript src="users.js"/>
</body>
</html>
