package restaurantreservationsystem

class UrlMappings {
    static mappings = {
        "/$controller/$action?/$id?(.$format)?" {
            constraints {
                // apply constraints here
            }
        }

        "/" (controller: 'Home')
        "/register" (controller: 'Registration') {
            action = [GET: "index", POST: "create"]
        }
        "/users" (controller: 'Users', action: 'index')
        name(userDelete: "/users/$id" (controller: 'Users', action: 'delete', method: 'DELETE'))
        "500" (view: '/error')
        "404" (view: '/notFound')
    }
}
