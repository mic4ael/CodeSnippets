package pl.dmcs.nsai

import grails.converters.JSON

import pl.dmcs.nsai.Table

import org.slf4j.Logger
import org.slf4j.LoggerFactory


class TablesController {
    Logger logger = LoggerFactory.getLogger(TablesController.class)

    def getAll() {
        def response = []
        for (it in Table.list()) {
            def tableConfig = JSON.parse(it.config)
            tableConfig.tableId = it.id
            response << tableConfig
        }

        return render(response as JSON)
    }

    def create() {
        def data = request.JSON
        def response = []

        for (object in data.objects) {
            if (object.tableId) {
                def table = Table.get(object.tableId)
                response << JSON.parse(object.toString())
                object.remove('tableId')
                table.config = object.toString()
                table.save(flush: true)
            } else {
                def table = new Table(config: object.toString()).save(flush: true)
                object.tableId = table.id
                response << object
            }
        }

        return render(response as JSON)
    }

    def delete() {
        def tableId = params.id
        def table = Table.get(tableId)
        def response = [success: false]

        if (table) {
            table.delete()
            response.success = true
            response.message = 'Table has been removed'
        } else {
            response.message = 'Table with id ${tableId} does not exist'
        }

        return render(response as JSON)
    }
}
