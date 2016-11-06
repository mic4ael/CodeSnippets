(function() {
    $(document).ready(function() {
        $('#reservations-list .cancel-reservation').on('click', function(evt) {
            evt.preventDefault();

            var $this = $(this);
            $.ajax({
                url: URLS.cancelReservation($this.closest('tr').data('reservation-id')),
                type: 'DELETE',
                success: function(data) {
                    if (data.success) {
                        $this.closest('tr').remove();
                    }
                }
            })
        })
    });
})();
