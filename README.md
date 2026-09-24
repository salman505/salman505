# True Tech Solutions – Odoo website

`website_truetech` is an Odoo 17 Website module that recreates the public
[www.truetech-sol.com](https://www.truetech-sol.com) site on the Odoo instance at
**erp.truetech-sol.com**.

## What it adds

| URL          | Page |
|--------------|------|
| `/`          | Homepage: hero, key stats, company intro, services, solutions, call to action |
| `/about`     | Company overview, mission, vision, team |
| `/services`  | IT Support, Managed Services, Consultancy, Turnkey Infrastructure, Software/ERP, Telecom |
| `/solutions` | IoT and RFID (Impinj), Retail Management, Integrated Security |
| `/contact`   | Offices, phone numbers, email, business hours |

It also adds the main menu entries, a company footer and brand styling
(`static/src/scss/truetech.scss`). All pages remain editable in the Odoo website builder.

## Install on erp.truetech-sol.com

1. Copy the `website_truetech` folder into a directory on the server's `addons_path`
   (for Odoo.sh: push this repository as a branch of your project).
2. Restart Odoo, then in **Apps**, click **Update Apps List**.
3. Search for **True Tech Solutions Website** and click **Install**
   (the **Website** app is installed automatically if it isn't already).

Command-line alternative:

```bash
odoo -d <your_database> -i website_truetech --stop-after-init
```

## After installing

- Upload the company logo under **Website → Configuration → Settings**.
- Delete the default "Contact us" menu entry if you don't want it next to the new **Contact** entry.
- Set the brand colours at the top of `truetech.scss` to match the logo.

## Preview

Screenshots from a clean Odoo 17 install are in [`screenshots/`](screenshots/).
