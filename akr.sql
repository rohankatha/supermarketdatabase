DROP DATABASE IF EXISTS `SUPERMARKETS`;
CREATE SCHEMA `SUPERMARKETS`;
USE `SUPERMARKETS`;
DROP TABLE IF EXISTS `DEPARTMENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;


--
-- Table structure for table `EMPLOYEE`
--

DROP TABLE IF EXISTS `EMPLOYEE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMPLOYEE` (
  `FNAME` varchar(15) NOT NULL,
  `MINIT` varchar(15) NOT NULL,
  `LNAME` varchar(15) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `EMPLOYEE_ID` char(15) NOT NULL,
  `ADDRESS` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`EMPLOYEE_ID`)
  /*CONSTRAINT `DEPENDENT_ibfk_1` FOREIGN KEY (`Essn`) REFERENCES `EMPLOYEE` (`Ssn`)*/
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMPLOYEE`
--

LOCK TABLES `EMPLOYEE` WRITE;
/*!40000 ALTER TABLE `EMPLOYEE` DISABLE KEYS */;

INSERT INTO `EMPLOYEE` VALUES ('John','smith','peter','1988-12-30','1','railwaystationroad'),('katha','rohan','reddy','2003-1-24','2','hullabrige'),('kiran','bhumi','reddy','2023-1-24','3','hullabrige');
/*!40000 ALTER TABLE `EMPLOYEE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PRODUCT`
--
CREATE TABLE `DEPARTMENT` (
  `DEPARTMENT_ID` int(11) NOT NULL,
  `EMPLOYEE_IN_DEPT` char(15) NOT NULL,
  
  PRIMARY KEY (`DEPARTMENT_ID`),
  
  CONSTRAINT `DEPARTMENT_ibfk_1` FOREIGN KEY (`EMPLOYEE_IN_DEPT`) REFERENCES `EMPLOYEE` (`EMPLOYEE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `DEPARTMENT` WRITE;

INSERT INTO `DEPARTMENT` VALUES ('1','1'),('28','2'),('4','3');
/*!40000 ALTER TABLE `DEPARTMENT` ENABLE KEYS */;
UNLOCK TABLES;
DROP TABLE IF EXISTS `PRODUCT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PRODUCT` (
  `MAXIMUM_RETAIL_PRICE` int(11) NOT NULL,
  `NAME_OF_THE_PRODUCT` varchar(55) NOT NULL,
  `BEST_BEFORE` int(11) NOT NULL,
  `MANUFACTURING_DATE` DATE DEFAULT NULL,
  `OFFER_PERCENTAGE` int(11) DEFAULT NULL,
  `QUNATITY_OF_THE_PRODUCT` varchar(15) NOT NULL,
  `PRODUCT_IN_DEPT` int(11) NOT NULL,
  PRIMARY KEY (`NAME_OF_THE_PRODUCT`),
  CONSTRAINT `PRODUCT_ibfk_1` FOREIGN KEY (`PRODUCT_IN_DEPT`) REFERENCES `DEPARTMENT` (`DEPARTMENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PRODUCT`
--

LOCK TABLES `PRODUCT` WRITE;
/*!40000 ALTER TABLE `PRODUCT` DISABLE KEYS */;
INSERT INTO `PRODUCT` VALUES (349,'colgate toothpaste',3,'2020-2-19',20,32,1),(3900,'Pepsi toothpaste',3,'2010-2-9',21,32,28),(100,'rexona ',9,'1998-7-29',20,32,4);
/*!40000 ALTER TABLE `PRODUCT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMPLOYEE`
--

DROP TABLE IF EXISTS `CUSTOMER_WITH_CARD`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CUSTOMER_WITH_CARD` (
  `USER_ID` int(9) NOT NULL,
  `NAME` varchar(20) NOT NULL,
  `RATING` int(2) DEFAULT NULL,
  `PRODUCTS` varchar(300) DEFAULT NULL,
  
  PRIMARY KEY (`USER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CUSTOMER_WITH_CARD`
--



/*!40000 ALTER TABLE `EMPLOYEE` DISABLE KEYS */;

INSERT INTO `CUSTOMER_WITH_CARD` VALUES (1,'john',5,'SOAP,TOOTHPASTE'),(2,'jACK',0,'CART,BREAD'),(4,'SASUKE',1,'SWORD,SUGAR');
/*!40000 ALTER TABLE `EMPLOYEE` ENABLE KEYS */;



DROP TABLE IF EXISTS `BRANCH`;

CREATE TABLE `BRANCH` (
  `ADDRESS` varchar(15) NOT NULL,
  `BRANCH_ID` int(11) NOT NULL,
  `EMPLOYEES` varchar(15) DEFAULT NULL,
  
  PRIMARY KEY (`BRANCH_ID`)
  
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BRANCH`
--



INSERT INTO `BRANCH` VALUES ('ProductX',1,'Bellaire'),('ProductY',2,'Sugarland'),('ProductZ',3,'Houston'),('Computerization',10,'Stafford');

DROP TABLE IF EXISTS `STOCK_MANAGEMENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `STOCK_MANAGEMENT` (
  `NUMBER_OF_PRODUCTS_ARRIVED` int(11) NOT NULL,
  `DATE` date NOT NULL,
  `NUMBERS_OF_PRODUCTS_SOLD` int(11) DEFAULT NULL,
  PRIMARY KEY (`DATE`)
 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `STOCK_MANAGEMENT` VALUES (21,'2001-6-9',20),(2,'2013-3-11',20),(21,'2003-4-12',34),(11,'2003-4-2',19);



