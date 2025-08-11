---
title: "Proof of Reserves (PoR)"
date: 2025-02-17T09:26:46+0000
lastmod: 2025-08-11T12:15:45
draft: false
description: "Proof of Reserves (PoR) - Payment industry knowledge and insights"
keywords: ["payments", "fintech", "money transfer", "banking"]
---

### Definition

Proof of Reserves (PoR) is a cryptographic method used by centralized cryptocurrency exchanges and [custodians to publicly verify that they hold enough assets to cover user balances](https://faisalkhanllc.xyz/resources/payments-wiki/c/custodying-in-cryptocurrency-and-blockchain/). It ensures transparency and builds trust by proving that an institution actually possesses the funds it claims to hold.

### Background / Backstory on Proof of Reserves

The concept of PoR gained traction after multiple high-profile crypto exchange collapses—most notably **FTX in 2022**, where billions of dollars in customer funds were mismanaged. This lack of transparency led to calls for stronger accountability measures in centralized exchanges (CEXs).

PoR emerged as a response to this crisis, enabling platforms to prove solvency without revealing sensitive user data. The method typically uses **Merkle trees** or **[zero-knowledge proofs (ZKPs)](https://faisalkhanllc.xyz/resources/payments-wiki/z/zero-knowledge-proof-zkp/)** to cryptographically confirm reserves without exposing individual account balances.

### How is Proof of Reserves Used in the Industry Today?

PoR is widely used by **centralized exchanges (CEXs), custodians, and lending platforms** to provide users and regulators with confidence that their assets are not being misused.

### How It Works: Step-by-Step Process

- **Snapshot of Reserves** – The exchange or custodian takes a snapshot of all customer balances at a given time.

- **Merkle Tree Hashing** – User balances are compiled into a Merkle tree (a cryptographic structure) to maintain privacy.

- **Cryptographic Proof Generation** – The total exchange reserves are compared to liabilities, with the result published as a cryptographic proof.

- **Independent Audit (Optional)** – Some firms engage third-party auditors to validate the results and enhance credibility.

### Example 1: Binance’s Proof of Reserves

Binance, the world’s largest crypto exchange, implemented PoR to reassure users after FTX collapsed. It publishes snapshots of its Bitcoin holdings and liabilities, using **Merkle tree proofs** to confirm that it holds enough BTC to cover customer deposits.

### Example 2: Kraken’s PoR with Third-Party Auditors

Kraken regularly conducts PoR audits, working with independent accounting firms to verify its holdings against customer balances. Instead of just self-reporting, Kraken’s PoR includes professional verification, making it more trustworthy.

### Analogy: The Locked Safe Example

Imagine a bank claims it has **$1 million** in its vault. Instead of letting customers open the vault to count the cash, the bank:

- Takes a **picture of the cash** inside the vault (snapshot of reserves).

- Uses a **special barcode scanner** that sums up the money and encrypts the total (Merkle tree proof).

- Shares the **encrypted receipt** with customers to verify the total exists—without revealing anyone’s personal deposits.

That’s how PoR ensures transparency while maintaining privacy.

### Stakeholders and Implementation

### **Who Uses PoR?**

- **Centralized Crypto Exchanges (CEXs)** – Binance, Kraken, OKX, and others use PoR to validate holdings.

- **Crypto Custodians** – [Institutions like BitGo and Fireblocks leverage PoR to confirm assets are secure](https://faisalkhanllc.xyz/resources/payments-wiki/c/custodying-in-cryptocurrency-and-blockchain/).

- **Lending Platforms** – Services like Nexo and BlockFi (before its collapse) relied on PoR to assure users of liquidity.

### **Challenges in Implementation**

- **Exclusion of Liabilities** – Many PoR reports only show assets without disclosing outstanding debts.

- **No Real-Time Verification** – Snapshots are taken at a specific time but don’t account for fluctuations.

- **Trust in Auditors** – If auditors are biased or unqualified, PoR results can be misleading.

### Pros & Cons

### ✅ **Pros**

- **Increases Transparency** – Users can verify reserves exist without blind trust.

- **Prevents Insolvency Risks** – Helps identify potential liquidity crises early.

- **Strengthens User Confidence** – Essential after major exchange collapses like FTX.

### ❌ **Cons**

- **Not a Complete Audit** – Doesn’t always include liabilities or hidden risks.

- **Manual & Infrequent** – Most exchanges update PoR data only periodically.

- **Potential for Manipulation** – Some firms might game the system by borrowing assets before a PoR check.

### Future Outlook

The **future of PoR** is evolving with:

- **Real-time Proof of Reserves** – Companies like Chainlink are developing blockchain-based PoR that updates in real time.

- **Zero-Knowledge Proofs (ZKPs)** – More exchanges are adopting ZKPs to enhance privacy while verifying reserves.

- **Regulatory Adoption** – Governments may mandate PoR for licensed exchanges to prevent fraud.

### Further Reading

- [Binance Proof of Reserves](https://www.binance.com/)

- [Kraken PoR Audit Reports](https://www.kraken.com/)

- [Understanding Merkle Trees](https://www.bitcoin.it/wiki/Merkle_tree)