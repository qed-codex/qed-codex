---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LineBundleRootFromRelationsStatement.lean",
  "declarations": [
    "GlobalTheory.T.line_bundle_root_from_relations"
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

## A line bundle root from multiplicative section relations

[Theorem AG.1434](https://andrewodesky.com/rh/lean/GlobalTheory.T.line_bundle_root_from_relations/)

Let $X$ be a scheme, $Q$ a line bundle on $X$, $k\ge1$, and $T$ any set. For every word $w:\{1,\ldots,k\}\to T$, let $u_w\in H^0(X,Q)$. Let $[w]$ denote the multiset of letters of $w$. Assume $$[w_1]+[w_2]=[w_3]+[w_4]\quad\Longrightarrow\quad u_{w_1}u_{w_2}=u_{w_3}u_{w_4},$$ as sections of $Q^{\otimes2}$, and assume the nonvanishing loci of the constant-word sections $u_{(i,\ldots,i)}$, for $i\in T$, cover $X$.

There is a line bundle $A$ with an isomorphism $\omega:A^{\otimes k}\simeq Q$ having the following property. For every scheme $Y$, morphism $b:Y\to X$, line bundle $L$ on $Y$, integers $d,D$ with $dk=D$, sections $a_i\in H^0(Y,L^{\otimes d})$ for $i\in T$, and isomorphism $\theta:b^*Q\simeq L^{\otimes D}$, if $$\theta(b^*u_w)=\prod_{j=1}^k a_{w(j)}\qquad\text{for all }w,$$ then $b^*A\simeq L^{\otimes d}$. Negative tensor powers mean powers of the dual line bundle.
