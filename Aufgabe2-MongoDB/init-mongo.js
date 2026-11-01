// Create "testdb" database
db = db.getSiblingDB('testdb');

// Insert some referenced data
db.users.insertMany([
    { _id: "1", name: 'Robin Windey', email: 'ro.windey@gmail.com' },
    { _id: "2", name: 'Kevin Kiefer', email: 'kevin@example.com' },
    { _id: "3", name: 'Another User', email: 'another.email@gmail.com' }
]);

db.orders.insertMany([
    { user_id: "1", product: 'Laptop', amount: 1299.99 },
    { user_id: "2", product: 'Mouse', amount: 29.99 },
    { user_id: "1", product: 'Keyboard', amount: 89.99 },
    { user_id: "3", product: 'Monitor', amount: 199.99 }
]);

// Insert some embedded data
db.embeddedUsers.insertMany([
    {
        name: 'Robin Windey',
        email: 'ro.windey@gmail.com',
        orders: [
            { product: 'Laptop', amount: 1299.99 },
            { product: 'Keyboard', amount: 89.99 }
        ]
    },
    {
        name: 'Kevin Kiefer',
        email: 'kevin@example.com',
        orders: [
            { product: 'Mouse', amount: 29.99 }
        ]
    }
]);
