CREATE DATABASE IF NOT EXISTS esquema_bookhub;
USE esquema_bookhub;

-- 1. Tabla Usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 2. Tabla Generos
CREATE TABLE IF NOT EXISTS generos (
    id_genero INT AUTO_INCREMENT PRIMARY KEY,
    genero VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 3. Tabla Libros
CREATE TABLE IF NOT EXISTS libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    descripcion TEXT,
    id_genero INT NOT NULL,
    id_usuario INT NOT NULL, -- Usuario que creó el libro en la plataforma
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_genero) REFERENCES generos(id_genero) ON DELETE CASCADE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- 4. Tabla Intermedia: Usuario_Libros (Libros agregados a "Mis libros")
CREATE TABLE IF NOT EXISTS usuario_libros (
    id_usuario_libro INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_libro INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_libro) REFERENCES libros(id_libro) ON DELETE CASCADE
);

USE esquema_bookhub;

-- 1. Insertar Géneros
INSERT INTO generos (genero) VALUES 
('Novela'),
('Ciencia Ficción'),
('Fantasía'),
('Historia'),
('Desarrollo Personal'),
('Misterio');

-- 2. Insertar Usuarios de Prueba (Contraseñas simuladas en texto/hash)
INSERT INTO usuarios (nombre, apellido, email, password) VALUES 
('Elena', 'Naranjo', 'elena@gmail.com', '$2b$12$eImiTXuWVxfM37uY4JANjQe8.Yg1u1vN7..'),
('Carlos', 'Mendoza', 'carlos@gmail.com', '$2b$12$eImiTXuWVxfM37uY4JANjQe8.Yg1u1vN7..'),
('Sofia', 'Rojas', 'sofia@gmail.com', '$2b$12$eImiTXuWVxfM37uY4JANjQe8.Yg1u1vN7..');

-- 3. Insertar Libros (Asociados a un género y al usuario que lo creó)
INSERT INTO libros (titulo, autor, descripcion, id_genero, id_usuario) VALUES 
('Cien Años de Soledad', 'Gabriel García Márquez', 'Historia de la familia Buendía en el pueblo ficticio de Macondo.', 1, 1),
('1984', 'George Orwell', 'Novela distópica sobre el control estatal y la vigilancia masiva.', 2, 1),
('El Hobbit', 'J.R.R. Tolkien', 'Fantasía épica sobre el viaje de Bilbo Bolsón para recuperar el reino enano.', 3, 2),
('Hábitos Atómicos', 'James Clear', 'Guía práctica para construir buenos hábitos y romper los malos.', 5, 3);

-- 4. Insertar Libros en la lista personal de los usuarios ("Mis Libros")
INSERT INTO usuario_libros (id_usuario, id_libro) VALUES 
(1, 1), -- Elena tiene en su lista "Cien Años de Soledad"
(1, 2), -- Elena tiene en su lista "1984"
(2, 3), -- Carlos tiene en su lista "El Hobbit"
(2, 1), -- Carlos agregó a su lista "Cien Años de Soledad"
(3, 4); -- Sofia tiene en su lista "Hábitos Atómicos"

