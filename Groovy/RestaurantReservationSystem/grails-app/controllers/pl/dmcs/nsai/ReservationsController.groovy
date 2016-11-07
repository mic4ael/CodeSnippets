package pl.dmcs.nsai

import pl.dmcs.nsai.Reservation
import pl.dmcs.nsai.Table

import grails.converters.JSON
import grails.plugin.springsecurity.SpringSecurityUtils
import org.slf4j.Logger
import org.slf4j.LoggerFactory



class ReservationsController {
    Logger logger = LoggerFactory.getLogger(ReservationsController.class)

    def springSecurityService
    def wkhtmltoxService
    def mailService

    def get() {
        def reservations
        if (SpringSecurityUtils.ifAllGranted('ROLE_ADMIN')) {
            reservations = Reservation.list()
        } else {
            reservations = Reservation.findAllByCreatedBy(springSecurityService.currentUser)
        }
        return render(view: 'index', model: [reservations: reservations])
    }

    def create() {
        def data = request.JSON
        def table = Table.get(data.tableId)
        def response = [success: false]

        if (!table) {
            response.message = "There is no table with id: ${data.tableId}"
        } else {
            def reservationData = data.reservation
            def reservationDt = Date.parse('dd.MM.yyyy HH:mm', reservationData['reservation-dt'])
            def existingReservation = Reservation.findByReservedAt(reservationDt)

            if (existingReservation) {
                response.message = "There is already another reservation at ${reservationDt}"
            } else {
                def reservation = new Reservation(firstName: reservationData['first-name'], lastName: reservationData['last-name'],
                                                  phoneNumber: reservationData['phone-number'], createdAt: new Date(),
                                                  reservedAt: reservationDt)

                springSecurityService.currentUser.addToReservations(reservation).save(validate: false)
                table.addToReservations(reservation).save(validate: false, flush: true)
                sendConfirmationPDF(reservation)
                response.success = true
                response.message = "You have successfully booked the table"
            }
        }

        return render(response as JSON)
    }

    def sendConfirmationPDF(reservation) {
        def byte[] pdfData = wkhtmltoxService.makePdf(view: "pdf/confirmation", model: [reservation: reservation], header: "pdf/confirmation-header",
                                                      footer: "pdf/confirmation-footer", marginLeft: 20, marginTop: 35,
                                                      marginBottom: 20, marginRight: 20, headerSpacing: 10)
        mailService.sendMail {
            multipart(true)
            async(true)
            to(reservation.createdBy.email)
            subject("Confirmation of the reservation")
            attachBytes("PDF Attachment.pdf", "application/pdf", pdfData)
            text(g.message(code: 'messages.confirmation'))
        }
    }

    def delete() {
        def reservation = Reservation.get(params.id)
        def response = [success: false]

        if (reservation) {
            reservation.delete()
            response.success = true
            response.message = "You have successfully cancelled the reservation"
        } else {
            response.message = "There is no reservation with id ${params.id}"
        }

        return render(response as JSON)
    }
}
