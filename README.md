# otctf/env 
---

## 简要说明

本 `repo` 为 [`otctf/env`](https://hub.docker.com/r/otctf/env) 的维护工程，其主要为 `ctf` 比赛提高各种相关的环境， 可以请搭配 `playground` 工程一起来使用

目前维护的主要对象是 `template\Dockerfile.j2` ，其构成了所有`Docker Image tag` 的模板。

## Tag 说明

- `all-14.04`
	- 提供基于 `ubuntu-14.04` 的『尽可能全』的通用环境
	- 是唯一一个安装了 `php5` 及相关工具的环境
	- 部分工具缺失，主要原因是对 `ruby` 版本的依赖
- `all-16.04`
	- 提供基于 `ubuntu-16.04` 的通用环境
- `all-18.04`
	- 提供基于 `ubuntu-18.04` 的通用环境
- `sagemath`
	- 提供基于 [`sagemath/sagemath`](https://hub.docker.com/r/sagemath/sagemath/) 的通用环境，其基于 `ubuntu-16.04`
- `keras`
  - 提供基于 [`gw000/keras`](https://hub.docker.com/r/gw000/keras/) 的通用环境，其基于 `debain 9.3`