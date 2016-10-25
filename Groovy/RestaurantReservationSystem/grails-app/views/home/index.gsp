<!doctype html>
<html>
<head>
    <sec:ifAllGranted roles="ROLE_ADMIN">
        <meta name="layout" content="admin"/>
    </sec:ifAllGranted>

    <sec:ifAllGranted roles="ROLE_USER">
        <meta name="layout" content="user"/>
    </sec:ifAllGranted>

    <title>Home</title>

    <asset:stylesheet src="application.css"/>
    <asset:stylesheet src="semantic.css"/>
    <asset:stylesheet src="styles.css"/>

    <asset:javascript src="jquery-2.2.0.min.js"/>
    <asset:javascript src="semantic.js"/>
</head>
<body>
    <div class="ui container home">
        <div class="ui secondary pointing menu">
            <a class="item">Home</a>
            <a class="item">Messages</a>
            <a class="item active">Friends</a>
            <div class="right menu">
                <g:link url="[action: '', controller: 'logout']" class="ui item">Logout</g:link>
            </div>
        </div>
        <div class="ui segment">
            <p></p>
        </div>
    </div>
</body>
</html>
