---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsAlgHomOfIsTranscendenceBasis.lean",
  "declarations": [
    "GlobalTheory.GenericValue.exists_value"
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

## A unique generic value descends to a constant

[Theorem AG.0590](https://andrewodesky.com/rh/lean/GlobalTheory.GenericValue.exists_value/)

Let $K$ be an algebraically closed field, $I$ a set, and $V_R(T,a)$ a predicate for every commutative $K$-algebra $R$, family $T\in R^I$, and $a\in R$. Assume:

1. For every local noetherian $K$-algebra $R$, local $K$-algebra $R'$, and $K$-algebra map $j:R\to R'$, $V_R(T,a)$ implies $V_{R'}(jT,j(a))$.
2. For every field extension $F/K$, $V_F(T,a)$ and $V_F(T,a')$ imply $a=a'$.
3. For every algebraically closed extension $\Omega/K$ and algebraically independent $T\in\Omega^I$, some $a\in\Omega$ satisfies $V_\Omega(T,a)$.
4. For every algebraically closed extension $\Omega/K$, if $T,T'\in\Omega^I$ are jointly algebraically independent over $K$, then $V_\Omega(T,a)$ and $V_\Omega(T',a')$ imply $a=a'$.
5. Let $O$ be a discrete valuation $K$-algebra and $r:O\to\Omega$ a $K$-algebra map to an algebraically closed extension with kernel the maximal ideal. If $T\in O^I$ and $V_\Omega(rT,a)$, there are a discrete valuation $K$-algebra $O'$, an injective $K$-algebra map $j:O\to O'$, a $K$-algebra map $r':O'\to\Omega$, and $u\in O'$ with $r'j=r$ and $V_{O'}(jT,u)$.

There is $\kappa\in K$ such that, for every field extension $F/K$, every $T\in F^I$, and every $a\in F$, $$V_F(T,a)\Longrightarrow a=\kappa.$$ In addition, $V_G((X_i)_{i\in I},\kappa)$ holds for $G=\overline{\operatorname{Frac}(K[X_i:i\in I])}$ and its canonical family of variables.
