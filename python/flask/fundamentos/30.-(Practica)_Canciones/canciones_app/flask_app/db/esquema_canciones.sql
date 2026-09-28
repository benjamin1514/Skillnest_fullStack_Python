/*drop database esquema_canciones;*/
CREATE DATABASE IF NOT EXISTS esquema_canciones;

USE esquema_canciones;
-- 1. Creación de Tablas

CREATE TABLE usuarios (
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
contrasena VARCHAR(255) NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE canciones (
id INT PRIMARY KEY AUTO_INCREMENT,
titulo VARCHAR(150) NOT NULL,
artista VARCHAR(100) NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE favoritos (
usuario_id INT NOT NULL,
cancion_id INT NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (usuario_id, cancion_id),
FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE,
FOREIGN KEY (cancion_id) REFERENCES canciones (id) ON DELETE CASCADE
);

-- 2. Poblado de datos

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