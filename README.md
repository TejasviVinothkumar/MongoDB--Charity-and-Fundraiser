
# Charity & Fundraiser Application (MongoDB)

A MongoDB-based backend design for a Charity and Fundraiser application. This project demonstrates how to use collections, schema validation, and data integrity rules for managing fundraisers, donations, and volunteers.

---

## Project Overview

This application manages three core components:

* **Fundraisers** – Campaigns created to raise funds
* **Donations** – Contributions made by donors
* **Volunteers** – Individuals supporting campaigns

MongoDB is used with schema validation to ensure consistent and reliable data.

---

## Database Setup

```js
use charityDB
```

Creates or switches to the `charityDB` database.

---

## Collections and Schema Design

### 1. Fundraisers Collection

#### Create Collection

```js
db.createCollection("fundraisers", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["title", "organizer", "targetAmount"],
      properties: {
        title: { bsonType: "string" },
        organizer: { bsonType: "string" },
        targetAmount: { bsonType: "int" },
        isActive: { bsonType: "bool" }
      }
    }
  }
})
```

#### Example Insert

```js
db.fundraisers.insertOne({
  title: "Help Flood Victims",
  organizer: "NGO Trust",
  targetAmount: 50000,
  isActive: true
})
```

#### Invalid Insert (Fails)

```js
db.fundraisers.insertOne({
  title: "Education Support",
  targetAmount: 30000
})
```

---

### 2. Donations Collection

#### Create Collection with Strict Validation

```js
db.createCollection("donations", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["donorId", "name", "amount", "category"],
      properties: {
        donorId: {
          bsonType: "string",
          pattern: "^DON[0-9]{3}$"
        },
        name: {
          bsonType: "string",
          minLength: 3
        },
        amount: {
          bsonType: "double",
          minimum: 10,
          maximum: 100000
        },
        category: {
          enum: ["Medical", "Education", "Disaster", "Animal"]
        }
      }
    }
  },
  validationLevel: "strict",
  validationAction: "error"
})
```

#### Valid Insert

```js
db.donations.insertOne({
  donorId: "DON101",
  name: "Ravi",
  amount: 2500,
  category: "Medical"
})
```

#### Invalid Insert (Fails)

```js
db.donations.insertOne({
  donorId: "101",
  name: "A",
  amount: 5,
  category: "Food"
})
```

---

### 3. Volunteers Collection

#### Create Collection

```js
db.createCollection("volunteers")
```

#### Add Validation using `collMod`

```js
db.runCommand({
  collMod: "volunteers",
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["volunteerId", "name", "hours"],
      properties: {
        volunteerId: {
          bsonType: "string",
          pattern: "^VOL[0-9]{3}$"
        },
        name: {
          bsonType: "string",
          minLength: 3
        },
        hours: {
          bsonType: "int",
          minimum: 1
        }
      }
    }
  },
  validationLevel: "moderate"
})
```

---

## Utility Commands

#### Show Collections

```js
show collections
```

#### Drop Collection

```js
db.fundraisers.drop()
```

#### Get Collection Info

```js
db.getCollectionInfos({ name: "donations" })
```

---

## Validation Rules Summary

| Collection  | Validation Level | Purpose                          |
| ----------- | ---------------- | -------------------------------- |
| Fundraisers | Default          | Ensures required campaign fields |
| Donations   | Strict           | Enforces strong data integrity   |
| Volunteers  | Moderate         | Flexible validation for updates  |

---

## Key Features

* Schema validation using `$jsonSchema`
* Required fields enforcement
* Pattern-based ID validation (DONxxx, VOLxxx)
* Enum constraints for categories
* Data consistency and error prevention
* Support for scalable charity systems

---

## Use Cases

* NGO fundraising platforms
* Disaster relief donation systems
* Educational sponsorship programs
* Volunteer management systems

---

## Conclusion

This project demonstrates how MongoDB can be effectively used to build a structured and reliable backend for a charity and fundraising system. By applying validation rules, the application ensures high data quality and prevents invalid entries.



