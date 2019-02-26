# 🚽

A scoring system for facilities visited at sites. Bring your own postgresQL DB. Written in Flask and DB Flash Alchemy to access PostgreSQL 11 data store

## How to use
The code is publicly there and a dockerfile is provided. Do not publish the docker image to a public repo with your database settings, use an environment variable (unpublished) or do not even publish publicly at all. why anyway ¯\_(ツ)_/¯

## What do I do for the DB?
Bring your connection string and replace with the redacted. The script needs a fully qualified connection string with conditions included, e.g. `postgres://db-user:db-password@db-hostname:5432/DBNAME?sslmode=require`

After that, in your environment, apply the configuration by executing (once 🙃) `dbsetup.py`

## What libraries?
Flask and Flask SQL Alchemy

## Where is the styling and other features?
On the way 🚂
