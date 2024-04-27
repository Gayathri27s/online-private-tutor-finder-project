-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 20, 2024 at 03:08 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `2privatetutor`
--

-- --------------------------------------------------------

--
-- Table structure for table `feedtb`
--

CREATE TABLE `feedtb` (
  `id` bigint(10) NOT NULL auto_increment,
  `SName` varchar(250) NOT NULL,
  `TName` varchar(250) NOT NULL,
  `Feed` varchar(250) NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `feedtb`
--

INSERT INTO `feedtb` (`id`, `SName`, `TName`, `Feed`, `Date`) VALUES
(1, 'sangeeth', 'san', 'good', '2024-01-20');

-- --------------------------------------------------------

--
-- Table structure for table `jointb`
--

CREATE TABLE `jointb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Sname` varchar(250) NOT NULL,
  `Tname` varchar(250) NOT NULL,
  `SubjectName` varchar(250) NOT NULL,
  `Sch` varchar(250) NOT NULL,
  `Duration` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `Sdate` date NOT NULL,
  `Edate` date NOT NULL,
  `CardName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `jointb`
--

INSERT INTO `jointb` (`id`, `Sname`, `Tname`, `SubjectName`, `Sch`, `Duration`, `Amount`, `Sdate`, `Edate`, `CardName`) VALUES
(1, 'sangeeth', 'san', 'Data Science', '10AM To 12PM', '1', '2000', '2024-01-20', '2024-02-19', 'MASTERCARD'),
(2, 'sangeeth', 'san', 'Data Science', '1PM To 2PM', '2', '60000', '2024-01-20', '2024-03-20', 'MASTERCARD');

-- --------------------------------------------------------

--
-- Table structure for table `schdtb`
--

CREATE TABLE `schdtb` (
  `id` bigint(10) NOT NULL auto_increment,
  `TName` varchar(250) NOT NULL,
  `ClassName` varchar(250) NOT NULL,
  `SubjectName` varchar(250) NOT NULL,
  `Schedu` varchar(250) NOT NULL,
  `Duration` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `Info` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `schdtb`
--

INSERT INTO `schdtb` (`id`, `TName`, `ClassName`, `SubjectName`, `Schedu`, `Duration`, `Amount`, `Info`) VALUES
(1, 'san', 'MSC', 'Data Science', '10AM To 12PM', '1', '2000', 'python '),
(2, 'san', 'MSC', 'Data Science', '1PM To 2PM', '2', '60000', 'master Data Science');

-- --------------------------------------------------------

--
-- Table structure for table `studenttb`
--

CREATE TABLE `studenttb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `studenttb`
--

INSERT INTO `studenttb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'sangeeth Kumar', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'sangeeth', 'sangeeth');

-- --------------------------------------------------------

--
-- Table structure for table `tutortb`
--

CREATE TABLE `tutortb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `Education` varchar(500) NOT NULL,
  `About` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tutortb`
--

INSERT INTO `tutortb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `Education`, `About`, `UserName`, `Password`) VALUES
(3, 'sangeeth Kumar', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'BE,ME', 'Image Processing,Data Sci', 'san', 'san');
