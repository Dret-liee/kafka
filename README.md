in this repo I will show you how to work with kafka 

what is Kafka? and why we need it?
Kafka is a distributed streaming platform that is used to publish and subscribe to streams of records. 
It is an open-source software platform developed by the Apache Software Foundation written in Scala and Java.
Kafka is used for fault tolerant storage and replicates topic log partitions to multiple servers.
Kafka is designed to allow your apps to process records as they occur and handle real-time data feeds.

If you are interested in using Kafka, follow these steps:
first download kafka from this website --> https://kafka.apache.org/downloads
after you unzipped the kafka file you need to start zookeeper and kafa in your system
so open cmd and go to your kafka file directory then type this -->    .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
do not close the cmd!! open another cmd and go to your kafka file directory and type this -->    .\bin\windows\kafka-server-start.bat .\config\server.properties

after this your zookeeper and kafka server is running in your local system 
first run the producer file(you can find it in this repo) and let the kafka produce some messages then run the consumer file(you can find it in this repo)
check your database you can see the result.
