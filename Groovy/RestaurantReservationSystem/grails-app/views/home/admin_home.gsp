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
    <div id="management-actions">
        <button type="button" class="ui primary button edit-layout">
            <i class="edit icon"></i><g:message code="buttons.edit"/>
        </button>
        <button type="button" class="ui primary button add-table" style="display: none;">
            <i class="add circle icon"></i><g:message code="buttons.addtable"/>
        </button>
        <button type="button" class="ui primary button save-layout" style="display: none;">
            <i class="save circle icon"></i><g:message code="buttons.save"/>
        </button>
    </div>
    <div class="ui segment">
        <canvas id="canvas"></canvas>
    </div>
    <div class="ui small modal new-table-modal">
        <div class="header">
            <g:message code="header.newtable"/>
        </div>
        <div class="content">
            <form class="ui form new-table-form" onsubmit="return false;">
                <div class="field">
                    <label><g:message code="labels.numberofseats"/></label>
                    <input type="text" name="numberOfSeats" step="1">
                </div>
                <div class="field">
                    <label><g:message code="labels.tableshape"/></label>
                    <select class="ui fluid dropdown" name="tableShape">
                        <option value="Circle"><g:message code="labels.circle"/></option>
                        <option value="Rect"><g:message code="labels.rect"/></option>
                    </select>
                </div>
            </form>
        </div>
        <div class="actions">
            <div class="ui approve button"><g:message code="buttons.create"/></div>
            <div class="ui cancel button"><g:message code="buttons.cancel"/></div>
        </div>
    </div>

    <script>
        var URLS = {
            removeTable: function(tableId) {
                return "${createLink(mapping: 'tableManagement')}" + '/' + tableId;
            },
            tableManagement: function() {
                return "${createLink(mapping: 'tableManagement')}";
            }
        };
    </script>
    <asset:javascript src="dependencies/fabric.min.js"/>
    <asset:javascript src="admin.js"/>
</body>
</html>
