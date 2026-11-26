---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/WdParameterMonodromyZeroIffPotentiallyCrystallin.lean",
  "declarations": [
    "GlobalTheory.PstLaws.isCrys_iff",
    "GlobalTheory.PstLaws.isPotCrys_iff",
    "GlobalTheory.PstLaws.wdParameterAt_monodromy_zero_iff_potCrystalline"
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

## Potential crystallinity and zero monodromy

[Theorem PHT.0255](https://andrewodesky.com/rh/lean/GlobalTheory.PstLaws.isPotCrys_iff/)

Let $\ell$ be prime and $K,L$ finite extensions of $\mathbb Q_\ell$ in a fixed algebraic closure. Fix the local period-ring datum of ([Potentially semistable periods become semistable over every large enough extension](https://andrewodesky.com/rh/lean/GlobalTheory.PstSst.isSst_resTo_of_isPst/)), and let $V$ be a finite-dimensional $L$-linear representation of $G_K$ with its compatible restricted $\mathbb Q_\ell$-scalar structure. Suppose $V$ is potentially semistable for this datum. If $N$ is the monodromy operator on $D_{\mathrm{pst}}(V)$, then $$N=0\quad\Longleftrightarrow\quad \text{there is a finite extension }K'/K\text{ such that }V|_{G_{K'}}\text{ is crystalline}.$$

## Potential crystallinity is equivalent to zero monodromy

[Theorem PHT.0344](https://andrewodesky.com/rh/lean/GlobalTheory.PstLaws.wdParameterAt_monodromy_zero_iff_potCrystalline/)

Let $\ell$ be prime, $E$ a number field, $\Omega$ an algebraic closure of $E$, $w$ a finite place, and $A\subseteq\Omega$ a valuation ring above $w$. Let $D_A\le\operatorname{Gal}(\Omega/E)$ be its decomposition group. Choose a topological commutative $\mathbb Z_\ell$-algebra $O$ and the source's local completion bridge from $D_A$ to $G_K$, for a finite extension $K/\mathbb Q_\ell$, with its valuation compatibility condition. Fix the source's local period-ring datum and an isomorphism $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$.

Let $r:D_A\to\operatorname{GL}_a(\overline{\mathbb Q}_\ell)$ have a potentially semistable finite-coefficient-field model for these data. Its associated Weil–Deligne parameter satisfies $$N_{\mathrm{WD}(r)}=0\quad\Longleftrightarrow\quad r\text{ is potentially crystalline}.$$

## Crystallinity from monodromy and inertia

[Theorem PHT.1204](https://andrewodesky.com/rh/lean/GlobalTheory.PstLaws.isCrys_iff/)

Let $\ell$ be prime, let $K,L$ be finite extensions of $\mathbb Q_\ell$ in a fixed algebraic closure, and fix the local period-ring datum of ([Potentially semistable periods become semistable over every large enough extension](https://andrewodesky.com/rh/lean/GlobalTheory.PstSst.isSst_resTo_of_isPst/)). Let $V$ be a finite-dimensional $L$-linear $G_K$-representation which is potentially semistable for that datum. Let $D_{\mathrm{pst}}(V)$ be its potentially semistable period module, with monodromy $N$ and induced Galois action. Then $$V\text{ is crystalline}\quad\Longleftrightarrow\quad N=0\ \text{ and }\ I_K\text{ acts trivially on }D_{\mathrm{pst}}(V),$$ where $I_K=G_K\cap\operatorname{Gal}(\overline{\mathbb Q}_\ell/\mathbb Q_\ell^{\mathrm{nr}})$.
