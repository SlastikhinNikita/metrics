# Metrics

Simple script based on psutils, wich show CPU and MEM stat.

## Getting Started

You must have python3 and psutil module.

### Prerequisites

Example for Debian/Ubuntu like systems

```
$ sudo apt-get install python3 python3-pip
$ pip install psutil
```

### Run

Run in console

```
$ python3 ./metrics PARAM
```

### Docker

Also you can use Docker container

```
$ docker pull slastikhin/metrics
$ docker run slastikhin/metrics PARAM
```


## PARAM and keys

PARAM:
mem - for display memory info
cpu - for display cpu info

Keys:
-p, --percpu - display non-one core CPU info (for each one CPU core)


## Authors

* **Slastikhin Nikita** - [SlastikhinNikita](https://github.com/SlastikhinNikita)


