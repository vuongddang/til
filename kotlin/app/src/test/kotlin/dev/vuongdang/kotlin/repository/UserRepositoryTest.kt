package dev.vuongdang.kotlin.repository

import dev.vuongdang.kotlin.entity.User
import dev.vuongdang.kotlin.helper.TestDatabase
import org.jetbrains.exposed.sql.transactions.transaction
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.BeforeAll
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.TestInstance
import kotlin.test.assertNull

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class UserRepositoryTest {

    @BeforeAll
    fun setUp() {
        // Use the TestDatabase singleton to initialize the database
        TestDatabase
    }

    @Test
    fun crudUser() {
        transaction {
            // Create
            val newUser = User.new {
                name = "Alice"
            }

            // Read
            val retrievedUser = User.findById(newUser.id)
            assertEquals("Alice", retrievedUser?.name)

            // Update
            retrievedUser?.apply {
                name = "Bob"
            }

            val updatedUser = User.findById(newUser.id)
            assertEquals("Bob", updatedUser?.name)

            // Delete
            updatedUser?.delete()
            val deletedUser = User.findById(newUser.id)
            assertNull(deletedUser)
        }
    }
}