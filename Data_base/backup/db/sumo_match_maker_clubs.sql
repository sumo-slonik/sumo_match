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
-- Table structure for table `clubs`
--

DROP TABLE IF EXISTS `clubs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clubs` (
  `club_name` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `foundation_date` date DEFAULT NULL,
  `club_id` int NOT NULL,
  `province` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`club_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clubs`
--

LOCK TABLES `clubs` WRITE;
/*!40000 ALTER TABLE `clubs` DISABLE KEYS */;
INSERT INTO `clubs` VALUES ('UKS Mieszko','Gorzów Wlkp.','1995-01-01',1500001,'lubuskie'),('UKJ LEGION','Zamość','2007-01-01',1500002,'lubelskie'),('LMUKS OLIMPIK','Suwałki','2003-01-01',1500003,'podlaskie'),('UKS CSW LIDER','Zamość','2010-01-01',1500004,'lubelskie'),('LKS Spartakus','Pyrzyce',NULL,1500005,'zachodniopomorskie'),('KS ONI','Lublin','2008-01-01',1500006,'lubelskie'),('UKS FUKS','Warszawa','2003-01-01',1500007,'mazowieckie'),('MULKS JUNIOR','Dzierżoniów','1999-01-01',1500008,'dolnośląskie'),('LUKS \"Lubzina\"','Lubzina','1995-01-01',1500009,'podkarpackie'),('UKSJ NIPPON','Olsztyn','2007-01-01',1500010,'warmińsko-mazurskie'),('UAKS PODLASIE','Białystok','2012-01-01',1500011,'podlaskie'),('ZTS Sokół','Lublin','1991-01-01',1500012,'lubelskie'),('UKS HUTNIK','Pieńsk','1965-01-01',1500013,'dolnośląskie'),('LUKS SYRENA','Gnojnica','1994-01-01',1500014,'podkarpackie'),('KS Koronowo','Koronowo','2011-01-01',1500015,'kujawsko-pomorskie'),('KS \"SOBIESKI\"','Poznań','1985-01-01',1500016,'wielkopolskie'),('UKS SAMSON przy S P','Kobylin','1996-01-01',1500017,'wielkopolskie'),('KS. AZS- AWF','Gorzów Wlkp.','1978-01-01',1500018,'lubuskie'),('TA ROZUM','Krotoszyn','2001-01-01',1500019,'wielkopolskie'),('UKS NIEDŹWIADEK','Warszawa','2011-01-01',1500021,'mazowieckie'),('ULKS GULIWER','Kielce','2006-01-01',1500022,'świętokrzyskie'),('MKS ROKITA','Brzeg Dolny',NULL,1500023,'dolnośląskie'),('KS BUDOWLANI','Olsztyn','1957-01-01',1500024,'warmińsko-mazurskie'),('KS \"Agros\"','Zamość',NULL,1500025,'lubelskie'),('WLKS Nowe Iganie','Siedlce - Nowe Iganie',NULL,1500026,'mazowieckie'),('UKS \"SORGA\'\'','Zamość','2010-01-01',1500027,'lubelskie'),('Klub Sportowy 20','Łódź','2005-01-01',1500028,'łódzkie'),('UKS ENERGETYK','Poznań',NULL,1500029,'wielkopolskie'),('KS Akademia Judo','Poznań','2009-01-01',1500030,'wielkopolskie'),('UKS \"SIÓDEMKA\"','Strzelce Opolskie','1999-01-01',1500032,'opolskie'),('UKS MARYSIN WAWERSKI','Warszawa','2005-01-01',1500033,'mazowieckie'),('KS DALIN','Myślenice','1921-01-01',1500034,'małopolskie'),('PTC','Pabianice','1906-01-01',1500035,'łódzkie'),('UKS HERKULES','Łomża','2000-01-01',1500036,'podlaskie'),('MKS POGOŃ TYSZOWCE','Tyszowce','2011-01-01',1500037,'lubelskie'),('UKS MUSTANG','Obra','2000-01-01',1500038,'wielkopolskie'),('UKS KORONA','Kaława','2010-01-01',1500039,'lubuskie'),('MUKZ GLADIATOR','Kraków','2000-01-01',1500040,'małopolskie'),('KS ORŁY','Milejów','2012-01-01',1500041,'lubelskie'),('LKS Feniks Pesta','Stargard','2000-01-01',1500042,'zachodniopomorskie'),('Gorzowskie Stowarzyszenie Sportu i Rekreacji','Gorzów Wlkp.','2004-01-01',1500043,'lubuskie'),('UKS GIMNAZJON','Suchy Las','2003-01-01',1500044,'wielkopolskie'),('UKS Atleta','Łódź','2007-01-01',1500045,'łódzkie'),('MKS JUVENIA','Wrocław','1946-01-01',1500046,'dolnośląskie'),('UKS Master','Łódź',NULL,1500047,'łódzkie'),('LUKS WARMIA','Lidzbark Warmiński',NULL,1500048,'warmińsko-mazurskie'),('ULKS Olimpijczyk','Chełm',NULL,1600001,'lubelskie'),('UKS IRON BULLS','Bielawa','2013-01-01',1600002,'dolnośląskie'),('SSA Legia 1926','Warszawa','1926-01-01',1600003,'mazowieckie'),('UKS Orzeł','Stary Zamość','2000-01-01',1600004,'lubelskie'),('UKS Międzychodzka Akademia Sumo','Międzychód','2016-01-01',1600005,'wielkopolskie'),('UKS SMS','Łódź','1997-01-01',1600006,'łódzkie'),('UKS ZDROWY TARGÓWEK','Warszawa','2001-01-01',1600007,'mazowieckie'),('KS Sumoka','Rzeszów','2014-01-01',1700001,'podkarpackie'),('AKADEMIA MLUKSIAKÓW','Karlino',NULL,1700002,'zachodniopomorskie'),('KS Młodzieży i Dzieci \"SMiD\"','Rogów',NULL,1700003,'mazowieckie'),('ULKS Bursztyn','Lewin Kłodzki','2002-01-01',1700004,'dolnośląskie'),('OLIMPIJCZYK','Sulmierzyce','2014-01-01',1800001,'wielkopolskie'),('ULKS IPPON','Jarocin',NULL,1800002,'wielkopolskie'),('ULKS Bizon','Milicz',NULL,1800003,'dolnośląskie'),('ULKS Bizon','Milicz','1985-01-01',1800004,'dolnośląskie'),('Judo Zielińscy Kwidzyn','Kwidzyn','2014-01-01',1900001,'pomorskie'),('KS Spartakus','Międzyrzecz',NULL,1900002,'lubuskie'),('LUKS przy OSP i SP nr 3','Kudowa Zdrój','1993-01-01',1900003,'dolnośląskie'),('Siedlecki Klub Sportowy Gladiator','Siedlce',NULL,1900004,'mazowieckie'),('Towarzystwo Sportowe \"Gwardia\" Olsztyn','Olsztyn','2005-01-01',2000001,'warmińsko-mazurskie'),('KS DRAGON Kwidzyn','Kwidzyn','2020-01-01',2000002,'pomorskie'),('UKS Progress','Warszawa','2015-01-01',2000003,'mazowieckie'),('ULKS \"28\" we Włyniu','Xxxxxx','2010-01-01',2000004,'łódzkie'),('KS Bieżanowianka','Kraków','1925-01-01',2000005,'małopolskie'),('UKS Niska','Warszawa',NULL,2000006,'mazowieckie'),('WKS Gymsport','Wrocław','2012-01-01',2000007,'dolnośląskie'),('Klub Sportowy \"BUDOWLANI\" Łódź','Łódź','1948-01-01',2000008,'łódzkie'),('FIGHTMAN','Bochnia','2010-01-01',2100001,'małopolskie'),('Klub Judo Shamo Ełk','Ełk','2017-01-01',2100002,'warmińsko-mazurskie'),('Polska Federacja Ju-jitsu i Kobudo','Jaworzno','1993-01-01',2100003,'śląskie'),('UKS JUDO','Jelcz-Laskowice',NULL,2100004,'dolnośląskie'),('LUKS POGOŃ Czartowczyk','Czartowczyk',NULL,2100005,'podkarpackie'),('GKS ARMATY','Stoczek Łukowski',NULL,2100006,'lubelskie'),('NISKA','Warszawa',NULL,2100007,'');
/*!40000 ALTER TABLE `clubs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-18 18:28:32
