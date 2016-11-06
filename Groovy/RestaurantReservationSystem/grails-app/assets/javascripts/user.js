(function() {
    $(document).ready(function() {
        fabric.Object.prototype.toObject = (function (toObject) {
            return function () {
                return fabric.util.object.extend(toObject.call(this), {
                    numberOfSeats: this.numberOfSeats,
                    tableId: this.tableId
                });
            };
        })(fabric.Object.prototype.toObject);

        function toggleSelectability() {
            canvas.deactivateAll();
            canvas.forEachObject(function(o) {
                o.selectable = false;
            });
        }

        function loadTablesFromJSON(tables) {
            var canvasConfig = {background: '', objects: []};
            for (var i = 0; i < tables.length; ++i) {
                canvasConfig.objects.push(tables[i]);
            }

            canvas.clear();
            canvas.loadFromJSON(canvasConfig, function() {
                toggleSelectability();
                canvas.renderAll();
            });
        }

        var canvas = new fabric.Canvas('canvas', {
            width: 1140,
            height: 580,
            selection: true
        });

        canvas.on('mouse:down', function(evt) {
            var tableObject = evt.target,
                $form = $('.reservation-modal .new-reservation-form');

            if (!tableObject || !tableObject.tableId) {
                return;
            }

            $('.reservation-modal').modal({
                onShow: function() {

                },
                onApprove: function() {
                    var reservationData = {};

                    $.each($form.serializeArray(), function() {
                        reservationData[this.name] = this.value;
                    });

                    $.ajax({
                        type: 'POST',
                        url: URLS.reservationManagement(),
                        data: JSON.stringify({tableId: tableObject.tableId, reservation: reservationData}),
                        dataType: 'json',
                        contentType: 'application/json',
                        success: function(data) {
                            $form[0].reset();
                        }
                    });
                }
            }).modal('show');
        });

        $.ajax({
            url: URLS.tableManagement(),
            type: 'GET',
            success: function(data) {
                loadTablesFromJSON(data);
            }
        });
    });
})();
