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

        function toggleSelectability(selectable) {
            if (!selectable) {
                canvas.deactivateAll();
            }

            canvas.forEachObject(function(o) {
                o.selectable = selectable;
            });
        }

        function loadTablesFromJSON(tables) {
            var canvasConfig = {background: '', objects: []};
            for (var i = 0; i < tables.length; ++i) {
                canvasConfig.objects.push(tables[i]);
            }

            canvas.clear();
            canvas.loadFromJSON(canvasConfig, function() {
                toggleSelectability(false);
                canvas.renderAll();
            });
        }

        var canvas = new fabric.Canvas('canvas', {
            width: 1140,
            height: 580,
            selection: true
        });

        canvas.on('object:selected', function(evt) {

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
