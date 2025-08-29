CREATE TABLE IF NOT EXISTS nacionalidad(
    id_nacionalidad INT AUTO_INCREMENT,
    pais VARCHAR(50) NOT NULL,
    nacionalidad VARCHAR(50) NOT NULL,

    CONSTRAINT pk_nacionalidad PRIMARY KEY (id_nacionalidad)
);

CREATE TABLE IF NOT EXISTS autor(
    id_autor INT AUTO_INCREMENT, 
    nombre_autor VARCHAR(100) NOT NULL, 
    pseudonimo VARCHAR(50) NULL, 
    id_nacionalidad INT NULL, 
    biografia VARCHAR(255) NULL,

    CONSTRAINT pk_autor PRIMARY KEY (id_autor),
    CONSTRAINT fk_autor_nacionalidad FOREIGN KEY (id_nacionalidad) REFERENCES nacionalidad(id_nacionalidad)
);

CREATE TABLE IF NOT EXISTS comuna(
    id_comuna INT AUTO_INCREMENT,
    codigo_comuna CHAR(5) NOT NULL,
    nombre_comuna VARCHAR(50) NOT NULL,

    CONSTRAINT pk_comuna PRIMARY KEY (id_comuna)
);

CREATE TABLE IF NOT EXISTS direccion(
    id_direccion INT AUTO_INCREMENT,
    id_comuna INT NOT NULL,
    calle VARCHAR(50) NOT NULL,
    numero VARCHAR(10) NULL,
    departamento VARCHAR(10) NULL,

    CONSTRAINT pk_direccion PRIMARY KEY (id_direccion),
    CONSTRAINT fk_direccion_comuna FOREIGN KEY (id_comuna) REFERENCES comuna(id_comuna)
);

CREATE TABLE IF NOT EXISTS biblioteca(
    id_biblioteca INT AUTO_INCREMENT,
    nombre_biblioteca VARCHAR(50) NOT NULL,
    id_direccion INT NULL,
    web VARCHAR(255) NULL,

    CONSTRAINT pk_biblioteca PRIMARY KEY (id_biblioteca),
    CONSTRAINT fk_biblioteca_direccion FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion)
);

CREATE TABLE IF NOT EXISTS lector(
    rut_lector INT NOT NULL UNIQUE,
    digito_verificador CHAR(1) NOT NULL,
    nombre_lector VARCHAR(100) NOT NULL,
    correo_lector VARCHAR(255) NOT NULL,
    id_biblioteca INT NOT NULL,
    id_direccion INT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_lector PRIMARY KEY (rut_lector),
    CONSTRAINT fk_lector_biblioteca FOREIGN KEY (id_biblioteca) REFERENCES biblioteca(id_biblioteca),
    CONSTRAINT fk_lector_direccion FOREIGN KEY (id_direccion) REFERENCES direccion(id_direccion)
);

CREATE TABLE IF NOT EXISTS categoria(
    id_categoria INT AUTO_INCREMENT,
    nombre_categoria VARCHAR(50) NOT NULL,
    descripcion_categoria VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_categoria PRIMARY KEY (id_categoria)
);

CREATE TABLE IF NOT EXISTS libro(
    id_libro INT AUTO_INCREMENT,
    id_biblioteca INT NOT NULL,
    id_autor INT NOT NULL,
    id_categoria INT NULL,
    titulo VARCHAR(255) NOT NULL,
    paginas INT NOT NULL,
    copias INT NULL DEFAULT 1,
    fisico TINYINT NOT NULL DEFAULT 1,
    ubicacion VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_libro PRIMARY KEY (id_libro),
    CONSTRAINT fk_libro_biblioteca FOREIGN KEY (id_biblioteca) REFERENCES biblioteca(id_biblioteca),
    CONSTRAINT fk_libro_autor FOREIGN KEY (id_autor) REFERENCES autor(id_autor),
    CONSTRAINT fk_libro_categorio FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);

CREATE TABLE IF NOT EXISTS prestamo(
    id_prestamo INT AUTO_INCREMENT,
    id_libro INT NOT NULL,
    rut_lector INT NOT NULL,
    fecha_prestamo DATETIME NOT NULL,
    fecha_devolucion DATETIME NOT NULL,
    fecha_entrega DATETIME NULL,

    CONSTRAINT pk_prestamo PRIMARY KEY (id_prestamo),
    CONSTRAINT fk_prestamo_libro FOREIGN KEY (id_libro) REFERENCES libro(id_libro),
    CONSTRAINT fk_prestamo_lector FOREIGN KEY (rut_lector) REFERENCES lector(rut_lector)
);