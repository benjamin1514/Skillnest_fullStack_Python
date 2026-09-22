-- ==========================================================
-- CREAR BASE DE DATOS
-- ==========================================================

CREATE DATABASE IF NOT EXISTS primera_flask;

USE primera_flask;


-- ==========================================================
-- CREAR TABLA
-- ==========================================================

CREATE TABLE IF NOT EXISTS mascotas (

    id INT AUTO_INCREMENT PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL,

    tipo VARCHAR(100) NOT NULL,

    color VARCHAR(100) NOT NULL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP

);


CREATE TABLE IF NOT EXISTS usuarios (

    id INT AUTO_INCREMENT PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL,

    correo VARCHAR(100) NOT NULL,

    edad INT NOT NULL,

    password VARCHAR(100) NOT NULL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP

);


-- ==========================================================
-- INSERTAR DATOS DE PRUEBA
-- ==========================================================

INSERT INTO mascotas
    (nombre, tipo, color)
VALUES
    ("Firulais", "Perro", "Café"),
    ("Michi", "Gato", "Negro"),
    ("Luna", "Perro", "Blanco"),
    ("Nala", "Gato", "Naranjo"),
    ("Coco", "Conejo", "Blanco");

INSERT INTO usuarios
    (nombre, correo, edad, password)
VALUES
    ("Juan Pérez", "juan@example.com", 30, "password123"),
    ("María López", "maria@example.com", 25, "password456");