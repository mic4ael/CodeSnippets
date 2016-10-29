(function() {
    $(document).ready(function() {
        $('#users-list .toggle-user-state').on('click', function(evt) {
            evt.preventDefault();

            var $this = $(this);
            $.ajax({
                url: $this.data('href'),
                type: 'PATCH',
                success: function(data) {
                    console.log(data)
                }
            })
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
                }
            });
        });
    });
})();
