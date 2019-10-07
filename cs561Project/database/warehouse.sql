/*
Navicat MySQL Data Transfer

Source Server         : 001
Source Server Version : 50016
Source Host           : localhost:3306
Source Database       : warehouse

Target Server Type    : MYSQL
Target Server Version : 50016
File Encoding         : 65001

Date: 2019-10-07 13:16:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for renter_account
-- ----------------------------
DROP TABLE IF EXISTS `renter_account`;
CREATE TABLE `renter_account` (
  `user_id` int(10) NOT NULL,
  `balance` float(200,0) default NULL,
  `rented_warehouse` int(11) default NULL,
  KEY `renter_account_ibfk_1` (`user_id`),
  CONSTRAINT `renter_account_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of renter_account
-- ----------------------------

-- ----------------------------
-- Table structure for rent_order
-- ----------------------------
DROP TABLE IF EXISTS `rent_order`;
CREATE TABLE `rent_order` (
  `order_id` int(10) NOT NULL,
  `user_id` int(10) default NULL,
  `order_date` datetime default NULL,
  PRIMARY KEY  (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of rent_order
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` int(10) NOT NULL,
  `username` varchar(150) default NULL,
  `password` varchar(128) default NULL,
  `last_login` datetime default NULL,
  `first_name` varchar(30) default NULL,
  `last_name` varchar(150) default NULL,
  `email` varchar(254) default NULL,
  PRIMARY KEY  (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user
-- ----------------------------

-- ----------------------------
-- Table structure for warehouse
-- ----------------------------
DROP TABLE IF EXISTS `warehouse`;
CREATE TABLE `warehouse` (
  `warehouse_id` int(11) NOT NULL,
  `warehouse_name` varchar(150) default NULL,
  `warehouse_size` int(10) default NULL,
  `warehouse_desc` varchar(254) default NULL,
  `warehouse_image` varchar(255) default NULL,
  `warehouse_price` double default NULL,
  `warehouse_category` varchar(150) default NULL,
  `warehouse_isAvailable` tinyint(1) default NULL,
  `warehouse_currentowenr_use_id` int(10) default NULL,
  PRIMARY KEY  (`warehouse_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of warehouse
-- ----------------------------
