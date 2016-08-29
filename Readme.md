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

## Running your Pyret Program
Unfortunately, this requires some copying, similar to compiling.
If we mount the directory containing the executable to `/opt/src`,
then we can't find the output file.
If we mount to `/pyret-lang`, then we mask and can't find `requirejs`.

## Troubleshooting
Remember to start the docker daemon:
```
sudo systemctl start docker
```

You might need to add your user to the docker group,
but I prefer to use sudo as explained in this article:
<link>http://www.projectatomic.io/blog/2015/08/why-we-dont-let-non-root-users-run-docker-in-centos-fedora-or-rhel/</link>

### Path must be a string
Try a different version of Node.
Version `5.10.1` works for sure.
