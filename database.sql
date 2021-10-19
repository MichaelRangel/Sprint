--
-- File generated with SQLiteStudio v3.3.3 on lun. oct. 18 09:16:36 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: mensajes
CREATE TABLE mensajes(
'message_id' Integer Primary_Key,
'from_id' Integer Foreign_Key,
'to_id' Integer Not Null,
'asunto' varchar Not Null,
'mensaje' varchar Not Null);
INSERT INTO mensajes (message_id, from_id, to_id, asunto, mensaje) VALUES (4, 4, 2, 'Chao', 'Hasta pronto Marcela');
INSERT INTO mensajes (message_id, from_id, to_id, asunto, mensaje) VALUES (3, 3, 4, 'Hello', 'Hola mundo :)');
INSERT INTO mensajes (message_id, from_id, to_id, asunto, mensaje) VALUES (2, 2, 1, 'Prueba', 'Saludos john');
INSERT INTO mensajes (message_id, from_id, to_id, asunto, mensaje) VALUES (1, 1, 4, 'Hola', 'Hola Ana');

-- Table: Usuario
CREATE TABLE Usuario (id INTEGER PRIMARY KEY, nombre VARCHAR (0, 20) NOT NULL, apellido VARCHAR (0, 30) NOT NULL, usuario VARCHAR (0, 20) NOT NULL, correo VARCHAR NOT NULL, contraseña VARCHAR NOT NULL);
INSERT INTO Usuario (id, nombre, apellido, usuario, correo, contraseña) VALUES (1, 'John', 'asa', 'john1', 'J@j.com', 'prueba1');
INSERT INTO Usuario (id, nombre, apellido, usuario, correo, contraseña) VALUES (2, 'Marcela', 'ad', 'Marcela1', 'm@m.com', 'prueba2');
INSERT INTO Usuario (id, nombre, apellido, usuario, correo, contraseña) VALUES (3, 'Pedro', 'Padada', 'Pedro1', 'p@p.com', 'prueba3');
INSERT INTO Usuario (id, nombre, apellido, usuario, correo, contraseña) VALUES (4, 'Ana', 'saa', 'Ana1', 'a@a.com', 'prueba4');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
