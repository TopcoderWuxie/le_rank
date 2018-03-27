# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from datetime import datetime

class LeshirankPipeline(object):
    def process_item(self, item, spider):

        self.host = spider.settings.get('MYSQL_HOST')
        self.port = spider.settings.get('MYSQL_PORT')
        self.user = spider.settings.get('MYSQL_USR')
        self.pwd = spider.settings.get('MYSQL_PWD')
        self.db = spider.settings.get('MYSQL_DB')

        # self.insertSql = 'insert into le_rank(vc_class, vc_subclass, vc_channel, nm_rank, vc_name, vc_nameUrl, vc_actors, vc_area, vc_type, nm_score, vc_listDays,vc_rankTop, nm_increment, vc_trend, nm_playCount, vc_infoid, vc_videoid, dt_date, dt_update, dt_create) values("%s", "%s", "%s", %d, "%s", "%s", "%s","%s","%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'
        self.callSql = 'call pro_add_le_rank("%s", "%s", "%s", %d, "%s", "%s", "%s","%s","%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'

        self.conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            passwd = self.pwd,
            db = self.db,
            charset = 'utf8',
        )

        self.cur = self.conn.cursor()

        try:
            # self.cur.execute(self.insertSql % (item['classification'], item['subclass'], item['channel'], item['rank'], item['name'], item['nameUrl'], item['actors'], item['area'], item['_type'], item['score'], item['listDays'], item['rankTop'], item['increment'], item['trend'], item['playCount'], item['infoId'], item['videoId'], item['_date'], item['update_time'], item['create_time']))
            self.cur.execute(self.callSql % (item['classification'], item['subclass'], item['channel'], item['rank'], item['name'], item['nameUrl'], item['actors'], item['area'], item['_type'], item['score'], item['listDays'], item['rankTop'], item['increment'], item['trend'], item['playCount'], item['infoId'], item['videoId'], item['_date'], item['update_time'], item['create_time']))
            self.conn.commit()
            print u"{}----插入成功".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),)
        except Exception as e:
            print u"{}----插入出错,出错原因为:{}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), e)
            self.conn.rollback()

        return item
