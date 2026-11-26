---
{
  "module": "src/Formalism/ThetaLogCoordinates/FockResolutionOnto/FockMonomialProofs/PartnerDeterminantHolds.lean",
  "declarations": [
    "Formalism.InvariantFactorPaths.L4.partner_determinant_holds"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## A determinant lower bound from pairings with primitive vectors

[Theorem PHT.0739](https://andrewodesky.com/rh/lean/Formalism.InvariantFactorPaths.L4.partner_determinant_holds/)

Let $p$ be prime, let $V$ be a $\mathbb Q_p$-vector space with its compatible $\mathbb Z_p$-module structure, and let $b:V\times V\to\mathbb Q_p$ be bilinear. Let $g_1,\ldots,g_k$ be $\mathbb Z_p$-linearly independent and put $L=\sum_i\mathbb Z_p g_i$. Let $D\in\mathbb R$. Suppose every primitive $u\in L$ has $u'\in L$ with $$p^{-D}\le|b(u,u')|_p.$$ Then $$p^{-Dk}\le\left|\det(b(g_i,g_j))_{1\le i,j\le k}\right|_p.$$
