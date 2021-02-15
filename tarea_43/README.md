**Pregunta 1**\
An illegal site's servers were seized in a recent operation. Please submit all users' details.

La tabla de usuarios contiene:

-   GivenName
-   LastName
-   Email
-   AccessTime
-   Downloads

Solución:

```
SELECT *
FROM users;
```

---

**Pregunta 2**\
An illegal site's servers were seized in a recent operation. Please submit all users' details.

La tabla de usuarios contiene:

-   GivenName
-   Surname
-   EmailAddress
-   LastAccess
-   NumberOfDownloads

Solución:

```
SELECT \*
FROM users;
```

---

**Pregunta 3**\
A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit all records number of kids, join dates and emails' details.

La tabla mailing_list contiene:

-   FirstName
-   LastName
-   Email
-   JoinDate
-   NumberOfKids

Solución:

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

La tabla users contiene:

-   GivenName
-   FamilyName
-   EmailAddress
-   LastAccess
-   Downloads

Solución:

```
SELECT
    FamilyName,
    LastAccess
FROM user;
```

---

**Pregunta 5**\
An illegal site's servers were seized in a recent operation. Please submit all users number of downloads' details. Please make sure there are no duplicates.

La tabla users contiene:

-   GivenName
-   FamilyName
-   Email
-   LastAccess
-   NumberOfDownloads

Solución:

```
SELECT DISTINCT NumberOfDownloads
FROM users;
```

---

**Pregunta 6**\
White hat hacker has sent SQLPD exposed members' details of a shady site connected to various persons of interest. Please submit all members' details sorted by mailing addresses in ascending order.

La tabla members contiene:

-   Username
-   FullName
-   HashedPassword
-   MemberSince
-   MailingAddress
-   Comments

Solución:

```
SELECT \*
FROM members
ORDER BY MailingAddress ASC;
```

---

**Pregunta 7**\
A hacked site subscribers' details have surfaced on a darknet forum. Please submit all subscribers' details sorted by full names in descending order.

La tabla subscribers contiene:

-   Username
-   FullName
-   PasswordHash
-   SubscriptionDate
-   Address
-   Comments

Solución:

```
SELECT \*
FROM subscribers
ORDER BY FullName DESC;
```

---

**Pregunta 8**\
An illegal site's servers were seized in a recent operation. Please submit all users number of posts and given names' details sorted by given names in descending order. Please make sure there are no duplicates.

La tabla users contiene:

-   GivenName
-   LastName
-   Email
-   LastAccess
-   NumberOfPosts

Solución:

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

La tabla mailing_list contiene:

-   GivenName
-   LastName
-   Email
-   JoinDate
-   Children

Solución:

```
SELECT
    Email,
    JoinDate,
    LastName
FROM mailing_list
ORDER BY Email ASC, LastName DESC;
```

---

**Pregunta 10**\
A mailing list of an illegal online service was sent to the SQLPD hot-line. Please submit all records emails, join dates and last names' details sorted by emails in descending order and then by last names in ascending order.

La tabla mailing_list contiene:

-   GivenName
-   LastName
-   Email
-   JoinDate
-   Children

Solución:

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

La tabla mailing_list contiene:

-   FirstName
-   Surname
-   EmailAddress
-   Joined
-   PasswordChanges

Solución:

```
SELECT \*
FROM mailing_list
ORDER BY EmailAddress DESC, Surname ASC
LIMIT 5;
```

---

**Pregunta 12**\
A hacked site subscribers' details have surfaced on a darknet forum. Please submit the top 10 subscribers subscription dates, full names and addresses' details when sorted by addresses in ascending order and then by full names in ascending order. Please make sure there are no duplicates.

La tabla subscribers contiene:

-   Username
-   FullName
-   PasswordHash
-   SubscriptionDate
-   Address
-   Comments

Solución:

```
SELECT DISTINCT
    SubscriptionDate,
    FullName,
    Address
FROM subscribers
ORDER BY Address ASC, FullName ASC
LIMIT 10;
```
