# Skylaunch 🚀

A full-stack AWS deployment project built to demonstrate real-world cloud engineering skills.

## What it does
A Flask web app containerised with Docker, deployed on EC2 inside a custom VPC, with a PostgreSQL RDS database, Nginx reverse proxy, SSL, and a custom domain via Route 53.

## Tech Stack
- **App:** Python / Flask
- **Database:** PostgreSQL (AWS RDS)
- **Containerisation:** Docker / Docker Compose
- **Infrastructure:** Terraform
- **CI/CD:** GitHub Actions
- **Cloud:** AWS (EC2, ECR, RDS, VPC, IAM, ACM, Route 53)

## Project Structure
```
skylaunch/
├── app/          # Flask application
├── terraform/    # Infrastructure as code
└── .github/
    └── workflows/ # CI/CD pipelines
```

## Stages
- [ ] Flask app + Dockerise
- [ ] Push image to ECR
- [ ] Launch EC2 in VPC
- [ ] RDS PostgreSQL setup
- [ ] Deploy with Docker Compose + Nginx
- [ ] SSL + custom domain
- [ ] Terraform everything
- [ ] GitHub Actions CI/CD
- [ ] Break and fix troubleshooting guide