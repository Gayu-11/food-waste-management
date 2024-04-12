-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 13, 2024 at 01:48 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `food_waste`
--

-- --------------------------------------------------------

--
-- Table structure for table `fo_admin`
--

CREATE TABLE `fo_admin` (
  `id` varchar(50) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fo_admin`
--

INSERT INTO `fo_admin` (`id`, `username`, `password`) VALUES
('1', 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `fo_booking`
--

CREATE TABLE `fo_booking` (
  `id` int(50) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `user_mobile` bigint(20) NOT NULL,
  `user_email` varchar(30) NOT NULL,
  `user_address` varchar(100) NOT NULL,
  `pro_place` varchar(40) NOT NULL,
  `pro_address` varchar(100) NOT NULL,
  `food_type` varchar(20) NOT NULL,
  `quantity` int(20) NOT NULL,
  `pro_username` varchar(20) NOT NULL,
  `pro_mobile` bigint(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `book_date` varchar(20) NOT NULL,
  `action` int(5) NOT NULL,
  `post_date` varchar(20) NOT NULL,
  `post_time` varchar(20) NOT NULL,
  `post_id` int(10) NOT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fo_booking`
--

INSERT INTO `fo_booking` (`id`, `user_name`, `user_mobile`, `user_email`, `user_address`, `pro_place`, `pro_address`, `food_type`, `quantity`, `pro_username`, `pro_mobile`, `username`, `book_date`, `action`, `post_date`, `post_time`, `post_id`) VALUES
(1, 'yuvan', 8148956634, 'huwaidom@gmail.com', '177, Chennai trunk road, Taluk, Srirangam, Thiruvanaikoil', 'Hotel', 'No. 131, Ammamandapam Rd, Srirangam, Tiruchirappalli', 'break_fast', 23, 'klj', 8148956634, 'yu', 'February 04, 2024', 0, 'February 04, 2024', '', 2),
(2, 'yuvan', 8148956634, 'huwaidom@gmail.com', '177, Chennai trunk road, Taluk, Srirangam, Thiruvanaikoil', 'Hotel', 'No. 131, Ammamandapam Rd, Srirangam, Tiruchirappalli', 'break_fast', 23, 'klj', 8148956634, 'yu', 'February 04, 2024', 0, 'February 04, 2024', '', 2),
(3, 'yuvan', 8148956634, 'huwaidom@gmail.com', '177, Chennai trunk road, Taluk, Srirangam, Thiruvanaikoil', 'Hotel', 'No. 131, Ammamandapam Rd, Srirangam, Tiruchirappalli', 'break_fast', 12, 'klj', 8148956634, 'yu', 'February 04, 2024', 0, 'February 04, 2024', '', 3),
(4, 'io', 9589859587, 'gfw@gmail.com', '28, Kuttiambalakaranpatti, Udayanpatti, K K Nagar, Tiruchirappalli', 'hall', '28, Kuttiambalakaranpatti, Udayanpatti, K K Nagar, Tiruchirappalli', 'break_fast', 12, 'huyyt', 8148956634, 'io', 'February 08, 2024', 1, 'February 08, 2024', '', 10);

-- --------------------------------------------------------

--
-- Table structure for table `fo_donate`
--

CREATE TABLE `fo_donate` (
  `id` int(20) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `username1` varchar(20) NOT NULL,
  `user_address` varchar(100) NOT NULL,
  `user_mobile` bigint(20) NOT NULL,
  `food_type` varchar(20) NOT NULL,
  `quantity` int(20) NOT NULL,
  `pro_name` varchar(20) NOT NULL,
  `pro_place` varchar(30) NOT NULL,
  `pro_address` varchar(100) NOT NULL,
  `pro_mobile` bigint(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `donate_date` varchar(20) NOT NULL,
  `user_email` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fo_donate`
--

INSERT INTO `fo_donate` (`id`, `user_name`, `username1`, `user_address`, `user_mobile`, `food_type`, `quantity`, `pro_name`, `pro_place`, `pro_address`, `pro_mobile`, `username`, `donate_date`, `user_email`) VALUES
(1, 'Ajay', 'aj', '52, to str, joy nagar, karur', 9098787346, 'lunch', 20, 'Sethu', 'Kani hotel', '12, Y2r Street, V.nagar, Karur', 9098787656, 'sethu', 'January 31, 2024', ''),
(2, 'Ajay', 'aj', '52, to str, joy nagar, karur', 9098787346, 'lunch', 20, 'Ram', 'Taj hall', '39, yr str, yahzl nagar, karur', 7890986767, 'ram', 'January 31, 2024', ''),
(3, 'John', 'jo', '34, u str, Nungambakam, karur', 9098787690, 'lunch', 45, 'Ram', 'Taj hall', '39, yr str, yahzl nagar, karur', 7890986767, 'ram', 'February 01, 2024', ''),
(4, 'John', 'jo', '34, u str, Nungambakam, karur', 9098787690, 'lunch', 55, 'Sethu', 'Kani hotel', '12, Y2r Street, V.nagar, Karur', 9098787656, 'sethu', 'February 01, 2024', ''),
(5, 'John', 'jo', '34, u str, Nungambakam, karur', 8148956634, 'lunch', 11, 'Sethu', 'Kani hotel', '12, Y2r Street, V.nagar, Karur', 9098787656, 'sethu', 'February 01, 2024', ''),
(6, 'Abinaya', 'abi', '67,str,karur', 8525923082, 'break_fast', 20, 'Ram', 'Taj hall', '39, yr str, yahzl nagar, karur', 7890986767, 'ram', 'February 02, 2024', ''),
(7, 'sankar', 'san', 'No . 41/87, Akila Nagar, 4th St', 9098675667, 'lunch', 20, 'jo', 'hai hall', '45,jhd,nagar', 8778890977, 'aj', 'February 02, 2024', ''),
(8, 'sankar', 'san', 'No . 41/87, Akila Nagar, 4th St', 9098675667, 'break_fast', 20, 'jo', 'hai hall', '45,jhd,nagar', 8778890977, 'aj', 'February 02, 2024', ''),
(9, 'jo', 'jo', '177, Chennai trunk road, Taluk, Srirangam, Thiruvanaikoil', 8778890978, 'break_fast', 23, 'jo', 'hai hall', '45,jhd,nagar', 8778890977, 'aj', 'February 02, 2024', ''),
(10, 'jo', 'jo', '177, Chennai trunk road, Taluk, Srirangam, Thiruvanaikoil', 8778890978, 'break_fast', 20, 'jo', 'hai hall', '45,jhd,nagar', 8778890977, 'aj', 'February 02, 2024', ''),
(11, 'jo', 'jo', '177, Chennai trunk road, Taluk, Srirangam, Thiruvanaikoil', 8148956634, 'break_fast', 20, 'jo', 'hai hall', '45,jhd,nagar', 8778890977, 'aj', 'February 02, 2024', ''),
(12, 'jo', 'jo', '177, Chennai trunk road, Taluk, Srirangam, Thiruvanaikoil', 8148956634, 'break_fast', 20, 'jo', 'hai hall', '45,jhd,nagar', 8778890977, 'aj', 'February 03, 2024', '8148956634'),
(13, 'yuvan', 'yu', '177, Chennai trunk road, Taluk, Srirangam, Thiruvanaikoil', 8148956634, 'lunch', 20, 'man', 'Hotel', 'No. 131, Ammamandapam Rd, Srirangam, Tiruchirappalli', 8148956634, 'klj', 'February 05, 2024', 'huwaidom@gmail.com'),
(14, 'io', 'io', '28, Kuttiambalakaranpatti, Udayanpatti, K K Nagar, Tiruchirappalli', 9589859587, 'break_fast', 12, 'ttt', 'hall', '28, Kuttiambalakaranpatti, Udayanpatti, K K Nagar, Tiruchirappalli', 8148956634, 'huyyt', 'February 08, 2024', 'gfw@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `fo_food`
--

CREATE TABLE `fo_food` (
  `id` int(30) NOT NULL,
  `food_type` varchar(10) NOT NULL,
  `food_item` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fo_food`
--

INSERT INTO `fo_food` (`id`, `food_type`, `food_item`) VALUES
(1, 'break_fast', 'Idly'),
(2, 'break_fast', 'Dosa'),
(3, 'break_fast', 'Vadai'),
(4, 'break_fast', 'Kesari'),
(5, 'break_fast', 'Puri'),
(6, 'break_fast', 'Pongal'),
(7, 'lunch', 'Chicken biryani'),
(8, 'lunch', 'Mutton biryani'),
(9, 'lunch', 'Sambar'),
(10, 'lunch', 'Rasam'),
(11, 'lunch', 'Brinjal salsa'),
(12, 'dinner', 'Chapathi');

-- --------------------------------------------------------

--
-- Table structure for table `fo_need`
--

CREATE TABLE `fo_need` (
  `id` int(20) NOT NULL,
  `user_name` varchar(30) NOT NULL,
  `user_address` varchar(100) NOT NULL,
  `user_mobile` bigint(20) NOT NULL,
  `user_email` varchar(30) NOT NULL,
  `food_type` varchar(30) NOT NULL,
  `quantity` int(20) NOT NULL,
  `post_date` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fo_need`
--


-- --------------------------------------------------------

--
-- Table structure for table `fo_post`
--

CREATE TABLE `fo_post` (
  `id` int(50) NOT NULL,
  `food_type` varchar(20) NOT NULL,
  `quantity` int(20) NOT NULL,
  `message` varchar(100) NOT NULL,
  `place` varchar(30) NOT NULL,
  `name` varchar(30) NOT NULL,
  `address` varchar(100) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `post_date` varchar(20) NOT NULL,
  `post_time` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `post_id` int(10) NOT NULL,
  `city` varchar(30) NOT NULL,
  `latitude` varchar(30) NOT NULL,
  `longitude` varchar(30) NOT NULL,
  `food_item` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fo_post`
--

INSERT INTO `fo_post` (`id`, `food_type`, `quantity`, `message`, `place`, `name`, `address`, `mobile`, `post_date`, `post_time`, `username`, `post_id`, `city`, `latitude`, `longitude`, `food_item`) VALUES
(10, 'break_fast', 12, 'ssas', 'hall', 'ttt', '28, Kuttiambalakaranpatti, Udayanpatti, K K Nagar, Tiruchirappalli', 8148956634, 'February 08, 2024', '04:57 PM', 'huyyt', 0, '', '10.60772038', '78.42581940', '');

-- --------------------------------------------------------

--
-- Table structure for table `fo_provider`
--

CREATE TABLE `fo_provider` (
  `id` int(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `name` varchar(20) NOT NULL,
  `address` varchar(100) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `reg_date` date NOT NULL,
  `action` int(5) NOT NULL,
  `latitude` varchar(30) NOT NULL,
  `longitude` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fo_provider`
--

INSERT INTO `fo_provider` (`id`, `place`, `name`, `address`, `mobile`, `email`, `username`, `password`, `reg_date`, `action`, `latitude`, `longitude`, `city`) VALUES
(1, 'Hotel', 'man', 'No. 131, Ammamandapam Rd, Srirangam, Tiruchirappalli', 8148956634, 'huwaidom@gmail.com', 'klj', '1234', '2024-02-24', 1, '10.8155 ', '78.69651', ''),
(2, 'hall', 'geo', 'No.3354, Shivaram Nagar, Bikshandarkoil, Tamil Nadu', 8148956634, 'hj@gmail.com', 'geo', '1234', '2024-02-26', 1, '11.00599003', '77.56089783', ''),
(3, 'Lo hotel', 'nani', '4/15, Srinivasa Nagar N Ext, Srirangam, Thiruvanaikoil, Tiruchirappalli', 8148956634, 'huwaidom@gmail.com', 'nani', '1234', '2024-02-24', 1, '10.72056961', '77.87950897', ''),
(4, 'hall', 'ttt', '28, Kuttiambalakaranpatti, Udayanpatti, K K Nagar, Tiruchirappalli', 8148956634, 'huwaidom@gmail.com', 'huyyt', '1234', '2024-02-24', 1, '10.60772038', '78.42581940', ''),
(5, 'hotel', 'ioioi', 'No.3354, Shivaram Nagar, Bikshandarkoil, Tamil Nadu', 8148956634, 'yyjt@gmail.com', 'yy', '1234', '2024-02-24', 1, '10.10501003', '78.11335754', '');

-- --------------------------------------------------------

--
-- Table structure for table `fo_user`
--

CREATE TABLE `fo_user` (
  `id` int(50) NOT NULL,
  `org_name` varchar(50) NOT NULL,
  `name` varchar(20) NOT NULL,
  `address` varchar(100) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `reg_date` date NOT NULL,
  `action` int(5) NOT NULL,
  `latitude` varchar(30) NOT NULL,
  `longitude` varchar(30) NOT NULL,
  `status` int(5) NOT NULL,
  `city` varchar(30) NOT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fo_user`
--

INSERT INTO `fo_user` (`id`, `org_name`, `name`, `address`, `mobile`, `email`, `username`, `password`, `reg_date`, `action`, `latitude`, `longitude`, `status`, `city`) VALUES
(1, ' A orphanage', 'yuvan', '177, Chennai trunk road, Taluk, Srirangam, Thiruvanaikoil', 8148956634, 'huwaidom@gmail.com', 'yu', '1234', '2024-02-02', 1, '10.8155', '78.69651', 0, 'Trichy'),
(2, 'B orphanage', 'sankar', 'No.3354, Shivaram Nagar, Bikshandarkoil, Tamil Nadu', 9098675667, 'huwaidom@gmail.com', 'san', '1234', '2024-02-02', 1, '11.00599003', '77.56089783', 0, 'karur'),
(3, 'C orphanage', 'dany', '19, 34, Chandra Nagar St, Periyar Nagar, Tiruchirappalli', 9089675645, 'jai@gmail.com', 'dan', '1234', '2024-02-02', 1, '11.11540985', '77.35456085', 0, 'Trichy'),
(4, 'D orphanage', 'Madhan', 'RP2Q+XM2, Vivek Nagar, Pappakurichi Kattur, Tiruchirappalli', 8148956634, 'huwaidom@gmail.com', 'mad', '1234', '2024-02-02', 1, '11.07750988', '77.88362885', 0, 'Trichy'),
(5, 'E orphanage', 'Harsh', '4/15, Srinivasa Nagar N Ext, Srirangam, Thiruvanaikoil, Tiruchirappalli', 8148956634, 'huwaidom@gmail.com', 'harsh', '1234', '2024-02-08', 1, '10.79426003', '77.71150208', 0, 'karur'),
(6, 'F orphanage', 'Muthu', '28, Kuttiambalakaranpatti, Udayanpatti, K K Nagar, Tiruchirappalli', 9589859590, 'hs@gmail.com', 'muthu', '1234', '2024-02-03', 1, '11.10824966', '78.00112915', 0, 'Trichy'),
(7, ' G orphanage', 'the', 'No. 131, Ammamandapam Rd, Srirangam, Tiruchirappalli', 8148956634, 'huwaidom@gmail.com', 'the', '1234', '2024-02-15', 1, '10.73828030', '77.53222656', 0, ''),
(8, 'Orphanage', 'run', '28, Kuttiambalakaranpatti, Udayanpatti, K K Nagar, Tiruchirappalli', 9589859590, 'hs@gmail.com', 'ro', '1234', '2024-02-03', 1, '10.95771027', '78.08094788', 0, ''),
(9, 'Orphanage', 'was', '4/15, Srinivasa Nagar N Ext, Srirangam, Thiruvanaikoil, Tiruchirappalli', 8148956634, 'huwaidom@gmail.com', 'was', '1234', '2024-02-08', 1, '10.72056961', '77.87950897', 0, ''),
(10, 'Orphanage', 'jack', '28, Kuttiambalakaranpatti, Udayanpatti, K K Nagar, Tiruchirappalli', 9589859590, 'hs1@gmail.com', 'jac', '1234', '2024-02-21', 1, '11.05935955', '78.13964844', 0, ''),
(11, 'Orphanage', 'farzi', '4/15, Srinivasa Nagar N Ext, Srirangam, Thiruvanaikoil, Tiruchirappalli', 8148956634, 'huwaidom@gmail.com', 'far', '1234', '2024-02-24', 1, '11.15217018', '78.21205139', 0, ''),
(12, 'Orphanage', 'io', '28, Kuttiambalakaranpatti, Udayanpatti, K K Nagar, Tiruchirappalli', 8148956634, 'huwaidom@gmail.com', 'io', '1234', '2024-02-24', 1, '11.14671040', '78.28996277', 0, ''),
(13, 'Fertilizer company', 'david', 'Kela Mettu Street, Lakshmi Nagar, No 1 Tollgate, Tiruchirappalli', 8148956634, 'huwaidom@gmail.com', 'dav', '1234', '2024-02-08', 1, '10.45034027', '77.52089691', 0, ''),
(14, 'Orphanage', 'little', 'No. 131, Ammamandapam Rd, Srirangam, Tiruchirappalli', 8148956634, 'huwaidom@gmail.com', 'dan', '1234', '2024-02-02', 1, '10.93486977', '78.41251373', 0, ''),
(15, 'Fertilizer company', 'jan', '28, Kuttiambalakaranpatti, Udayanpatti, K K Nagar, Tiruchirappalli', 9589859587, 'iuu@gmail.com', 'pl', '1234', '2024-02-03', 1, '11.12417030', '78.44915771', 0, ''),
(16, 'orphanage', 'art', 'VPH7+F66, 1, Tollgate, Annai Nagar, No 1 Tollgate, Bikshandarkoil, Tiruchirappalli', 9087566778, 'kl@gmail.com', 'war', '1234', '2024-02-24', 1234, '10.60772038', '78.42581940', 0, ''),
(17, 'Orphanage', 'pop', '136-2a/2b, Pudukottai Road, Gundur Village, Ramanathapuram Rd, Tiruchirappalli', 8977675690, 'haj@gmail.com', 'kop', '123', '2024-02-29', 1, '11.14968014', '78.59870148', 0, ''),
(18, 'Farmer', 'esaki', '4/15, Srinivasa Nagar N Ext, Srirangam, Thiruvanaikoil, Tiruchirappalli,', 6789095678, 'hgghs@gmail.com', 'uyef@gmail.com', '1234', '2024-02-14', 1, '10.53102016', '77.95018768', 0, '');
