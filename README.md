# Session Cookie to Header Microservice (SCHM)

This microservice takes a session cookie from a request and adds its hash as a header. This allows sessions tracked via cookies to be used as the grouping device for Traefik ratelimiting middleware.

Don't use this unless you really need to, its a bit scuffed.
