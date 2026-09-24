CREATE DATABASE esquema_usuarios;
use esquema_usuarios;

CREATE TABLE usuarios (
id INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL,
nombre varchar(45) NOT NULL,
apellido varchar(45) NOT NULL,
email varchar(45) NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO usuarios (nombre, apellido, email) 
VALUES 
('Ana', 'Gómez', 'ana.gomez@email.com'),
('Carlos', 'Mendoza', 'carlos.mendoza@email.com'),
('Lucía', 'Fernández', 'lucia.fernandez@email.com');

SELECT * FROM usuarios;

