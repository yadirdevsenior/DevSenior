
CREATE DATABASE IF NOT EXISTS academia;
USE academia;

CREATE TABLE Estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    fecha_nacimiento DATE
);

CREATE TABLE Profesores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    especialidad VARCHAR(100)
);

CREATE TABLE Cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    id_profesor INT,
    FOREIGN KEY (id_profesor) REFERENCES Profesores(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE TABLE Matriculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    id_curso INT,
    fecha_matricula DATE,
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_curso) REFERENCES Cursos(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE Horarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_curso INT,
    dia_semana ENUM('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo') NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    FOREIGN KEY (id_curso) REFERENCES Cursos(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

