**Pregunta 1**\
An illegal site's servers were seized in a recent operation. Please submit all users' details.

La tabla **users** contiene:

-   GivenName
-   LastName
-   Email
-   AccessTime
-   Downloads

Solución:

Por lo tanto nos piden todos los detalles (columnas) de todos los usuarios (la tabla **users**). Aunque podríamos haber especificado cada una de las columnas de la tabla en la consulta, he optado por utilizar el símbolo _\*_ que pide todas las columnas automáticamente.

```
SELECT *
FROM users;
```

---

**Pregunta 2**\
An illegal site's servers were seized in a recent operation. Please submit all users' details.

La tabla **users** contiene:

-   GivenName
-   Surname
-   EmailAddress
-   LastAccess
-   NumberOfDownloads

Solución:

Pide todas las columnas de la tabla de usuarios (**users**). Aunque podríamos haber especificado cada una de las columnas de la tabla en la consulta, he optado por utilizar el símbolo _\*_ que pide todas las columnas automáticamente.

```
SELECT \*
FROM users;
```

---

**Pregunta 3**\
A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit all records number of kids, join dates and emails' details.

La tabla **mailing_list** contiene:

-   FirstName
-   LastName
-   Email
-   JoinDate
-   NumberOfKids

Solución:

Pide que de cada entrada en la tabla **mailing_list** mostremos las columnas _NumberOfKids_, _JoinDate_ y _Email_. Ya que en este caso queremos mostrar los datos de sólamente unas columnas específicas, las introducimos en la consulta de manera explícita tras el _SELECT_.

```
SELECT
    NumberOfKids,
    JoinDate,
    Email
FROM mailing_list;
```

---

**Pregunta 4**\
An illegal site's servers were seized in a recent operation. Please submit all users family names and last access times' details.

La tabla **users** contiene:

-   GivenName
-   FamilyName
-   EmailAddress
-   LastAccess
-   Downloads

Solución:

Pide que de cada entrada en la tabla **users** mostremos las columnas _NumberOfKids_, _JoinDate_ y _Email_. Ya que en este caso queremos mostrar los datos de sólamente unas columnas específicas, las introducimos en la consulta de manera explícita tras el _SELECT_.

```
SELECT
    FamilyName,
    LastAccess
FROM user;
```

---

**Pregunta 5**\
An illegal site's servers were seized in a recent operation. Please submit all users number of downloads' details. Please make sure there are no duplicates.

La tabla **users** contiene:

-   GivenName
-   FamilyName
-   Email
-   LastAccess
-   NumberOfDownloads

Solución:

Nos pide que mostremos de la tabla **users** las entradas _sin duplicados_ de la columna _NumberOfDownloads_. Para que la consulta ignore los resultados duplicados, añadimos _DISTINCT_ inmediatamente después del _SELECT_.

```
SELECT DISTINCT NumberOfDownloads
FROM users;
```

---

**Pregunta 6**\
White hat hacker has sent SQLPD exposed members' details of a shady site connected to various persons of interest. Please submit all members' details sorted by mailing addresses in ascending order.

La tabla **members** contiene:

-   Username
-   FullName
-   HashedPassword
-   MemberSince
-   MailingAddress
-   Comments

Solución:

Se nos pide que mostremos todas las entradas y columnas de la tabla **members**, y que ordenemos los resultados en base a la columna _MailingAddress_, en orden ascendente. Para ordenar los resultados utilizamos el comando _ORDER BY_ lo que hace que se ordenen los resultados en base a la columna que indiquemos. No es necesario añadir _ASC_ para que ser ordenen de modo ascendente ya que ordena la columna en modo ascendente por defecto, pero he preferido añadirlo para mayor claridad.

```
SELECT *
FROM members
ORDER BY MailingAddress ASC;
```

---

**Pregunta 7**\
A hacked site subscribers' details have surfaced on a darknet forum. Please submit all subscribers' details sorted by full names in descending order.

La tabla **subscribers** contiene:

-   Username
-   FullName
-   PasswordHash
-   SubscriptionDate
-   Address
-   Comments

Solución:

Se nos pide que mostremos todas las columnas de todas las entradas de la tabla **subscribers** ordenadas en modo descendente por la columna _FullName_. Para ordenar los resultados utilizamos el comando _ORDER BY_ lo que hace que se ordenen los resultados en base a la columna que indiquemos. Es necesario añadir _DESC_ para que ser ordenen de modo descendente ya que si no lo especificamos los resultados se ordenarían de modo ascendente.

```
SELECT *
FROM subscribers
ORDER BY FullName DESC;
```

---

**Pregunta 8**\
An illegal site's servers were seized in a recent operation. Please submit all users number of posts and given names' details sorted by given names in descending order. Please make sure there are no duplicates.

La tabla **users** contiene:

-   GivenName
-   LastName
-   Email
-   LastAccess
-   NumberOfPosts

Solución:

Se nos pide que mostremos las columnas _NumberOfPosts_ y _GivenName_ de la tabla **users** sin mostrar duplicados y ordenados de modo descendiente por la columna _GivenName_.

Para que la consulta ignore los resultados duplicados, añadimos _DISTINCT_ inmediatamente después del _SELECT_.

Para ordenar los resultados utilizamos el comando _ORDER BY_ lo que hace que se ordenen los resultados en base a la columna que indiquemos. Es necesario añadir _DESC_ para que ser ordenen de modo descendente ya que si no lo especificamos los resultados se ordenarían de modo ascendente.

