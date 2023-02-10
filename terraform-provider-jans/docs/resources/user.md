---
# generated by https://github.com/hashicorp/terraform-plugin-docs
page_title: "jans_user Resource - terraform-provider-jans"
subcategory: ""
description: |-
  Resource represents a user resource. See section 4.1 of RFC 7643.
---

# jans_user (Resource)

Resource represents a user resource. See section 4.1 of RFC 7643.

## Example Usage

```terraform
resource jans_user "user" {
  display_name        = "test-user"
  schemas             = [ "urn:ietf:params:scim:schemas:core:2.0:User" ]
  external_id         = "ext1234"
  user_name           = "test-user"
  nick_name           = "test-user"
  profile_url         = "https://localhost:9443/scim/v2/Users/1234"
  title               = "Mr"
  user_type           = "Employee"
  preferred_language  = "en"
  locale              = "en_US"
  timezone            = "UTC"
  active              = true
  password            = "password"
  
  name {
    family_name     = "Doe"
    given_name       = "John"
    middle_name      = "M"
    honorific_prefix = "Dr"
    honorific_suffix = "Jr"
    formatted				 = "Dr John M Doe Jr"
  }

  emails {
    value   = "john.doe@jans.io"
    display = "Work"
    type    = "work"
    primary = true
  }
  
  phone_numbers {
    value   = "1234567890"
    display = "Mobile"
    type    = "work"
    primary = true
  }

  ims {
    value   = "@john.doe"
    display = "Messenger"
    type    = "Messenger"
    primary = true
  }

  photos {
    value   = "https://localhost:9443/scim/v2/Users/1234/photo"
    display = "Photo"
    type    = "photo"
    primary = true
  }

  addresses {
    formatted       = "123 Main St"
    street_address  = "123 Main St"
    locality        = "New York"
    region          = "NY"
    postal_code     = "12345"
    country         = "US"
    type            = "work"
    primary         = true
  }

  entitlements {
    value   = "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:entitlement"
    display = "Entitlement"
    type    = "entitlement"
    primary = true
  }

  roles {
    value   = "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:role"
    display = "Role"
    type    = "role"
    primary = true
  }

  x509_certificates {
    value   = "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:x509Certificates"
    display = "X509Certificates"
    type    = "PEM"
    primary = true
  }
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Optional

- `active` (Boolean)
- `addresses` (Block List) (see [below for nested schema](#nestedblock--addresses))
- `display_name` (String) Name of the user suitable for display to end-users
- `emails` (Block List) (see [below for nested schema](#nestedblock--emails))
- `entitlements` (Block List) (see [below for nested schema](#nestedblock--entitlements))
- `extensions` (Map of String) Extended attributes
- `external_id` (String) Identifier of the resource useful from the perspective of the provisioning client. See section 3.1 of RFC 7643
- `ims` (Block List) (see [below for nested schema](#nestedblock--ims))
- `locale` (String) Used for purposes of localizing items such as currency and dates Example: en-US
- `name` (Block List, Max: 1) (see [below for nested schema](#nestedblock--name))
- `nick_name` (String) Casual way to address the user in real life
- `password` (String)
- `phone_numbers` (Block List) (see [below for nested schema](#nestedblock--phone_numbers))
- `photos` (Block List) (see [below for nested schema](#nestedblock--photos))
- `preferred_language` (String) Preferred language as used in the Accept-Language HTTP header Example: en
- `profile_url` (String) URI pointing to a location representing the User's online profile
- `roles` (Block List) (see [below for nested schema](#nestedblock--roles))
- `schemas` (List of String) A list of URIs of the schemas used to define the attributes of the user.
- `timezone` (String) Example: America/Los_Angeles
- `title` (String) Example: Vice President
- `user_name` (String) Identifier for the user, typically used by the user to directly authenticate (id and externalId are opaque identifiers generally not known by users)
- `user_type` (String) Used to identify the relationship between the organization and the user Example: Contractor
- `x509_certificates` (Block List) (see [below for nested schema](#nestedblock--x509_certificates))

### Read-Only

- `groups` (List of Object) (see [below for nested schema](#nestedatt--groups))
- `id` (String) The unique identifier for the user.
- `meta` (List of Object) A complex type that contains meta attributes associated with the resource. (see [below for nested schema](#nestedatt--meta))

<a id="nestedblock--addresses"></a>
### Nested Schema for `addresses`

Optional:

- `country` (String) Country expressed in ISO 3166-1 'alpha-2' code format Example: UK
- `formatted` (String) Full mailing address, formatted for display or use with a mailing label
- `locality` (String) City or locality of the address
- `postal_code` (String) Zip code
- `primary` (Boolean) Denotes if this is the preferred address among others, if any
- `region` (String) State or region of the address
- `street_address` (String) Example: 56 Acacia Avenue
- `type` (String) Example: home


<a id="nestedblock--emails"></a>
### Nested Schema for `emails`

Required:

- `value` (String) Example: johndoe@jans.io

Optional:

- `display` (String)
- `primary` (Boolean) Denotes if this is the preferred e-mail among others, if any
- `type` (String) Example: work


<a id="nestedblock--entitlements"></a>
### Nested Schema for `entitlements`

Required:

- `value` (String) Example: Stakeholder

Optional:

- `display` (String)
- `primary` (Boolean) Denotes if this is the preferred entitlement among others, if any
- `type` (String)


<a id="nestedblock--ims"></a>
### Nested Schema for `ims`

Required:

- `value` (String)

Optional:

- `display` (String)
- `primary` (Boolean) Denotes if this is the preferred messaging addressed among others, if any
- `type` (String) Example: gtalk


<a id="nestedblock--name"></a>
### Nested Schema for `name`

Optional:

- `family_name` (String)
- `given_name` (String)
- `honorific_prefix` (String) A 'title' like 'Ms.', 'Mrs.'
- `honorific_suffix` (String) Name suffix, like 'Junior', 'The great', 'III'
- `middle_name` (String)

Read-Only:

- `formatted` (String) Full name, including all middle names, titles, and suffixes as appropriate


<a id="nestedblock--phone_numbers"></a>
### Nested Schema for `phone_numbers`

Required:

- `value` (String) Example: +1-555-555-8377

Optional:

- `display` (String)
- `primary` (Boolean) Denotes if this is the preferred phone number among others, if any
- `type` (String) Example: fax


<a id="nestedblock--photos"></a>
### Nested Schema for `photos`

Required:

- `value` (String) Example: https://static.jans.io/profile.png

Optional:

- `display` (String)
- `primary` (Boolean) Denotes if this is the preferred photo among others, if any
- `type` (String) Example: thumbnail


<a id="nestedblock--roles"></a>
### Nested Schema for `roles`

Required:

- `value` (String) Example: Project manager

Optional:

- `display` (String)
- `primary` (Boolean) Denotes if this is the preferred role among others, if any
- `type` (String)


<a id="nestedblock--x509_certificates"></a>
### Nested Schema for `x509_certificates`

Required:

- `value` (String) DER-encoded X.509 certificate

Optional:

- `display` (String)
- `primary` (Boolean) Denotes if this is the preferred certificate among others, if any
- `type` (String)


<a id="nestedatt--groups"></a>
### Nested Schema for `groups`

Read-Only:

- `display` (String)
- `ref` (String)
- `type` (String)
- `value` (String)


<a id="nestedatt--meta"></a>
### Nested Schema for `meta`

Read-Only:

- `created` (String)
- `last_modified` (String)
- `location` (String)
- `resource_type` (String)

