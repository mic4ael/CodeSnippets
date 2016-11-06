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
        <sec:ifAllGranted roles="ROLE_ADMIN">
            <g:link url="[action: 'index', controller: 'Users']" class="ui item ${controllerName == 'users' ? 'active' : ''}">
                <i class="users icon"></i>
                <g:message code="menu.items.users"/>
            </g:link>
        </sec:ifAllGranted>
        <g:link url="[controller: 'Reservations']" class="ui item ${controllerName == 'reservations' ? 'active' : ''}">
            <g:message code="menu.items.reservations"/>
        </g:link>
        <div class="right menu">
            <g:link url="[action: '', controller: 'logout']" class="ui item">
                <i class="sign out icon"></i>
                <g:message code="menu.items.logout"/>
            </g:link>
        </div>
    </div>
    <div id="reservations-list" class="ui">
        <table class="ui padded table">
            <thead>
                <tr>
                    <th><g:message code="labels.tableNo"/></th>
                    <th><g:message code="labels.reservationDate"/></th>
                    <th><g:message code="labels.firstName"/></th>
                    <th><g:message code="labels.lastName"/></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <g:each var="reservation" in="${reservations}">
                    <tr data-reservation-id="${reservation.id}">
                        <td>${reservation.reservedTable.id}</td>
                        <td>${reservation.reservedAt}</td>
                        <td>${reservation.firstName}</td>
                        <td>${reservation.lastName}</td>
                        <td>
                            <i class="large link icon remove cancel-reservation"
                               data-href="${createLink(mapping: 'reservationManagement', params: [id: reservation.id])}"></i>
                        </td>
                    </tr>
                </g:each>
            </tbody>
        </table>
    </div>
    <script>
        var URLS = {
            cancelReservation: function(reservationId) {
                return "${createLink(mapping: 'reservationManagement')}" + '/' + reservationId;
            }
        };
    </script>
    <asset:javascript src="reservations.js"/>
</body>
</html>
