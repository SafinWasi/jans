# Changelog

## 1.0.2 (2022-08-30)


### Features

* add support for date ranges in statistic client [#1575](https://github.com/JanssenProject/jans/issues/1575) ([#1653](https://github.com/JanssenProject/jans/issues/1653)) ([8048cd9](https://github.com/JanssenProject/jans/commit/8048cd9b6ab393b8a3e4a1aaf36e09abe20f605b))
* endpoint to get details of connected FIDO devices registered to users [#1465](https://github.com/JanssenProject/jans/issues/1465) ([#1466](https://github.com/JanssenProject/jans/issues/1466)) ([62522fe](https://github.com/JanssenProject/jans/commit/62522fe5aaa2971835c76e8e9b0d4280fee1db32))
* fix the dependencies and code issues ([#1473](https://github.com/JanssenProject/jans/issues/1473)) ([f4824c6](https://github.com/JanssenProject/jans/commit/f4824c6c6c6a036c5d01b7a6710f51477a49a3fb))
* **jans-auth-server:** added allowSpontaneousScopes AS json config [#2074](https://github.com/JanssenProject/jans/issues/2074) ([#2111](https://github.com/JanssenProject/jans/issues/2111)) ([3083a3f](https://github.com/JanssenProject/jans/commit/3083a3f28f6d6c6a9de319f23fd745ac69477249))
* **jans-auth-server:** added restriction for request_uri parameter (blocklist and allowed client.request_uri) [#1503](https://github.com/JanssenProject/jans/issues/1503) ([0696d92](https://github.com/JanssenProject/jans/commit/0696d92094eeb2ed36f6b0075680634acbf8992f))
* **jans-auth-server:** removed dcrSkipSignatureValidation configuration property [#1623](https://github.com/JanssenProject/jans/issues/1623) ([6550247](https://github.com/JanssenProject/jans/commit/6550247ca727d9437ffceec3fa12b9fef93b81e4))
* **jans-auth-server:** removed id_generation_endpoint and other claims from discovery response [#1827](https://github.com/JanssenProject/jans/issues/1827) ([4068197](https://github.com/JanssenProject/jans/commit/40681972a84d691b5d138bc603f32ec80de84fa2))
* **jans-config-api:** added new attributes ([#1940](https://github.com/JanssenProject/jans/issues/1940)) ([757b22f](https://github.com/JanssenProject/jans/commit/757b22fcc03c28d950eb98b4503d1915fa15b025))
* **jans-config-api:** agama configuration integration ([#1501](https://github.com/JanssenProject/jans/issues/1501)) ([e84575b](https://github.com/JanssenProject/jans/commit/e84575b018f1910860ca6fbf13f5418e8fa131f6))
* **jans-config-api:** agama flow endpoint ([#1898](https://github.com/JanssenProject/jans/issues/1898)) ([0e73306](https://github.com/JanssenProject/jans/commit/0e73306f7642a74a3ed2cf8a8687a1ea447aa7bd))
* **jans-config-api:** agama patch endpoint ([#2028](https://github.com/JanssenProject/jans/issues/2028)) ([0b96a95](https://github.com/JanssenProject/jans/commit/0b96a95399cac02fee614523ae5b552c99c1e254))
* **jans-config-api:** endpoint to get UmaResource based on clientId and swagger changes ([#1912](https://github.com/JanssenProject/jans/issues/1912)) ([a3f9145](https://github.com/JanssenProject/jans/commit/a3f91453dd8fa5e9c903827b458bc58e735eda55))
* **jans-config-api:** enhancement to agama and uma resource endpoint  ([#2015](https://github.com/JanssenProject/jans/issues/2015)) ([f2c19a1](https://github.com/JanssenProject/jans/commit/f2c19a14b0b5b869eb97afd24ac7169328f22b2f))
* **jans-config-api:** enhancement to expose user inum at root level of response ([#1477](https://github.com/JanssenProject/jans/issues/1477)) ([1e4b6bc](https://github.com/JanssenProject/jans/commit/1e4b6bc9955a0cd91d6dff000a860ca96b6bd822))
* **jans-config-api:** fetch the associated clients_id in GET scopes api response  ([#1946](https://github.com/JanssenProject/jans/issues/1946)) ([ffe743c](https://github.com/JanssenProject/jans/commit/ffe743ca007d3a1ca7011f47df9c0a4124c93e5c))
* **jans-config-api:** fixed user management swagger spec for mandatory fields ([#1519](https://github.com/JanssenProject/jans/issues/1519)) ([29ff812](https://github.com/JanssenProject/jans/commit/29ff812c7d6cb94e98886ea7cab0ab08a44879dd))
* **jans-config-api:** new endpoint to fetch scope by creator and type ([#2098](https://github.com/JanssenProject/jans/issues/2098)) ([cf15d67](https://github.com/JanssenProject/jans/commit/cf15d678f26de3bb2e645040ad25bcb21a03691f))
* **jans-config-api:** new functionality and swagger fix  ([#1802](https://github.com/JanssenProject/jans/issues/1802)) ([fc81d1d](https://github.com/JanssenProject/jans/commit/fc81d1d8a974350547bb6d1d22a8818140325f57))
* **jans-config-api:** Scope object changes for creator details ([#2033](https://github.com/JanssenProject/jans/issues/2033)) ([a8b8d76](https://github.com/JanssenProject/jans/commit/a8b8d76640ff6520a462ff2bb477db50c2b60207))
* **jans-config-api:** session management endpoint ([#2158](https://github.com/JanssenProject/jans/issues/2158)) ([30f6e1a](https://github.com/JanssenProject/jans/commit/30f6e1a4bacb90a711ed6f91bc124267d44b9d44))
* **jans-config-api:** swagger spec change to expose user inum at root level of response ([#1483](https://github.com/JanssenProject/jans/issues/1483)) ([c202705](https://github.com/JanssenProject/jans/commit/c202705f2585c4f8f8c9259ad41b388e97f97573))
* **jans-config-api:** user management endpoint 418 ([#1548](https://github.com/JanssenProject/jans/issues/1548)) ([b95fa7b](https://github.com/JanssenProject/jans/commit/b95fa7bcd56ef39f8478a9e879c493f815b29dd3))
* need to fetch the associated clients_id in GET scopes api response [#1923](https://github.com/JanssenProject/jans/issues/1923) ([#1949](https://github.com/JanssenProject/jans/issues/1949)) ([88606a5](https://github.com/JanssenProject/jans/commit/88606a5ad01b9444f533ee4ea85ea0ca57dc49d8))


### Bug Fixes

* : start_date and end_date not required in /stat reponse (swagger specs) [#1767](https://github.com/JanssenProject/jans/issues/1767) ([#1768](https://github.com/JanssenProject/jans/issues/1768)) ([c21452a](https://github.com/JanssenProject/jans/commit/c21452a95567da2f7441e57268268b8d6cb65cfb))
* add path parameter to /fido2/registration/entries [#1465](https://github.com/JanssenProject/jans/issues/1465) ([#1508](https://github.com/JanssenProject/jans/issues/1508)) ([808d0c4](https://github.com/JanssenProject/jans/commit/808d0c4a9b2701c9238926141e22662b918e5990))
* **config-api:** fixing discrepancies in the api ([#2216](https://github.com/JanssenProject/jans/issues/2216)) ([af4d3a5](https://github.com/JanssenProject/jans/commit/af4d3a51ce2cbe8c531f8dca213d0c3ef087aad5))
* fido2-plugin throwing error during deployment [#1632](https://github.com/JanssenProject/jans/issues/1632) ([#1633](https://github.com/JanssenProject/jans/issues/1633)) ([90d2c8a](https://github.com/JanssenProject/jans/commit/90d2c8ace819b784a293df698e316c13a8548fd1))
* fix typos and other issues in jans-config-api swagger specs [#1665](https://github.com/JanssenProject/jans/issues/1665) ([#1668](https://github.com/JanssenProject/jans/issues/1668)) ([3c3a0f4](https://github.com/JanssenProject/jans/commit/3c3a0f47f6274c8b106bebabc38df927a4238ac3))
* jans-config-api add JAVA to programmingLanguage (ref: [#1656](https://github.com/JanssenProject/jans/issues/1656)) ([#1667](https://github.com/JanssenProject/jans/issues/1667)) ([a885a92](https://github.com/JanssenProject/jans/commit/a885a925cdd711158435fedd643f1dd67afad736))
* **jans-config-api:** avoid loss of attributes in agama endpoints ([#2058](https://github.com/JanssenProject/jans/issues/2058)) ([3c8f816](https://github.com/JanssenProject/jans/commit/3c8f816b62b0efdfffc0e3f53d8371f4510d3ef6))
* **jans-config-api:** config-api compilation failed in main [#2030](https://github.com/JanssenProject/jans/issues/2030) ([#2031](https://github.com/JanssenProject/jans/issues/2031)) ([1659da1](https://github.com/JanssenProject/jans/commit/1659da1ff4d1d930300ef9c3b3e040eabc7bc0fb))
* **jans-config-api:** Fix to not update Metadata for PUT and PATCH agama endpoint ([#2046](https://github.com/JanssenProject/jans/issues/2046)) ([da93050](https://github.com/JanssenProject/jans/commit/da93050442d3bc1812d3a8076686ca3e02800c26))
* **jans-config-api:** fixed due to couchbase cluster changes([#1863](https://github.com/JanssenProject/jans/issues/1863)) ([c996b51](https://github.com/JanssenProject/jans/commit/c996b516cb3f0c4880c4bc78038a5eba666a62c6))
* **jans-config-api:** fixes for path conflict for SCIM config and spec for UMA Resource mandatory fields ([#1805](https://github.com/JanssenProject/jans/issues/1805)) ([6d8cff6](https://github.com/JanssenProject/jans/commit/6d8cff64d74634e16e100193f34b06990c356d1c))
* **jans-config-api:** issue UMA scope request being saved as OAUTH ([#2063](https://github.com/JanssenProject/jans/issues/2063)) ([81472aa](https://github.com/JanssenProject/jans/commit/81472aa3da4b02af7ed1bd47753d6938ec0c3e01))
* **jans-config-api:** rectified endpoint url in swagger spec for uma resource ([#1965](https://github.com/JanssenProject/jans/issues/1965)) ([0dc3b2e](https://github.com/JanssenProject/jans/commit/0dc3b2e60825f9921f28c9eeff30ffefa8bda269))
* **jans-config-api:** removed java_script from programmingLanguages ([8b935d8](https://github.com/JanssenProject/jans/commit/8b935d8249ab97f912993a07be0a093b89e52c8b))
* **jans-config-api:** swagger spec change to add missing attributes for Client ([#1786](https://github.com/JanssenProject/jans/issues/1786)) ([e623771](https://github.com/JanssenProject/jans/commit/e62377194616a8a39c86689b30cab92235124fc3))
* **jans-config-api:** switch to 1.0.1-SNAPSHOT ([e8a9186](https://github.com/JanssenProject/jans/commit/e8a918647da488038ff593da875614b6d7c60cc2))


### Documentation

* **agama:** work on TODOs ([#2093](https://github.com/JanssenProject/jans/issues/2093)) ([157ac8b](https://github.com/JanssenProject/jans/commit/157ac8bb097321d33333440c4780abb9c5c67c74))
* no docs ([3083a3f](https://github.com/JanssenProject/jans/commit/3083a3f28f6d6c6a9de319f23fd745ac69477249))
* no docs ([1659da1](https://github.com/JanssenProject/jans/commit/1659da1ff4d1d930300ef9c3b3e040eabc7bc0fb))
* no docs required ([4068197](https://github.com/JanssenProject/jans/commit/40681972a84d691b5d138bc603f32ec80de84fa2))


### Miscellaneous Chores

* release 1.0.1 ([828bfe8](https://github.com/JanssenProject/jans/commit/828bfe80cee87e639839391f98ac3dc2f2d4a920))
* release 1.0.2 ([43dead6](https://github.com/JanssenProject/jans/commit/43dead615f3508ca393c330c2db27a8fb9d1017a))

## [1.0.1](https://github.com/JanssenProject/jans/compare/jans-config-api-v1.0.0...jans-config-api-v1.0.1) (2022-07-06)


### Features

* add support for date ranges in statistic client [#1575](https://github.com/JanssenProject/jans/issues/1575) ([#1653](https://github.com/JanssenProject/jans/issues/1653)) ([8048cd9](https://github.com/JanssenProject/jans/commit/8048cd9b6ab393b8a3e4a1aaf36e09abe20f605b))
* endpoint to get details of connected FIDO devices registered to users [#1465](https://github.com/JanssenProject/jans/issues/1465) ([#1466](https://github.com/JanssenProject/jans/issues/1466)) ([62522fe](https://github.com/JanssenProject/jans/commit/62522fe5aaa2971835c76e8e9b0d4280fee1db32))
* fix the dependencies and code issues ([#1473](https://github.com/JanssenProject/jans/issues/1473)) ([f4824c6](https://github.com/JanssenProject/jans/commit/f4824c6c6c6a036c5d01b7a6710f51477a49a3fb))
* **jans-auth-server:** added restriction for request_uri parameter (blocklist and allowed client.request_uri) [#1503](https://github.com/JanssenProject/jans/issues/1503) ([0696d92](https://github.com/JanssenProject/jans/commit/0696d92094eeb2ed36f6b0075680634acbf8992f))
* **jans-auth-server:** removed dcrSkipSignatureValidation configuration property [#1623](https://github.com/JanssenProject/jans/issues/1623) ([6550247](https://github.com/JanssenProject/jans/commit/6550247ca727d9437ffceec3fa12b9fef93b81e4))
* **jans-config-api:** agama configuration integration ([#1501](https://github.com/JanssenProject/jans/issues/1501)) ([e84575b](https://github.com/JanssenProject/jans/commit/e84575b018f1910860ca6fbf13f5418e8fa131f6))
* **jans-config-api:** enhancement to expose user inum at root level of response ([#1477](https://github.com/JanssenProject/jans/issues/1477)) ([1e4b6bc](https://github.com/JanssenProject/jans/commit/1e4b6bc9955a0cd91d6dff000a860ca96b6bd822))
* **jans-config-api:** fixed user management swagger spec for mandatory fields ([#1519](https://github.com/JanssenProject/jans/issues/1519)) ([29ff812](https://github.com/JanssenProject/jans/commit/29ff812c7d6cb94e98886ea7cab0ab08a44879dd))
* **jans-config-api:** swagger spec change to expose user inum at root level of response ([#1483](https://github.com/JanssenProject/jans/issues/1483)) ([c202705](https://github.com/JanssenProject/jans/commit/c202705f2585c4f8f8c9259ad41b388e97f97573))
* **jans-config-api:** user management endpoint 418 ([#1548](https://github.com/JanssenProject/jans/issues/1548)) ([b95fa7b](https://github.com/JanssenProject/jans/commit/b95fa7bcd56ef39f8478a9e879c493f815b29dd3))


### Bug Fixes

* add path parameter to /fido2/registration/entries [#1465](https://github.com/JanssenProject/jans/issues/1465) ([#1508](https://github.com/JanssenProject/jans/issues/1508)) ([808d0c4](https://github.com/JanssenProject/jans/commit/808d0c4a9b2701c9238926141e22662b918e5990))
* fido2-plugin throwing error during deployment [#1632](https://github.com/JanssenProject/jans/issues/1632) ([#1633](https://github.com/JanssenProject/jans/issues/1633)) ([90d2c8a](https://github.com/JanssenProject/jans/commit/90d2c8ace819b784a293df698e316c13a8548fd1))
* fix typos and other issues in jans-config-api swagger specs [#1665](https://github.com/JanssenProject/jans/issues/1665) ([#1668](https://github.com/JanssenProject/jans/issues/1668)) ([3c3a0f4](https://github.com/JanssenProject/jans/commit/3c3a0f47f6274c8b106bebabc38df927a4238ac3))
* jans-config-api add JAVA to programmingLanguage (ref: [#1656](https://github.com/JanssenProject/jans/issues/1656)) ([#1667](https://github.com/JanssenProject/jans/issues/1667)) ([a885a92](https://github.com/JanssenProject/jans/commit/a885a925cdd711158435fedd643f1dd67afad736))
* **jans-config-api:** removed java_script from programmingLanguages ([8b935d8](https://github.com/JanssenProject/jans/commit/8b935d8249ab97f912993a07be0a093b89e52c8b))
* **jans-config-api:** switch to 1.0.1-SNAPSHOT ([e8a9186](https://github.com/JanssenProject/jans/commit/e8a918647da488038ff593da875614b6d7c60cc2))


### Miscellaneous Chores

* release 1.0.0 ([3df6f77](https://github.com/JanssenProject/jans/commit/3df6f7721a8e9d57e28d065ee29153d023dfe9ea))
* release 1.0.0 ([9644d1b](https://github.com/JanssenProject/jans/commit/9644d1bd29c291e57c140b0c9ac67243c322ac35))
* release 1.0.1 ([828bfe8](https://github.com/JanssenProject/jans/commit/828bfe80cee87e639839391f98ac3dc2f2d4a920))

## 1.0.0 (2022-05-19)


### Features

* add acrValues property in admin-ui configuration. [#1016](https://github.com/JanssenProject/jans/issues/1016) ([#1017](https://github.com/JanssenProject/jans/issues/1017)) ([88b591a](https://github.com/JanssenProject/jans/commit/88b591a64bf9ed0fb49942b770d9f0e334b7433c))
* adding logs to debug license issues[#1258](https://github.com/JanssenProject/jans/issues/1258) ([#1281](https://github.com/JanssenProject/jans/issues/1281)) ([8a08771](https://github.com/JanssenProject/jans/commit/8a08771014e3394d4d7b0864d603a1e4b91e2d81))
* config-cli enumerate scope type ([275533b](https://github.com/JanssenProject/jans/commit/275533b26f4715113d83ea9cabe4a66cd283a189))
* create apis to verify and save license api-keys in Admin UI [#1196](https://github.com/JanssenProject/jans/issues/1196) ([#1203](https://github.com/JanssenProject/jans/issues/1203)) ([315faec](https://github.com/JanssenProject/jans/commit/315faeca46045716d8aa38fa5448c7581a5e4212))
* **jans-auth-config:** user mgmt endpoint - wip ([9c8094a](https://github.com/JanssenProject/jans/commit/9c8094aaed4802d399da812898e1270fe0a0cae5))
* **jans-auth,jans-cli,jans-config-api:** changes to handle new attribute description in Client object and new custom script type ([d64e042](https://github.com/JanssenProject/jans/commit/d64e0424063c79e35b135f4a8bd48f04591b043c))
* **jans-auth,jans-cli,jans-config-api:** changes to handle new attribute description in Client object and new custom script type ([a096110](https://github.com/JanssenProject/jans/commit/a096110d157dec7a0c047692e158c53872fe92fe))
* **jans-auth,jans-cli,jans-config-api:** changes to handle new attribute description in Client object and new custom script type ([d4a9f15](https://github.com/JanssenProject/jans/commit/d4a9f15c3244961cfef6e3229c2e2e49cf85ba0d))
* jans-cli tabulate attribute list ([#1313](https://github.com/JanssenProject/jans/issues/1313)) ([a684484](https://github.com/JanssenProject/jans/commit/a684484d403f9ed52e4c6749f21bd255523a134e))
* **jans-config-api:** added custom script patch endpoint ([6daa4f6](https://github.com/JanssenProject/jans/commit/6daa4f61d3a72a0523912bb79566e2e62a6d84be))
* **jans-config-api:** added patch endpoint for custom script ([e274e20](https://github.com/JanssenProject/jans/commit/e274e206188e76654de759bc687a56a80cf4bfbc))
* **jans-config-api:** added patch endpoint for custom script ([f8da77d](https://github.com/JanssenProject/jans/commit/f8da77df201f67055ea7c23c3410e5818a170785))
* **jans-config-api:** added scope DN validation while client creation ([#1293](https://github.com/JanssenProject/jans/issues/1293)) ([f276605](https://github.com/JanssenProject/jans/commit/f276605cb3a1cedb869733253a48d2d63be2fcdc))
* **jans-config-api:** converting fido2 endpoint to plugin  ([#1304](https://github.com/JanssenProject/jans/issues/1304)) ([88c3fff](https://github.com/JanssenProject/jans/commit/88c3fffe177840324fa5f3c4437fa3d02b9ead9b))
* **jans-config-api:** exposed attributes at root value ([3c3df7a](https://github.com/JanssenProject/jans/commit/3c3df7a1beee57fb851a4c820fcbbffb8418bd78))
* **jans-config-api:** exposed attributes at root value ([40570a7](https://github.com/JanssenProject/jans/commit/40570a7b9d2d03358cbfb0d8c3964a4111e15bb5))
* **jans-config-api:** fixed build issue due to LocalizedString change ([#1329](https://github.com/JanssenProject/jans/issues/1329)) ([3b5ab78](https://github.com/JanssenProject/jans/commit/3b5ab783ed9ddf7c7b47612508cc6ab4c334375d))
* **jans-config-api:** ignore client.customObjectClasses value for persistence type other than LDAP ([#1073](https://github.com/JanssenProject/jans/issues/1073)) ([622bcf4](https://github.com/JanssenProject/jans/commit/622bcf4afae94cddff2a19ca5178f2b8230165d5))
* **jans-config-api:** rectified test properties file  ([#1222](https://github.com/JanssenProject/jans/issues/1222)) ([5b80f67](https://github.com/JanssenProject/jans/commit/5b80f672508ea4fa6956c466bfa971684892b6ce))
* **jans-config-api:** removed encrypttion and decryption of user password ([7f50ad0](https://github.com/JanssenProject/jans/commit/7f50ad064a68412ec67145f1b0866f136804761b))
* **jans-config-api:** removed unused import ([8a41484](https://github.com/JanssenProject/jans/commit/8a41484412cbcf5cfc00c550506ad81fb0c70e7c))
* **jans-config-api:** user custom attributes at root level - 1348 ([5b3f0a1](https://github.com/JanssenProject/jans/commit/5b3f0a13e25cd842e0bbd4be3d21eb48ab1d108f))
* **jans-config-api:** user management api ([b367d44](https://github.com/JanssenProject/jans/commit/b367d440fbcc34fff923bc3040dc4e6026d165fd))
* **jans-config-api:** user management api ([517e7f2](https://github.com/JanssenProject/jans/commit/517e7f235b536f833fec11e2f0da49b8ab0f26c8))
* **jans-config-api:** user management api ([a034bc3](https://github.com/JanssenProject/jans/commit/a034bc3f2b80e4eaaa3ed8fba29b52692a5f91a2))
* **jans-config-api:** user management endpoint ([f28f3b8](https://github.com/JanssenProject/jans/commit/f28f3b86d36199fc137714160cfbdad08e9265f9))
* **jans-config-api:** user management enhancement to chk mandatory feilds ([903ba5a](https://github.com/JanssenProject/jans/commit/903ba5a9a778c87de6280332dfee0eea71eaf2f5))
* **jans-config-api:** user management enhancement to chk mandatory feilds ([0bc2282](https://github.com/JanssenProject/jans/commit/0bc22822a390fdd82370c54ed4e15cad06064e02))
* **jans-config-api:** user management enhancement to chk mandatory feilds ([e6e2781](https://github.com/JanssenProject/jans/commit/e6e2781c70ffbbffe92cbaf87e8607854c3d8da1))
* **jans-config-api:** user management mandatory field chk changes ([e242ec6](https://github.com/JanssenProject/jans/commit/e242ec6c2d5edf86cc773d467fc4cd848e4bce13))
* **jans-config-api:** user management patch endpoint ([0a7ad7d](https://github.com/JanssenProject/jans/commit/0a7ad7dba82b419d412329414f5895c22fdcaa68))
* **jans-config-api:** user mgmt endpoint ([a093758](https://github.com/JanssenProject/jans/commit/a0937580eed7c32a0f8bf573bddb9ac8b7080e2c))
* **jans-config-api:** user mgmt endpoint ([ad66713](https://github.com/JanssenProject/jans/commit/ad66713700b6988378c4e3c603fb3518f8ade247))
* **jans-config-api:** user mgmt endpoint ([0f7a723](https://github.com/JanssenProject/jans/commit/0f7a723bc24dd89fdaf3f71afdb4565e1e25f7fe))
* **jans-config-api:** user mgmt endpoint ([379ca09](https://github.com/JanssenProject/jans/commit/379ca09461c31ec9817d1094aebf5b0fa8c16148))
* **jans-config-api:** user mgmt endpoint ([f98c59e](https://github.com/JanssenProject/jans/commit/f98c59e15bb1199037cf6ad9caa67ffff23ca451))
* **jans-config-api:** user mgmt endpoint ([0ea10fd](https://github.com/JanssenProject/jans/commit/0ea10fd10fdd82ea2f170ecfa990c494591ba653))
* **jans-config-api:** user mgmt endpoint - wip ([70987f6](https://github.com/JanssenProject/jans/commit/70987f65c920943a7e214b9b742cd1f83e877995))
* **jans-config-api:** user mgmt endpoint - wip ([af30358](https://github.com/JanssenProject/jans/commit/af30358d6f8933c405e68449041d5a9e121f3b9f))
* **jans-config-api:** user mgmt endpoint - wip ([aadbf8b](https://github.com/JanssenProject/jans/commit/aadbf8b094d42f8acbf031ead6d4324c9925bed0))
* **jans-config-api:** user mgmt endpoint -wip ([ac35327](https://github.com/JanssenProject/jans/commit/ac35327db9183bd75d314ff162e304e70132a035))
* **jans-config-api:** user mgmt endpoints ([1d53b2e](https://github.com/JanssenProject/jans/commit/1d53b2e2acd1d0b4f33b37088ad90506aea522f6))
* **jans-config-api:** user mgmt endpoints ([5cd1ad5](https://github.com/JanssenProject/jans/commit/5cd1ad5fbfddf43dfdbe6f6abf557f386437133d))
* **jans-config-api:** user mgmt patch endpoint ([1180068](https://github.com/JanssenProject/jans/commit/1180068431f92cd6c21fe024371d363cf5eedd01))
* **jans-config-api:** user mgmt patch endpoint ([12a08e1](https://github.com/JanssenProject/jans/commit/12a08e13105467c3912680fb47dc1943590b985a))
* **jans-config-api:** user mgmt patch endpoint ([0427186](https://github.com/JanssenProject/jans/commit/0427186a48def0f16465c96d7839134d8c7902d9))
* **jans-config-api:** user mgmt patch endpoint ([cb7d36c](https://github.com/JanssenProject/jans/commit/cb7d36cd21ac04f683c38f73d4c9642654886c18))
* **jans-config-api:** user mgt plugin ([ccc56f8](https://github.com/JanssenProject/jans/commit/ccc56f888cbcda657cb2b66e2915e1cae8c96f88))
* **jans-config-api:** user mgt plugin ([ae132cf](https://github.com/JanssenProject/jans/commit/ae132cfe829a3d2ff628b22b23ea716e879c769e))
* **jans-config-api:** user-management endpoints ([#1167](https://github.com/JanssenProject/jans/issues/1167)) ([d8e97c4](https://github.com/JanssenProject/jans/commit/d8e97c4b47b1ff38d4a0207d3f07f461fb807630))
* **jans-core:** remove UPDATE_USER and USER_REGISTRATION scripts [#1289](https://github.com/JanssenProject/jans/issues/1289) ([c34e75d](https://github.com/JanssenProject/jans/commit/c34e75d49db89999633249376c7b42c41bb1ce24))
* jans-linux-setup config-api fido2-plugin (ref: [#1303](https://github.com/JanssenProject/jans/issues/1303)) ([#1308](https://github.com/JanssenProject/jans/issues/1308)) ([ea929c0](https://github.com/JanssenProject/jans/commit/ea929c0637c40ee75f3adbd5377c5e08aebbe087))
* **jans:** jetty 11 integration ([#1123](https://github.com/JanssenProject/jans/issues/1123)) ([6c1caa1](https://github.com/JanssenProject/jans/commit/6c1caa1c4c92d28571f8589cd701e6885d4d85ef))
* support regex client attribute to validate redirect uris ([#1005](https://github.com/JanssenProject/jans/issues/1005)) ([a78ee1a](https://github.com/JanssenProject/jans/commit/a78ee1a3cfc4e7a6d08a500750edb5db0f7709a4))
* user management enhancement to chk mandatory feilds ([3ac4b19](https://github.com/JanssenProject/jans/commit/3ac4b19ada28b11a27707c56ad266ce282f13b60))


### Bug Fixes

* **admin-ui:** the backend issues related to jetty 11 migration [#1258](https://github.com/JanssenProject/jans/issues/1258) ([#1259](https://github.com/JanssenProject/jans/issues/1259)) ([d61be0b](https://github.com/JanssenProject/jans/commit/d61be0bf633020c6bd989e603bb983dc7a45b78b))
* **config-api:** scim user management endpoint failing due to conflict with user mgmt path ([#1181](https://github.com/JanssenProject/jans/issues/1181)) ([8ee47a0](https://github.com/JanssenProject/jans/commit/8ee47a0c62ac1d13ad4a62367744e106c759bbc9))
* fix license apis[#1258](https://github.com/JanssenProject/jans/issues/1258) ([#1271](https://github.com/JanssenProject/jans/issues/1271)) ([14c6a2b](https://github.com/JanssenProject/jans/commit/14c6a2b757bf94116faf9c0f13ab8c5e64c31f32))
* **jans-auth-server:** disabled issuing AT by refresh token if user status=inactive ([3df72a8](https://github.com/JanssenProject/jans/commit/3df72a83a59d11b2ac32aad80ec8207560f4813e))
* jans-cli scope dn/id when creating client ([518f971](https://github.com/JanssenProject/jans/commit/518f97147970c3a2465f4ef7d14481b05129f346))
* **jans-config-api:** corrected typo in swagger spec ([3c11556](https://github.com/JanssenProject/jans/commit/3c115566c843e42ae9827a76496145ddc6288155))
* **jans-config-api:** create openid client throwing 502 ([#1004](https://github.com/JanssenProject/jans/issues/1004)) ([3f58aff](https://github.com/JanssenProject/jans/commit/3f58affce39a15e051a1188c619b40115607f437))
* **jans-config-api:** LDAP test endpoint fix ([#1320](https://github.com/JanssenProject/jans/issues/1320)) ([fb0e132](https://github.com/JanssenProject/jans/commit/fb0e13251ee645862d8f02cbade5d64a2673a0b6))
* Typo httpLoggingExludePaths jans-auth-server jans-cli jans-config-api jans-linux-setup docker-jans-persistence-loader ([47a20ee](https://github.com/JanssenProject/jans/commit/47a20eefa781d1ca07a9aa30a5adcde3793076d1))
* Use highest level script in case ACR script is not found. Added FF to keep existing behavior. ([#1070](https://github.com/JanssenProject/jans/issues/1070)) ([07473d9](https://github.com/JanssenProject/jans/commit/07473d9a8c3e31f6a75670a874e17341518bf0be))


### Miscellaneous Chores

* release 1.0.0 ([b2895f2](https://github.com/JanssenProject/jans/commit/b2895f224b5772c0724ea0afbdf67a417a5c537c))
* release 1.0.0-beta.16 ([a083ad6](https://github.com/JanssenProject/jans/commit/a083ad6b1d43201126e8d4f690a55ea1b109524c))
* release 1.0.0-beta.16 ([90e4bb2](https://github.com/JanssenProject/jans/commit/90e4bb29df040bd9fe5921a054bc4226d34ca1ef))
* release 1.0.0-beta.16 ([eec2073](https://github.com/JanssenProject/jans/commit/eec2073be9fd25544f31087e171934afb9a71e6d))
* release 1.0.0-beta.16 ([cd92ead](https://github.com/JanssenProject/jans/commit/cd92ead2ca654383091c4923d3de5619b70fc5b9))
* release 1.0.0-beta.16 ([7f0a91b](https://github.com/JanssenProject/jans/commit/7f0a91bd90efc1cd7a80047f9cd6b7c6a22417a2))
* release 1.0.0-beta.16 ([c2ad604](https://github.com/JanssenProject/jans/commit/c2ad604dc29e7401bc4cb0788feaa20e11de0440))
* release 1.0.0-beta.16 ([a641486](https://github.com/JanssenProject/jans/commit/a6414864712789d1fcf80b823338100aebda030e))
* release 1.0.0-beta.16 ([94d5791](https://github.com/JanssenProject/jans/commit/94d5791a23fce4ecb8913c16c940cfbbc85fed4c))
* release 1.0.0-beta.16 ([16de429](https://github.com/JanssenProject/jans/commit/16de4299bc5e9c4a842f279ae0d3ae8282a4ff2c))
* release 1.0.0-beta.16 ([72915c0](https://github.com/JanssenProject/jans/commit/72915c0e82b9684ac1c59934d5b9a36c2456058d))
* release 1.0.0-beta.16 ([3ea2b37](https://github.com/JanssenProject/jans/commit/3ea2b37deac3416564614fb6a4e84b056ddbed3f))
* release 1.0.0-beta.16 ([78a6d39](https://github.com/JanssenProject/jans/commit/78a6d39ffadf9abee18c7be0e14ad3eb6ec2ef1b))
* release 1.0.0-beta.16 ([11bfa93](https://github.com/JanssenProject/jans/commit/11bfa9368e6ee482cc44240de08c8133d91b3f4c))
* release 1.0.0-beta.16 ([22b180b](https://github.com/JanssenProject/jans/commit/22b180bba9a08045a6daa7ca8ee2b71abd42a973))
* release 1.0.0-beta.16 ([b9acd0b](https://github.com/JanssenProject/jans/commit/b9acd0bceeeb54e3c47f869f11d97a22e8dc161f))
* release 1.0.0-beta.16 ([328cd30](https://github.com/JanssenProject/jans/commit/328cd309ae1655a52709e13ca2f89441c6c965a2))
* release 1.0.0-beta.16 ([5a84602](https://github.com/JanssenProject/jans/commit/5a84602838fb5d2e667422220fcd44dc53543e23))
* release 1.0.0-beta.16 ([4923277](https://github.com/JanssenProject/jans/commit/4923277b100b5c814d94b27b88d1809794dfc413))
* release 1.0.0-beta.16 ([258ba96](https://github.com/JanssenProject/jans/commit/258ba962bd93eb5be4d51e7de3a80da89c2e222f))
* release 1.0.0-beta.16 ([77c4423](https://github.com/JanssenProject/jans/commit/77c4423d82b697fd91a0e61f40bad6bd9da0dba8))
* release 1.0.0-beta.16 ([688b324](https://github.com/JanssenProject/jans/commit/688b32407b396917695cca787c08e95fe98269a1))
* release 1.0.0-beta.16 ([4e86f15](https://github.com/JanssenProject/jans/commit/4e86f15fc39ec89d4790ebfaa7d30e7053fef606))
* release 1.0.0-beta.16 ([8d514ee](https://github.com/JanssenProject/jans/commit/8d514ee63d840627321de2d89e816577dd919914))
* release 1.0.0-beta.16 ([0899898](https://github.com/JanssenProject/jans/commit/0899898e80ba9b7e6a915574737bdf0756b59a14))

## [1.0.0-beta.16](https://github.com/JanssenProject/jans/compare/jans-config-api-v1.0.0-beta.15...jans-config-api-v1.0.0-beta.16) (2022-03-14)


### Features

* add acrValues property in admin-ui configuration. [#1016](https://github.com/JanssenProject/jans/issues/1016) ([#1017](https://github.com/JanssenProject/jans/issues/1017)) ([88b591a](https://github.com/JanssenProject/jans/commit/88b591a64bf9ed0fb49942b770d9f0e334b7433c))
* **jans-config-api:** swagger spec change to add extension ([4f9d76c](https://github.com/JanssenProject/jans/commit/4f9d76cef689649f993df25e88e56526cfd26d02))
* **jans-config-api:** swagger spec change to add extension to differentiate plugin en… ([4f9d76c](https://github.com/JanssenProject/jans/commit/4f9d76cef689649f993df25e88e56526cfd26d02))
* support regex client attribute to validate redirect uris ([#1005](https://github.com/JanssenProject/jans/issues/1005)) ([a78ee1a](https://github.com/JanssenProject/jans/commit/a78ee1a3cfc4e7a6d08a500750edb5db0f7709a4))
* swagger spec change to add extension to differentiate plugin endpoint ([bb3b88a](https://github.com/JanssenProject/jans/commit/bb3b88a59376ff8875e1b38048a9c360e01de8de))


### Bug Fixes

* change in swagger spec for jwks to return missing attributes ([477643b](https://github.com/JanssenProject/jans/commit/477643bf6cc1fc6226ce7790e05c1a981324d06e))
* **jans-config-api:** create openid client throwing 502 ([#1004](https://github.com/JanssenProject/jans/issues/1004)) ([3f58aff](https://github.com/JanssenProject/jans/commit/3f58affce39a15e051a1188c619b40115607f437))


### Miscellaneous Chores

* release 1.0.0-beta.16 ([a083ad6](https://github.com/JanssenProject/jans/commit/a083ad6b1d43201126e8d4f690a55ea1b109524c))
* release 1.0.0-beta.16 ([90e4bb2](https://github.com/JanssenProject/jans/commit/90e4bb29df040bd9fe5921a054bc4226d34ca1ef))
* release 1.0.0-beta.16 ([eec2073](https://github.com/JanssenProject/jans/commit/eec2073be9fd25544f31087e171934afb9a71e6d))
* release 1.0.0-beta.16 ([cd92ead](https://github.com/JanssenProject/jans/commit/cd92ead2ca654383091c4923d3de5619b70fc5b9))
* release 1.0.0-beta.16 ([7f0a91b](https://github.com/JanssenProject/jans/commit/7f0a91bd90efc1cd7a80047f9cd6b7c6a22417a2))
* release 1.0.0-beta.16 ([c2ad604](https://github.com/JanssenProject/jans/commit/c2ad604dc29e7401bc4cb0788feaa20e11de0440))
* release 1.0.0-beta.16 ([a641486](https://github.com/JanssenProject/jans/commit/a6414864712789d1fcf80b823338100aebda030e))
* release 1.0.0-beta.16 ([94d5791](https://github.com/JanssenProject/jans/commit/94d5791a23fce4ecb8913c16c940cfbbc85fed4c))
* release 1.0.0-beta.16 ([16de429](https://github.com/JanssenProject/jans/commit/16de4299bc5e9c4a842f279ae0d3ae8282a4ff2c))
* release 1.0.0-beta.16 ([72915c0](https://github.com/JanssenProject/jans/commit/72915c0e82b9684ac1c59934d5b9a36c2456058d))
* release 1.0.0-beta.16 ([3ea2b37](https://github.com/JanssenProject/jans/commit/3ea2b37deac3416564614fb6a4e84b056ddbed3f))
* release 1.0.0-beta.16 ([78a6d39](https://github.com/JanssenProject/jans/commit/78a6d39ffadf9abee18c7be0e14ad3eb6ec2ef1b))
* release 1.0.0-beta.16 ([11bfa93](https://github.com/JanssenProject/jans/commit/11bfa9368e6ee482cc44240de08c8133d91b3f4c))
* release 1.0.0-beta.16 ([22b180b](https://github.com/JanssenProject/jans/commit/22b180bba9a08045a6daa7ca8ee2b71abd42a973))
* release 1.0.0-beta.16 ([b9acd0b](https://github.com/JanssenProject/jans/commit/b9acd0bceeeb54e3c47f869f11d97a22e8dc161f))
* release 1.0.0-beta.16 ([328cd30](https://github.com/JanssenProject/jans/commit/328cd309ae1655a52709e13ca2f89441c6c965a2))
* release 1.0.0-beta.16 ([5a84602](https://github.com/JanssenProject/jans/commit/5a84602838fb5d2e667422220fcd44dc53543e23))
* release 1.0.0-beta.16 ([4923277](https://github.com/JanssenProject/jans/commit/4923277b100b5c814d94b27b88d1809794dfc413))
* release 1.0.0-beta.16 ([258ba96](https://github.com/JanssenProject/jans/commit/258ba962bd93eb5be4d51e7de3a80da89c2e222f))
* release 1.0.0-beta.16 ([77c4423](https://github.com/JanssenProject/jans/commit/77c4423d82b697fd91a0e61f40bad6bd9da0dba8))
* release 1.0.0-beta.16 ([688b324](https://github.com/JanssenProject/jans/commit/688b32407b396917695cca787c08e95fe98269a1))
* release 1.0.0-beta.16 ([4e86f15](https://github.com/JanssenProject/jans/commit/4e86f15fc39ec89d4790ebfaa7d30e7053fef606))
* release 1.0.0-beta.16 ([8d514ee](https://github.com/JanssenProject/jans/commit/8d514ee63d840627321de2d89e816577dd919914))
* release 1.0.0-beta.16 ([0899898](https://github.com/JanssenProject/jans/commit/0899898e80ba9b7e6a915574737bdf0756b59a14))

## 1.0.0-beta.15 (2022-03-02)


### Features

* add deletable flag to admin-ui role object [#888](https://github.com/JanssenProject/jans/issues/888) ([#901](https://github.com/JanssenProject/jans/issues/901)) ([5b95a55](https://github.com/JanssenProject/jans/commit/5b95a552130f69df91b3d841e07df5d7d64e3c74))
* **jans-config-api:** add deletable flag to admin-ui role object [#888](https://github.com/JanssenProject/jans/issues/888) ([#900](https://github.com/JanssenProject/jans/issues/900)) ([500a773](https://github.com/JanssenProject/jans/commit/500a77358ad6d811fc95de3a13829d6f983bc1b0))
* **jans-config-api:** all config-api plugins should be in same plugins folder in maven repo [#851](https://github.com/JanssenProject/jans/issues/851) ([#852](https://github.com/JanssenProject/jans/issues/852)) ([cca93b2](https://github.com/JanssenProject/jans/commit/cca93b2cf6befad9488a8c0bdbf2554d4886faf1))
* **jans-config-api:** config api interception script ([#840](https://github.com/JanssenProject/jans/issues/840)) ([8e4c688](https://github.com/JanssenProject/jans/commit/8e4c68889f9286e68ddd79d05ebd0d1bebd68097))
* **jans-config-api:** organization configuration management endpoints ([#790](https://github.com/JanssenProject/jans/issues/790)) ([40ca464](https://github.com/JanssenProject/jans/commit/40ca464b17a5dc0324d01b0510dac8b0beec9bd0))
* **jans-config-api:** scim config endpoint issue [#271](https://github.com/JanssenProject/jans/issues/271) ([#665](https://github.com/JanssenProject/jans/issues/665)) ([a6e9a04](https://github.com/JanssenProject/jans/commit/a6e9a0435a30816fd738b9287a4842fe03321a6c))
* **jans-config-api:** security issue - upgrade dependencies ([#883](https://github.com/JanssenProject/jans/issues/883)) ([10568ff](https://github.com/JanssenProject/jans/commit/10568ff1123bc27900254bcf865d23f6be4c59ad))
* **jans-config-api:** swagger update for default value ([#862](https://github.com/JanssenProject/jans/issues/862)) ([8f59921](https://github.com/JanssenProject/jans/commit/8f599219f00f85f1624d89745ec74eaf5c17df49))
* **jans-config-api:** underlying server stats [#275](https://github.com/JanssenProject/jans/issues/275) ([ae6f2d7](https://github.com/JanssenProject/jans/commit/ae6f2d7f89ae3c72e62bcb42b1e62c9c350f657e))
* underlying server stats ([ae6f2d7](https://github.com/JanssenProject/jans/commit/ae6f2d7f89ae3c72e62bcb42b1e62c9c350f657e))
* underlying server stats ([0f36336](https://github.com/JanssenProject/jans/commit/0f36336da9cacad8de8f1bfc060da66235494b79))
* underlying server stats ([56b72e9](https://github.com/JanssenProject/jans/commit/56b72e9272d0bd69b4a31bb0f8320d662233988a))


### Bug Fixes

* **jans-config-api:** excluded test from execution ([#760](https://github.com/JanssenProject/jans/issues/760)) ([3af6672](https://github.com/JanssenProject/jans/commit/3af6672401f9d7782b2fc13e5bf67f763b58e9b4))
* **jans-config-api:** license validity period should be read only [#731](https://github.com/JanssenProject/jans/issues/731) ([f88095b](https://github.com/JanssenProject/jans/commit/f88095b1f52f0639221e4109ed7262099e06d0e9))
* **jans-config-api:** multiple custom lib not working  ([#907](https://github.com/JanssenProject/jans/issues/907)) ([9ef6fa4](https://github.com/JanssenProject/jans/commit/9ef6fa49afe0efb64ee87aa2485f95a7716e4259))
* **jans-config-api:** sql configuration endpoints are not found [#793](https://github.com/JanssenProject/jans/issues/793) ([#794](https://github.com/JanssenProject/jans/issues/794)) ([d8f2ea9](https://github.com/JanssenProject/jans/commit/d8f2ea949aa7735c3d236a5685d30c4085f7892c))
* license validity period should be read only [#731](https://github.com/JanssenProject/jans/issues/731) ([#746](https://github.com/JanssenProject/jans/issues/746)) ([73931f5](https://github.com/JanssenProject/jans/commit/73931f56d9bd216f172008ec3c3a713e40cb4645))


### Miscellaneous Chores

* release 1.0.0-beta.15 ([ee5b719](https://github.com/JanssenProject/jans/commit/ee5b719bee5cc4bdaebf81a5103e6a7ab0695dbb))
* release 1.0.0-beta.15 ([ca6d1c9](https://github.com/JanssenProject/jans/commit/ca6d1c9e2acb5e6422e1cd26ac277dd3eba4e56e))
* release 1.0.0-beta.15 ([b65bab2](https://github.com/JanssenProject/jans/commit/b65bab20530b7d6736dd404e26649abf47c0fb60))