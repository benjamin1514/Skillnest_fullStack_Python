-- =====================================================
-- CONFIGURACIÓN INICIAL
-- =====================================================
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- =====================================================
-- CREACIÓN DEL SCHEMA (Limpio para desarrollo)
-- =====================================================
DROP SCHEMA IF EXISTS `sistema_gimnasio`;
CREATE SCHEMA IF NOT EXISTS `sistema_gimnasio` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `sistema_gimnasio`;


CREATE TABLE `tipo_usuarios` (
    `id_tipo_usuario`          INT          NOT NULL AUTO_INCREMENT,
    `nombre_tipo_usuario`      VARCHAR(100) NOT NULL,
    `descripcion_tipo_usuario` VARCHAR(100) NOT NULL,
    `created_at`               DATETIME     DEFAULT CURRENT_TIMESTAMP,
    `updated_at`               DATETIME     DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `created_by`               INT          NULL,
    `deleted`                  TINYINT(1)   DEFAULT 0,
    PRIMARY KEY (`id_tipo_usuario`)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `tipo_plan_entrenamientos` (
    `id_tipo_plan_entrenamiento` INT          NOT NULL AUTO_INCREMENT,
    `nombre_tipo_plan`           VARCHAR(100) NOT NULL,
    `descripcion_tipo_plan`      VARCHAR(150) NOT NULL,
    `created_at`                 DATETIME     DEFAULT CURRENT_TIMESTAMP,
    `updated_at`                 DATETIME     DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `created_by`                 INT          NULL,
    `deleted`                    TINYINT(1)   DEFAULT 0,
    PRIMARY KEY (`id_tipo_plan_entrenamiento`)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `personas` (
    `id_persona`  INT         NOT NULL AUTO_INCREMENT,
    `nombre`      VARCHAR(20) NOT NULL,
    `apellido`    VARCHAR(20) NOT NULL,
    `created_at`  DATETIME    DEFAULT CURRENT_TIMESTAMP,
    `updated_at`  DATETIME    DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `created_by`  INT         NULL,
    `deleted`     TINYINT(1)  DEFAULT 0,
    PRIMARY KEY (`id_persona`)
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `clientes` (
    `id_cliente`  INT        NOT NULL AUTO_INCREMENT,
    `id_persona`  INT        NOT NULL,
    `created_at`  DATETIME   DEFAULT CURRENT_TIMESTAMP,
    `updated_at`  DATETIME   DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `created_by`  INT        NULL,
    `deleted`     TINYINT(1) DEFAULT 0,
    PRIMARY KEY (`id_cliente`),
    INDEX `fk_clientes_personas_idx` (`id_persona` ASC) VISIBLE,
    CONSTRAINT `fk_clientes_personas`
        FOREIGN KEY (`id_persona`)
        REFERENCES `personas` (`id_persona`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `entrenadores` (
    `id_entrenador` INT        NOT NULL AUTO_INCREMENT,
    `id_persona`    INT        NOT NULL,
    `created_at`    DATETIME   DEFAULT CURRENT_TIMESTAMP,
    `updated_at`    DATETIME   DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `created_by`    INT        NULL,
    `deleted`       TINYINT(1) DEFAULT 0,
    PRIMARY KEY (`id_entrenador`),
    INDEX `fk_entrenadores_personas_idx` (`id_persona` ASC) VISIBLE,
    CONSTRAINT `fk_entrenadores_personas`
        FOREIGN KEY (`id_persona`)
        REFERENCES `personas` (`id_persona`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `usuarios` (
    `id_usuario`      INT          NOT NULL AUTO_INCREMENT,
    `username`        VARCHAR(100) NOT NULL,
    `email`           VARCHAR(150) NOT NULL,
    `telefono`        VARCHAR(15)  NOT NULL,
    `password_hash`   VARCHAR(255) NOT NULL,
    `id_persona`      INT          NOT NULL,
    `id_tipo_usuario` INT          NOT NULL,
    `created_at`      DATETIME     DEFAULT CURRENT_TIMESTAMP,
    `updated_at`      DATETIME     DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `created_by`      INT          NULL,
    `deleted`         TINYINT(1)   DEFAULT 0,
    PRIMARY KEY (`id_usuario`),
    UNIQUE INDEX `username_UNIQUE`  (`username` ASC) VISIBLE,
    UNIQUE INDEX `email_UNIQUE`     (`email`    ASC) VISIBLE,
    UNIQUE INDEX `telefono_UNIQUE`  (`telefono` ASC) VISIBLE,
    INDEX `fk_usuarios_personas_idx`      (`id_persona`      ASC) VISIBLE,
    INDEX `fk_usuarios_tipo_usuarios_idx` (`id_tipo_usuario` ASC) VISIBLE,
    CONSTRAINT `fk_usuarios_personas`
        FOREIGN KEY (`id_persona`)
        REFERENCES `personas` (`id_persona`)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT `fk_usuarios_tipo_usuarios`
        FOREIGN KEY (`id_tipo_usuario`)
        REFERENCES `tipo_usuarios` (`id_tipo_usuario`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `plan_entrenamientos` (
    `id_plan_entrenamiento`      INT        NOT NULL AUTO_INCREMENT,
    `duracion_semanas`           INT        NOT NULL,
    `id_tipo_plan_entrenamiento` INT        NOT NULL,
    `id_entrenador`              INT        NOT NULL,
    `id_cliente`                 INT        NOT NULL,
    `created_at`                 DATETIME   DEFAULT CURRENT_TIMESTAMP,
    `updated_at`                 DATETIME   DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `created_by`                 INT        NULL,
    `deleted`                    TINYINT(1) DEFAULT 0,
    PRIMARY KEY (`id_plan_entrenamiento`),
    INDEX `fk_plan_tipo_plan_idx`    (`id_tipo_plan_entrenamiento` ASC) VISIBLE,
    INDEX `fk_plan_entrenadores_idx` (`id_entrenador`              ASC) VISIBLE,
    INDEX `fk_plan_clientes_idx`     (`id_cliente`                 ASC) VISIBLE,
    CONSTRAINT `fk_plan_tipo_plan`
        FOREIGN KEY (`id_tipo_plan_entrenamiento`)
        REFERENCES `tipo_plan_entrenamientos` (`id_tipo_plan_entrenamiento`)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT `fk_plan_entrenadores`
        FOREIGN KEY (`id_entrenador`)
        REFERENCES `entrenadores` (`id_entrenador`)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT `fk_plan_clientes`
        FOREIGN KEY (`id_cliente`)
        REFERENCES `clientes` (`id_cliente`)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================
-- RESTAURAR CONFIGURACIÓN
-- =====================================================
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


USE sistema_gimnasio;


INSERT INTO tipo_usuarios (nombre_tipo_usuario, descripcion_tipo_usuario) VALUES 
    ('admin',      'Control total del sistema'),
    ('cliente',    'Usuario que contrata planes de entrenamiento'),
    ('entrenador', 'Usuario que dirige los planes');

INSERT INTO tipo_plan_entrenamientos (nombre_tipo_plan, descripcion_tipo_plan) VALUES 
    ('Fuerza',     'Plan enfocado en aumento de fuerza muscular'),
    ('Pliometría', 'Plan de saltos y explosividad'),
    ('Pierna',     'Plan específico para tren inferior');


INSERT INTO personas (nombre, apellido) VALUES 
    ('José',    'González'),
    ('Martina', 'López'),
    ('Luciano', 'Pérez'),
    ('Marcos',  'Soto'),
    ('Sofía',   'Ramírez'),
    ('Luis',    'Torres');


INSERT INTO clientes (id_persona) VALUES (1), (2), (3);
INSERT INTO entrenadores (id_persona) VALUES (4), (5), (6);

INSERT INTO usuarios (username, email, telefono, password_hash, id_persona, id_tipo_usuario) VALUES 
    ('jose123',    'jose@gmail.com',    '932494323', '$2b$10$hash123...', 1, 2),
    ('martina123', 'martina@gmail.com', '932674532', '$2b$10$hash456...', 2, 2),
    ('luciano123', 'luciano@gmail.com', '932895643', '$2b$10$hash789...', 3, 2),
    ('marcos123',  'marcos@gmail.com',  '932293363', '$2b$10$hashABC...', 4, 3),
    ('sofia123',   'sofia@gmail.com',   '921296383', '$2b$10$hashDEF...', 5, 3),
    ('luis123',    'luis@gmail.com',    '932192346', '$2b$10$hashGHI...', 6, 3);

INSERT INTO plan_entrenamientos (duracion_semanas, id_tipo_plan_entrenamiento, id_entrenador, id_cliente) VALUES 
    (4, 1, 1, 1),
    (2, 2, 2, 2),
    (2, 3, 3, 3);

-- MOSTRAR PLANES ACTIVOS
SELECT id_plan_entrenamiento, duracion_semanas, deleted
FROM plan_entrenamientos
WHERE deleted = 0;

-- MOSTRAR USUARIOS ACTIVOS CON SU TIPO
SELECT username, email, id_tipo_usuario, deleted
FROM usuarios 
WHERE deleted = 0;

-- BORRADO LÓGICO DE UN USUARIO
UPDATE usuarios
SET deleted = 1
WHERE id_usuario = 1;

-- RECUPERAR USUARIO
UPDATE usuarios
SET deleted = 0
WHERE id_usuario = 1;