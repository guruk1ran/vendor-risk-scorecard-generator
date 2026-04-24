# Vendor Risk Scorecard Generator

# Vendor Risk Scorecard Generator (Backend)

## Overview
This project contains the core backend implementation of the **Vendor Risk Scorecard Generator** built using Spring Boot. It provides REST APIs for managing authentication, vendors, and scorecards, along with secure access and database integration.

---

## Features Implemented

- Spring Boot project setup with a proper folder structure  
- REST APIs for:
  - Authentication
  - Vendor management
  - Scorecard operations  
- JWT-based authentication and authorization  
- PostgreSQL and Redis integration using Docker  
- Flyway for database migration  
- Data seeder for demo users, vendors, and scorecards  
- Layered architecture:
  - Controller
  - Service
  - Repository  
- Basic exception handling  

---

## API Testing

All APIs have been successfully tested using:
- **curl**
- **Postman**

---

## The following enhancements are still pending:

### 1. Redis Caching
- Add `@Cacheable` for GET APIs  
- Add `@CacheEvict` for POST/PUT/DELETE APIs  

### 2. Role-Based Access Control
- Restrict APIs using `@PreAuthorize`  
- Example: Only `ADMIN` can create/update/delete  

---

## Tech Stack

- Java (Spring Boot)  
- PostgreSQL  
- Redis  
- Docker  
- Flyway  
- JWT (Authentication)  

---

## Project Status

Core backend implementation is completed.  
Further improvements (caching and role-based access) are planned.

---

## Contribution

Please review the implementation and share your feedback or any changes needed.

---

## Author

**Ullas G T**  
(Java Developer 1)