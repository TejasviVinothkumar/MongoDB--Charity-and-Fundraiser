Charity & Fundraiser Platform with MongoDB
This project demonstrates the design and implementation of a Charity and Fundraiser Platform using MongoDB. It focuses on core database operations, schema validation, and data integrity techniques required to build a reliable backend for managing campaigns, donations, and volunteers.

Based on a structured set of experiments, this repository showcases how MongoDB can be effectively used to enforce rules, validate data, and manage collections in a real-world application. 


Project Overview
The system simulates a platform where:

Organizations can create fundraising campaigns

Donors can contribute to causes

Volunteers can participate in activities

Data integrity is maintained using validation rules

Experiments Covered
Experiment 1: Basic Collection Operations
Creation of collections using db.createCollection()

Viewing collections using show collections

Dropping collections using .drop()

Key Learning:

Understanding the lifecycle of MongoDB collections

Managing temporary and permanent data storage

Experiment 2: Schema Validation Setup
Implementation of schema validation using $jsonSchema

Enforcing required fields such as:

campaignTitle

campaignId

organizationName

Data type validation for fields like:

goalAmount

isActive

Key Learning:

Ensuring data consistency at the database level

Preventing invalid or incomplete data entry

Experiment 2 (Continued): Document Validation
Valid Insert
Documents with all required fields and correct data types are successfully inserted

Invalid Insert
Documents missing required fields are rejected by MongoDB

Key Learning:

MongoDB automatically enforces schema rules

Invalid data is blocked before entering the system

Experiment 3: Advanced Validation Rules
Advanced constraints implemented include:

String length validation

Enum constraints (restricted categories)

Range checks (minimum donation amounts)

Pattern matching (transaction ID format)

Validation in Action:
Valid documents pass all constraints

Invalid documents fail due to:

Incorrect enum values

Missing required fields

Key Learning:

Strong validation improves data quality

Complex rules can be enforced efficiently

Experiment 4: Modifying Existing Collections
Use of collMod command to add validation rules to existing collections

No need to drop and recreate collections

Steps:

Create collection

Apply validation using collMod

Set validation level (strict or moderate)

Key Learning:

Enables updates in production systems without data loss

Supports backward compatibility

Experiment 5: Viewing Validation Rules
Use of db.getCollectionInfos() to inspect collection metadata

Key Learning:

Verify if validation rules are correctly applied

Useful for debugging and auditing

Technologies Used
MongoDB

MongoDB Shell (mongosh)

Key Features
Schema-based validation using JSON Schema

Prevention of invalid data insertion

Advanced rule enforcement (patterns, enums, ranges)

Ability to modify existing collections

Easy verification of validation rules

Use Case
This project can serve as a backend foundation for:

Fundraising platforms

Donation management systems

NGO campaign tracking systems

Conclusion
This project demonstrates how MongoDB can be used beyond simple data storage by incorporating validation and structured schema design. The experiments collectively show how to build a robust and reliable database layer for real-world applications.




