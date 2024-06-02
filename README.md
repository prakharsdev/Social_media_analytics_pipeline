# Social Media Analytics Pipeline

This project demonstrates a data pipeline for collecting, transforming, and analyzing social media data using Snowflake, DBT, Airflow, and Docker, with X (Twitter) as a data source.

## Project Structure

- `airflow/`: Contains Airflow DAGs and configuration.
- `dbt/`: Contains DBT models and configurations.
- `scripts/`: Contains the Python script to fetch tweets.
- `docker-compose.yml`: Docker Compose file to set up the project environment.
- `Dockerfile`: Dockerfile to build the environment.

## Setup Instructions

1. Clone the repository.

2. Create a `.env` file in the root of your project directory with the following content:

    ```env
    TWITTER_API_KEY=<your_twitter_api_key>
    TWITTER_API_SECRET_KEY=<your_twitter_api_secret_key>
    TWITTER_ACCESS_TOKEN=<your_twitter_access_token>
    TWITTER_ACCESS_TOKEN_SECRET=<your_twitter_access_token_secret>
    SNOWFLAKE_USER=<your_snowflake_user>
    SNOWFLAKE_PASSWORD=<your_snowflake_password>
    SNOWFLAKE_ACCOUNT=<your_snowflake_account>
    SNOWFLAKE_WAREHOUSE=<your_snowflake_warehouse>
    SNOWFLAKE_DATABASE=<your_snowflake_database>
    SNOWFLAKE_SCHEMA=<your_snowflake_schema>
    ```

3. Build the Docker images:
    ```sh
    docker-compose build
    ```

4. Start the Docker containers:
    ```sh
    docker-compose up
    ```

5. Access the Airflow web interface at `http://localhost:8080` and trigger the DAG `twitter_dag`.

6. Run DBT transformations:
    ```sh
    docker-compose run dbt run
    ```

## Tools Used

- **Twitter API**: For fetching raw tweet data.
- **Snowflake**: For data warehousing and analytics.
- **DBT**: For data transformation and modeling.
- **Airflow**: For workflow orchestration.
- **Docker**: For containerization and consistent deployment.


![SocialMediaAnalyticsPipeline](https://github.com/prakharsdev/Social_media_analytics_pipeline/assets/26145700/55e57b43-bbfe-41ca-bf1d-2a055849850e)
