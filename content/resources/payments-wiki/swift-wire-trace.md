---
title: "SWIFT Wire Trace"
date: 2024-08-06T18:51:30+0000
lastmod: 2025-08-11T12:15:45
draft: false
description: "SWIFT Wire Trace - Payment industry knowledge and insights"
keywords: ["payments", "fintech", "money transfer", "banking"]
---

### How to Trace a SWIFT Wire Transfer?

Understanding how to trace a SWIFT wire transfer is crucial, especially when the recipient claims they haven't received the funds. This guide will explain the process of swift wire tracking from both the sending and receiving perspectives, making it easy for even a novice to follow.

### What is SWIFT?

[SWIFT (Society for Worldwide Interbank Financial Telecommunication)](https://faisalkhan.com/learn/payments-wiki/society-for-worldwide-interbank-financial-telecommunication-swift/) is a network that enables secure financial transactions between banks globally. When you send money internationally through your bank, it often goes through the SWIFT network.

### Sending a SWIFT Wire Transfer

- **Initiating the Transfer**:

You (the sender) visit your bank to initiate an international wire transfer.

- Provide necessary details: recipient’s name, address, bank name, bank address, SWIFT/BIC code of the recipient’s bank, the recipient’s account number, and the amount to be sent.

- **Bank Processing**:

Your bank creates a SWIFT message ([MT103](https://faisalkhanllc.xyz/resources/payments-wiki/s/society-for-worldwide-interbank-financial-telecommunication-swift/what-is-swift-mt103/)) containing all transaction details.

- This message is sent through the SWIFT network to the recipient’s bank or intermediary banks if the transfer requires routing through multiple banks.

- **Transfer Confirmation**:

Your bank provides you with a reference number (often called the [UETR - Unique End-to-End Transaction Reference](https://faisalkhanllc.xyz/resources/payments-wiki/u/uetr-number/)) and possibly a copy of the SWIFT message as proof of the transfer.

### Tracing the Transfer (Sending Angle)

- **Initial Check**:

Ensure that all details provided for the transfer were correct.

- Wait for a reasonable time (typically 1-5 business days) depending on the countries involved.

- **Contact Your Bank**:

If the recipient hasn’t received the funds within the expected timeframe, contact your bank.

- Provide the reference number (UETR) and request them to initiate swift wire tracking.

- **Bank Investigation**:

Your bank will use the SWIFT network to send an MT199 (free format message) or MT192 (request for cancellation) to the recipient’s bank, querying the status of the transfer.

- The recipient’s bank will respond with the status update.

- **Status Update**:

Your bank will inform you about the status: whether the transfer is still in progress, has been received, or if there was an error.

### Receiving a SWIFT Wire Transfer

- **Notification**:

When a SWIFT transfer is initiated, the recipient's bank receives the SWIFT message (MT103).

- The recipient’s bank processes the transaction and credits the funds to the recipient’s account.

- **No Funds Received**:

If the recipient hasn’t received the funds, they should first verify their account details and check for any notifications from their bank regarding pending transactions.

- **Recipient’s Bank Inquiry**:

The recipient contacts their bank, providing details of the expected transfer and the sender’s information.

- The recipient’s bank uses the SWIFT reference (UETR) to trace the transaction within their system.

### Tracing the Transfer (Receiving Angle)

- **Bank’s Internal Check**:

The recipient’s bank checks their internal systems for any pending or delayed transactions.

- They verify if there were any issues with the crediting process.

- **Communication with Sender’s Bank**:

If the transfer is not found, the recipient’s bank communicates with the sender’s bank via the SWIFT network.

- They may send an MT192 or MT199 message to query the status or request more details about the transfer.

- **Response to Inquiry**:

The sender’s bank provides information on the transfer’s status.

- The recipient’s bank updates the recipient about the findings and takes necessary action to locate the funds.

### Common Issues and Solutions

- **Incorrect Details**: Incorrect recipient details can cause delays. Ensure all information provided is accurate.

- **Intermediary Banks**: Some transfers go through intermediary banks, which can introduce delays. Both sender and recipient banks should check with these intermediaries.

- **Bank Processing Times**: Different banks have different processing times, which can affect transfer speed.

- **Compliance Checks**: Large transfers may undergo additional scrutiny for compliance with anti-money laundering regulations.

### Conclusion

Swift wire tracking involves cooperation between the sender, recipient, and their respective banks. Using the SWIFT network, banks can send and receive messages to trace and resolve any issues with the transfer. Always keep the transaction reference number (UETR) handy, as it is crucial for tracking the transfer’s status.