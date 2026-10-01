# W16 补充阅读：从队列策略到集群准入与放置

[范围与验收](README.md) · [三段导学](study-guide.md) · [更新流程](../../docs/weekly-refresh.md) · [来源登记](../../resources/frontier-watchlist.md#s16)

资料快照：2026-10-01。开课复核：待进行。本地状态：仅阅读，相关实现尚未运行。

开课前用30分钟核对本页资料。这里的练习并入本周报告，额外实现留作选修。

## 现在怎样做

FIFO/非抢占 SJF 仿真用于理解等待、完成时间和任务假设；Ray 是可选执行层。先验证不丢任务、不超分配，区分实际耗时已知的仿真假设与现实中的估计误差。

## 这一方向还有哪些进展

更成熟的资源管理把配额/准入、多个任务协同放置、拓扑和公平性组合起来。这个系统分层比给 FIFO 换一个更复杂评分函数更值得先理解。

**读哪里**：[Kueue 与 KAI Scheduler](https://kueue.sigs.k8s.io/docs/overview/)。Overview 中 workload admission、资源配额与支持工作负载的说明；再读 KAI 介绍中的 bin packing、queueing、gang scheduling 与拓扑需求。配套：[NVIDIA Cloud Functions 的 KAI Scheduler 说明](https://docs.nvidia.com/nvcf/compute-plane/kai-scheduler)。

**目前的状态**：有官方项目文档与具体产品集成说明；NVCF 使用 KAI 的证据不代表行业全部采用，也不是对本机的部署验证。

**在我们的设备上**：不在本周创建 Kubernetes 集群。CPU 仿真可以解释策略，真实 GPU placement、隔离与网络仍未验证。

## 真正用起来，还要考虑什么

真实队列还受配额、优先级、gang、拓扑、抢占和资源碎片影响；有限轨迹无法证明不会饥饿，知道作业真实时长的 SJF 也有信息优势。

**写进本周报告**：在调度报告画四层：接收作业→配额/准入→节点/GPU 放置→执行/观测。加入一例总空闲卡数足够但受拓扑或 gang 约束仍不能启动的纸面反例，不改变主线两策略。

## 下次更新时

核对 Kueue/KAI 的职责和集成边界；选择平台分支后再定义容器、集群与故障验收，不把模拟通过写成生产就绪。更新写入 [开课记录](../../templates/weekly-refresh.md)，保留旧实验的配置。
