**基于gin框架的restful api 示例**

**项目层级结构**
```
│--router.go  路由管理, 入口
│
├─apis  api层
│      person.go   用户api
│
├─database   数据库配置
│      mysql.go   mysql配置
│
└─models   模型层
        person.go  用户模型
```

**涉及数据表 test.person**
```
CREATE TABLE `person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(40) NOT NULL DEFAULT '',
  `last_name` varchar(40) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

**参考文档**

- [Gin实战：Gin+Mysql简单的Restful风格的API](https://www.jianshu.com/p/a3f63b5da74c)
