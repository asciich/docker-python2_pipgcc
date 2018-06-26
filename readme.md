# python2_pipcc container

Provides Python2, pip and gcc based on alpine container. This container allows the installation of pip packages which need compilation.

For pure python packages the [asciich/python2_pip](https://hub.docker.com/r/asciich/python2_pip/) container can be used.

To run automatic tests against the container image use tox:

```bash
tox
```

