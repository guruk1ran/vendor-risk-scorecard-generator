# Vendor Risk Scorecard Generator

# 🚀 Vendor Risk Scorecard Generator (Backend)

## 📌 Overview
This project contains the backend implementation of the **Vendor Risk Scorecard Generator** built using Spring Boot. It provides secure REST APIs for managing authentication, vendors, and scorecards with database integration and caching support.

---

## ✅ Features Implemented

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
- Global exception handling  

---

## 🔐 Security

- JWT-based authentication  
- Role-based access control using `@PreAuthorize`  
- Method-level security enabled using `@EnableMethodSecurity`  
- Secured APIs require Bearer Token  

---

## ⚡ Caching

- Redis caching implemented using:
  - `@Cacheable` for GET APIs  
  - `@CacheEvict` for POST/PUT/DELETE APIs  

---

## 🧪 Testing

- Unit and controller test cases implemented  
- Testing frameworks used:
  - `@WebMvcTest`
  - Mockito  
- Test execution:
```bash
mvn test