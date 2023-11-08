package dev.vuongdang.dropwizard.resource

import dev.vuongdang.dropwizard.dto.HelloDto
import jakarta.ws.rs.*
import jakarta.ws.rs.core.MediaType

@Path("/hello")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
class HelloWorldResource {

    @GET
    fun sayHello(@QueryParam("name") name: String?): HelloDto {
        val message = if (name != null) "Hello, $name!" else "Hello World!"
        return HelloDto(message)
    }
}