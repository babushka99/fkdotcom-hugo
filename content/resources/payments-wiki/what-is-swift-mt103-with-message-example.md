---
title: "SWIFT MT103 with Message Example"
date: 2023-12-14T13:19:01+0000
lastmod: 2025-08-11T12:00:59
draft: false
description: "SWIFT MT103 with Message Example - Payment industry knowledge and insights"
keywords: ["payments", "fintech", "money transfer", "banking"]
---

Looking for SWIFT MT103 with Message Example, this is the right place. The SWIFT MT103 is a type of financial message format used by the [Society for Worldwide Interbank Financial Telecommunication (SWIFT)](https://faisalkhanllc.xyz/resources/payments-wiki/s/society-for-worldwide-interbank-financial-telecommunication-swift/). It's commonly used for client and bank transfers. To learn more about the SWIFT MT103, including its structure, mandatory and optional fields, and how it works, you can follow these steps:

  ## UNLOCK PREMIUM BANKING ACCESS
  
  Stop being rejected. Money service businesses and fintechs deserve elite banking relationships with instant global payments and multi-currency support.

        ✓ US Bank Accounts

        ✓ Pooled Accounts

        ✓ FBO Accounts

        ✓ Collection Accounts

        ✓ Multi-Currency

        ✓ Named Accounts

        ✓ SWIFT & IBANs

        ✓ Crypto Friendly

  [SECURE YOUR ACCOUNT](https://faisalkhan.com/knowledge-center/forms/bank-account-inquiry-form/?utm_source=organic&utm_medium=website&utm_term=swift-mt-103-example)
  
  96% approval rate • Setup in as little as 7 days

- **SWIFT User Handbook:** The most detailed and authoritative source would be the SWIFT User Handbook, which provides comprehensive information on all SWIFT message types, including MT103. This handbook typically requires a subscription or access through a financial institution.

- **Online Financial Courses:** There are numerous online courses and tutorials that cover SWIFT messaging, including MT103. Websites like Udemy, Coursera, or LinkedIn Learning often have such courses.

- **Financial Institutions' Websites:** Many banks and [financial institutions](https://faisalkhanllc.xyz/resources/payments-wiki/f/financial-institution-fi/) provide guides or summaries of different SWIFT message types on their websites. These can be a good resource for understanding the practical aspects of these messages.

- **Books and Publications:** There are books focused on financial messaging and SWIFT operations. You can search for these at libraries or bookstores.

- **Forums and Online Communities:** Online forums like Stack Exchange or specialized finance forums can be valuable resources for practical insights and tips from professionals in the field.

- **YouTube Tutorials:** YouTube may have tutorials or explanatory videos on SWIFT messages.

- **Professional Training:** If you're working in a related field, your employer might provide access to professional training courses that include SWIFT messaging systems.

- **SWIFT's Official Website:** SWIFT's official website sometimes provides overviews and basic information on different message types, including MT103.

Download SWIFT MT103 Cheatsheet

- [SWIFT MT103 with Message Example Cheatsheet](https://faisalkhan.com/wp-content/uploads/2024/12/SWIFT-MT103-Message-Format-Cheatsheet-Faisal-Khan-LLC.pdf)

Understanding a SWIFT MT103 message involves learning about its various fields, such as the sender's and receiver's information, transaction details, and optional vs. mandatory fields. This message is used to specify a transfer of funds between two banks and includes important financial details.

The SWIFT MT103 format is used for making a single customer credit transfer and contains various fields to specify the details of the transaction. Here's a breakdown of its key components:

#### 1. **Basic Header Block**

- **Field 1:** Contains the message type, in this case, "103" for a customer transfer.

#### 2. **Application Header Block**

- **Field 2:** Sender's and receiver's bank information, including bank identifiers and branch information.

#### 3. **User Header Block**

- Optional fields for specific user information, not always used.

#### 4. **Text Block**

- **Field 20:** Transaction Reference Number.

- **Field 23B:** Bank Operation Code.

- **Field 32A:** Value Date, Currency, and Amount.

- **Field 33B:** Currency/Instructed Amount.

- **Field 50A, F, or K:** Ordering Customer (payer).

- **Field 51A:** Sending Institution.

- **Field 52A, D, or R:** Ordering Institution.

- **Field 53A, B, or D:** Sender's Correspondent.

- **Field 54A, B, or D:** Receiver's Correspondent.

- **Field 56A, C, or D:** Intermediary Institution.

- **Field 57A, B, C, or D:** Account With Institution (beneficiary's bank).

- **Field 59:** Beneficiary Customer.

- **Field 70:** Remittance Information (reason/payment details).

- **Field 71A:** Details of Charges.

- **Field 71F:** Sender's Charges.

- **Field 71G:** Receiver's Charges.

- **Field 72:** Sender to Receiver Information.

#### 5. **Trailer Block**

- Contains check sums and end-of-message indicators.

### Mandatory and Optional Fields:

- **Mandatory Fields:** Fields like 20 (Transaction Reference Number), 32A (Value Date, Currency, and Amount), 50A/K/F (Ordering Customer), and 59 (Beneficiary Customer) are mandatory. They are essential for the transaction's basic information.

- **Optional Fields:** Fields like 71F (Sender's Charges) or 72 (Sender to Receiver Information) are optional and may be used depending on the specifics of the transaction or the requirements of the banks involved.

Each of these fields has a specific format and set of rules for what information must be included. The MT103 format is standardized to ensure consistency and clarity in international financial transactions. Understanding the details of each field can require some familiarity with financial terminology and international banking practices.

  ### Doing Cross-Border Payments? You’ll Need the Right Bank.
  SWIFT MT103s are only useful if your bank supports the right features. We work with MSB-friendly banks that offer:

    - Named accounts with IBAN & SWIFT
    - Multi-currency accounts
    - Segregated & pooled account options
    - OUR/BEN/SHA support
    - Virtual accounts mapped to a master IBAN
    - Fast onboarding for regulated entities
    - Crypto-compatible banking (optional)
  
  [Request an introduction →](https://faisalkhan.com/knowledge-center/forms/bank-account-inquiry-form/?utm_source=organic&utm_medium=website&utm_term=swift-mt-103-example)

## SWIFT MT103 with Message Example: Please note that this is a fictional example for illustrative purposes only:

`{1:F01BANKBEBBAXXX1234567890}{2:O1031130050901BANKBEBBAXXX12345678900509011311N}{3:{108:MT103}}
{4:
:20:REFERENCE12345
:23B:CRED
:32A:230501EUR123456,78
:50A:/12345678901234567890
MR. JOHN DOE
:59:/23456789012345678901
MS. JANE SMITH
:70:INVOICE 987654
:71A:SHA
-}`

Explanation of the fields in this example:

- **{1:F01BANKBEBBAXXX1234567890}**: Basic Header Block indicating the message type (F01) and the sender's bank identifier (BANKBEBBAXXX with a logical terminal address of 1234567890).

- **{2:O1031130050901BANKBEBBAXXX12345678900509011311N}**: Application Header Block with sender's and receiver's information.

- **{3:{108:MT103}}**: User Header Block with a reference to MT103.

- **:20:REFERENCE12345**: Transaction Reference Number.

- **:23B:CRED**: Bank Operation Code (Credit).

- **:32A:230501EUR123456,78**: Value Date (YYMMDD - 23rd May 2001), Currency (EUR), and Transaction Amount.

- **:50A:/12345678901234567890 MR. JOHN DOE**: Ordering Customer’s Account Number and Name.

- **:59:/23456789012345678901 MS. JANE SMITH**: Beneficiary Customer’s Account Number and Name.

- **:70:INVOICE 987654**: Details of Remittance (e.g., Invoice Number).

- **:71A:SHA**: Details of Charges (SHA for shared).

This example illustrates the format and type of information typically included in a SWIFT MT103 message. Each field provides specific details required for processing the international transfer, including who is sending the money, who is receiving it, the amount, and any other relevant information.

Here's a more complex example of a SWIFT MT103 message, featuring additional details and optional fields. As before, this is a fictional example for illustrative purposes:

`{1:F01DEUTDEFFXXXX1234567890}{2:O1030953230523NORDDKKKXXXX12345678932305230953N}{3:{108:ILOVESEPA1234567890}}
{4:
:20:TXNREF1234567890
:23B:CRED
:32A:230523EUR100000,50
:50K:/12345678
JOHN DOE
123, FAKE STREET
FAKETOWN
:52A:DEUTDEFFXXX
:53B:/DE12345678901234567890
:54A:CHASUS33XXX
:56C:IRVTUS3NXXX
:57A:NORDDKKKXXX
:59:/DK5000400440116243
JANE SMITH
789, REAL ROAD
REALVILLE
:70:PAYMENT FOR INVOICE 998877
:71A:OUR
:72:/ACC/RENT/MAY
/INV/998877
-}
{5:{CHK:123456789ABC}{TNG:}}`

### Explanation of the Fields:

- **{1:F01DEUTDEFFXXXX1234567890}**: Basic Header. It indicates the message format (F01) and the sender's bank BIC (DEUTDEFFXXXX with a terminal address of 1234567890).

- **{2:O1030953230523NORDDKKKXXXX12345678932305230953N}**: Application Header. It contains details like the message type, sender's and receiver's information, and date and time of sending.

- **{3:{108:ILOVESEPA1234567890}}**: User Header. It has an optional reference (ILOVESEPA1234567890) for the message.

- **:20:TXNREF1234567890**: Transaction Reference Number for the bank's internal use.

- **:23B:CRED**: Bank Operation Code, indicating it's a credit transfer.

- **:32A:230523EUR100000,50**: Date (23rd May 2023), currency (EUR), and amount (100,000.50 Euros).

- **:50K:/12345678 JOHN DOE 123, FAKE STREET FAKETOWN**: Ordering Customer's account number, name, and address.

- **:52A:DEUTDEFFXXX**: Ordering Institution - the BIC of the bank where the ordering customer has their account.

- **:53B:/DE12345678901234567890**: Sender's Correspondent - the account used by the sender's bank to make the payment.

- **:54A:CHASUS33XXX**: Receiver's Correspondent - the receiver bank's correspondent bank.

- **:56C:IRVTUS3NXXX**: Intermediary Bank - a third bank involved in the transaction.

- **:57A:NORDDKKKXXX**: 'Account With' Institution - the BIC of the receiver's bank.

- **:59:/DK5000400440116243 JANE SMITH 789, REAL ROAD REALVILLE**: Beneficiary Customer's account number, name, and address.

- **:70:PAYMENT FOR INVOICE 998877**: Remittance Information - details of the payment purpose.

- **:71A:OUR**: Details of Charges - 'OUR' indicates all charges are borne by the sender.

- **:72:/ACC/RENT/MAY /INV/998877**: Sender to Receiver Information - additional instructions or details for the receiving bank.

- **{5:{CHK:123456789ABC}{TNG:}}**: Trailer Block containing the message checksum for validation.

This example illustrates a more complex SWIFT MT103 message, with comprehensive information including intermediary banks, detailed addresses of the [payer](https://faisalkhanllc.xyz/resources/payments-wiki/p/payer/) and [payee](https://faisalkhanllc.xyz/resources/payments-wiki/p/payee/), and specific instructions for the transaction. The inclusion of intermediary and [correspondent banks](https://faisalkhanllc.xyz/resources/payments-wiki/c/correspondent-bank/) is common in international transactions where direct routes between the sending and receiving banks are not available.

  ## Need a Bank That Supports Your SWIFT Needs?
  We work with banks that understand MSBs, PSPs, and Fintechs. Stop getting rejected. Start transacting.

  [Get Introduced to a Bank](https://faisalkhan.com/knowledge-center/forms/bank-account-inquiry-form/?utm_source=organic&utm_medium=website&utm_term=swift-mt-103-example)

## External Link:

[SWIFT Home Page](https://www.swift.com/)