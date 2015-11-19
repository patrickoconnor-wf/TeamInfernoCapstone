This will enable you to run your own Spring MVC server.
 

# What you need:
Maven: (you only need the binaries): http://maven.apache.org/download.cgi

Java

Once you install Maven, you need to set up environment variables. This website here goes through all of the steps on different operating systems 

http://www.tutorialspoint.com/maven/maven_environment_setup.htm

Once that is done, all you need to do is compile the project and run it. This can be done with the command

*mvn clean package*

And to run it you need the command

*java –jar target/team-inferno-spring-0.1.0.jar*

If everything works, you will be able to find your website at 
http://localhost:8080/index

If I missed anything or if you want more info about the individual files that make this server, you can go here
https://spring.io/guides/gs/serving-web-content/
