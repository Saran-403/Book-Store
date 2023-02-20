-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 19, 2022 at 06:10 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `abc_store`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_login_details`
--

CREATE TABLE `admin_login_details` (
  `admin` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `login_date` date DEFAULT NULL,
  `login_time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_login_details`
--

INSERT INTO `admin_login_details` (`admin`, `password`, `login_date`, `login_time`) VALUES
('walter', 'albino', '2022-04-19', '15:08:07'),
('walter', 'albino', '2022-04-19', '15:10:42'),
('walter', 'albino', '2022-04-19', '15:14:37'),
('walter', 'admin', '2022-04-19', '17:52:08'),
('walter', 'albino', '2022-04-19', '17:59:53'),
('walter', 'albino', '2022-04-19', '18:01:31'),
('walter', 'albino', '2022-04-19', '18:05:16'),
('walter', 'albino', '2022-04-19', '18:18:22'),
('walter', 'albino', '2022-04-19', '18:20:25'),
('walter', 'albino', '2022-04-19', '18:23:04'),
('walter', 'albino', '2022-04-19', '18:35:35'),
('walter', 'albino', '2022-04-19', '18:38:08'),
('walter', 'albino', '2022-04-19', '18:40:10'),
('walter', 'albino', '2022-04-19', '18:43:57'),
('walter', 'albino', '2022-04-19', '18:46:16'),
('walter', 'albino', '2022-04-19', '18:47:08'),
('walter', 'albino', '2022-04-19', '18:49:01'),
('walter', 'albino', '2022-04-19', '18:54:46'),
('walter', 'albino', '2022-04-19', '18:59:00'),
('walter', 'albino', '2022-04-19', '19:01:11'),
('walter', 'albino', '2022-04-19', '19:02:58'),
('walter', 'albino', '2022-04-19', '19:04:14'),
('walter', 'albino', '2022-04-19', '19:49:38'),
('charlie', 'great_den', '2022-04-19', '20:39:33');

-- --------------------------------------------------------

--
-- Table structure for table `books_info`
--

CREATE TABLE `books_info` (
  `book_no` int(50) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `subject_code` varchar(50) DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  `publisher` varchar(50) DEFAULT NULL,
  `price` decimal(60,2) DEFAULT NULL,
  `quantity` int(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `genre` char(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books_info`
--

INSERT INTO `books_info` (`book_no`, `title`, `subject_code`, `author`, `publisher`, `price`, `quantity`, `location`, `genre`, `description`) VALUES
(1689, 'Ulysses', '1679', 'James Joyce', 'Shakespeare and Company', '2300.00', 8, 'Dublin', 'Fiction', 'talk about modern changes'),
(2304, 'Beloved', 'H567', 'Toni Morrison', 'Alfred A. Knopf Inc.', '2300.00', 5, 'Africa', 'Magical Realism', 'it tells the story of a family of formerly enslaved people');

-- --------------------------------------------------------

--
-- Table structure for table `chapters`
--

CREATE TABLE `chapters` (
  `book_no` int(50) DEFAULT NULL,
  `chapter_no` varchar(20) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `starting_page_no` int(30) DEFAULT NULL,
  `ending_page_no` int(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chapters`
--

INSERT INTO `chapters` (`book_no`, `chapter_no`, `title`, `starting_page_no`, `ending_page_no`) VALUES
(13, '3', 'false', 6, 35),
(1678, '2', 'Truth', 34, 42);

-- --------------------------------------------------------

--
-- Table structure for table `customer_login_details`
--

CREATE TABLE `customer_login_details` (
  `user` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `login_date` date DEFAULT NULL,
  `login_time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `subject_code` varchar(50) NOT NULL,
  `name` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`subject_code`, `name`) VALUES
('23', 'we'),
('1679', 'Novel');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books_info`
--
ALTER TABLE `books_info`
  ADD PRIMARY KEY (`book_no`);

--
-- Indexes for table `chapters`
--
ALTER TABLE `chapters`
  ADD KEY `book_no` (`book_no`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD KEY `subject_code` (`subject_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
