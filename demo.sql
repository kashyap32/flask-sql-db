-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema demo_flask_login_registration
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema demo_flask_login_registration
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `demo_flask_login_registration` DEFAULT CHARACTER SET utf8 ;
USE `demo_flask_login_registration` ;

-- -----------------------------------------------------
-- Table `demo_flask_login_registration`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `demo_flask_login_registration`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 18
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
