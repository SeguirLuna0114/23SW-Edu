use testdb;

CREATE TABLE `userTbl` 
( `userID` char(8) NOT NULL,
  `name` varchar(10) NOT NULL,
  `mobile` char(16) DEFAULT NULL,
  `gender` varchar(8) NOT NULL,
  `birth` int NOT NULL,
  `mDate` date DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;