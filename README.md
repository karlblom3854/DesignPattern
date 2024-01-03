# Design Pattern
学习教材：《人人都懂设计模式》
## 监听模式
### 作用
在对象间定义一种一对多的依赖关系，当这个对象状态发生改变时，所有依赖它的对象都会被通知并自动更新。
### 类图
![](./asserts/监听模式-类图.png)
### 练习
1. 热水器-饮用模式&洗澡模式（water_heater.py）
2. 异常登陆（abnormal_login.py）
3. 新闻发布系统（news_release_system.py）
### 模型说明
1. 明确谁是观察者，谁是被观察者。一般，观察者和被观察者是多对一的关系。
2. 被观察者利用notify_observers()函数通知观察者时，无需指定具体的观察者，有观察者自己决定是否处理该通知。
    > 当然应该也可以屏蔽某个观察者
3. 被观察者需要能够添加和移除观察者观察者（add_observer(Observer), remove_observer(Observer)）。
4. 被观察者的实例化对象，需要在自身状态变化时（change()），通过父类通知给观察者（notify_observers）。
   > 如示例中的login()和set_temperature()函数
5. 推模型和拉模型
   1. 推模型 
      1. 被观察者将某些详细信息利用notify_observers(info)函数推送给观察者，再传递到update(info)函数，通过info变量传递。 
      2. info变量一般为object类型，即json｜字典。
   2. 拉模型
      1. 被观察者在通知观察者的时候，只传递少量信息。如果观察者需要更具体的信息，由观察者主动到被观察者对象中获取，相当于观察者从被观察者对象中拉数据。

### 个人理解&注意事项
1. 被观察者Observable，观察者Observer，对应各自的实例化对象。
2. 观察者对于被观察者是组合关系，因为没有被观察者的话，观察者就没有存在的必要。
3. 观察者不需要进行实例化，直接由被观察者的示例对象通过add_observer()函数添加。

## 状态模式
### 作用

### 类图

### 练习

### 模型说明

### 个人理解&注意事项
