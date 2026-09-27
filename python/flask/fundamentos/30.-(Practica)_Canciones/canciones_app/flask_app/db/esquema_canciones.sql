CREATE DATABASE IF NOT EXISTS esquema_canciones;

USE esquema_canciones;

-- -----------------------------------------------------
-- 1. Creación de Tablas
-- -----------------------------------------------------

CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE canciones (
    id_cancion INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(45) NOT NULL,
    artista VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE favoritos (
    id_usuario INT NOT NULL,
    id_cancion INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_usuario, id_cancion),
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_cancion) REFERENCES canciones (id_cancion) ON DELETE CASCADE
);

-- -----------------------------------------------------
-- 2. Poblado de datos (Contraseñas simples)
-- -----------------------------------------------------

INSERT INTO usuarios (nombre, email, contrasena) VALUES
('Ana Gómez', 'ana.gomez@example.com', '123456'),
('Carlos López', 'carlos.lopez@example.com', 'password'),
('María Rodríguez', 'maria.rodriguez@example.com', 'maria2024'),
('Juan Pérez', 'juan.perez@example.com', 'secret123');

INSERT INTO canciones (titulo, artista) VALUES
('Bohemian Rhapsody', 'Queen'),
('Billie Jean', 'Michael Jackson'),
('Hotel California', 'Eagles'),
('Shape of You', 'Ed Sheeran'),
('Blinding Lights', 'The Weeknd'),
('De Música Ligera', 'Soda Stereo');