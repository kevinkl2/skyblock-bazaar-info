DROP DATABASE IF EXISTS bazaar;
CREATE DATABASE bazaar;
USE bazaar;

DROP TABLE IF EXISTS `productStats`;
CREATE TABLE `productStats` (
	`ts` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `name` VARCHAR(255) NOT NULL,
    `lowestSellOrderPrice` DOUBLE,
    `highestBuyOrderPrice` DOUBLE,
    `profit` DOUBLE,
    `sellOrderVolume` DOUBLE NOT NULL,
    `buyOrderVolume` DOUBLE NOT NULL,
    `fulfilledSellOrderVolumeWeek` DOUBLE NOT NULL,
    `fulfilledBuyOrderVolumeWeek` DOUBLE NOT NULL,
	PRIMARY KEY (`ts`, `name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE INDEX name_index ON productStats(name);