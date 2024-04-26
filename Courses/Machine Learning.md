# Embracing Domain Differences in Fake News: Cross-domain Fake News Detection using Multimodal Data

## Abstract

With the rapid evolution of social media, fake news has become a significant social problem, which cannot be addressed in a timely manner using manual investigation. This has motivated numerous studies on automating fake news detection. Most studies explore supervised training models with different modalities (e.g., text, images, and propagation networks) of news records to identify fake news. However, the performance of such techniques generally drops if news records are coming from different domains (e.g., politics, entertainment), especially for domains that are unseen or rarely-seen during training. As motivation, we empirically show that news records from different domains have significantly different word usage and propagation patterns. Furthermore, due to the sheer volume of unlabelled news records, it is challenging to select news records for manual labelling so that the domain-coverage of the labelled dataset is maximized. Hence, this work: (1) proposes a novel framework that jointly preserves domain-specific and cross-domain knowledge in news records to detect fake news from different domains; and (2) introduces an unsupervised technique to select a set of unlabelled informative news records for manual labelling, which can be ultimately used to train a fake news detection model that performs well for many domains while minimizing the labelling cost. Our experiments show that the integration of the proposed fake news model and the selective annotation approach achieves state-of-the-art performance for cross-domain news datasets, while yielding notable improvements for rarely-appearing domains in news datasets.

## Introduction

### Motivation

Social media is considered as one of the leading and fastest media to seek news information online. Thus, social media platforms provide an ideal environment to spread fake news

社交媒体被视为网络中获取新闻信息最快的渠道之一。因此，社交媒体平台为传播假新闻（即虚假信息）提供了一个非常理想环境。假新闻往往会造成大量损失，所以尽早发现并阻止此类信息的传播非常重要。

### Challenges

我们在改进这方面主要的挑战是什么呢，

首先，现有的大多数技术都是使用仅限于单个领域（如政治、娱乐、医疗保健）的数据集进行训练和评估的。然而，一个真实的新闻流通常涵盖了许多种类的领域。

其次，大多数虚假新闻检测技术在识别训练期间未见过或很少见过的领域的虚假新闻记录方面表现不佳。

作为解决方案，可以使用涵盖尽可能多领域的虚假新闻检测模型进行学习。

### Solution

要解决跨领域新闻数据集中的虚假新闻检测问题，需要考虑如何保留新闻记录中的领域特定知识和跨领域知识。

识别需要标注的信息性新闻记录，以便最终标记的数据集能够覆盖多个领域，同时避免任何选择偏差。

### Contributions

1. We propose a multimodal2 fake news detection technique for cross-domain news datasets that learns domain-specific and cross-domain information of news records using two independent embedding spaces, which are subsequently used to identify fake news records. Our experiments show that the proposed framework outperforms state-of-the-art fake news detection models by as much as 7.55% in F1-score.
2. We propose an unsupervised technique to select a given number of news records from a large data pool such that the selected dataset maximizes the domain coverage. By using such a dataset to train a fake news detection model, we show that the model achieves around 25% F1-score improvements for rarely-appearing domains in news datasets.

## Problem Statement

**数据集:**

- 每个记录 $r$ 由时间戳 $t^r$、文本内容 $W^r$ 和传播网络 $G^r$ 组成。
- 时间窗口 $\Delta T$ 为 5 小时，用于评估虚假新闻检测性能。
- 传播网络 $G^r$ 是一个有向图，包含顶点 $V^r$、边 $E^r$ 和顶点属性 $X^r$。

**研究问题:**

1. 从数据集 $R$ 中选择一个标记数据集 $R^L$，并遵守标记预算 $B$。
2. 使用 $R^L$ 训练一个模型来预测新记录 $r$ 是虚假还是真实新闻。

## Approach

### Overview of the proposed framework

首先是文章提出的框架概览：所提出的假新闻检测模型由两个主要部分组成：（1）无监督多模态域发现（模块A）； (2) 有监督的与领域无关的新闻分类（模块 B）。这两个组件集成在一起，可以识别假新闻，同时利用新闻记录中的特定领域和跨领域知识。此外，文章提出的实例选择方法（模块C）采用相同的域嵌入学习组件来选择信息丰富的新闻记录进行标记，最终产生一个最大化域覆盖范围的标记数据集。

### Unsupervised Domain Discovery

第一部分：**无监督领域发现**

对于一个给定的新闻记录 *r*，假设它的领域标签是不可用的。文章提出的无监督领域嵌入学习技术利用 r 的多模态内容（例如，文本、传播网络）来表示 r 的领域，即为 r构建一个低维向量 $f_{domain}(r)$​。文中的方法受到以下两点的启发：（1）用户倾向于形成包含有相似兴趣的人的群体（即同质性），这导致不同领域具有不同的用户基础；（2）不同领域在词语使用上存在显著差异。

