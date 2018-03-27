# �������ݿ�
USE `ysali`;
DROP TABLE IF EXISTS `le_rank`;

CREATE TABLE `le_rank` (
	`nm_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '������������ID', 
	`dt_date` date DEFAULT NULL COMMENT 'ʱ��', 
	`vc_infoid` varchar(255) DEFAULT NULL COMMENT '����info��', 
	`vc_videoid` varchar(255) DEFAULT NULL COMMENT '����video��', 
	`vc_class` varchar(100) DEFAULT NULL COMMENT '�����;�Ȳ�/����/����', 
	`vc_subclass` varchar(100) DEFAULT NULL COMMENT '������;��/��/��/ȫ��', 
	`vc_channel` varchar(100) DEFAULT NULL COMMENT 'Ƶ��;��Ӱ/���Ӿ�/����', 
	`nm_rank` int(10) DEFAULT NULL COMMENT '����', 
	`vc_name` varchar(100) DEFAULT NULL COMMENT 'Ƭ��', 
	`vc_nameUrl` varchar(1000) DEFAULT NULL COMMENT 'Ƭ������', 
	`vc_actors` varchar(100) DEFAULT NULL COMMENT '����', 
	`vc_area` varchar(100) DEFAULT NULL COMMENT '����', 
	`vc_type` varchar(100) DEFAULT NULL COMMENT '����', 
	`nm_score` varchar(10) DEFAULT NULL COMMENT '����', 
	`vc_trend` varchar(100) DEFAULT NULL COMMENT '����', 
	`nm_playCount` varchar(100) DEFAULT NULL COMMENT '�ܲ�����',
	`vc_listDays` varchar(100) DEFAULT NULL COMMENT '�ϰ�����', 
	`vc_rankTop` varchar(100) DEFAULT NULL COMMENT '�������', 
	`nm_increment` varchar(100) DEFAULT NULL COMMENT '����',  
	`dt_create` datetime DEFAULT NULL COMMENT '�ɼ�ʱ��', 
	`dt_update` datetime DEFAULT NULL COMMENT '����ʱ��', 
	PRIMARY KEY (`nm_id`), 
	UNIQUE KEY `idx_dt_create` (`dt_date`, `vc_class`, `vc_subclass`, `vc_infoid`, `vc_videoid`)
) ENGINE = InnoDB AUTO_INCREMENT = 0 CHARSET = utf8 COMMENT = '����-Ӱ������'


# �洢����
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