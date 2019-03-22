/*
SQLyog 企业版 - MySQL GUI v8.14 
MySQL - 5.6.43-log : Database - im30
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`im30` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `im30`;

/*Table structure for table `tbl_webserver` */

DROP TABLE IF EXISTS `tbl_webserver`;

CREATE TABLE `tbl_webserver` (
  `svr_id` int(10) unsigned NOT NULL DEFAULT '1',
  `status` tinyint(3) NOT NULL DEFAULT '0',
  `active` int(11) DEFAULT '0',
  `svr_name` varchar(32) NOT NULL DEFAULT '',
  `zone` varchar(16) NOT NULL DEFAULT '',
  `ip_inner` varchar(16) NOT NULL DEFAULT '',
  `ip_pub` varchar(16) NOT NULL DEFAULT '',
  `port` int(10) NOT NULL DEFAULT '8088',
  `redis_instance` int(10) NOT NULL DEFAULT '6379',
  `ver_client` varchar(50) DEFAULT NULL,
  `ver_server` varchar(16) NOT NULL DEFAULT '',
  `db_ref` varchar(64) NOT NULL DEFAULT '',
  `is_recommend` tinyint(1) NOT NULL DEFAULT '0',
  `is_hot` tinyint(1) NOT NULL DEFAULT '0',
  `is_new` tinyint(1) NOT NULL DEFAULT '0',
  `is_test` tinyint(1) NOT NULL DEFAULT '0',
  `is_cnserver` tinyint(1) NOT NULL DEFAULT '0',
  `is_merge` tinyint(1) NOT NULL DEFAULT '0',
  `cn_move_out` tinyint(1) NOT NULL DEFAULT '0',
  `open_time` int(10) NOT NULL DEFAULT '0',
  `create_time` int(10) NOT NULL DEFAULT '0',
  `update_time` int(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`svr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `tbl_webserver` */

insert  into `tbl_webserver`(`svr_id`,`status`,`active`,`svr_name`,`zone`,`ip_inner`,`ip_pub`,`port`,`redis_instance`,`ver_client`,`ver_server`,`db_ref`,`is_recommend`,`is_hot`,`is_new`,`is_test`,`is_cnserver`,`is_merge`,`cn_move_out`,`open_time`,`create_time`,`update_time`) values (1,1,0,'COK115','COK115','10.0.5.17','192.169.100.1',9933,16494,'10.2.2.1:3306/cokdb115','','',0,0,0,0,0,0,0,1437118814,1437118814,1437118814),(2,1,0,'COK134','COK134','10.0.5.17','192.169.100.1',9933,16513,'10.2.2.1:3306/cokdb134','','',0,0,0,0,0,0,0,1437118843,1437118842,1437118834),(3,1,0,'COK8050','COK8050','10.1.3.66','192.169.2.2',9933,24429,'10.2.2.1:3306/cokdb8050','','',0,0,0,0,0,0,0,1437118843,1437118842,1437118834),(4,1,0,'COK8103','COK8103','10.1.3.89','192.169.2.3',9923,24482,'10.1.3.89:3306/cokdb8103','','',0,0,0,0,0,0,0,1437118814,1437118814,1437118814),(5,1,0,'COK234','COK234','10.0.6.71','192.169.130.1',9933,16613,'10.2.5.1:3306/cokdb234','','',0,0,0,0,0,0,0,1437118814,1437118814,1437118814),(6,1,0,'COK345','COK345','10.0.6.48','192.169.140.1',9933,16724,'10.2.6.1:3306/cokdb345','','',0,0,0,0,0,0,0,1437118814,1437118814,1437118814),(7,1,0,'COK8907','COK8907','10.3.56.60','192.169.50.1',9933,25286,'10.2.32.1:3306/cokdb8907','','',0,0,0,0,0,0,0,1437118814,1437118814,1437118814),(8,1,0,'COK8317','COK8317','10.5.36.67','192.169.20.1',9933,24696,'10.2.33.1:3306/cokdb8317','','',0,0,0,0,0,0,0,1437118814,1437118814,1437118814);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
