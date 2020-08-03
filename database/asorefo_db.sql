-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 03, 2020 at 07:24 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `asorefo_db`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_api_consumer` (IN `first_name` VARCHAR(200), IN `last_name` VARCHAR(200), IN `username` VARCHAR(200), IN `email` VARCHAR(200), IN `phone` VARCHAR(200), IN `password` VARCHAR(200), IN `x_api_key` VARCHAR(200), IN `x_api_secret` VARCHAR(200))  NO SQL
BEGIN

INSERT INTO `api_consumers` ( `first_name`, `last_name`, `username`, `email`, `phone`, `password`, `x_api_key`, `x_api_secret`, `created_at`, `updated_at`) VALUES ( first_name, last_name, username, email, phone, password, x_api_key, x_api_secret, current_timestamp(), current_timestamp());

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `create_user_profile` (IN `first_name` VARCHAR(200), IN `last_name` VARCHAR(200), IN `email` VARCHAR(200), IN `password` VARCHAR(200))  NO SQL
BEGIN
	DECLARE last_insert_id varchar(11);

INSERT INTO `user_profile` ( `first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`) VALUES ( first_name, last_name, email, password, current_timestamp(), current_timestamp());
SELECT LAST_INSERT_ID() INTO last_insert_id;

-- SELECT last_insert_id;

 SELECT id, first_name, last_name, email FROM user_profile up WHERE up.id = last_insert_id;

END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `api_consumers`
--

CREATE TABLE `api_consumers` (
  `id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `password` varchar(100) NOT NULL,
  `x_api_key` varchar(100) NOT NULL,
  `x_api_secret` varchar(100) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `api_consumers`
--

INSERT INTO `api_consumers` (`id`, `first_name`, `last_name`, `username`, `email`, `phone`, `password`, `x_api_key`, `x_api_secret`, `created_at`, `updated_at`) VALUES
(14, 'KWABENA', 'AMPAH', 'KWABENA', 'AMPAH@GMAIL.COM', NULL, '0AF2103DC12EE1EE92B999DB862E8726DDF02CDD', '5729AD6D-F698-5C69-9624-F1E59FB44734', 'D6511B0B0351', '2020-08-02 19:31:49', '2020-08-02 19:31:49');

-- --------------------------------------------------------

--
-- Table structure for table `user_profile`
--

CREATE TABLE `user_profile` (
  `id` int(12) NOT NULL,
  `first_name` varchar(70) NOT NULL,
  `last_name` varchar(70) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_profile`
--

INSERT INTO `user_profile` (`id`, `first_name`, `last_name`, `email`, `phone`, `password`, `created_at`, `updated_at`) VALUES
(11, 'KWABENA', 'AMPAH', 'AMPAH@GMAIL.COM', NULL, '0AF2103DC12EE1EE92B999DB862E8726DDF02CDD', '2020-08-03 15:55:30', '2020-08-03 15:55:30');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `api_consumers`
--
ALTER TABLE `api_consumers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_profile`
--
ALTER TABLE `user_profile`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `api_consumers`
--
ALTER TABLE `api_consumers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `user_profile`
--
ALTER TABLE `user_profile`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
