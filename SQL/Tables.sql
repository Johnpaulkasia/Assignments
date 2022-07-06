CREATE TABLE Employer
(
Employer_ID serial Primary key,
FullName varchar,
JoiningDate date,
CurrentPosition varchar,
Department varchar,
AssignedProject varchar
);


CREATE TABLE Services
(
Software_ID serial Primary key,
Name varchar,
Category varchar,
Size int,
NumberOfInstallments int
);
CREATE TABLE  Software_Requests
( 
Employer_ID int references Employer(Employer_ID),
Software_ID int references Services(Software_ID),
Request_Start_Date date,
Request_Closed_Date date,
Status boolean
);
