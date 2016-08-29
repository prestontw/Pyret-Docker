# Pyret Language Docker

## Building the Docker Image
```
sudo docker build -t pyret-compiler .
```

## Compiling your Pyret Program
```
sudo docker run --rm -v <abs path to host dir>:opt/src pyret-compiler pyretc <file to compile>
```
### Example
```
sudo docker run --rm -v /home/john/src:/opt/src pyret-compiler pyretc test.arr -o a.out
```
## Troubleshooting
Remember to start the docker daemon:
```
sudo systemctl start docker
```

You might need to add your user to the docker group,
but I prefer to use sudo as explained in this article:
<link>http://www.projectatomic.io/blog/2015/08/why-we-dont-let-non-root-users-run-docker-in-centos-fedora-or-rhel/</link>

### Path must be a string
I have encountered this error all over this place.
It stops make from running,
and it finally has stopped compilation from working.
I will try to resolve it and see what happens.
