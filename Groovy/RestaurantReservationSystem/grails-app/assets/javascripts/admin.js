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

            canvas.selection = selectable;
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
            selection: false
        });

        $.ajax({
            url: $('#canvas').data('href'),
            type: 'GET',
            success: function(data) {
                loadTablesFromJSON(data);
            }
        });

        $('#management-actions .add-table').on('click', function(evt) {
            evt.preventDefault();

            $('.ui.new-table-modal').modal({
                onApprove: function() {
                    var $this = $(this),
                        $form = $this.find('form.new-table-form'),
                        formData = $form.serializeArray(),
                        tableType = formData[1].value,
                        numberOfSeats = parseInt(formData[0].value) || 1,
                        group = new fabric.Group([], {
                            top: 100,
                            left: 100,
                            stateProperties: ['numberOfSeats'],
                            numberOfSeats: numberOfSeats
                        });

                    if (tableType == 'Circle') {
                        fabric.Image.fromURL('/assets/circle-table.png', function(img) {
                            group.addWithUpdate(img);
                            group.setCoords();
                            canvas.renderAll();
                        }, {height: 70, width: 100});
                    } else if (tableType == 'Rect') {
                        fabric.Image.fromURL('/assets/rect-table.png', function(img) {
                            group.addWithUpdate(img);
                            group.setCoords();
                            canvas.renderAll();
                        }, {height: 50, width: 100});
                    }

                    canvas.add(group);
                    canvas.renderAll();
                }
            }).modal('show');
        });

        var $editLayoutBtn = $('#management-actions .edit-layout'),
            $saveLayoutBtn = $('#management-actions .save-layout'),
            $addTableBtn = $('#management-actions .add-table');

        $editLayoutBtn.on('click', function(evt) {
            evt.preventDefault();

            $(this).hide();
            $addTableBtn.show();
            $saveLayoutBtn.show();
            toggleSelectability(true);
        });

        $saveLayoutBtn.on('click', function(evt) {
            evt.preventDefault();

            var $this = $(this);
            $.ajax({
                url: $this.data('href'),
                type: 'POST',
                data: JSON.stringify(canvas),
                dataType: 'json',
                contentType: 'application/json',
                success: function(data) {
                    $this.hide();
                    $addTableBtn.hide();
                    $editLayoutBtn.show();
                    loadTablesFromJSON(data);
                    toggleSelectability(false);
                }
            });
        });
    });
})();