```
SELECT DISTINCT
    NumberOfPosts,
    GivenName
FROM users
ORDER BY GivenName DESC;
```

---

**Pregunta 9**\
A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit all records emails, join dates and last names' details sorted by emails in descending order and then by last names in ascending order.

La tabla **mailing_list** contiene:

-   GivenName
-   LastName
-   Email
-   JoinDate
-   Children

Solución:

Se nos pide que mostremos las columnas _Email_, _JoinDate_ y _Lastname_ de la tabla **mailing_list**, ordenados primero de modo descendiente por la columna _Email_ y después por modo ascendente por la columna _LastName_.

Para ordenar los resultados utilizamos el comando _ORDER BY_ lo que hace que se ordenen los resultados en base a la columna que indiquemos. En este caso ya que la primera ordenación queremos que sea por la columna _Email_ la especificamos primero y ponemos _LastName_ después. Es necesario añadir _DESC_ en el caso de la columna _Email_ para que ser ordenen de modo descendente ya que si no lo especificamos los resultados se ordenarían de modo ascendente. No es necesario especificar _ASC_ en el caso de la columna _LastName_ pero he optado por añadirlo para mayor claridad.

```
SELECT
    Email,
    JoinDate,
    LastName
FROM mailing_list
ORDER BY Email DESC, LastName ASC;
```

---

**Pregunta 10**\
A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit all records emails, join dates and last names' details sorted by emails in descending order and then by last names in ascending order.

La tabla **mailing_list** contiene:

-   GivenName
-   LastName
-   Email
-   JoinDate
-   Children

Solución:

Se nos pide que mostremos las columnas _Email_, _JoinDate_ y _Lastname_ de la tabla **mailing_list**, ordenados primero de modo descendiente por la columna _Email_ y después por modo ascendente por la columna _LastName_.

Para ordenar los resultados utilizamos el comando _ORDER BY_ lo que hace que se ordenen los resultados en base a la columna que indiquemos. En este caso ya que la primera ordenación queremos que sea por la columna _Email_ la especificamos primero y ponemos _LastName_ después. Es necesario añadir _DESC_ en el caso de la columna _Email_ para que ser ordenen de modo descendente ya que si no lo especificamos los resultados se ordenarían de modo ascendente. No es necesario especificar _ASC_ en el caso de la columna _LastName_ pero he optado por añadirlo para mayor claridad.

```
SELECT
    Email,
    JoinDate,
    LastName
FROM mailing_list
ORDER BY Email DESC, LastName ASC;
```

---

**Pregunta 11**\
A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit the top 5 records' details when sorted by email addresses in descending order and then by surnames in ascending order.

La tabla **mailing_list** contiene:

-   FirstName
-   Surname
-   EmailAddress
-   Joined
-   PasswordChanges

Solución:

Se nos pide que mostremos todas las columnas de la tabla **mailing_list**, ordenados primero de modo descendiente por la columna _Email_ y después por modo ascendente por la columna _LastName_.

Para mostrar todas las columnas he utilizado \* aunque también se podrían haber especificado todos los nombres de las columnas a continuación del _SELECT_.

Para ordenar los resultados utilizamos el comando _ORDER BY_ lo que hace que se ordenen los resultados en base a la columna que indiquemos. En este caso ya que la primera ordenación queremos que sea por la columna _EmailAddress_ la especificamos primero y ponemos _Surname_ después. Es necesario añadir _DESC_ en el caso de la columna _EmailAddress_ para que ser ordenen de modo descendente ya que si no lo especificamos los resultados se ordenarían de modo ascendente. No es necesario especificar _ASC_ en el caso de la columna _Surname_ pero he optado por añadirlo para mayor claridad.

Finalmente el enunciado indica que sólo mostremos los primeros 5 resultados, para lo que añadimos el comando _LIMIT_ y le pasamos el número 5, de modo que limitará los resultados mostrados a únicamente los 5 primeros.

```
SELECT *
FROM mailing_list
ORDER BY EmailAddress DESC, Surname ASC
LIMIT 5;
```

---

**Pregunta 12**\
A hacked site subscribers' details have surfaced on a darknet forum. Please submit the top 10 subscribers subscription dates, full names and addresses' details when sorted by addresses in ascending order and then by full names in ascending order. Please make sure there are no duplicates.

La tabla **subscribers** contiene:

-   Username
-   FullName
-   PasswordHash
-   SubscriptionDate
-   Address
-   Comments

Solución:

Se nos pide que mostremos las columnas _SubscriptionDate_, _FullName_ y _Address_ de la tabla **subscribers**, ordenados primero de modo ascendiente por la columna _Address_ y después por modo ascendente por la columna _FullName_.

Para ordenar los resultados utilizamos el comando _ORDER BY_ lo que hace que se ordenen los resultados en base a la columna que indiquemos. En este caso ya que la primera ordenación queremos que sea por la columna _Address_ la especificamos primero y ponemos _FullName_ después. No ess necesario añadir _ASC_ en ninguno de los dos casos, ya que si no lo especificamos los resultados se ordenarían de modo ascendente, pero he optado por añadirlo para mayor claridad.

Finalmente el enunciado indica que sólo mostremos los primeros 10 resultados, para lo que añadimos el comando _LIMIT_ y le pasamos el número 10, de modo que limitará los resultados mostrados a únicamente los 10 primeros.

```
SELECT DISTINCT
    SubscriptionDate,
    FullName,
    Address
FROM subscribers
ORDER BY Address ASC, FullName ASC
LIMIT 10;
```
