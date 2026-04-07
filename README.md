Charity & Fundraiser Platform with MongoDB:
A MongoDB database project demonstrating collection management, schema validation, and data integrity enforcement for a charity and fundraiser platform.

Overview:
This project explores MongoDB's core features — collection lifecycle management, JSON Schema validation, and dynamic rule modification — applied to a real-world charity platform use case involving campaigns, donations, and volunteers.

Collections:
CollectionDescriptioncampaignsFundraiser campaign data with required fields and type validationdonationsDonor records with enum, range, and pattern constraintsvolunteersVolunteer data with role restrictions and ID format validation

Experiment 1: Basic Collection Operations:

Create a collection using db.createCollection()
List all collections with show collections
Drop a collection using db.collection.drop()

jsdb.createCollection("temp_campaigns")
show collections
db.temp_campaigns.drop()

Experiment 2: Schema Validation Setup:
Create a campaigns collection with a JSON Schema validator enforcing required fields and BSON types.
Required fields: campaignTitle, campaignId, organizationName
jsdb.createCollection("campaigns", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["campaignTitle", "campaignId", "organizationName"],
      properties: {
        campaignTitle:    { bsonType: "string" },
        campaignId:       { bsonType: "string" },
        organizationName: { bsonType: "string" },
        goalAmount:       { bsonType: ["double", "null"] },
        isActive:         { bsonType: "bool" }
      }
    }
  }
})
Valid insert:
jsdb.campaigns.insertOne({
  campaignTitle: "Clean Water for All",
  campaignId: "CMP2025001",
  organizationName: "AquaHope NGO",
  goalAmount: 500000.5,
  isActive: true
})
Invalid insert  — missing campaignId causes rejection:
jsdb.campaigns.insertOne({
  campaignTitle: "Feed the Children",
  organizationName: "HopeFoundation"
})

Experiment 3: Advanced Validation Rules
The donations collection enforces:

String length — donor name: 3–100 characters
Enum constraints — donation category restricted to predefined values
Range checks — amount > 50, units ≥ 1
Pattern matching — transaction ID must match ^TXN[A-Z0-9]{8}$

Valid insert:
jsdb.donations.insertOne({
  donorName: "Priya Sharma",
  donationCategory: "Medical Aid",
  amount: 7500.0,
  unitsReceived: NumberInt(10),
  transactionId: "TXN123456AB"
})
Invalid insert  — "Sports" not in enum, transactionId missing:
jsdb.donations.insertOne({
  donorName: "Arjun Mehta",
  donationCategory: "Sports",
  amount: 1000.1,
  unitsReceived: NumberInt(5)
})

Experiment 4: Modifying Existing Collections:
Use collMod to add validation rules to an existing collection without dropping and recreating it — ideal for production/legacy systems.
jsdb.createCollection("volunteers")

db.runCommand({
  collMod: "volunteers",
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["volunteerId", "fullName", "role", "hoursCommitted"],
      properties: {
        volunteerId:    { bsonType: "string", pattern: "^VOL[0-9]{5}$" },
        fullName:       { bsonType: "string", minLength: 3 },
        role:           { enum: ["Field Worker", "Coordinator", "Fundraiser", "Medical Staff"] },
        hoursCommitted: { bsonType: "double", minimum: 1.0 }
      }
    }
  },
  validationLevel: "moderate"
})

Tip: validationLevel: "moderate" enforces rules on new inserts while allowing updates to existing documents that pre-date the validator.


Experiment 5: Viewing Validation Rules:
Inspect the validation rules applied to any collection using getCollectionInfos():
jsdb.getCollectionInfos({ name: "donations" })
db.getCollectionInfos({ name: "volunteers" })
This returns metadata including the full validator schema, creation options, and indexes — useful for verifying correct implementation and troubleshooting.
