-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: sumo_match_maker
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `weight_categories`
--

DROP TABLE IF EXISTS `weight_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weight_categories` (
  `weight_category` varchar(45) NOT NULL,
  `age_category` varchar(45) NOT NULL,
  `category_id` int NOT NULL,
  `gender` varchar(45) NOT NULL,
  PRIMARY KEY (`category_id`),
  KEY `category_id_idx` (`age_category`),
  CONSTRAINT `category_id` FOREIGN KEY (`age_category`) REFERENCES `age_categories` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weight_categories`
--

LOCK TABLES `weight_categories` WRITE;
/*!40000 ALTER TABLE `weight_categories` DISABLE KEYS */;
INSERT INTO `weight_categories` VALUES ('open','Młodzierzowiec (u23)',788791,'mężczyźni'),('70','Junior (u18)',1139907,'mężczyźni'),('50','Dziecko (u12)',2050588,'mężczyźni'),('+95','Senior ',2569929,'kobiety'),('45','Młodzik (u14)',3670053,'mężczyźni'),('+95','Młodzierzowiec (u21)',5344828,'kobiety'),('+ 95','Młodzierzowiec (u21)',5940729,'kobiety'),('70','Kadet (u16)',6159943,'kobiety'),('+ 115','Młodzierzowiec (u23)',6543956,'mężczyźni'),('+115','Młodzierzowiec (u23)',7056214,'mężczyźni'),('+ 65','Młodzik (u14)',7427520,'kobiety'),('55','Kadet (u16)',7976387,'mężczyźni'),('+ 70','Młodzik (u14)',9625102,'mężczyźni'),('+ 115','Młodzierzowiec (u21)',10078352,'mężczyźni'),('+95','Młodzierzowiec (u23)',11060543,'kobiety'),('115','Senior ',11416468,'mężczyźni'),('open','Młodzierzowiec (u21)',11789269,'kobiety'),('60','Młodzik (u14)',12172638,'mężczyźni'),('50','Młodzik (u14)',12459831,'mężczyźni'),('75','Kadet (u16)',12740731,'mężczyźni'),('60','Młodzierzowiec (u23)',13341910,'kobiety'),('open','Senior ',14022542,'mężczyźni'),('60','Młodzik (u14)',16718394,'kobiety'),('+70','Kadet (u16)',18262850,'kobiety'),('35','Dziecko (u12)',18934046,'mężczyźni'),('100','Junior (u18)',21145055,'mężczyźni'),('60','Dziecko (u12)',21564439,'kobiety'),('65','Młodzierzowiec (u21)',22435073,'kobiety'),('+ 60','Dziecko (u12)',23051990,'kobiety'),('77','Senior ',23083275,'mężczyźni'),('+80','Młodzierzowiec (u23)',23115853,'kobiety'),('+70','Junior (u18)',25012099,'kobiety'),('70','Junior (u18)',25935642,'kobiety'),('73','Młodzierzowiec (u21)',26031361,'kobiety'),('40','Dziecko (u12)',26710485,'kobiety'),('35','Młodzik (u14)',26793261,'mężczyźni'),('85','Kadet (u16)',27190850,'mężczyźni'),('60','Dziecko (u12)',27235287,'mężczyźni'),('90','Junior (u18)',27495083,'mężczyźni'),('+ 95','Senior ',27840463,'kobiety'),('50','Kadet (u16)',28321054,'kobiety'),('+60','Młodzik (u14)',29465572,'kobiety'),('55','Junior (u18)',29525267,'kobiety'),('+ 60','Dziecko (u12)',30568855,'mężczyźni'),('45','Młodzik (u14)',31241511,'kobiety'),('+ 65','Kadet (u16)',31926035,'kobiety'),('73','Młodzierzowiec (u23)',33129588,'kobiety'),('95','Młodzierzowiec (u21)',33585448,'kobiety'),('50','Młodzik (u14)',33660626,'kobiety'),('65','Młodzierzowiec (u23)',34416420,'kobiety'),('40','Młodzik (u14)',37887177,'mężczyźni'),('open','Kadet (u16)',38363885,'mężczyźni'),('+ 70','Kadet (u16)',38554438,'kobiety'),('open','Junior (u18)',39317916,'kobiety'),('60','Kadet (u16)',39475554,'kobiety'),('115','Młodzierzowiec (u21)',39607754,'mężczyźni'),('+ 70','Junior (u18)',39822348,'kobiety'),('95','Młodzierzowiec (u23)',40363279,'kobiety'),('70','Młodzierzowiec (u23)',41656182,'mężczyźni'),('70','Młodzierzowiec (u21)',41809318,'mężczyźni'),('77','Młodzierzowiec (u21)',42205546,'mężczyźni'),('+75','Junior (u18)',44495100,'kobiety'),('45','Dziecko (u12)',45007095,'mężczyźni'),('60','Junior (u18)',47242545,'mężczyźni'),('50','Młodzierzowiec (u21)',49044578,'kobiety'),('55','Młodzik (u14)',50932801,'kobiety'),('+80','Młodzierzowiec (u21)',50984542,'kobiety'),('40','Dziecko (u12)',51082679,'mężczyźni'),('92','Senior ',51487447,'mężczyźni'),('60','Młodzierzowiec (u21)',52426492,'kobiety'),('+70','Młodzik (u14)',53528406,'mężczyźni'),('+ 115','Senior ',54223405,'mężczyźni'),('+115','Senior ',54667287,'mężczyźni'),('55','Dziecko (u12)',55896051,'kobiety'),('45','Kadet (u16)',56297599,'kobiety'),('+ 75','Junior (u18)',56394402,'kobiety'),('50','Młodzierzowiec (u23)',58200198,'kobiety'),('100','Młodzierzowiec (u21)',58652226,'mężczyźni'),('+115','Młodzierzowiec (u21)',59339920,'mężczyźni'),('92','Młodzierzowiec (u23)',59373987,'mężczyźni'),('50','Junior (u18)',59727583,'kobiety'),('50','Senior ',59940831,'kobiety'),('+ 95','Kadet (u16)',60885067,'mężczyźni'),('55','Młodzierzowiec (u23)',61254926,'kobiety'),('95','Senior ',61255731,'kobiety'),('+65','Młodzik (u14)',62383971,'kobiety'),('open','Junior (u18)',62723316,'mężczyźni'),('100','Senior ',63984148,'mężczyźni'),('+80','Senior ',64020189,'kobiety'),('77','Młodzierzowiec (u23)',64118465,'mężczyźni'),('60','Senior ',66216656,'kobiety'),('85','Młodzierzowiec (u23)',66299006,'mężczyźni'),('80','Młodzierzowiec (u21)',67536125,'kobiety'),('80','Junior (u18)',68089859,'mężczyźni'),('30','Dziecko (u12)',68621770,'kobiety'),('55','Młodzierzowiec (u21)',69124551,'kobiety'),('+ 80','Senior ',70204260,'kobiety'),('+65','Kadet (u16)',71047097,'kobiety'),('100','Młodzierzowiec (u23)',71470219,'mężczyźni'),('60','Junior (u18)',72099783,'kobiety'),('65','Młodzik (u14)',72124177,'kobiety'),('+ 100','Junior (u18)',73184421,'mężczyźni'),('+ 95','Młodzierzowiec (u23)',74535916,'kobiety'),('65','Młodzik (u14)',75406477,'mężczyźni'),('80','Młodzierzowiec (u23)',75988168,'kobiety'),('50','Dziecko (u12)',76171079,'kobiety'),('open','Młodzierzowiec (u23)',77097494,'kobiety'),('65','Kadet (u16)',77179560,'kobiety'),('55','Kadet (u16)',77949250,'kobiety'),('70','Senior ',78089605,'mężczyźni'),('35','Dziecko (u12)',78637428,'kobiety'),('55','Senior ',79628097,'kobiety'),('75','Junior (u18)',81140219,'kobiety'),('80','Senior ',82469258,'kobiety'),('35','Młodzik (u14)',82701054,'kobiety'),('65','Senior ',85547759,'kobiety'),('55','Dziecko (u12)',86382074,'mężczyźni'),('45','Dziecko (u12)',86397177,'kobiety'),('95','Kadet (u16)',86711937,'mężczyźni'),('55','Młodzik (u14)',86747354,'mężczyźni'),('+60','Dziecko (u12)',86784665,'mężczyźni'),('65','Junior (u18)',87364286,'kobiety'),('92','Młodzierzowiec (u21)',87739309,'mężczyźni'),('+60','Dziecko (u12)',87761194,'kobiety'),('73','Senior ',87942210,'kobiety'),('55','Junior (u18)',88262922,'mężczyźni'),('+95','Kadet (u16)',89229112,'mężczyźni'),('+100','Junior (u18)',89281419,'mężczyźni'),('open','Młodzierzowiec (u21)',90100993,'mężczyźni'),('85','Senior ',90937103,'mężczyźni'),('open','Senior ',91758832,'kobiety'),('40','Młodzik (u14)',92308081,'kobiety'),('+ 80','Młodzierzowiec (u23)',92506928,'kobiety'),('115','Młodzierzowiec (u23)',93404901,'mężczyźni'),('70','Młodzik (u14)',93696283,'mężczyźni'),('+ 80','Młodzierzowiec (u21)',94520584,'kobiety'),('85','Młodzierzowiec (u21)',94855613,'mężczyźni'),('50','Kadet (u16)',95805007,'mężczyźni'),('65','Kadet (u16)',96294494,'mężczyźni'),('open','Kadet (u16)',97216500,'kobiety'),('+ 60','Młodzik (u14)',98177835,'kobiety');
/*!40000 ALTER TABLE `weight_categories` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-18 18:28:36
