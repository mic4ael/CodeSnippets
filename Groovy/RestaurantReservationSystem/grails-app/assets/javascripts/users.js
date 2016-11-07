(function() {
    $(document).ready(function() {
        $('#users-list .toggle-user-state').on('change', function() {
            var $this = $(this);
            $.ajax({
                url: $this.data('href'),
                data: JSON.stringify({enabled: $this[0].checked}),
                dataType: 'json',
                contentType: 'application/json',
                type: 'PUT',
                success: function(data) {
                    if (data.message) {
                        $.notify(data.message, data.success ? 'success' : 'error');
                    }
                }
            });
        });

        $('#users-list .remove-user').on('click', function(evt) {
            evt.preventDefault();

            var $this = $(this);
            $.ajax({
                url: $this.data('href'),
                type: 'DELETE',
                success: function(data) {
                    if (data.success) {
                        $this.closest('tr').remove();
                    }

                    if (data.message) {
                        $.notify(data.message, data.success ? 'success' : 'error');
                    }
                }
            });
        });
    });
})();
