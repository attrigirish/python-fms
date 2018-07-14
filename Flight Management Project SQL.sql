create table if not exists Cancellation
(
	bookingid int PRIMARY KEY auto_increment,
	flightno int not null,
	bookingdate date not null,
	cancellationdate date not null
);


create table if not exists login
(
	userid int PRIMARY KEY auto_increment,
	name varchar(20) not null,
	password varchar(20) not null,
	type char(1) not null
);


create table if not exists flight
(
	flightno int PRIMARY KEY auto_increment,
	flightname varchar(50) NOT NULL,
	source varchar(50) NOT NULL,
	destination varchar(50) NOT NULL,
	fare decimal(10,2)	
);


create table if not exists booking
(
	bookingid int PRIMARY KEY auto_increment,
	userid int NOT NULL,
	flightno int NOT NULL,
	bookingdate datetime NOT NULL
);