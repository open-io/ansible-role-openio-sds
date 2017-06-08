# Ansible role `openio-sds`

[![Build Status](https://travis-ci.org/cdelgehier/ansible-role-openio-sds.svg?branch=master)](https://travis-ci.org/cdelgehier/ansible-role-openio-sds)

An Ansible role for [OpenIO SDS](http://www.openio.io) Object Storage solution.  
Specifically, the responsibilities of this role are to:

- Configure the Openio SDS repository
- Generate the Puppet manifest for each servers
- Run the Puppet manifest

This role supports Centos 7 and Ubuntu 16.04 Xenial.

If you like/use this role, please consider giving it a star or reviewing it on Ansible Galaxy. Thanks!


## Requirements

No specific requirement

## Role Variables


| Variable      	| Default 					| Comments (type)  |
| :---          	| :---    					| :---             |
| `sds_version` 	| `16.10`     					| The SDS version to install |
| `openio_zk_cluster_ip`		| `['127.1.1.1', '127.2.2.2', '127.3.3.3']`	| List of IP addresses where to install the Zookeeper cluster (3 IPs min / 5 IPs max) |
| `conscience_ip`	| `'127.1.1.1'`					| IP address where to put the conscience service |
| `openio_redis_cluster_ip`		| `['127.1.1.1', '127.2.2.2', '127.3.3.3']`					| List os IP addresses of the Redis cluster |
| `openio_bootstrap`		| `false`					| Bootstrap the OpenIO namespace |


## Dependencies

No dependencies.

## Example Playbook

 [Docker](https://github.com/cdelgehier/ansible-role-openio-sds/blob/docker-tests/test.yml) test environment. See the section Testing for details.

## Testing

Tests are run using Docker. It is suitable for running automated tests on [Travis-CI](https://travis-ci.org/). Test code is kept in separate orphan branches. For details of how to set up these test environments on your own machine, see the README files in the respective branches:

- Docker: [docker-tests](https://github.com/cdelgehier/ansible-role-openio-sds/tree/docker-tests)

## Contributing

Issues, feature requests, ideas are appreciated and can be posted in the Issues section.

Pull requests are also very welcome. The best way to submit a PR is by first creating a fork of this Github project, then creating a topic branch for the suggested change and pushing that branch to your own fork. Github can then easily create a PR based on that branch.

## License

Apache License version 2.0

## Contributors

- [Cédric Delgehier](https://github.com/cdelgehier/) (maintainer)
- [Romain Acciari](https://github.com/racciari/)
