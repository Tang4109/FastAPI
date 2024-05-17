from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `clas` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL  COMMENT '班组名称'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `employee` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL  COMMENT '姓名',
    `pwd` VARCHAR(32) NOT NULL  COMMENT '密码',
    `eno` INT NOT NULL  COMMENT '编号',
    `clas_id` INT NOT NULL,
    CONSTRAINT `fk_employee_clas_7e83148e` FOREIGN KEY (`clas_id`) REFERENCES `clas` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `leader` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL  COMMENT '姓名',
    `pwd` VARCHAR(32) NOT NULL  COMMENT '密码',
    `lno` INT NOT NULL  COMMENT '领导编号'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `project` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL  COMMENT '工程名称',
    `addr` VARCHAR(32) NOT NULL  COMMENT '办公室' DEFAULT '',
    `leader_id` INT NOT NULL,
    CONSTRAINT `fk_project_leader_04b5e3bb` FOREIGN KEY (`leader_id`) REFERENCES `leader` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `employee_project` (
    `employee_id` INT NOT NULL,
    `project_id` INT NOT NULL,
    FOREIGN KEY (`employee_id`) REFERENCES `employee` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`project_id`) REFERENCES `project` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
