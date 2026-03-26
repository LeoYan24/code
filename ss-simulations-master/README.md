# SS_Simulations

# 介绍
《信号与系统Python实践》的配套代码
请勿直接使用本代码训练或微调AI模型，如需使用，请与作者联系
robinhou@bupt.edu.cn

# 软件架构

按照教材章节顺序组织代码

# 依赖的库
建议使用conda管理一个虚拟环境。
大多数库使用pip安装即可

1. sympy
2. numpy
3. scipy
4. matplotlib
5. wave
6. sounddevice
7. control

个别案例需要slycot（判断系统的可控制性和可观察性），该库的安装较为麻烦，建议使用conda环境安装（参考教材第八章），如果不做这个例子则不需要安装该库，也不必一定使用conda环境。

8. pillow
9. lcapy
（绘制电路图需要latex环境等，请参考lcapy官网或教材第六章）

# 使用说明

建议首先设置pip国内源（建立阿里源，清华源有的库有问题），再进行库的安装，理论上说只要是较新的版本都行，不需要特别指定版本

```bash
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
```

# 更新记录
## 2025.8.1
加入了更多案例，包括一些动画演示等

