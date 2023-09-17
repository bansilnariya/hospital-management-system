-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 17, 2023 at 06:28 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mydata`
--

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

CREATE TABLE `hospital` (
  `Nameoftables` varchar(255) NOT NULL,
  `Reference_No` int(255) NOT NULL,
  `dose` varchar(45) NOT NULL,
  `Numberoftablets` int(45) NOT NULL,
  `lot` varchar(45) NOT NULL,
  `issuedate` varchar(45) NOT NULL,
  `expdate` varchar(45) NOT NULL,
  `dailydose` varchar(45) NOT NULL,
  `sideEfect` varchar(45) NOT NULL,
  `FurtherInformation` varchar(45) NOT NULL,
  `DrivingUsingMachine` varchar(45) NOT NULL,
  `storage` varchar(45) NOT NULL,
  `HowToUseMedication` varchar(255) NOT NULL,
  `PatientId` int(255) NOT NULL,
  `nhsnumber` varchar(45) NOT NULL,
  `PatientName` varchar(45) NOT NULL,
  `DateOfBirth` varchar(45) NOT NULL,
  `patientaddress` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital`
--

INSERT INTO `hospital` (`Nameoftables`, `Reference_No`, `dose`, `Numberoftablets`, `lot`, `issuedate`, `expdate`, `dailydose`, `sideEfect`, `FurtherInformation`, `DrivingUsingMachine`, `storage`, `HowToUseMedication`, `PatientId`, `nhsnumber`, `PatientName`, `DateOfBirth`, `patientaddress`) VALUES
('Corona Vacacina', 1, 'CORONA VAC.', 10, '10', '20-01-2023', '20-01-2025', '1', 'NO EFFECT', 'STAY HOME', '130', 'NO ADVICE', 'NO', 2, 'NHS0123', 'xyz', '04-05-2003', 'abc,def'),
('Corona Vacacina', 33, 'CORONA', 100, '10', '12-12-2023', '12-12-2024', 'NO DOSE ', 'NO EFFECT', 'NO INFOPRMATION', '130', 'NO ADVICE', 'NO MEDITION ', 1711, 'NHS1711', 'abc', '17-11-2002', 'pqr,stu'),
('Adderall', 99, 'CORONA VACION', 10, 'NO', '12-12-2000', '12-12-2004', 'YES', 'NO EFFECT', 'NO ', 'O+', 'NO ', 'NO', 405, 'NHSNO0405', 'pqr', '04-05-1999', 'XYZ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hospital`
--
ALTER TABLE `hospital`
  ADD PRIMARY KEY (`Reference_No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hospital`
--
ALTER TABLE `hospital`
  MODIFY `Reference_No` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1003;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
