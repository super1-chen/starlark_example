# 文档说明

本文档用来记录记录本人学习bazel和starlark的过程

## starlark

```shell
# 安装
go install go.starlark.net/cmd/starlark@latest
brew install starlark
# 使用， 快速验证starlark开发完成后的功能
starlark fib.star
```

## bazel python

这个地方比较坑爹

学习资源

1. [youtube](https://www.youtube.com/watch?v=8P3m1-U7v0k&list=PLdk2EmelRVLovmSToc_DK7F1DV_ZEljbx&index=2) 内容有些陈旧了好命令需要自己调整
2. [官网](https://github.com/bazel-contrib/rules_python/tree/main) 很多例子可以参考
3. [flask例子](https://github.com/alwaysprep/bazel-flask-example/blob/master/3rdparty/python/requirements.txt)


### 一些奇怪的地方

bazel 构建python需要提供完整依赖requirements.txt 可以通过的工具创建`pip-compile` 解析 `requirements.in` 导出 requirements.txt

```shell
pip-compile requirements.in
```

### bazel test 

bazel test project/calculator:calculator_test

这个`calculator_test.py`  需要加上 main 入口

```python

```