所使用的算法如图所示，这个算法大致可以描述为：

#### Gemini

1. 构建一个异构网络，该网络由发布新闻的用户和新闻标题中的词作为节点。
2. 使用 Louvain 算法识别网络中的社区。
3. 计算记录在每个社区中的成员概率p。
4. 将记录在社区中的成员概率连接起来，构成该记录的领域嵌入 $f_{domain}(r)$。

### Domain-agnostic News Classification

In our news classification model, 

each news record $r$ is represented as a vector $f_{\text{input}}(r)$ using the textual content $W^r$ and the propagation network $G^r$ of $r$ (elaborated in the section Experiments). Then, our classification model maps $f_{\text{input}}(r)$ into two different subspaces such that one preserves the domain-specific knowledge, $f_{\text{specific}}: f_{\text{input}}(r) \rightarrow \mathbb{R}^d$, and the other preserves the cross-domain knowledge $f_{\text{shared}}: f_{\text{input}}(r) \rightarrow \mathbb{R}^d$, of $r$. Here $d$ is the dimension of the subspaces. Then, the concatenation of the $f_{\text{specific}}(r)$ and $f_{\text{shared}}(r)$ is used to recover the label $y'$ and the input representation $f_{\text{input}}(r)$ of $r$ during training via two decoder functions $g_{\text{pred}}$ and $g_{\text{recons}}$ respectively.



在我们的新闻分类模型中，每个新闻记录$r$用向量$f_{\text{input}}(r)$表示，该向量使用文本内容$W^r$和传播网络$G^r$来表示（详见实验部分）。然后，我们的分类模型将$f_{\text{input}}(r)$映射到两个不同的子空间，一个保留领域特定知识$f_{\text{specific}} \colon f_{\text{input}}(r) \rightarrow \mathbb{R}^d$，另一个保留跨领域知识$f_{\text{shared}} \colon f_{\text{input}}(r) \rightarrow \mathbb{R}^d$。这里$d$是子空间的维度。然后，连接$f_{\text{specific}}(r)$和$f_{\text{shared}}(r)$用于在训练期间恢复标签$y^r$和输入表示$f_{\text{input}}(r)$，通过两个解码函数$g_{\text{pred}}$和$g_{\text{recons}}$分别实现。
$$
y^r = g_{\text{pred}}(f_{\text{specific}}(r) \oplus f_{\text{shared}}(r))
$$

$$
\hat{f}_{\text{input}}(r) = g_{\text{recons}}(f_{\text{specific}}(r) \oplus f_{\text{shared}}(r))
$$

$$
L_{\text{pred}} = \text{BCE}(y^r, \hat{y}^r)
$$

$$
L_{\text{recon}} = \| f_{\text{input}}(r) - \hat{f}_{\text{input}}(r) \|^2
$$

其中$y^r$和$\hat{f}_{\text{input}}(r)$分别表示预测的标签和预测的输入表示。BCE代表二元交叉熵损失函数。我们最小化然而，$L_{\text{pred}}$和$L_{\text{recon}}$没有考虑到新闻记录中的领域差异。因此，我们现在讨论如何利用函数$f_{\text{specific}}$和$f_{\text{shared}}$进一步学习，以保留新闻记录中的领域特定知识和跨领域知识。

**利用领域特定知识** 为了保留领域特定的知识，我们利用一个辅助项$L_{\text{specific}}$来学习一个新的解码器函数$g_{\text{specific}}$。为了反映领域特定表示的优化，我们使用域函数$f_{\text{domain}}(r)$或其正则化的表示$f_{\text{specific}}(r)$。我们最小化$L_{\text{specific}}$来找到只包含领域特定知识的最优参数$f_{\text{specific}}$，这个过程可以定义如下：
$$
L_{\text{specific}} = \left\| f_{\text{domain}}(r) - g_{\text{specific}}(f_{\text{specific}}(r)) \right\|^2
$$

$$
f_{\text{specific}} = \arg\min_{f_{\text{specific}}} L_{\text{specific}}
$$

**利用跨领域知识** 相比之下，我们学习$f_{\text{shared}}$忽略领域特定知识，跨领域重构新闻记录。因此，我们训练一个解码器函数$g_{\text{shared}}$来准确预测领域知识的$f_{\text{shared}}(r)$。与此同时，我们训练$f_{\text{shared}}$通过最大化$L_{\text{shared}}$的损失来只依赖于领域知识，这些知识有助于转移知识编码常模。这个过程可以定义如下：
$$
L_{\text{shared}} = \left\| g_{\text{shared}}(f_{\text{shared}}(r)) - f_{\text{domain}}(r) \right\|^2
$$

