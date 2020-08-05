Run docker image:
  given:
    python version: 3.7.0
    setup: |
      from hitchdocker import DockerImage
      
      image = DockerImage("../Dockerfile_echo", "test")
    files:
      Dockerfile_echo: |
        FROM alpine:3.7
        ENTRYPOINT ["echo"]
  steps:
  - run: image.ensure_built()
  - run: 
      code: print(image.run("hello").output())
      will output: hello
