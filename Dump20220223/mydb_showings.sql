-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `showings`
--

DROP TABLE IF EXISTS `showings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `showings` (
  `idshowing` int NOT NULL AUTO_INCREMENT,
  `movies_idmovies` int NOT NULL,
  `time` datetime NOT NULL,
  `auditoriums_idauditorium` int NOT NULL,
  PRIMARY KEY (`idshowing`),
  KEY `fk_showings_movies_idx` (`movies_idmovies`),
  KEY `fk_showings_auditoriums1_idx` (`auditoriums_idauditorium`),
  CONSTRAINT `fk_showings_auditoriums1` FOREIGN KEY (`auditoriums_idauditorium`) REFERENCES `auditoriums` (`idauditorium`),
  CONSTRAINT `fk_showings_movies` FOREIGN KEY (`movies_idmovies`) REFERENCES `movies` (`idmovies`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `showings`
--

LOCK TABLES `showings` WRITE;
/*!40000 ALTER TABLE `showings` DISABLE KEYS */;
INSERT INTO `showings` VALUES (1,1,'2022-02-25 18:30:00',1),(2,3,'2022-02-27 09:00:00',2),(3,2,'2022-03-04 14:20:00',3),(4,2,'2022-04-04 15:30:00',2),(5,1,'2022-05-01 16:02:00',2),(6,3,'2022-04-08 13:00:00',2);
/*!40000 ALTER TABLE `showings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-23 14:14:39
