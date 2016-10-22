package restaurantreservationsystem

class UrlMappings {
    static mappings = {
        "/$controller/$action?/$id?(.$format)?" {
            constraints {
                // apply constraints here
            }
        }

        "/" (controller: 'Home')
        "/register" (controller: 'Registration')
        "500" (view: '/error')
        "404" (view: '/notFound')
    }
}