$$
f_{\text{shared}} = \arg\min_{f_{\text{shared}}} (-L_{\text{shared}})
$$

 **集成模型** 然后最终的损失函数模型被表述为：

$$ L_{final} = \lambda_1 L_{prox} + \lambda_2 L_{species} + \lambda_3 L_{shared} - \lambda_4 L_{backward} \quad (7) $$

其中 $\lambda_1$，$\lambda_2$ 和 $\lambda_3$ 控制赋予每个损失项的重要性（例如，主任务）。$L_{prox}$ 是最小化点 $L_{shared}$ 的损失项相比于 $L_{prox}$（即，主任务）。要使最终的损失函数 $L_{final}$ 在等式 (8) 中有效地被优化，接下来两步：

$$ (\hat{\theta}_1) = \underset{\theta_1}{\text{argmin}} \, L_{final}(\theta_1, \theta_2) \quad (8) $$

$$ (\hat{\theta}_2) = \underset{\theta_2}{\text{argmax}} \, L_{final}(\theta_1, \theta_2) \quad (9) $$

其中 $\theta_1$ 和 $\theta_2$ 分别表示在 $(f_{species}^{shared}, f_{species}^{prox}, f_{species}^{recon})$ 和 $(f_{shared}^{species}, f_{shared}^{prox}, f_{shared}^{recon})$​ 中的参数。已经提出的优化方案的收敛性质在 (Silva et al. 2021) 中有详细研究。

#### Gemini

第二部分：**跨领域新闻分类**

模型的输入是一个新闻记录$r$，输出是一个标签$y$。

模型首先将新闻记录$r$编码成一个向量$f_{input}(r)$。

然后，模型将$f_{input}(r)$分成两个部分：$f_{specific}(r)$和$f_{shared}(r)$。

$f_{specific}(r)$包含领域特定知识，$f_{shared}(r)$​包含跨领域知识。

训练过程中，将 $f_{specific}(r)$ 和 $f_{shared}(r)$ 连接起来，用于恢复新闻记录 $r$ 的标签 $y'$ 和输入表示 $f_{input}(r)$。这一过程通过两个解码函数 $g_{pred}$ 和 $g_{recons}$ 分别实现。

我们使$L_{pred}$和$L_{recon}$最小以找到$f_{specific}(r)$和$f_{shared}(r)$，$g_{pred}$和$$g_{recons}$$的最优参数

**利用领域特定知识**

我们最小化$L_{\text{specific}}$来找到只包含领域特定知识的最优参数$f_{\text{specific}}$，这个过程可以定义如下：

**利用跨领域知识**

相比之下，我们学习$f_{\text{shared}}$忽略领域特定知识，跨领域重构新闻记录。通过最大化$L_{\text{shared}}$的损失来训练$f_{\text{shared}}$只依赖于领域知识，这些知识有助于转移知识编码常模。这个过程可以定义如下：

**集成模型**

最终的损失函数模型被表述为$L_{final} = \lambda_1 L_{prox} + \lambda_2 L_{species} + \lambda_3 L_{shared} - \lambda_4 L_{backward}$，其中 $\lambda_1$, $\lambda_2$, $\lambda_3$ 和 $\lambda_4$ 控制赋予每个损失项的重要性。

### LSH-based Instance Selection

上述模型能够利用新闻记录中的特定领域和跨领域知识来识别其准确性。尽管如此，如果该模型用于在训练期间识别看不见或很少出现的领域中的虚假新闻记录时，我们凭经验观察到模型的性能大幅下降。这一观察结果是预期的，并且与 (Castelo et al. 2019) 中的发现一致，这可能是由于特定领域的单词使用和传播模式所致，如图 1 所示。因此，我们提出了一种无监督技术使用给定标记预算 B 的标记训练数据集，使其覆盖尽可能多的领域。这项技术的最终目标是使用这样的数据集来学习一个在许多领域表现良好的模型。

我们的方法最初用其领域嵌入 $f_{domain}(r)$ 来表示每个新闻记录 $r \in R$。然后，我们基于随机投影提出了一种局部敏感哈希 (LSH) 算法，以在领域嵌入空间中选择一组距离较远的记录集 $R$，这可以通过以下步骤来详细说明：

1. 创建 $|H|$ 个不同的哈希函数，例如 $H_i(r) = \text{sgn}(h_i \cdot f_{domain}(r))$，其中 $i \in \{0, 1, \ldots, |H|-1\}$ 且 $h_i$ 是一个随机向量，$\text{sgn}(.)$ 是符号函数。这些随机向量 $h_i$ 是根据以下概率分布生成的，这种分布被证明在基于随机投影技术中表现良好 (Achlioptas 2001)：

