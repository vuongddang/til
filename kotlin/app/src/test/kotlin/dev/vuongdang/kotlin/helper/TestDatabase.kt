package dev.vuongdang.kotlin.helper
import com.zaxxer.hikari.HikariConfig
import com.zaxxer.hikari.HikariDataSource
import dev.vuongdang.kotlin.entity.Users
import org.jetbrains.exposed.sql.Database
import org.jetbrains.exposed.sql.SchemaUtils
import org.jetbrains.exposed.sql.transactions.transaction
import org.testcontainers.containers.MySQLContainer

object TestDatabase {

    private val mySQLContainer: MySQLContainer<Nothing> = MySQLContainer<Nothing>("mysql:8.0.26").apply {
        withDatabaseName("test-db")
        withUsername("test-user")
        withPassword("test-password")
        start() // Start the container
    }

    init {
        val config = HikariConfig().apply {
            jdbcUrl = mySQLContainer.jdbcUrl
            username = mySQLContainer.username
            password = mySQLContainer.password
            driverClassName = "com.mysql.cj.jdbc.Driver"
            maximumPoolSize = 10
        }
        val dataSource = HikariDataSource(config)

        // This doesn't connect to the database but provides a descriptor for future usage
        // In the main app, we would do this on system start up
        // https://github.com/JetBrains/Exposed/wiki/Database-and-DataSource
        Database.connect(dataSource)

        // Create the schema
        transaction {
            SchemaUtils.create(Users)
        }
    }
}
