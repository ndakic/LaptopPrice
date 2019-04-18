FROM openjdk:8
ADD target/original-server-api-0.0.1-SNAPSHOT.jar original-server-api.jar
EXPOSE 9005
ENTRYPOINT ["java", "-jar", "original-server-api.jar"]