$$ h_{i,j} = \sqrt{3} \times
\begin{cases}
  +1 & \text{概率为 } 1/6 \\
  0  & \text{概率为 } 2/3 \\
  -1 & \text{概率为 } 1/6
\end{cases} $$

2. 为每条新闻记录 $r$ 构建一个 $|H|$ 维的哈希值，表示为 $H_0(r) \oplus H_1(r) \oplus \ldots \oplus H_{|H|-1}(r)$，其中 $\oplus$ 表示串联操作。根据约翰逊-林登施特劳斯引理（Johnson et al. 1984），这样的哈希保留了原始嵌入空间中新闻记录与高概率的近似最大内积。因此，领域嵌入空间中相邻的记录会有相似的哈希值。
3. 将具有相似哈希值的新闻记录分组。
4. 随机从哈希表的每个箱中挑选一条记录，添加到数据集池中。
5. 重复步骤 (1)，(2)，(3) 和 (4)，直到数据集池达到标记预算 $B$。

在图例中，我们选取了原始数据集的 10% 使用提出的方法和随机选择。可以看出，随机选择遵循经验分布，而很少出现的领域（例如，波兰的假/真新闻）中的样本在训练中表现不佳。因此，这样的数据集可能对罕见领域的表现不佳。相比之下，提出的方法提供了一个显著数量的样本，从罕见的领域中选取样本。

此外，提出的方法非常高效（$O(|H||R|)$ 复杂度），与其他基于实例的优化算法（例如，k-均值（Lloyd 1982））相比，具有 $O(|R|^2)$ 的复杂度，其中 $|R| \gg |H|$。为了衡量领域内嵌入的距离，我们采用了 Laib 等人（2017）提出的选择方法，可以为给定的记录集 $r_1, r_2, \ldots, r_n$ 计算距离，这些记录使用相同的方法表示。

领域嵌入：$\lambda = \frac{1}{4n} \left( \sum_{i} (\delta_i - \bar{\delta})^2 \right)^{\frac{1}{2}}$，其中 $\delta_i = \min(k, L2\text{norm}(f_{domain}(r_i), f_{domain}(r_j)))$ 和 $\bar{\delta} = \Sigma \delta_i / n$。如果覆盖率高，$\lambda$​​ 小。因此，提出的方法与随机实例选择相比，如图 4b 所示，提供了更好的领域覆盖率。

LSH使用多个哈希函数，这些哈希函数设计成保持局部敏感性，即距离近的对象通过这些函数有更大的概率映射到相同的哈希值。通过这种方式，可以有效地进行近似最近邻搜索，而不必比较数据集中的每个点，从而在处理大数据集时提高效率。

#### Gemini

文中的技术使用局部敏感哈希 (LSH) 算法来选择一个标记训练数据集，该数据集覆盖尽可能多的领域。该算法通过以下步骤实现：

1. 创建哈希函数，并使用这些函数计算每个新闻记录的哈希值。
2. 将具有相似哈希值的新闻记录分组。
3. 随机从每个组中选择一条记录添加到数据集池。
4. 重复步骤 1-3，直到数据集池达到标记预算。

从图4-a可以看出，相比于随机选择，文中所提出的方法甚至提供了来自很少出现的域的大量样本。

从图4-b可以看出，与随机实例选择相比，所提出的方法产生了更好的域覆盖率，如图 4b 所示。

## Experiment

这张表格展示了多种方法在假新闻检测任务上的结果，这些方法分为三类：（1）基于文本内容的方法（T），（2）基于社交背景的方法（S），以及（3）多模态方法（M）。这些方法在不同数据集上的表现通过几项指标来衡量：准确率（Acc）、精确率（Prec）、召回率（Rec）以及F1分数。

我们将我们的方法与七种广泛使用的虚假新闻检测技术及其变体进行了比较

所提出的方法在所有三个领域都产生了明显更好的结果，F1 分数比最佳基线高出 7.55%。

- 多模态方法（M）通常在各项指标上表现较好，这表明结合文本内容和社交背景信息是有效的。
- 在相关领域的之前工作和提出的方法（Our Approach）中，当使用全部的池化新闻记录时，文章中的模型在准确率、精确率、召回率和F1分数通常更高。
- 消融研究（Ablation Study）显示，移除特定的模型组件（如域共享损失、域特定损失、网络模态或文本模态）会导致性能下降，这验证了这些组件在模型中的重要性。



## Conclusion

在这篇文章中，提出了一个新的假新闻检测框架，利用了新闻记录中的领域特定和跨领域知识。同时还引入了一种新的无监督方法，从大量未标记的新闻记录中选择信息丰富的实例进行手动标记。利用这些标记数据，训练了一个能够在不同领域中表现出色的模型。