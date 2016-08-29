# Pyret Language Docker

## Building the Docker Image
```
sudo docker build -t pyret-compiler .
```

## Compiling your Pyret Program
```
sudo docker run --rm -v <absolute path to host directory>:<absolute path to docker directory>\
<docker image> <command>
```
### Example
```
sudo docker run --rm -v /home/john/src:/opt/src pyret-image pyretc test.arr -o a.out
```
## Troubleshooting
Remember to start the docker daemon:
```
sudo systemctl start docker
```

You might need to add your user to the docker group,
but I prefer to use sudo as explained in this article:
<link>http://www.projectatomic.io/blog/2015/08/why-we-dont-let-non-root-users-run-docker-in-centos-fedora-or-rhel/</link>
