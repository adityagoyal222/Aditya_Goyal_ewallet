-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: ewallet
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `normal_account`
--

DROP TABLE IF EXISTS `normal_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `normal_account` (
  `username` varchar(100) DEFAULT NULL,
  `account_id` int NOT NULL AUTO_INCREMENT,
  `balance` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`account_id`),
  KEY `username` (`username`),
  CONSTRAINT `normal_account_ibfk_1` FOREIGN KEY (`username`) REFERENCES `normal_user` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_account`
--

LOCK TABLES `normal_account` WRITE;
/*!40000 ALTER TABLE `normal_account` DISABLE KEYS */;
INSERT INTO `normal_account` VALUES ('aditya',1,1000),('AdityaGoyal',2,0),('a',3,2503.14),('b',4,2304);
/*!40000 ALTER TABLE `normal_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normal_user`
--

DROP TABLE IF EXISTS `normal_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `normal_user` (
  `username` varchar(100) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normal_user`
--

LOCK TABLES `normal_user` WRITE;
/*!40000 ALTER TABLE `normal_user` DISABLE KEYS */;
INSERT INTO `normal_user` VALUES ('a','a','a','a','a'),('aditya','Aditya Goyal','password','9801181121','goyaladitya85@gmail.com'),('AdityaGoyal','Aditya Goyal','123456','934865207','kgbdjs'),('b','b','b','b','b');
/*!40000 ALTER TABLE `normal_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_account`
--

DROP TABLE IF EXISTS `service_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_account` (
  `servicename` varchar(100) NOT NULL,
  `servicetype` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `balance` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`servicename`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_account`
--

LOCK TABLES `service_account` WRITE;
/*!40000 ALTER TABLE `service_account` DISABLE KEYS */;
INSERT INTO `service_account` VALUES ('Nepal Electricity Board','Electricity','98028743569','neb@gov.np',0),('Water Department','Water','2435623445','akgthejkdn',0);
/*!40000 ALTER TABLE `service_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction` (
  `account_id` int DEFAULT NULL,
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `detail` varchar(300) NOT NULL,
  `amount` float NOT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `account_id` (`account_id`),
  CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `normal_account` (`account_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (3,1,'Amount was loaded to wallet from Janata Bank Account No. 1234.',500),(3,2,'Amount was loaded to wallet from Century Bank Account No. 4567.',750),(3,3,'Amount was loaded to wallet from Bank of Kathmandu Account No. 2020.',250),(3,4,'Paid money to aditya through e-wallet.',500),(1,5,'Received money from a through e-wallet.',500),(3,6,'Paid money to aditya through e-wallet.',500),(1,7,'Received money from a through e-wallet.',500),(3,8,'Paid money to Nepal Electricity Board for their service through e-wallet.',500),(3,9,'Amount was loaded to wallet from Janata Bank Account No. 8273059.',500),(3,10,'Paid money to Nepal Electricity Board for their service through e-wallet.',250),(3,11,'Received cashback from Nepal Electricity Board through e-wallet.',5),(3,12,'Paid money to Nepal Electricity Board for their service through e-wallet.',250),(3,13,'Received cashback from Nepal Electricity Board through e-wallet.',5),(3,14,'Paid money to Nepal Electricity Board for their service through e-wallet.',7),(3,15,'Received cashback from Nepal Electricity Board through e-wallet.',0.14),(4,16,'Amount was loaded to wallet from Janata Bank Account No. 347528697.',5000),(4,17,'Transferred money to a through e-wallet.',2500),(3,18,'Received money from b through e-wallet.',2500),(4,19,'Paid money to Nepal Electricity Board for their service through e-wallet.',200),(4,20,'Received cashback from Nepal Electricity Board through e-wallet.',4);
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-24 12:02:04
