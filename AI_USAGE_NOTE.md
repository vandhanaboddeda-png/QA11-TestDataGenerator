# AI_USAGE_NOTE

## Project Title

AI-Powered Test Data Generator with Constraints

## AI Tools Used

### 1. Google Gemini API

Used to generate synthetic customer test data based on user-defined constraints.

### 2. ChatGPT

Used for:

* Project planning
* Code guidance
* Documentation assistance
* Validation logic design
* Export generation support (JSON, CSV, SQL)

## How AI Was Used

The project uses Google's Gemini API to generate customer records according to specified constraints such as:

* Customer ID starting from 1
* Age between 18 and 60
* Gmail-only email addresses

The generated records are validated using custom Python validation logic and exported into multiple formats including JSON, CSV, and SQL.

AI assistance was also used during development to:

* Understand project requirements
* Design the project architecture
* Create documentation
* Develop and test code components

## Human Contributions

The team performed the following tasks:

* Requirement analysis
* Project design
* YAML schema creation
* Gemini API integration
* Validation implementation
* Testing and debugging
* Documentation preparation
* Final project submission

## Example Prompt Used

Generate 10 Indian customer records.

Use ONLY these fields:

* customer_id
* name
* age
* email

Rules:

* Customer ID should start from 1
* Age between 18 and 60
* Gmail addresses only

Return JSON only.

## Limitations

* Output quality depends on AI-generated responses.
* Internet connectivity is required for Gemini API access.
* The current implementation focuses on customer data generation only.
* Generated data is synthetic and intended for testing purposes.

## Ethical Considerations

The generated customer data is artificial and does not represent real individuals. The system is intended solely for software testing, QA validation, and educational purposes.
