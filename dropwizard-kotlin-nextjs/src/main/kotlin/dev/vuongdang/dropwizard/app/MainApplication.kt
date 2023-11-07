package dev.vuongdang.dropwizard.app

import dev.vuongdang.dropwizard.config.Config
import dev.vuongdang.dropwizard.resource.HelloWorldResource
import io.dropwizard.core.Application
import io.dropwizard.core.setup.Bootstrap
import io.dropwizard.core.setup.Environment

class MainApplication : Application<Config>() {

    override fun initialize(bootstrap: Bootstrap<Config>?) {
        // Initialization logic here
    }
    
    override fun run(configuration: Config, environment: Environment) {
        // Set up your resources, health checks, etc.
        environment.jersey().register(HelloWorldResource())
    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            MainApplication().run(*args)
        }
    }
}