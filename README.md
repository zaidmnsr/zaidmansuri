# Microservices App


#### Below are components of Application.

  - User Interface 
  - API Gateway 
  - Authentication API 
  - Public Endpoints 
  - Internal APIs 
  - OAuthorization Server 
  - Long Running Workers/Jobs (~30mins) 
  - Queues (Like RabbitMQ, Bull, etc) 
  - Database 
  - Redis

#### Note: 

  > The Microservices backend Application is built on Java

  > UI (Frontend) is built on ReactJS


#### Below is Planned Strategy to implement above components of Application.

  - User Interface 
    [*Frontend Application in ReactJS and hosted on AWS S3 as static website and DNS can be mapped to AWS Cloudfront*]
  - API Gateway 
    [*AWS API Gateway service*]
  - Authentication API 
    [*AWS IAM to authenticate the API*]
  - Public Endpoints 
    [*AWS Ingress to route traffic inside kubernetes cluster*]
  - Internal APIs 
    [*Will be developed by development team for internal communication between microservices*]
  - OAuthorization Server 
    [*AWS Cognito*]
  - Long Running Workers/Jobs (~30mins) 
    [*Implement the application as type JOB in kubernetes manifests file and schedule to a separate node to avoid load on running server*]
  - Queues (Like RabbitMQ, Bull, etc) 
    [*Install redis on AWS EC2 machine. Preferrably on docker via docker-compose file. Allow Redis ports in security group to communicate with application*]
  - Database 
    [*Choice 1: MongoDB on AWS EC2 machine. Preferrably on docker via docker-compose file. Allow MongoDB ports in security group to communicate with application*
    *Choice 2: AWS DynamoDB. But this will require to segragate environments by creating schema*]
  - Redis 
    [*AWS Elasticache Service*]

### Objective 1

  - Strategy to follow for code collaboration should be *Feature Branch Workflow* 
  - Create separate branches for each features developed and naming should be *feature/<JIRA-ID>-Title-of-JIRA-assigned-to-develop-feature*
  - Create Pullrequest to merge feature in *dev* branch and delete the feature branch
  - Merge changes to *uat* branch after testing on dev branch
  - Merge changes to *prod* branch after uat testing and confirmation from Senior management/Lead
  - Deploy code to prod as per the release cycle

### Objective 2 

  - Setup Jenkins for CI/CD on AWS EC2 machine. Preferrably on docker via docker-compose file.
  - Create secret in Jenkins for AWS Access and Secret Key, AWS Docker registry credentials, Kubernetes config file, Sonar host URl, Slack url and server credentials
  - Create separate Declarative pipeline for each microservices to deploy in development environment.
  - Run Linting on Dockerfile
  - Run Maven Unit tests
  - Run Maven Dependency Vulnerability Analysis
  - Run Sonarqube analysis
  - Compile code
  - Create Docker Image
  - Scan Docker Image for vulnerabilities
  - Push Image to AWS ECR 
  - Deploy to k8s cluster

### Objective 3

  - UAT Deployment will be similar to dev environment ( Can remove Dev environment to reduce cost ). All tests mentioned above in *Objective 1* will be included in this pipeline. If planning to keep dev environment, then we can use Choice parameters in Jenkins to deploy to that environment.
  - Create a promotion job in jenkins to deploy the code to Staging and Production environment. Production deployment step will need approval to proceed. ( Staging and Production parameters will be handled by environment variables and Choice parameters inside Jenkins Job)
  - The Staging environment docker image will be the latest pushed in registry for UAT environment. Here it will be re-tagged to bifurcate for Staging environment.
  - The Production environment docker image will be latest pushed to registry for staging environment. Here it will be re-tagged to bifurcate for Production environment.
  - The instances/nodes running on staging should be destroyed after the production release cycle to save costs on Infra. ( Destruction of staging environment can be easily handled through Terraform )
  - Also Production k8s nodes and AWS EC2 instances should be reserved instances to save costs.

### Objective 4

  - For viewing logs of all 3 environments, we will use ELK ( ELastisearch Logstash Kibana) stack.
  - We will need to deploy filebeat as a sidecar container in microservices which will send logs to centralized server whcih is configured to Kibana dashboard.
  - Kibana dashboard will show the logs for all environments.

### Objective 5

  - For microservice monitoring we can deploy Prometheus and Grafana stack which will also monitor the Kubernetes cluster health
  - For alerts, we can configure slack, email, etc from Grafana dashboard
  - For AWS components we can use AWS Cloudwatch to configure alerts and monitor the utilization as well.

#### Extra Points 1

  - Increase in user traffic can be handled through ingress Application Loadbalancer
  - Also, can scale kubernetes pods based on custom metrics
  - Also can autoscale kubernetes node to accumulate the extra traffic

#### Extra Points 2

  - Above all strategy and deployment plan is based on AWS Cloud Services
