---
title: "Formulas for Automated Market Makers (AMMs)"
date: 2024-02-17T12:26:02+0000
lastmod: 2025-08-11T12:00:59
draft: false
description: "Formulas for Automated Market Makers (AMMs) - Payment industry knowledge and insights"
keywords: ["payments", "fintech", "money transfer", "banking"]
---

Automated Market Makers (AMM) use mathematical formulas to determine the price of assets in a [liquidity pool](https://faisalkhanllc.xyz/resources/payments-wiki/l/liquidity-pool/). The most common formula is the Constant Product Formula, represented as **x*y=k**, where:

- **x** is the amount of one token in the liquidity pool,

- **y** is the amount of the other token, and

- **k** is a constant value.

This formula ensures that the total value of the tokens in the pool remains constant before and after a trade. The price of a token in the pool is determined by the ratio of **x** to **y**. When a trade occurs, the supply of one token decreases while the other increases, automatically adjusting the price according to the formula.

### Example 1: Basic Trade

Let's consider a liquidity pool containing 2 tokens: Token A and Token B. Suppose the pool has 1,000 Token A and 1,000 Token B, making **k = 1,000 * 1,000 = 1,000,000**.

If someone wants to buy 100 Token A from the pool, the AMM adjusts the amounts of Token A and Token B to keep **k** constant. After the purchase, let's say the pool has 900 Token A; to find the new amount of Token B (**y**), we rearrange the formula to **y = k / x**.

`y = 1,000,000 / 900 = 1,111.11`

So, to keep **k** constant, the pool now needs 1,111.11 Token B, meaning the trader added approximately 111.11 Token B to buy 100 Token A.

### Example 2: Adding Liquidity

When adding liquidity, a user must maintain the existing ratio of the pool. Suppose the pool has 2,000 Token A and 4,000 Token B (**x:y** ratio is 1:2). If a user wants to add 500 Token A to the pool, they must also add 1,000 Token B to keep the ratio constant.

After adding liquidity, the pool has 2,500 Token A and 5,000 Token B, maintaining the **k** value at **2,500 * 5,000 = 12,500,000**.

### Example 3: Removing Liquidity

When a liquidity provider wants to remove their share of the pool, they do so according to their percentage of the pool's total liquidity. For instance, if the pool has 5,000 Token A and 10,000 Token B, and the provider owns 10% of the pool, they can withdraw 500 Token A and 1,000 Token B, maintaining the constant **k** value for the remaining liquidity.

This example showcases how the AMM formula maintains balance in the pool, ensuring that the action of adding or removing liquidity doesn't disrupt the market but instead follows the predetermined ratio, keeping the value of **k** constant.

These examples illustrate the fundamental working mechanism of AMMs in DeFi, demonstrating how trades, and liquidity additions or withdrawals, are facilitated while maintaining the pool's overall balance and integrity.

## Other Formulas for Automated Market Makers (AMMs)

Besides the Constant Product Formula ((x*y = k)), which is widely used in decentralized finance (DeFi) platforms like Uniswap, there are other formulas that Automated Market Makers (AMM) use to determine asset prices in liquidity pools. These alternative formulas cater to different market conditions and assets, aiming to mitigate issues like impermanent loss or provide more stable pricing for certain types of assets. Here are some of the other AMM formulas:

### 1. Constant Sum Formula

The Constant Sum Formula is represented as (x + y = k), where (x) and (y) are the quantities of two different tokens in the liquidity pool, and (k) is a constant sum. This formula ensures that the total sum of tokens in the pool remains constant. It's simpler and might be used for pools where price stability between the two assets is desired. However, it's not commonly used in practice because it doesn't provide sufficient liquidity depth and can lead to one of the assets being completely drained from the pool.

### 2. Constant Mean Formula

The Constant Mean Formula generalizes the Constant Product model to support pools with more than two assets. It is used by platforms like Balancer and is represented as (\prod (x_i)^{w_i} = k), where (x_i) is the quantity of each token in the pool, (w_i) is the weight of each token, and (k) is a constant. This formula allows for the creation of pools with different ratios of assets, providing more flexibility in how liquidity is provided and priced.

### 3. Hybrid Function Models

Hybrid models combine aspects of the above formulas to mitigate their downsides, such as impermanent loss or slippage. Curve Finance uses a hybrid model optimized for stablecoins, which are expected to have relatively stable prices. Their formula is designed to reduce impermanent loss for assets that have prices meant to be [pegged](https://faisalkhanllc.xyz/resources/payments-wiki/p/peg/) to each other, like different stablecoins or wrapped tokens of the same underlying asset.

### 4. Dynamic Automated Market Makers (DAMM)

Dynamic AMMs adjust their pricing formula based on external market conditions or internal pool metrics. For example, a DAMM might use different formulas or adjust token weights dynamically to reduce impermanent loss or to better manage [liquidity](https://faisalkhanllc.xyz/resources/payments-wiki/l/liquidity/) under volatile market conditions. This approach allows for more flexible liquidity management but can be complex to implement and manage.

### 5. Concentrated Liquidity

Introduced by Uniswap v3, this is not a different formula per se but a significant evolution in how liquidity can be provided. Liquidity providers can allocate their funds to specific price ranges within a pool, allowing for more capital efficiency and enabling providers to earn more fees with less capital. This model allows for a more granular approach to liquidity provision, where providers can target specific market segments they believe will be the most active.

These formulas and models represent the diversity of approaches within the AMM space to address various challenges, such as providing sufficient liquidity, minimizing impermanent loss, and accommodating the needs of different types of assets and trading strategies. Each has its strengths and is suited to particular market conditions or asset types.