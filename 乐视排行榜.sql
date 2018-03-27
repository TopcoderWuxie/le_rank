# 创建数据库
USE `ysali`;
DROP TABLE IF EXISTS `le_rank`;

CREATE TABLE `le_rank` (
	`nm_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '主键；自增长ID', 
	`dt_date` date DEFAULT NULL COMMENT '时间', 
	`vc_infoid` varchar(255) DEFAULT NULL COMMENT '关联info表', 
	`vc_videoid` varchar(255) DEFAULT NULL COMMENT '关联video表', 
	`vc_class` varchar(100) DEFAULT NULL COMMENT '榜单类别;热播/热搜/好评', 
	`vc_subclass` varchar(100) DEFAULT NULL COMMENT '榜单子类;日/周/月/全部', 
	`vc_channel` varchar(100) DEFAULT NULL COMMENT '频道;电影/电视剧/综艺', 
	`nm_rank` int(10) DEFAULT NULL COMMENT '排名', 
	`vc_name` varchar(100) DEFAULT NULL COMMENT '片名', 
	`vc_nameUrl` varchar(1000) DEFAULT NULL COMMENT '片名链接', 
	`vc_actors` varchar(100) DEFAULT NULL COMMENT '主演', 
	`vc_area` varchar(100) DEFAULT NULL COMMENT '地区', 
	`vc_type` varchar(100) DEFAULT NULL COMMENT '类型', 
	`nm_score` varchar(10) DEFAULT NULL COMMENT '评分', 
	`vc_trend` varchar(100) DEFAULT NULL COMMENT '走势', 
	`nm_playCount` varchar(100) DEFAULT NULL COMMENT '总播放量',
	`vc_listDays` varchar(100) DEFAULT NULL COMMENT '上榜天数', 
	`vc_rankTop` varchar(100) DEFAULT NULL COMMENT '最高排名', 
	`nm_increment` varchar(100) DEFAULT NULL COMMENT '新增',  
	`dt_create` datetime DEFAULT NULL COMMENT '采集时间', 
	`dt_update` datetime DEFAULT NULL COMMENT '更新时间', 
	PRIMARY KEY (`nm_id`), 
	UNIQUE KEY `idx_dt_create` (`dt_date`, `vc_class`, `vc_subclass`, `vc_infoid`, `vc_videoid`)
) ENGINE = InnoDB AUTO_INCREMENT = 0 CHARSET = utf8 COMMENT = '乐视-影视排行'


# 存储过程
DELIMITER $$

USE `ysali`$$

DROP PROCEDURE IF EXISTS `pro_add_le_rank`$$

CREATE PROCEDURE `pro_add_le_rank`(
		v_class varchar(100), v_subclass varchar(100), v_channel varchar(100), v_rank int(10), v_name varchar(100), v_nameUrl varchar(1000), v_actors varchar(100), 
		v_area varchar(100), v_type varchar(100), v_score varchar(10), v_listDays varchar(100),v_rankTop varchar(100), v_increment varchar(100), 
		v_trend varchar(100), v_playCount varchar(100), v_infoid varchar(255), v_videoid varchar(255), v_date date, v_update datetime, v_create datetime
)
BEGIN
	INSERT INTO le_rank (
		vc_class, vc_subclass, vc_channel, nm_rank, vc_name, vc_nameUrl, vc_actors, vc_area, vc_type, nm_score, 
		vc_listDays,vc_rankTop, nm_increment, vc_trend, nm_playCount, vc_infoid, vc_videoid,dt_date, dt_update, dt_create
	)
	VALUES (
		v_class, v_subclass, v_channel, v_rank, v_name, v_nameUrl, v_actors, v_area, v_type, v_score, 
		v_listDays, v_rankTop, v_increment, v_trend, v_playCount, v_infoid, v_videoid, NOW(), NOW(), NOW()
	);
END$$

DELIMITER ;