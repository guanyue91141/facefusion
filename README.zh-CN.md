FaceFusion
==========

> 行业领先的面部操作平台。

[![构建状态](https://img.shields.io/github/actions/workflow/status/facefusion/facefusion/ci.yml.svg?branch=master)](https://github.com/facefusion/facefusion/actions?query=workflow:ci)
[![覆盖率状态](https://img.shields.io/coveralls/facefusion/facefusion.svg)](https://coveralls.io/r/facefusion/facefusion)
![许可证](https://img.shields.io/badge/license-OpenRAIL--AS-green)


预览
-------

![预览](https://raw.githubusercontent.com/facefusion/facefusion/master/.github/preview.png?sanitize=true)


安装
------------

请注意，[安装](https://docs.facefusion.io/installation) 需要一定的技术技能，不推荐初学者尝试。如果您不习惯使用终端，我们的 [Windows 安装程序](http://windows-installer.facefusion.io) 和 [macOS 安装程序](http://macos-installer.facefusion.io) 可以帮助您快速入门。


用法
-----

运行命令：

```
python facefusion.py [commands] [options]

options:
  -h, --help                                      显示此帮助信息并退出
  -v, --version                                   显示程序版本号并退出

commands:
    run                                           运行程序
    headless-run                                  以无头模式运行程序
    batch-run                                     以批处理模式运行程序
    force-download                                强制自动下载并退出
    benchmark                                     对程序进行基准测试
    job-list                                      按状态列出任务
    job-create                                    创建草稿任务
    job-submit                                    提交草稿任务使其成为排队任务
    job-submit-all                                提交所有草稿任务使其成为排队任务
    job-delete                                    删除草稿、排队、失败或已完成的任务
    job-delete-all                                删除所有草稿、排队、失败和已完成的任务
    job-add-step                                  向草稿任务添加步骤
    job-remix-step                                从草稿任务中重新混合上一步骤
    job-insert-step                               向草稿任务插入步骤
    job-remove-step                               从草稿任务中移除步骤
    job-run                                       运行排队任务
    job-run-all                                   运行所有排队任务
    job-retry                                     重试失败的任务
    job-retry-all                                 重试所有失败的任务
```


文档
-------------

阅读[文档](https://docs.facefusion.io) 以深入了解。
