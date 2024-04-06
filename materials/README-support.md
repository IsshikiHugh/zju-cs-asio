# ZJU CS - All Sum in One!

[Page](https://isshikihugh.github.io/zju-cs-asio/) | [Repository](https://github.com/IsshikiHugh/zju-cs-asio)

## 介绍

本仓库目前主要以收集各类与 ZJU-CS 有关的网站形式的资料为主，具体分四大类：

1. 💎 由个人维护的个人笔记网站/博客网站等，可以了解到各个同学的具体学习经历和比较个人化的知识理解，不乏精品；
2. 🔮 由学生组织维护的教学资料网站等，相对来说范围更广，覆盖面更全，完成度更高，但多样性可能较差；
3. 🧲 课程组维护的教学资料网站等，如实验手册等，适合提前了解特定课程的相关内容；
4. 🎉 其他，例如个人整理的课程资料

出于一些原因，我并不打算在这个仓库中收集诸如课本、真题、大作业等可能引发一系列问题的资料，本仓库希望为各个相对来说更具有原创性的资料提供一个汇总、索引、引流的根入口。

（由于混计人数在混合班中基数较大，所以也收录了一部分 ckc 的资源。）

如果你喜欢这个项目，可以给这个项目一个 ⭐️；如果你发现项目中部分资源信息过时或有误（如链接失效、有更合适的描述等），又或者是你想分享更多的资源，请查看[贡献方法](#贡献方法)！

## 目录

- [ZJU CS - All Sum in One!](#zju-cs---all-sum-in-one)
  - [介绍](#介绍)
  - [目录](#目录)
  - [All-Sum-in-One](#all-sum-in-one)
  - [动机](#动机)
  - [贡献方法](#贡献方法)
  - [鸣谢 / 灵感来源](#鸣谢--灵感来源)
  - [许可](#许可)
  - [Star History](#star-history)


## All-Sum-in-One

> [!IMPORTANT]
>
> 注：仅按照大类进行排序，先后顺序并不暗示笔记质量！
>
> 另外，针对在 GitHub 仓库中访问的同学：由于 [Idea: Introduce new rule against use of target="_blank" on links](https://github.com/github/erblint-github/issues/26)，所以所有在 GitHub 仓库中访问链接直接点击都会导致直接在当前页跳转，所以如果你希望保留该页面，请使用 鼠标中键/三指/快捷键+左键 等方式访问链接。

<!-- ASIO-EMBED-HERE -->

## 动机

> [!NOTE]
>
> 这部分是一些碎碎念，对于仅希望来获取资源的同学可以跳过，当然你也可以选择停下脚步来一起听听故事！

2022 年 5 月的某一日，[xyx](https://github.com/smd1121) 一拍脑袋，拉着我和 [27rabbit](https://github.com/27rabbit-penguin)，决定一起搞一个在语雀上的[知识库](https://www.yuque.com/xianyuxuan/saltfish_shop)，按照 [xyx](https://github.com/smd1121) 自己的[说法](https://xuan-insr.github.io/%E4%B8%BB%E9%A1%B5/about/#%E5%85%B3%E4%BA%8E%E5%92%B8%E9%B1%BC%E8%82%86)：

> 在 2022 年 5 月，我们怀揣着创建一个计算机方面的知识 & 生涯树，以及将记笔记爱好者们联结起来的[愿景](https://www.yuque.com/xianyuxuan/saltfish_shop/weekly001_welcome)，创建了咸鱼肆。我们曾收集了大家的[课程笔记](https://www.yuque.com/xianyuxuan/saltfish_shop/course_res_index)，让大家[介绍自己和自己的知识库](https://www.yuque.com/xianyuxuan/saltfish_shop/intro)，并撰写了 24 期周报，分享自己所知道的内容。

但由于种种原因，我们放弃了周报的形式，也放弃了继续在语雀平台创作，一切陷入了一个短暂的静止。

某一天，我发现了 [xg](https://github.com/TonyCrane) 的基于 [MkDocs](https://www.mkdocs.org/) 的[笔记本](https://note.tonycrane.cc/)，突然意识到所谓的 docs 的组织结构，和我们在语雀上使用知识库搭建的笔记结构不是一样的吗，一边感叹于这种跳出思维定势的创意，我一边把 xg 的笔记分享给了 xyx。不久之后，xyx 也搭建了他的 MkDocs [笔记本](https://xuan-insr.github.io/)，然后我也搭了我的 MkDocs [笔记本](https://note.isshikih.top/)。慢慢的我发现，身边有越来越多的人加入到这个队伍中来，也看到越来越多的前辈、后辈产出优质的笔记。回想我自己写完笔记后希望自己的内容能给别人带来启发的想法，我决定把这些散落的星辰汇聚起。


## 贡献方法

首先 Fork 本仓库，然后使用下面两个方法之一来贡献你的资料，最后提交 PR 即可。


<details><summary>1. 使用 py 脚本一键导入（增加资源推荐这个方案）</summary>

<pre class="highlight">
  <code>python scripts/asio_helper.py <span class="nt">-a</span></code>
</pre>

然后根据提示输入相关信息即可。

</details>


<details><summary>2. 直接编辑 csv 文件（修正资源推荐这个方案）</summary>

直接编辑 <code>data.csv</code> 文件，按照 csv 文件格式在行末添加数据。

请确保你的数据格式和内容正确！（详细要求见下方“注意”。）

</details>


您可以使用如下命令来检查渲染后的结果以保证数据没有问题：

```bash
python scripts/asio_helper.py -r # The output will overwrite `README.md`.
```

**注意**：

1. 本项目仅仅收集资源链接，而不实际存储资源，**请勿提交资源文件**；
2. 请注意排版问题，包括但不限于：**中西文间加空格**，**描述末尾加句号**等；

如果发现项目中涉及的内容有误或链接失效等，可以直接修改 `data.csv` 中对应内容。

## 鸣谢 / 灵感来源

- [QSCTech/zju-icicles](https://github.com/QSCTech/zju-icicles)
- [timqian/chinese-independent-blogs](https://github.com/timqian/chinese-independent-blogs/tree/master)
- [SaltyfishShop/big_discusson](https://github.com/SaltyfishShop/big_discusson)

以及 Contributors：

<a href="https://github.com/IsshikiHugh/zju-cs-asio/graphs/contributors">
    <img width="550" src="https://contrib.rocks/image?repo=IsshikiHugh/zju-cs-asio" />
</a>

## 许可

本文档采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 协议进行许可，转载请注明出处。

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=IsshikiHugh/zju-cs-asio&type=Date)](https://star-history.com/#IsshikiHugh/zju-cs-asio&Date)



<details><summary>彩蛋</summary>

<img src="materials/img/stupid-isshikih.png">

</details>