#!/bin/bash

docker build ./Applications/Operators/toy_example_classifier \
  -f ./Applications/Operators/toy_example_classifier/Dockerfile \
  --tag warvito/toy-example-classifier-airflow:v1

docker push warvito/toy-example-classifier-airflow:v1


docker build ./Applications/Operators/preprocessing_2d_image \
  -f ./Applications/Operators/preprocessing_2d_image/Dockerfile \
  --tag warvito/preprocessing-airflow:v1

docker push warvito/preprocessing-airflow:v1