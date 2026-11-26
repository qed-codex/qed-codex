---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsTestFamiliesProjectedTranslationOperatorsStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_testFamilies_projectedTranslationOperators"
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

## Test functions realizing projected translations in every smooth representation

[Theorem REP.0945](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_testFamilies_projectedTranslationOperators/)

Fix the source's global arithmetic datum and Hermitian space $V$. Let $G_f$ be its finite adelic unitary group, $K_v$ the lattice stabilizers, and $T$ finite local type data supported on $S$. Choose the prescribed auxiliary split place $u\notin S$, split lattice frame, uniformizer $\varpi$, and Iwahori subgroup $I_u$. Let $\mu_v$ be Haar measures with $\mu_v(K_v)=1$ for almost every $v$, and $\nu$ a Haar measure on $G_f$ satisfying the product integral formula for restricted tensor test functions.

There is a family $e=(e_v)$ of locally constant compactly supported functions, equal to $1_{K_v}$ for almost every $v$, with the following properties. Write $e_f(g)=\prod_v e_v(g_v)$. In every smooth complex representation $\sigma$, any operator $P=\sigma(e_f)$ satisfies $P^2=P$ and is nonzero if $\sigma$ contains a vector of type $T$.

For every $g\in G_f$ there is another such family $f=(f_v)$ with $f_u$ left $I_u$-invariant and $$\sigma(f_f)=P\sigma(g)P$$ in every smooth $\sigma$ and for every integral operator $P=\sigma(e_f)$. For every strictly dominant diagonal torus element $t$ defined by $\varpi$, replacing $f_u$ by the auxiliary frame's Iwahori double-coset test function gives an allowed test family of type $T$, bi-$K_v$-invariant at every $v\notin S\cup\{u\}$.
