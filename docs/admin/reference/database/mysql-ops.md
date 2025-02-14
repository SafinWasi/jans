---
tags:
  - administration
  - reference
  - database
  - additional claims to database
  - jansPerson
  - LDAP to MySQL Migration Script
---

Below operations require to log into mysql workspace first with command: `mysql`

### **Change password for user `jans`** :

*  `ALTER USER 'jans'@'localhost' IDENTIFIED BY 'TopSecret';`
*  `GRANT ALL PRIVILEGES ON jansdb.* TO 'jans'@'localhost';`

### Create new user claims to `jansPerson`: 
* You can add additional attributes to `jansPerson` table and use them. This will be similar to LDAP where DB stores all user attributes in one entry. Additional attributes will not affect the server functionality.
* Ensure you restart services after DB schema modification

### **Modify column size of jansPerson** :
Say we want to increase the size of `mail` field to 144. Do the following:<br>
* a. Modify column size - 
 ```
 ALTER TABLE `jansdb`.`jansPerson` CHANGE COLUMN `mail` `mail` VARCHAR(144) NULL DEFAULT NULL ;
 ```
* b. Drop indexes and re-create - 
 ```
 ALTER TABLE jansdb.jansPerson DROP INDEX `jansPerson_CustomIdx2`;
 ALTER TABLE jansdb.jansPerson ADD INDEX `jansPerson_CustomIdx2` ((lower(`mail`)));
 ```
* c. Ensure you restart services after DB schema modification

### **Search user** : 

* `use jansdb; select * from jansPerson where uid='admin'\G;`

### Add custom attribute

There are two steps here: 

* Create attribute in MySQL database: `ALTER TABLE `jansdb`.`jansPerson` ADD COLUMN `cmdAttr` VARCHAR(64) NULL;` 
* Create attribute from TUI: ![tui_custom_attribute](../../assets/TUI_CustomAttribute.png)

### LDAP to MySQL Migration Script

Please refer to [these steps](./converting-data.md#ldap-to-mysql-migration-script).


!!! Contribute
If you’d like to contribute to this document, get started with the [Contribution Guide](https://docs.jans.io/head/CONTRIBUTING/#contributing-to-the-documentation)
