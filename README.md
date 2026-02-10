# E-Commerce Backend Engineering 

## Project Description
This project is a **backend-first e-commerce system** designed to simulate a **real-world product catalog service**.  

Built as part of the **ALX ProDev Backend Engineering Program**, the project focuses on **scalability, security, clean architecture, background processing, containerization, and CI/CD** — mirroring how modern backend systems are designed and shipped in professional environments.

The system exposes well-documented REST APIs for frontend or third-party consumption and is structured to be easily deployable to production infrastructure.

The project follows a phased development approach starting with system design and progressing through implementation, testing, documentation, and deployment.

---

## Project details
A robust e-commerce backend API that provides:
- Secure user authentication using JWT
- CRUD operations for products and categories
- Product discovery features including filtering, sorting, and pagination
- A well-structured relational database optimized for performance
- Background task processing using message queues
- Comprehensive API documentation and testing workflows
- The system is designed to reflect real production backend systems and not just a demo application.

## Project Goals
- Design and optimize a relational database schema using PostgreSQL
- Build scalable and secure APIs using Django and Django REST Framework
- Implement filtering, sorting and pagination for large datasets
- Apply backend performance optimizations 
- Document APIs clearly using Swagger/OpenAPI
- Prepare the system for containerized deployment and CI/CD pipelines
- System Design


## Key Features

- JWT-based authentication (access & refresh tokens)
- Role-based permissions (admin write / public read)
- Products & categories management
- Inventory updates via background tasks (Celery)
- PostgreSQL relational database
- RabbitMQ message broker
- Dockerized development & deployment
- Automated CI with GitHub Actions
- Swagger (OpenAPI) documentation
- Rate-limited authentication endpoints

---

## Tech Stack

### Backend
- Python 3.12
- Django
- Django REST Framework

### Database & Messaging
- PostgreSQL
- RabbitMQ

### Background Tasks
- Celery

### Authentication & Security
- JWT (SimpleJWT)
- Role-based permissions
- Rate limiting (django-ratelimit)

### DevOps & Tooling
- Docker & Docker Compose
- GitHub Actions (CI)
- Swagger / OpenAPI (DRF Spectacular)
- Postman

---

## Architecture Overview

### High-Level Architecture

Client (Frontend / API Consumer)
|
v
Django REST API (JWT Auth, Permissions)
|
v
PostgreSQL (Primary Data Store)
|
v
Celery Workers <---- RabbitMQ (Message Broker)


- **Django REST API** handles all HTTP requests, authentication, and permissions
- **PostgreSQL** stores users, products, categories, and inventory data
- **Celery** processes background tasks (emails, inventory updates)
- **RabbitMQ** queues asynchronous jobs
- **Docker Compose** orchestrates all services

---

## Database Design (ERD)

The database schema is based on a carefully designed **Entity Relationship Diagram (ERD)** that defines the core domain models and their relationships.

### Core Entities
- User
- Category
- Product
- Order
- OrderItem

 ERD location: **alx-project-nexus/erd.png**


---

## API Documentation

### Swagger UI
Interactive API documentation is available via Swagger:
 http://localhost:8000/api/docs/

Features:
- Full endpoint listing
- Request/response schemas
- JWT authentication via **Authorize** button

---

## API Usage Instructions

### Authentication

#### Login
```http
POST /api/auth/login/

{
  "email": "user@example.com",
  "password": "StrongPassword123"
}

Refresh Token
POST /api/auth/refresh

Categories
| Method | Endpoint              | Access |
| ------ | --------------------- | ------ |
| GET    | /api/categories/      | Public |
| POST   | /api/categories/      | Admin  |
| PATCH  | /api/categories/{id}/ | Admin  |
| DELETE | /api/categories/{id}/ | Admin  |

Products
| Method | Endpoint            | Access |
| ------ | ------------------- | ------ |
| GET    | /api/products/      | Public |
| POST   | /api/products/      | Admin  |
| PATCH  | /api/products/{id}/ | Admin  |
| DELETE | /api/products/{id}/ | Admin  |


Supports
- Search
- Ordering
- Pagination



* Development Workflow (Docker only)
Start the project
docker-compose up -d

Run migrations
docker-compose exec web python manage.py migrate

Create superuser
docker-compose exec web python manage.py createsuperuser

Run tests
docker-compose exec web python manage.py test

**Important:**
This project is designed to run entirely inside Docker.
Do not run python manage.py runserver on the host machine.


CI/CD Pipeline

The project includes a GitHub Actions CI pipeline that runs on every push and pull request to main.

CI Features
PostgreSQL service
RabbitMQ service
Automated migrations
Test execution
Linting (flake8)
Formatting checks (black)


Security & Performance
JWT authentication with refresh tokens
Role-based access control
Rate limiting on authentication endpoints
Database indexing and query optimization
Background processing for non-blocking operations


Testing Strategy
Unit tests for models and serializers
Integration tests for API endpoints
Authentication & permission tests
Inventory and product behavior tests



Key Learnings
Designing scalable relational database schemas
Implementing secure JWT authentication flows
Managing background tasks with Celery and RabbitMQ
Dockerizing multi-service backend systems
Writing meaningful automated tests
Building CI pipelines for backend projects
Structuring production-ready Django applications



Challenges & Solutions
Docker Networking Issues
Problem: Database host resolution errors (db not found)
Solution: Enforced Docker-only workflow and consistent service naming

Asynchronous Task Reliability
Problem: Blocking operations affecting request performance
Solution: Offloaded inventory updates and emails to Celery workers

Authentication Security
Problem: Brute-force login risks
Solution: Implemented rate limiting on auth endpoints



Best Practices Applied
Separation of concerns
Environment-based configuration
Dockerized services
Automated testing & CI
Clear API documentation
Least-privilege access control
Production-oriented project structure


