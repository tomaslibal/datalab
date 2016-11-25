# datalab

    data lab / and labeller

## Purpose

Store data as datapoints and add labels to each datapoint. Datapoints can
be organized into different datasets and downloaded as labelled data.

## Entities

Each datapoint derives from an entity. Entity is a special type which
stores the data in a specific way.

### Image entity

When storing image data, this entity extracts the pixel array and stores
it in 3-tuples of RGB components.

![datapoints table screenshot](http://libal.eu/imghost/datalab_screen_0001.PNG)

## Installation

This is a Django project

### Requirements and dependencies

- Python 3.5.2+
- pip packages (see `requirements.txt`)

## Brief story

Datalab is a label manager for data (different entities are supported) 
with the export function of the data. The initial motivation for this 
project was the need to keep labelled training data organized for 
generating the input to train models in machine learning.

This is not the end.