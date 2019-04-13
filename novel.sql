-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: novel
-- ------------------------------------------------------
-- Server version	5.7.21-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Channel`
--

DROP TABLE IF EXISTS `Channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Channel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `channel_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `NovelChaPter`
--

DROP TABLE IF EXISTS `NovelChaPter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `NovelChaPter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `novelchapter_name` varchar(30) NOT NULL,
  `novelchapter_text` longtext NOT NULL,
  `novelchapter_num` int(11) NOT NULL,
  `novelchapter_time` datetime(6) NOT NULL,
  `novelchapter_cover_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5753 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `NovelCol`
--

DROP TABLE IF EXISTS `NovelCol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `NovelCol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `addtime` datetime(6) NOT NULL,
  `novel_id` int(11) DEFAULT NULL,
  `user` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `NovelCol_addtime_d7c3d6d1` (`addtime`),
  KEY `NovelCol_novel_id_ccba4615_fk_NovelModel_id` (`novel_id`),
  CONSTRAINT `NovelCol_novel_id_ccba4615_fk_NovelModel_id` FOREIGN KEY (`novel_id`) REFERENCES `NovelModel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `NovelModel`
--

DROP TABLE IF EXISTS `NovelModel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `NovelModel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `novel_name` varchar(30) DEFAULT NULL,
  `novel_image` varchar(100) DEFAULT NULL,
  `novel_user` varchar(30) DEFAULT NULL,
  `novel_byte` int(11) NOT NULL DEFAULT '0',
  `novel_read` int(11) unsigned zerofill NOT NULL DEFAULT '00000000000',
  `novel_comment` int(11) unsigned zerofill NOT NULL DEFAULT '00000000000',
  `novel_text` longtext,
  `novel_fave` int(11) unsigned zerofill NOT NULL DEFAULT '00000000000',
  `novel_next` int(11) unsigned zerofill NOT NULL DEFAULT '00000000000',
  `novel_time` datetime(6) NOT NULL ON UPDATE CURRENT_TIMESTAMP(6),
  `novel_tag_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `NovelModel_novel_tag_id_f55a530c_fk_TagModel_id` (`novel_tag_id`),
  CONSTRAINT `NovelModel_novel_tag_id_f55a530c_fk_TagModel_id` FOREIGN KEY (`novel_tag_id`) REFERENCES `TagModel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `TagModel`
--

DROP TABLE IF EXISTS `TagModel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TagModel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(20) NOT NULL,
  `tag_id_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `TagModel_tag_id_id_96282f4a_fk_Channel_id` (`tag_id_id`),
  CONSTRAINT `TagModel_tag_id_id_96282f4a_fk_Channel_id` FOREIGN KEY (`tag_id_id`) REFERENCES `Channel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Tage`
--

DROP TABLE IF EXISTS `Tage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Tage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-13 11:48:06
