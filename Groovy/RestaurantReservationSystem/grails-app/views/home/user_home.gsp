<!doctype html>
<html>
<head>
    <meta name="layout" content="home"/>

    <asset:javascript src="dependencies/jquery.datetimepicker.full.js"/>
    <asset:javascript src="dependencies/jquery.validate.js"/>

    <asset:stylesheet src="jquery.datetimepicker.min.css"/>
    <title>Home</title>
</head>
<body>
    <div class="ui secondary pointing menu">
        <g:link url="[action: 'index', controller: 'Home']" class="ui item ${controllerName == 'home' ? 'active' : ''}">
            <i class="home icon"></i>
            <g:message code="menu.items.home"/>
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
    <div class="ui segment">
        <canvas id="canvas"></canvas>
    </div>
    <div class="ui small modal reservation-modal">
        <div class="header">
            <g:message code="header.newreservation"/>
        </div>
        <div class="content">
            <form class="ui form new-reservation-form" onsubmit="return false;">
                <div class="field required">
                    <label><g:message code="labels.firstName"/></label>
                    <input type="text" name="first-name" required>
                </div>
                <div class="field required">
                    <label><g:message code="labels.lastName"/></label>
                    <input type="text" name="last-name" required>
                </div>
                <div class="field required">
                    <label><g:message code="labels.phoneNumber"/></label>
                    <input type="text" name="phone-number" required>
                </div>
                <div class="field required">
                    <label><g:message code="labels.reservationDate"/></label>
                    <input type="text" name="reservation-dt" required>
                </div>
            </form>
        </div>
        <div class="actions">
            <button class="ui approve button" disabled><g:message code="buttons.create"/></button>
            <button class="ui cancel button"><g:message code="buttons.cancel"/></button>
        </div>
    </div>
    <script>
        $('.reservation-modal .new-reservation-form').validate({
            rules: {
                'phone-number': {
                    required: true,
                    number: true
                }
            }
        });

        $('.reservation-modal input').on('change', function() {
            var enable = true,
                form = $('.reservation-modal .new-reservation-form'),
                approveBtn = $('.reservation-modal .ui.approve');

            $('.reservation-modal input').each(function() {
                var $this = $(this);
                if (!$this.val()) {
                    enable = false;
                }
            });

            enable = form.valid();
            if (enable) {
                approveBtn.removeAttr('disabled');
            } else {
                approveBtn.attr('disabled', 'disabled');
            }
        });

        $('.reservation-modal input[name=reservation-dt]').datetimepicker({
            format:'d.m.Y H:i',
            inline: true,
            lang: 'pl',
            defaultTime: '10:00',
            defaultDate: new Date(),
            minDate: new Date(),
            allowTimes: ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00']
        });

        var URLS = {
            tableManagement: function() {
                return "${createLink(mapping: 'tableManagement')}";
            },
            reservationManagement: function() {
                return "${createLink(mapping: 'reservationManagement')}";
            }
        };
    </script>

    <asset:javascript src="dependencies/fabric.min.js"/>
    <asset:javascript src="user.js"/>
</body>
</html>
