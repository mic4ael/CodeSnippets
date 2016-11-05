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
            var tableObject = evt.target;
            $('.reservation-modal').modal({
                onShow: function() {

                },
                onApprove: function() {

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
