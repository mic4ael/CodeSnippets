<!doctype html>
<html>
<head>
    <meta name="layout" content="home"/>
    <title>Home</title>
</head>
<body>
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
                    <tr data-user-id="${user.id}" data-href="${createLink(controller: 'users', action: 'update')}">
                        <td>${user.email}</td>
                        <td>${user.username}</td>
                        <td>
                            <g:if test="${user.enabled}">
                                <div class="ui toggle checkbox">
                                    <input class="toggle-user-state" type="checkbox" ${user.enabled ? 'checked' : ''}>
                                    <label></label>
                                </div>
                            </g:if>
                        </td>
                        <td>
                            <i class="remove user large link icon remove-user"
                               data-href="${createLink(mapping: 'userDelete', params: [id: user.id])}"></i>
                        </td>
                    </tr>
                </g:each>
            </tbody>
        </table>
    </div>
    <asset:javascript src="users.js"/>
</body>
</html>
